"""Daily-marked, periodically rebalanced portfolio backtester.

Timing (no look-ahead)
----------------------
On each rebalance date ``d`` the strategy's ``weight_fn(d, prices.loc[:d])``
sees closing prices up to and including ``d``. The resulting target weights
are held from the close of ``d``; the first return they earn is that of the
next trading day. Between rebalances weights drift with prices.

Costs
-----
``cost_bps`` is charged on the traded notional of risky assets
(sum of |target - current| weights) at every rebalance.

Cash
----
Unallocated weight earns the daily return of ``cash`` (a ticker in ``prices``,
e.g. BIL) where available, otherwise the constant ``cash_rate``.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable

import numpy as np
import pandas as pd

from . import metrics as M

WeightFn = Callable[[pd.Timestamp, pd.DataFrame], pd.Series]


@dataclass
class BacktestResult:
    name: str
    equity: pd.Series
    weights: pd.DataFrame
    turnover: pd.Series
    total_cost: float
    stats: dict = field(default_factory=dict)

    @property
    def returns(self) -> pd.Series:
        return M.returns_from(self.equity).dropna()

    def yearly(self) -> pd.Series:
        return M.calendar_year_returns(self.equity)


def rebalance_dates(index: pd.DatetimeIndex, freq: str | None) -> pd.DatetimeIndex:
    """Last trading day of each period in ``index`` (``M``, ``Q``, ``A``) or first day only."""
    if len(index) == 0:
        return index
    if freq is None or freq.lower() in {"none", "never", "once"}:
        return index[:1]
    key = {"M": index.to_period("M"), "Q": index.to_period("Q"), "A": index.to_period("Y")}[freq.upper()[0]]
    s = pd.Series(index, index=index)
    last = s.groupby(key).max()
    return pd.DatetimeIndex(last.to_numpy())


def cash_returns(prices: pd.DataFrame, index: pd.DatetimeIndex, cash: str | None, cash_rate: float) -> np.ndarray:
    const = (1.0 + cash_rate) ** (1.0 / 252) - 1.0
    if cash and cash in prices.columns:
        r = prices[cash].pct_change(fill_method=None).reindex(index)
        return r.fillna(const).to_numpy()
    return np.full(len(index), const)


def run_backtest(
    prices: pd.DataFrame,
    weight_fn: WeightFn,
    *,
    start: str | pd.Timestamp | None = None,
    end: str | pd.Timestamp | None = None,
    freq: str | None = "M",
    cost_bps: float = 10.0,
    cash: str | None = "BIL",
    cash_rate: float = 0.03,
    name: str = "strategy",
    bench: pd.Series | None = None,
    allow_leverage: bool = False,
) -> BacktestResult:
    prices = prices.sort_index()
    trade_idx = prices.loc[start:end].index
    if len(trade_idx) < 2:
        raise ValueError(f"{name}: not enough data between {start} and {end}")
    rebal = rebalance_dates(trade_idx, freq)
    # Always make the very first day a decision date so the strategy starts invested.
    rebal = pd.DatetimeIndex(sorted(set(rebal) | {trade_idx[0]}))
    rebal = rebal[rebal < trade_idx[-1]]
    rebal_set = set(rebal)

    cols = list(prices.columns)
    rets = prices[cols].pct_change(fill_method=None).reindex(trade_idx).fillna(0.0).to_numpy()
    last_px = prices[cols].reindex(trade_idx).to_numpy()
    cret = cash_returns(prices, trade_idx, cash, cash_rate)

    n_assets = len(cols)
    w = np.zeros(n_assets)
    wc = 1.0
    eq = np.empty(len(trade_idx))
    eq[0] = 1.0
    w_records: dict[pd.Timestamp, np.ndarray] = {}
    turnover: dict[pd.Timestamp, float] = {}
    total_cost = 0.0

    for i, d in enumerate(trade_idx):
        if i > 0:
            gross = w * (1.0 + rets[i])
            cval = wc * (1.0 + cret[i])
            tot = gross.sum() + cval
            eq[i] = eq[i - 1] * tot
            if tot != 0:
                w = gross / tot
                wc = cval / tot
        if d in rebal_set:
            tgt_s = weight_fn(d, prices.loc[:d])
            tgt = tgt_s.reindex(cols).fillna(0.0).to_numpy(dtype="float64") if tgt_s is not None else np.zeros(n_assets)
            # Never allocate to an asset without a price on the decision date.
            tgt = np.where(np.isnan(last_px[i]), 0.0, tgt)
            if (tgt < -1e-12).any():
                raise ValueError(f"{name}: negative weights are not supported")
            s = tgt.sum()
            if s > 1.0 + 1e-9 and not allow_leverage:
                tgt = tgt / s
            traded = float(np.abs(tgt - w).sum())
            cost = cost_bps / 1e4 * traded
            eq[i] *= 1.0 - cost
            total_cost += cost
            turnover[d] = 0.5 * (traded + abs((1.0 - tgt.sum()) - wc))
            w = tgt
            wc = 1.0 - tgt.sum()
            w_records[d] = np.append(tgt, wc)

    equity = pd.Series(eq, index=trade_idx, name=name)
    weights = pd.DataFrame.from_dict(w_records, orient="index", columns=cols + ["CASH"])
    weights = weights.loc[:, (weights.abs() > 1e-9).any(axis=0)]
    res = BacktestResult(
        name=name,
        equity=equity,
        weights=weights,
        turnover=pd.Series(turnover, name="turnover"),
        total_cost=total_cost,
    )
    rf = None
    if cash and cash in prices.columns:
        rf = pd.Series(cret, index=trade_idx)
    res.stats = M.summarize(equity, bench=bench.loc[trade_idx[0]:] if bench is not None else None, rf=rf if rf is not None else 0.0)
    to = res.turnover
    yrs = max(res.stats.get("years", 0) or 0, 1e-9)
    res.stats["annual_turnover"] = float(to.sum() / yrs) if len(to) else 0.0
    res.stats["cost_drag_total"] = float(total_cost)
    return res


def leveraged_equity(
    returns: pd.Series,
    leverage: float,
    expense_ratio: float = 0.0095,
    borrow_rate: float | pd.Series = 0.03,
    borrow_spread: float = 0.005,
) -> pd.Series:
    """Equity of a daily-rebalanced leveraged product (like a 2x/3x ETF).

    Daily return = L * r - (L - 1) * (borrow_rate + spread) / 252 - expense / 252.
    Wealth is floored at zero (a -100% day wipes it out permanently).
    """
    r = returns.dropna()
    if isinstance(borrow_rate, pd.Series):
        br = borrow_rate.reindex(r.index).ffill().fillna(0.03)
    else:
        br = pd.Series(borrow_rate, index=r.index)
    daily = leverage * r - (leverage - 1.0) * (br + borrow_spread) / 252.0 - expense_ratio / 252.0
    daily = daily.clip(lower=-1.0)
    eq = (1.0 + daily).cumprod()
    first = pd.Series([1.0], index=[r.index[0] - pd.Timedelta(days=1)])
    return pd.concat([first, eq])
