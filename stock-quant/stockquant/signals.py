"""Price-based factor features and a composite screening score.

Every feature is computed from data up to an ``asof`` date only, so the same
functions are safe to use inside backtests (no look-ahead).

Features (per ticker)
---------------------
ret_1m/3m/6m/12m   trailing total returns
mom_12_1, mom_6_1  momentum skipping the most recent month (Jegadeesh-Titman)
vol_3m, vol_1y     annualised daily volatility
risk_adj_mom       mom_12_1 / vol_1y  (falls back to 6-1 for young listings)
sma200_gap         price / 200-day average - 1
golden             50-day average above 200-day average
sma200_slope_up    200-day average rising over the last month
dd_from_high       distance from 52-week high
maxdd_1y, maxdd_3y worst peak-to-trough inside the window
cagr_3y, cagr_5y   annualised returns
beta_1y, corr_1y   versus the benchmark (default SPY)
rel_strength_12m   12-month return minus benchmark 12-month return
adv_3m_usd         average daily dollar volume, last 3 months (if volume given)
"""
from __future__ import annotations

import math

import numpy as np
import pandas as pd

TD = 252

# Weights of the composite score. Missing features (e.g. young IPOs without a
# 12-month history) have their weight redistributed over available features.
PRESETS: dict[str, dict[str, float]] = {
    # Trend-quality blend: rewards strong *and* orderly uptrends.
    "balanced": {
        "risk_adj_mom": 0.25,
        "mom_6_1": 0.10,
        "trend": 0.15,
        "rel_strength": 0.10,
        "low_vol": 0.15,
        "dd_resilience": 0.10,
        "long_term": 0.15,
    },
    # Pure trend-following tilt.
    "momentum": {
        "risk_adj_mom": 0.30,
        "mom_6_1": 0.25,
        "trend": 0.20,
        "rel_strength": 0.15,
        "low_vol": 0.05,
        "dd_resilience": 0.05,
    },
    # For core holdings: steadiness first.
    "defensive": {
        "risk_adj_mom": 0.15,
        "trend": 0.15,
        "low_vol": 0.30,
        "dd_resilience": 0.25,
        "long_term": 0.15,
    },
}


def _ret(s: np.ndarray, k: int, skip: int = 0) -> float:
    n = len(s)
    if n <= k:
        return float("nan")
    return float(s[n - 1 - skip] / s[n - 1 - k] - 1.0)


def _max_dd(s: np.ndarray) -> float:
    if len(s) < 2:
        return float("nan")
    peak = np.maximum.accumulate(s)
    return float(np.min(s / peak - 1.0))


def _cagr(s: np.ndarray, years: int) -> float:
    k = years * TD
    if len(s) <= k:
        return float("nan")
    return float((s[-1] / s[-1 - k]) ** (1.0 / years) - 1.0)


