"""Performance and risk statistics for price / equity series.

Conventions
-----------
* ``equity`` is a value series (any starting level), e.g. adjusted prices or a
  backtest equity curve. ``returns`` are simple periodic returns.
* Annualisation uses 252 trading days unless ``periods`` says otherwise.
* CAGR uses calendar time between the first and last observation.
"""
from __future__ import annotations

import math

import numpy as np
import pandas as pd

TRADING_DAYS = 252


def returns_from(equity: pd.Series | pd.DataFrame) -> pd.Series | pd.DataFrame:
    """Simple returns, without filling gaps (pandas>=3 semantics made explicit)."""
    return equity.pct_change(fill_method=None)


def years_between(index: pd.DatetimeIndex) -> float:
    if len(index) < 2:
        return 0.0
    return (index[-1] - index[0]).days / 365.25


def cagr(equity: pd.Series) -> float:
    s = equity.dropna()
    yrs = years_between(s.index)
    if yrs <= 0 or s.iloc[0] <= 0:
        return float("nan")
    return float((s.iloc[-1] / s.iloc[0]) ** (1.0 / yrs) - 1.0)


def total_return(equity: pd.Series) -> float:
    s = equity.dropna()
    return float(s.iloc[-1] / s.iloc[0] - 1.0) if len(s) > 1 else float("nan")


def ann_vol(returns: pd.Series, periods: int = TRADING_DAYS) -> float:
    r = returns.dropna()
    return float(r.std(ddof=1) * math.sqrt(periods)) if len(r) > 2 else float("nan")


def _excess(returns: pd.Series, rf: float | pd.Series, periods: int) -> pd.Series:
    if isinstance(rf, pd.Series):
        return (returns - rf.reindex(returns.index).fillna(0.0)).dropna()
    return (returns - rf / periods).dropna()


def sharpe(returns: pd.Series, rf: float | pd.Series = 0.0, periods: int = TRADING_DAYS) -> float:
    ex = _excess(returns, rf, periods)
    sd = ex.std(ddof=1)
    return float(ex.mean() / sd * math.sqrt(periods)) if sd and sd > 0 else float("nan")


def sortino(returns: pd.Series, rf: float | pd.Series = 0.0, periods: int = TRADING_DAYS) -> float:
    ex = _excess(returns, rf, periods)
    downside = np.sqrt(np.mean(np.minimum(ex.to_numpy(), 0.0) ** 2))
    return float(ex.mean() / downside * math.sqrt(periods)) if downside > 0 else float("nan")


def drawdown(equity: pd.Series) -> pd.Series:
    s = equity.dropna()
    return s / s.cummax() - 1.0


def max_drawdown(equity: pd.Series) -> float:
    dd = drawdown(equity)
    return float(dd.min()) if len(dd) else float("nan")


def max_drawdown_info(equity: pd.Series) -> dict:
    """Depth, peak date, trough date and recovery date (None if not recovered)."""
    s = equity.dropna()
    if len(s) < 2:
        return {"depth": float("nan"), "peak": None, "trough": None, "recovery": None}
    dd = s / s.cummax() - 1.0
    trough = dd.idxmin()
    peak = s.loc[:trough].idxmax()
    after = s.loc[trough:]
    rec = after[after >= s.loc[peak]]
    return {
        "depth": float(dd.min()),
        "peak": str(peak.date()),
        "trough": str(trough.date()),
        "recovery": str(rec.index[0].date()) if len(rec) else None,
    }


def ulcer_index(equity: pd.Series) -> float:
    dd = drawdown(equity)
    return float(np.sqrt(np.mean(np.square(dd.to_numpy())))) if len(dd) else float("nan")


def calmar(equity: pd.Series) -> float:
    mdd = max_drawdown(equity)
    return float(cagr(equity) / abs(mdd)) if mdd and mdd < 0 else float("nan")


def beta_corr(returns: pd.Series, bench: pd.Series) -> tuple[float, float]:
    df = pd.concat([returns, bench], axis=1, join="inner").dropna()
    if len(df) < 20:
        return float("nan"), float("nan")
    a, b = df.iloc[:, 0], df.iloc[:, 1]
    var_b = b.var(ddof=1)
    beta = float(a.cov(b) / var_b) if var_b > 0 else float("nan")
    return beta, float(a.corr(b))


def capture_ratios(returns: pd.Series, bench: pd.Series, freq: str = "ME") -> tuple[float, float]:
    """Up/down capture on monthly returns (ratio of geometric means)."""
    m = (1 + pd.concat([returns, bench], axis=1, join="inner").dropna()).resample(freq).prod() - 1
    if len(m) < 6:
        return float("nan"), float("nan")
    s, b = m.iloc[:, 0], m.iloc[:, 1]
    up, dn = b > 0, b < 0

    def gm(x: pd.Series) -> float:
        return float(np.prod(1 + x) ** (1 / len(x)) - 1) if len(x) else float("nan")

    upc = gm(s[up]) / gm(b[up]) if up.any() else float("nan")
    dnc = gm(s[dn]) / gm(b[dn]) if dn.any() else float("nan")
    return float(upc), float(dnc)


def calendar_year_returns(equity: pd.Series) -> pd.Series:
    s = equity.dropna()
    ye = s.resample("YE").last()
    first = s.iloc[:1]
    first.index = [s.index[0] - pd.Timedelta(days=1)]
    yr = pd.concat([first, ye]).pct_change(fill_method=None).dropna()
    yr.index = yr.index.year
    return yr


def monthly_returns(equity: pd.Series) -> pd.Series:
    s = equity.dropna()
    return s.resample("ME").last().pct_change(fill_method=None).dropna()


def rolling_cagr(equity: pd.Series, years: int) -> pd.Series:
    """Rolling annualised return over ``years`` (monthly sampling)."""
    m = equity.dropna().resample("ME").last()
    n = 12 * years
    return (m / m.shift(n)) ** (1.0 / years) - 1.0


def summarize(
    equity: pd.Series,
    bench: pd.Series | None = None,
    rf: float | pd.Series = 0.0,
    periods: int = TRADING_DAYS,
) -> dict:
    """One-stop summary dictionary for an equity curve."""
    s = equity.dropna()
    r = returns_from(s).dropna()
    out = {
        "start": str(s.index[0].date()) if len(s) else None,
        "end": str(s.index[-1].date()) if len(s) else None,
        "years": round(years_between(s.index), 2),
        "total_return": total_return(s),
        "multiple": float(s.iloc[-1] / s.iloc[0]) if len(s) > 1 else float("nan"),
        "cagr": cagr(s),
        "vol": ann_vol(r, periods),
        "sharpe": sharpe(r, rf, periods),
        "sortino": sortino(r, rf, periods),
        "max_drawdown": max_drawdown(s),
        "calmar": calmar(s),
        "ulcer": ulcer_index(s),
    }
    mr = monthly_returns(s)
    out["pct_positive_months"] = float((mr > 0).mean()) if len(mr) else float("nan")
    yr = calendar_year_returns(s)
    if len(yr):
        out["best_year"] = float(yr.max())
        out["worst_year"] = float(yr.min())
    if bench is not None:
        br = returns_from(bench.dropna()).dropna()
        beta, corr = beta_corr(r, br)
        upc, dnc = capture_ratios(r, br)
        out.update({"beta": beta, "corr": corr, "up_capture": upc, "down_capture": dnc})
    return out
