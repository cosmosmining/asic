import numpy as np
import pandas as pd
import pytest

from conftest import geometric_series
from stockquant import strategies as ST
from stockquant.backtest import leveraged_equity, rebalance_dates, run_backtest


def _always(weights):
    return lambda d, h: pd.Series(weights, dtype=float)


def test_buy_and_hold_tracks_asset(bdays):
    px = pd.DataFrame({"A": geometric_series(bdays, 0.12)})
    res = run_backtest(px, _always({"A": 1.0}), freq=None, cost_bps=0, cash=None, cash_rate=0.0)
    assert res.equity.iloc[-1] == pytest.approx(px["A"].iloc[-1] / px["A"].iloc[0], rel=1e-9)


def test_weight_fn_never_sees_future_rows(bdays):
    px = pd.DataFrame({"A": geometric_series(bdays, 0.05)})
    seen = []

    def spy(d, h):
        seen.append((d, h.index[-1]))
        return pd.Series({"A": 1.0})

    run_backtest(px, spy, cost_bps=0, cash=None)
    assert seen and all(d == last for d, last in seen)


def test_no_lookahead_jump_on_decision_day():
    """A jump that happens ON the decision day must not be captured by a buy at that close."""
    idx = pd.bdate_range("2021-01-01", "2021-03-31")
    a = pd.Series(100.0, index=idx)
    jan_end = idx[idx.month == 1][-1]
    a.loc[jan_end:] = 200.0  # +100% on the last trading day of January
    px = pd.DataFrame({"A": a})

    def buy_from_february(d, h):
        return pd.Series({"A": 1.0}) if d >= jan_end else pd.Series(dtype=float)

    res = run_backtest(px, buy_from_february, cost_bps=0, cash=None, cash_rate=0.0)
    assert res.equity.iloc[-1] == pytest.approx(1.0)


def test_jump_after_decision_day_is_captured():
    idx = pd.bdate_range("2021-01-01", "2021-03-31")
    a = pd.Series(100.0, index=idx)
    jan_end = idx[idx.month == 1][-1]
    first_feb = idx[idx.month == 2][0]
    a.loc[first_feb:] = 200.0
    px = pd.DataFrame({"A": a})

    def buy_from_jan_end(d, h):
        return pd.Series({"A": 1.0}) if d >= jan_end else pd.Series(dtype=float)

    res = run_backtest(px, buy_from_jan_end, cost_bps=0, cash=None, cash_rate=0.0)
    assert res.equity.iloc[-1] == pytest.approx(2.0)


def test_costs_reduce_returns(bdays):
    rng = np.random.default_rng(3)
    px = pd.DataFrame(
        {k: 100 * np.exp(np.cumsum(0.0003 + 0.02 * rng.standard_normal(len(bdays)))) for k in ("A", "B")},
        index=bdays,
    )
    free = run_backtest(px, _always({"A": 0.5, "B": 0.5}), cost_bps=0, cash=None)
    paid = run_backtest(px, _always({"A": 0.5, "B": 0.5}), cost_bps=50, cash=None)
    assert paid.equity.iloc[-1] < free.equity.iloc[-1]
    assert paid.total_cost > 0


def test_cash_earns_cash_rate(bdays):
    px = pd.DataFrame({"A": geometric_series(bdays, 0.20)})
    res = run_backtest(px, lambda d, h: pd.Series(dtype=float), cost_bps=0, cash=None, cash_rate=0.04)
    yrs = (bdays[-1] - bdays[0]).days / 365.25
    # 252 compounding steps per year vs calendar time: within a few bp a year
    assert res.stats["cagr"] == pytest.approx(0.04, abs=0.003)
    assert res.stats["max_drawdown"] == pytest.approx(0.0)
    assert yrs > 5


def test_no_allocation_before_listing():
    idx = pd.bdate_range("2020-01-01", "2020-12-31")
    a = pd.Series(np.linspace(100, 150, len(idx)), index=idx)
    b = pd.Series(np.nan, index=idx)
    b.iloc[150:] = np.linspace(10, 20, len(idx) - 150)
    px = pd.DataFrame({"A": a, "B": b})
    res = run_backtest(px, _always({"A": 0.5, "B": 0.5}), cost_bps=0, cash=None, cash_rate=0.0)
    first_b = b.first_valid_index()
    pre = res.weights.loc[res.weights.index < first_b]
    assert (pre.get("B", pd.Series(0.0, index=pre.index)) == 0).all()


def test_rebalance_dates_month_end():
    idx = pd.bdate_range("2021-01-01", "2021-04-30")
    rd = rebalance_dates(idx, "M")
    assert [d.month for d in rd] == [1, 2, 3, 4]
    assert all(d == idx[idx.month == d.month][-1] for d in rd)


def test_leveraged_equity_daily_reset():
    idx = pd.bdate_range("2020-01-01", periods=3)
    r = pd.Series([0.10, -0.10, 0.0], index=idx)
    eq = leveraged_equity(r, 2.0, expense_ratio=0.0, borrow_rate=0.0, borrow_spread=0.0)
    assert eq.iloc[-1] == pytest.approx(1.2 * 0.8)


def test_leveraged_equity_floors_at_zero():
    idx = pd.bdate_range("2020-01-01", periods=3)
    r = pd.Series([-0.40, 0.10, 0.10], index=idx)
    eq = leveraged_equity(r, 3.0, expense_ratio=0.0, borrow_rate=0.0, borrow_spread=0.0)
    assert eq.iloc[-1] == 0.0


def test_momentum_picks_strongest(bdays):
    px = pd.DataFrame(
        {
            "UP": geometric_series(bdays, 0.30),
            "MID": geometric_series(bdays, 0.10),
            "DOWN": geometric_series(bdays, -0.10),
        }
    )
    rng = np.random.default_rng(5)
    px = px * np.exp(0.001 * rng.standard_normal(px.shape))  # give them some volatility
    w = ST.momentum_top_n(["UP", "MID", "DOWN"], n=1, rank_by="return", trend_sma=None, max_weight=None)(bdays[-1], px)
    assert list(w.index) == ["UP"]
    assert w.sum() == pytest.approx(1.0)


def test_momentum_abs_filter_leaves_cash(bdays):
    px = pd.DataFrame({"DOWN": geometric_series(bdays, -0.10)})
    px = px * np.exp(0.001 * np.random.default_rng(6).standard_normal(px.shape))
    w = ST.momentum_top_n(["DOWN"], n=1, trend_sma=None)(bdays[-1], px)
    assert w.empty or w.sum() == 0


def test_trend_filter_exits_below_sma():
    idx = pd.bdate_range("2020-01-01", periods=400)
    s = pd.Series(np.r_[np.linspace(100, 200, 300), np.linspace(200, 120, 100)], index=idx)
    px = pd.DataFrame({"A": s})
    fn = ST.trend_filter({"A": 1.0}, sma_days=200)
    assert fn(idx[299], px.loc[: idx[299]]).sum() == pytest.approx(1.0)
    assert fn(idx[-1], px).sum() == 0


def test_dual_momentum_goes_safe_when_equities_lag_cash():
    idx = pd.bdate_range("2020-01-01", periods=300)
    px = pd.DataFrame(
        {
            "SPY": np.linspace(100, 90, 300),
            "EFA": np.linspace(100, 85, 300),
            "IEF": np.linspace(100, 101, 300),
            "BIL": np.linspace(100, 102, 300),
        },
        index=idx,
    )
    w = ST.dual_momentum("SPY", "EFA", "IEF", "BIL")(idx[-1], px)
    assert list(w.index) == ["IEF"]