def ticker_features(
    s: pd.Series,
    bench: pd.Series | None = None,
    volume: pd.Series | None = None,
    raw_close: pd.Series | None = None,
) -> dict:
    """Feature dict for one adjusted-price series (already truncated to asof)."""
    s = s.dropna()
    a = s.to_numpy(dtype="float64")
    n = len(a)
    f: dict[str, float | bool | str | None] = {
        "price": float(raw_close.dropna().iloc[-1]) if raw_close is not None and raw_close.notna().any() else (float(a[-1]) if n else float("nan")),
        "last_date": str(s.index[-1].date()) if n else None,
        "history_years": round(n / TD, 2),
    }
    if n < 63:
        f["trend_state"] = "insufficient history"
        return f
    r = np.diff(a) / a[:-1]
    f.update(
        {
            "ret_1m": _ret(a, 21),
            "ret_3m": _ret(a, 63),
            "ret_6m": _ret(a, 126),
            "ret_12m": _ret(a, TD),
            "mom_12_1": _ret(a, TD, skip=21),
            "mom_6_1": _ret(a, 126, skip=21),
            "vol_3m": float(np.std(r[-63:], ddof=1) * math.sqrt(TD)),
            "vol_1y": float(np.std(r[-TD:], ddof=1) * math.sqrt(TD)) if len(r) >= 126 else float("nan"),
            "dd_from_high": float(a[-1] / np.max(a[-TD:]) - 1.0),
            "maxdd_1y": _max_dd(a[-TD:]),
            "maxdd_3y": _max_dd(a[-3 * TD :]) if n >= 2 * TD else float("nan"),
            "cagr_3y": _cagr(a, 3),
            "cagr_5y": _cagr(a, 5),
        }
    )
    f["vol_1m"] = float(np.std(r[-21:], ddof=1) * math.sqrt(TD))
    # Takeover-target signature: normally volatile, now pinned flat near a deal price.
    f["pinned"] = bool(
        n >= 200
        and f["vol_3m"] < 0.08
        and abs(f["ret_3m"]) < 0.05
        and not math.isnan(f["vol_1y"])
        and f["vol_1y"] > 0.20
    )
    vol_for_ram = f["vol_1y"] if not math.isnan(f["vol_1y"]) else f["vol_3m"]
    mom = f["mom_12_1"] if not math.isnan(f["mom_12_1"]) else f["mom_6_1"]
    f["risk_adj_mom"] = float(mom / vol_for_ram) if vol_for_ram and not math.isnan(mom) else float("nan")

    if n >= 200:
        sma50 = float(np.mean(a[-50:]))
        sma200 = float(np.mean(a[-200:]))
        sma200_prev = float(np.mean(a[-221:-21])) if n >= 221 else float("nan")
        f["sma200_gap"] = float(a[-1] / sma200 - 1.0)
        f["golden"] = bool(sma50 > sma200)
        f["sma200_slope_up"] = bool(sma200 > sma200_prev) if not math.isnan(sma200_prev) else None
        price = a[-1]
        if price > sma50 > sma200 and f["sma200_slope_up"]:
            state = "strong uptrend"
        elif price > sma200 and sma50 > sma200:
            state = "uptrend (pullback)"
        elif price > sma200:
            state = "recovering"
        elif sma50 > sma200:
            state = "weakening"
        else:
            state = "downtrend"
        f["trend_state"] = "pinned (likely pending deal)" if f["pinned"] else state
        f["extended"] = bool(f["sma200_gap"] > 0.40)
    else:
        f["sma200_gap"] = float(a[-1] / np.mean(a) - 1.0)
        f["golden"] = None
        f["sma200_slope_up"] = None
        f["trend_state"] = "young listing"
        f["extended"] = bool(f["sma200_gap"] > 0.40)

    if bench is not None:
        b = bench.dropna()
        joined = pd.concat([s.pct_change(fill_method=None), b.pct_change(fill_method=None)], axis=1, join="inner").dropna().iloc[-TD:]
        if len(joined) >= 60:
            x, y = joined.iloc[:, 0], joined.iloc[:, 1]
            vb = y.var(ddof=1)
            f["beta_1y"] = float(x.cov(y) / vb) if vb > 0 else float("nan")
            f["corr_1y"] = float(x.corr(y))
        b_al = b.loc[: s.index[-1]].to_numpy(dtype="float64")
        f["rel_strength_12m"] = f["ret_12m"] - _ret(b_al, TD) if not math.isnan(f["ret_12m"]) else float("nan")

    if volume is not None and raw_close is not None:
        dv = (raw_close * volume).dropna().iloc[-63:]
        f["adv_3m_usd"] = float(dv.mean()) if len(dv) else float("nan")
    return f


def features_table(
    px: pd.DataFrame,
    bench: str | pd.Series | None = "SPY",
    asof: pd.Timestamp | str | None = None,
    volume: pd.DataFrame | None = None,
    close: pd.DataFrame | None = None,
) -> pd.DataFrame:
    """Features for every column of ``px`` using data up to ``asof``."""
    if asof is not None:
        px = px.loc[:asof]
        volume = volume.loc[:asof] if volume is not None else None
        close = close.loc[:asof] if close is not None else None
    if isinstance(bench, str):
        bench_s = px[bench] if bench in px.columns else None
    else:
        bench_s = bench
    rows = {}
    for t in px.columns:
        rows[t] = ticker_features(
            px[t],
            bench=bench_s,
            volume=volume[t] if volume is not None and t in volume else None,
            raw_close=close[t] if close is not None and t in close else None,
        )
    return pd.DataFrame.from_dict(rows, orient="index")


def _pct_rank(x: pd.Series) -> pd.Series:
    return x.rank(pct=True, na_option="keep") * 100.0


