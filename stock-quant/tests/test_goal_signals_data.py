import math

import numpy as np
import pandas as pd
import pytest

from conftest import geometric_series
from stockquant import goal as G
from stockquant import portfolio as P
from stockquant import signals as S
from stockquant.data import PriceFetchError, parse_chart_payload


# ----------------------------------------------------------------------- goal
def test_years_and_required_cagr_for_50x():
    assert G.years_to_multiple(50, 0.10) == pytest.approx(41.04, abs=0.01)
    assert G.required_cagr(50, 20) == pytest.approx(0.2161, abs=1e-4)
    assert G.required_cagr(50, 10) == pytest.approx(0.4788, abs=1e-4)


def test_future_value_zero_return_is_contributions():
    fv = G.future_value(1000, 100, 10, 0.0)
    assert fv["final"] == pytest.approx(1000 + 100 * 120)
    assert fv["multiple_on_contributed"] == pytest.approx(1.0)


def test_volatility_drag():
    assert G.median_cagr(0.10, 0.0001) == pytest.approx(0.10, abs=1e-6)
    assert G.median_cagr(0.10, 0.40) < 0.04


def test_monte_carlo_median_matches_lognormal_theory():
    sim = G.simulate(1.0, 0.0, 20, mean=0.10, vol=0.20, n_paths=40_000, seed=1)
    mu, _ = G.lognormal_params(0.10, 0.20)
    assert np.median(sim.terminal) == pytest.approx(math.exp(mu * 20), rel=0.03)
    p_mc = float(np.mean(sim.terminal >= 5))
    assert p_mc == pytest.approx(G.prob_lump_sum_multiple(0.10, 0.20, 5, 20), abs=0.01)


def test_bootstrap_uses_history_only():
    hist = np.full(120, 0.01)  # +1% every month
    sim = G.simulate(100.0, 0.0, 10, hist_monthly=hist, n_paths=200, seed=2)
    assert np.allclose(sim.terminal, 100 * 1.01**120)


def test_prob_increases_with_horizon():
    ps = [G.prob_lump_sum_multiple(0.12, 0.20, 50, y) for y in (10, 20, 30, 40)]
    assert ps == sorted(ps)


def test_kelly():
    assert G.kelly_fraction(0.10, 0.20, 0.02) == pytest.approx(2.0)


# -------------------------------------------------------------------- signals
def test_features_and_score_rank_smooth_uptrend_first(bdays):
    rng = np.random.default_rng(9)
    smooth = geometric_series(bdays, 0.25) * np.exp(0.002 * rng.standard_normal(len(bdays)))
    choppy = geometric_series(bdays, 0.05) * np.exp(np.cumsum(0.03 * rng.standard_normal(len(bdays))) * 0.2)
    crash = geometric_series(bdays, 0.10).copy()
    crash.iloc[-150:] *= np.linspace(1, 0.5, 150)
    px = pd.DataFrame({"SMOOTH": smooth, "CHOPPY": choppy, "CRASH": crash, "SPY": geometric_series(bdays, 0.08)})
    feat = S.features_table(px, bench="SPY")
    assert feat.loc["SMOOTH", "trend_state"] == "strong uptrend"
    assert feat.loc["CRASH", "trend_state"] in {"downtrend", "weakening"}
    scored = S.composite_scores(feat.drop(index="SPY"), "balanced")
    assert scored.index[0] == "SMOOTH"
    assert scored.index[-1] == "CRASH"


def test_young_listing_gets_partial_coverage():
    idx = pd.bdate_range("2024-01-01", periods=120)
    px = pd.DataFrame({"NEW": np.linspace(10, 20, 120), "OLD": np.linspace(10, 12, 120)}, index=idx)
    feat = S.features_table(px, bench=None)
    scored = S.composite_scores(feat, "balanced")
    assert scored.loc["NEW", "coverage"] < 1.0


def test_valuation_flags():
    scored = pd.DataFrame({"score": [80, 70, 60]}, index=["A", "B", "C"])
    fund = pd.DataFrame(
        {"fwd_pe": [20, 90, np.nan], "rev_growth": [0.2, 0.5, 1.0], "profitable": [True, True, False]},
        index=["A", "B", "C"],
    )
    out = S.apply_fundamentals(scored, fund)
    assert out.loc["A", "valuation_flag"] == "reasonable"
    assert out.loc["B", "valuation_flag"] == "stretched"
    assert out.loc["C", "valuation_flag"].startswith("speculative")


# ------------------------------------------------------------------ portfolio
def test_risk_parity_equalises_contributions():
    cov = pd.DataFrame([[0.04, 0.01, 0.0], [0.01, 0.09, 0.02], [0.0, 0.02, 0.16]], index=list("ABC"), columns=list("ABC"))
    w = P.risk_parity_weights(cov)
    rc = P.risk_contributions(w, cov)
    assert w.sum() == pytest.approx(1.0)
    assert rc.max() - rc.min() < 1e-6


def test_inverse_vol_cap():
    rng = np.random.default_rng(4)
    idx = pd.bdate_range("2020-01-01", periods=100)
    px = pd.DataFrame({k: 100 * np.exp(np.cumsum(s * rng.standard_normal(100))) for k, s in {"LO": 0.002, "MID": 0.01, "HI": 0.03}.items()}, index=idx)
    w = P.inverse_vol_weights(px, window=63, max_weight=0.5)
    assert w.sum() == pytest.approx(1.0)
    assert w.max() <= 0.5 + 1e-9


# ----------------------------------------------------------------------- data
def _payload(ts, close, adj):
    return {
        "chart": {
            "result": [
                {
                    "meta": {"exchangeTimezoneName": "America/New_York", "currency": "USD"},
                    "timestamp": ts,
                    "indicators": {"quote": [{"close": close, "volume": [1000] * len(ts)}], "adjclose": [{"adjclose": adj}]},
                }
            ],
            "error": None,
        }
    }


def test_parse_chart_payload_uses_exchange_dates_and_drops_nulls():
    # 14:30 UTC on consecutive days = 09:30 New York
    ts = [1704205800, 1704292200, 1704378600]
    df = parse_chart_payload("TEST", _payload(ts, [10.0, None, 12.0], [9.5, None, 11.4]))
    assert list(df.index.strftime("%Y-%m-%d")) == ["2024-01-02", "2024-01-04"]
    assert df["adjclose"].tolist() == [9.5, 11.4]


def test_parse_chart_payload_error():
    with pytest.raises(PriceFetchError):
        parse_chart_payload("BAD", {"chart": {"result": None, "error": {"code": "Not Found", "description": "No data"}}})


def test_prices_align_to_calendar(tmp_path):
    from stockquant.data import PriceStore

    us = pd.bdate_range("2024-01-01", periods=30)
    extra = pd.DatetimeIndex([pd.Timestamp("2024-01-06")])  # a Saturday "foreign" session
    for name, idx in (("AAA", us), ("BBB", us.union(extra))):
        df = pd.DataFrame({"close": 1.0, "adjclose": np.arange(len(idx), dtype=float) + 1, "volume": 1.0}, index=idx)
        df.index.name = "date"
        df.to_csv(tmp_path / f"{name}.csv")
    store = PriceStore(cache_dir=tmp_path, offline=True)
    px = store.prices(["AAA", "BBB"], calendar="AAA")
    assert px.index.equals(us)
    assert len(store.prices(["AAA", "BBB"])) == len(us) + 1
