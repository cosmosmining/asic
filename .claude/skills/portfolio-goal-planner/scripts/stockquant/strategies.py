"""Strategy weight functions for :func:`stockquant.backtest.run_backtest`.

Each factory returns ``weight_fn(date, hist) -> pd.Series`` where ``hist`` holds
prices up to and including ``date``. Weights are fractions of equity; whatever
is not allocated sits in cash.
"""
from __future__ import annotations

import math
from typing import Iterable

import numpy as np
import pandas as pd

from .backtest import WeightFn

TD = 252


def _trailing_return(col: pd.Series, lookback: int, skip: int = 0) -> float:
    s = col.dropna()
    if len(s) <= lookback:
        return float("nan")
    return float(s.iloc[-1 - skip] / s.iloc[-1 - lookback] - 1.0)


def _trailing_vol(col: pd.Series, window: int) -> float:
    r = col.dropna().pct_change(fill_method=None).dropna().iloc[-window:]
    return float(r.std(ddof=1) * math.sqrt(TD)) if len(r) >= max(20, window // 2) else float("nan")


def _above_sma(col: pd.Series, days: int) -> bool:
    s = col.dropna()
    if len(s) < days:
        return False
    return bool(s.iloc[-1] > s.iloc[-days:].mean())


def is_pinned(col: pd.Series, window: int = 63) -> bool:
    """Heuristic for a takeover target pinned near its cash deal price.

    Normally volatile (1y vol > 20%) but dead flat recently (3m vol < 8% and
    |3m return| < 5%). Momentum rules must not chase such names.
    """
    s = col.dropna()
    if len(s) < 200:
        return False
    r = s.pct_change(fill_method=None).dropna()
    v3 = r.iloc[-window:].std(ddof=1) * math.sqrt(TD)
    v1y = r.iloc[-TD:].std(ddof=1) * math.sqrt(TD)
    ret3 = s.iloc[-1] / s.iloc[-window - 1] - 1.0
    return bool(v3 < 0.08 and abs(ret3) < 0.05 and v1y > 0.20)


def _cap_and_renormalise(w: pd.Series, max_weight: float | None, budget: float) -> pd.Series:
    """Scale to ``budget`` and cap single positions, re-spreading the excess
    over uncapped names. Cash is only left over when every name is capped."""
    if w.empty or w.sum() <= 0:
        return w
    w = w / w.sum() * budget
    if max_weight is None:
        return w
    if max_weight * len(w) <= budget + 1e-12:
        return pd.Series(max_weight, index=w.index)
    for _ in range(100):
        over = w > max_weight + 1e-12
        if not over.any():
            break
        excess = float((w[over] - max_weight).sum())
        w = w.where(~over, max_weight)
        free = w < max_weight - 1e-12
        if not free.any():
            break
        w = w + (excess * w / w[free].sum()).where(free, 0.0)
    return w


def fixed_weights(weights: dict[str, float]) -> WeightFn:
    """Constant mix, restored at every rebalance (or bought once if freq=None)."""
    target = pd.Series(weights, dtype="float64")

    def fn(date: pd.Timestamp, hist: pd.DataFrame) -> pd.Series:
        # A component that has not listed yet keeps its share in cash.
        avail = [t for t in target.index if t in hist.columns and not np.isnan(hist[t].iloc[-1])]
        return target[avail]

    return fn


def momentum_top_n(
    universe: Iterable[str],
    n: int = 5,
    lookback: int = TD,
    skip: int = 21,
    rank_by: str = "risk_adj",
    weighting: str = "inv_vol",
    vol_window: int = 63,
    max_weight: float | None = 0.25,
    abs_filter: float | None = 0.0,
    trend_sma: int | None = 200,
    budget: float = 1.0,
    min_history: int | None = None,
    skip_pinned: bool = True,
    vol_floor: float = 0.10,
) -> WeightFn:
    """Cross-sectional momentum: hold the ``n`` strongest names.

    rank_by: "return" (12-1 momentum) or "risk_adj" (momentum / volatility).
    abs_filter: require momentum above this (time-series momentum); empty slots
                stay in cash. ``None`` disables.
    trend_sma: also require price above its N-day average. ``None`` disables.
    skip_pinned: ignore names that look pinned to a pending takeover price.
    vol_floor: minimum volatility used for ranking/weighting.
    """
    names = list(dict.fromkeys(universe))
    need = min_history or (lookback + 1)

    def fn(date: pd.Timestamp, hist: pd.DataFrame) -> pd.Series:
        rows = []
        for t in names:
            if t not in hist.columns:
                continue
            col = hist[t]
            if col.iloc[-1:].isna().all() or col.notna().sum() < need:
                continue
            mom = _trailing_return(col, lookback, skip)
            if math.isnan(mom):
                continue
            vol = _trailing_vol(col, vol_window)
            if math.isnan(vol) or vol <= 0:
                continue
            if abs_filter is not None and mom <= abs_filter:
                continue
            if trend_sma and not _above_sma(col, trend_sma):
                continue
            if skip_pinned and is_pinned(col):
                continue
            vol = max(vol, vol_floor)  # calm names must not get huge weights
            key = mom / vol if rank_by == "risk_adj" else mom
            rows.append((t, key, vol))
        if not rows:
            return pd.Series(dtype="float64")
        rows.sort(key=lambda x: x[1], reverse=True)
        picked = rows[:n]
        if weighting == "inv_vol":
            w = pd.Series({t: 1.0 / v for t, _, v in picked})
        else:
            w = pd.Series({t: 1.0 for t, _, _ in picked})
        # Each slot is worth budget/n: with fewer qualifiers the rest stays in cash.
        slot_budget = budget * len(picked) / n
        return _cap_and_renormalise(w, max_weight, slot_budget)

    return fn


def trend_filter(weights: dict[str, float], sma_days: int = 210) -> WeightFn:
    """Hold each asset at its weight only while price > N-day SMA (~10 months), else cash."""
    target = pd.Series(weights, dtype="float64")

    def fn(date: pd.Timestamp, hist: pd.DataFrame) -> pd.Series:
        out = {}
        for t, wt in target.items():
            if t in hist.columns and _above_sma(hist[t], sma_days):
                out[t] = wt
        return pd.Series(out, dtype="float64")

    return fn


def dual_momentum(
    us: str = "SPY",
    intl: str = "EFA",
    safe: str = "AGG",
    cash: str = "BIL",
    lookback: int = TD,
) -> WeightFn:
    """Antonacci-style Global Equities Momentum (GEM)."""

    def fn(date: pd.Timestamp, hist: pd.DataFrame) -> pd.Series:
        r_us = _trailing_return(hist[us], lookback) if us in hist else float("nan")
        r_in = _trailing_return(hist[intl], lookback) if intl in hist else float("nan")
        r_cash = _trailing_return(hist[cash], lookback) if cash in hist else 0.0
        if math.isnan(r_cash):
            r_cash = 0.0
        if math.isnan(r_us):
            return pd.Series({safe: 1.0}) if safe in hist and not np.isnan(hist[safe].iloc[-1]) else pd.Series(dtype="float64")
        if r_us > r_cash:
            best = intl if (not math.isnan(r_in) and r_in > r_us) else us
            return pd.Series({best: 1.0})
        return pd.Series({safe: 1.0}) if safe in hist and not np.isnan(hist[safe].iloc[-1]) else pd.Series(dtype="float64")

    return fn


def inverse_vol(universe: Iterable[str], window: int = 63, max_weight: float | None = None, min_history: int = 64) -> WeightFn:
    names = list(dict.fromkeys(universe))

    def fn(date: pd.Timestamp, hist: pd.DataFrame) -> pd.Series:
        w = {}
        for t in names:
            if t in hist.columns and hist[t].notna().sum() >= min_history and not np.isnan(hist[t].iloc[-1]):
                v = _trailing_vol(hist[t], window)
                if v and not math.isnan(v) and v > 0:
                    w[t] = 1.0 / v
        s = pd.Series(w, dtype="float64")
        return _cap_and_renormalise(s, max_weight, 1.0)

    return fn


def equal_weight(universe: Iterable[str], min_history: int = 1) -> WeightFn:
    names = list(dict.fromkeys(universe))

    def fn(date: pd.Timestamp, hist: pd.DataFrame) -> pd.Series:
        live = [t for t in names if t in hist.columns and hist[t].notna().sum() >= min_history and not np.isnan(hist[t].iloc[-1])]
        if not live:
            return pd.Series(dtype="float64")
        return pd.Series(1.0 / len(live), index=live)

    return fn


def blend(parts: list[tuple[WeightFn, float]]) -> WeightFn:
    """Combine sleeves, e.g. 70% core index + 30% momentum satellite."""

    def fn(date: pd.Timestamp, hist: pd.DataFrame) -> pd.Series:
        total = pd.Series(dtype="float64")
        for sleeve, share in parts:
            w = sleeve(date, hist)
            if w is None or w.empty:
                continue
            total = total.add(w * share, fill_value=0.0)
        return total

    return fn