def composite_scores(feat: pd.DataFrame, preset: str | dict = "balanced") -> pd.DataFrame:
    """Add sub-scores (0-100 percentile within the table) and a composite score."""
    weights = PRESETS[preset] if isinstance(preset, str) else dict(preset)
    f = feat.copy()
    num = lambda c: pd.to_numeric(f.get(c), errors="coerce") if c in f else pd.Series(np.nan, index=f.index)  # noqa: E731

    trend_raw = num("sma200_gap").clip(-0.4, 0.6)
    trend_raw = trend_raw + 0.10 * f.get("golden", pd.Series(False, index=f.index)).fillna(False).astype(float)
    trend_raw = trend_raw + 0.10 * f.get("sma200_slope_up", pd.Series(False, index=f.index)).fillna(False).astype(float)

    long_term = num("cagr_5y").fillna(num("cagr_3y"))
    raw = pd.DataFrame(
        {
            "risk_adj_mom": num("risk_adj_mom"),
            "mom_6_1": num("mom_6_1"),
            "trend": trend_raw,
            "rel_strength": num("rel_strength_12m"),
            "low_vol": -num("vol_1y").fillna(num("vol_3m")),
            "dd_resilience": num("maxdd_1y"),
            "long_term": long_term,
        },
        index=f.index,
    )
    subs = raw.apply(_pct_rank)
    for k in subs.columns:
        f[f"s_{k}"] = subs[k].round(1)

    w = pd.Series(weights, dtype="float64")
    sub = subs[w.index]
    avail = sub.notna().astype(float).mul(w, axis=1)
    denom = avail.sum(axis=1)
    score = sub.fillna(0.0).mul(w, axis=1).sum(axis=1) / denom.replace(0, np.nan)
    # Penalise very short histories (noisy stats) and deal-pinned prices (no upside).
    hist = num("history_years").fillna(0.0)
    score = score * np.where(hist < 1.0, 0.85, 1.0)
    if "pinned" in f:
        score = score * np.where(f["pinned"].fillna(False).astype(bool), 0.3, 1.0)
    f["score"] = score.round(1)
    f["coverage"] = (denom / w.sum()).round(2)
    f["grade"] = pd.cut(
        f["score"], bins=[-1, 35, 50, 65, 80, 101], labels=["E", "D", "C", "B", "A"]
    ).astype("string")
    return f.sort_values("score", ascending=False)


def apply_fundamentals(scored: pd.DataFrame, fundamentals: pd.DataFrame | None) -> pd.DataFrame:
    """Join an optional fundamentals snapshot and flag valuation risk.

    ``fundamentals`` columns used if present: fwd_pe, ev_sales, rev_growth (decimal),
    gross_margin, net_debt_ebitda, profitable (bool), as_of.
    """
    if fundamentals is None or fundamentals.empty:
        return scored
    out = scored.join(fundamentals, how="left", rsuffix="_f")

    def flag(row: pd.Series) -> str | None:
        pe = row.get("fwd_pe")
        evs = row.get("ev_sales")
        prof = row.get("profitable")
        g = row.get("rev_growth")
        if pd.isna(pe) and pd.isna(evs) and (prof is None or (not isinstance(prof, (bool, str)) and pd.isna(prof))):
            return None
        if prof is False or (isinstance(prof, str) and prof.lower() == "false"):
            return "speculative (unprofitable)"
        if (not pd.isna(pe) and pe > 60) or (not pd.isna(evs) and evs > 20):
            return "stretched"
        # A tiny P/E on booming sales is the classic cyclical-peak trap, not a bargain.
        if not pd.isna(pe) and pe < 12 and g is not None and not pd.isna(g) and g > 0.75:
            return "peak-cycle risk (low P/E on boom earnings)"
        if not pd.isna(pe) and pe > 35:
            return "premium"
        return "reasonable"

    out["valuation_flag"] = out.apply(flag, axis=1)
    if "fwd_pe" in out and "rev_growth" in out:
        g = pd.to_numeric(out["rev_growth"], errors="coerce") * 100
        out["growth_adj_pe"] = (pd.to_numeric(out["fwd_pe"], errors="coerce") / g.where(g > 0)).round(2)
    return out


def theme_index(px: pd.DataFrame, members: list[str], min_members: int = 3) -> pd.Series:
    """Equal-weight, daily-rebalanced index of available members (starts at 1)."""
    cols = [m for m in members if m in px.columns]
    if not cols:
        return pd.Series(dtype="float64")
    r = px[cols].pct_change(fill_method=None)
    count = r.notna().sum(axis=1)
    ew = r.mean(axis=1, skipna=True).where(count >= min_members)
    ew = ew.dropna()
    return (1 + ew).cumprod()
