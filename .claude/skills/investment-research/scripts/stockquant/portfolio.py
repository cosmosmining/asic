"""Portfolio construction and position sizing helpers."""
from __future__ import annotations

import math

import numpy as np
import pandas as pd

TD = 252


def inverse_vol_weights(prices: pd.DataFrame, window: int = 63, max_weight: float | None = None) -> pd.Series:
    r = prices.pct_change(fill_method=None).iloc[-window:]
    vol = r.std(ddof=1) * math.sqrt(TD)
    w = (1.0 / vol.replace(0, np.nan)).dropna()
    w = w / w.sum()
    if max_weight is not None:
        for _ in range(50):  # iterative capping keeps the sum at 1
            over = w > max_weight
            if not over.any():
                break
            excess = (w[over] - max_weight).sum()
            w[over] = max_weight
            under = ~over
            w[under] += excess * w[under] / w[under].sum()
    return w


def risk_contributions(weights: pd.Series, cov: pd.DataFrame) -> pd.Series:
    w = weights.reindex(cov.index).fillna(0.0).to_numpy()
    c = cov.to_numpy()
    port_var = float(w @ c @ w)
    mrc = c @ w
    return pd.Series(w * mrc / port_var, index=cov.index)


def risk_parity_weights(cov: pd.DataFrame, tol: float = 1e-10, max_iter: int = 10_000) -> pd.Series:
    """Equal-risk-contribution weights (long only) via multiplicative updates."""
    c = cov.to_numpy()
    n = c.shape[0]
    w = np.full(n, 1.0 / n)
    for _ in range(max_iter):
        mrc = c @ w
        rc = w * mrc
        target = rc.mean()
        w_new = w * (target / np.maximum(rc, 1e-18)) ** 0.5
        w_new /= w_new.sum()
        if np.max(np.abs(w_new - w)) < tol:
            w = w_new
            break
        w = w_new
    return pd.Series(w, index=cov.index)


def annual_cov(prices: pd.DataFrame, window: int = 252) -> pd.DataFrame:
    r = prices.pct_change(fill_method=None).iloc[-window:].dropna(how="all")
    return r.cov() * TD


def vol_target_exposure(returns: pd.Series, target_vol: float, window: int = 63, cap: float = 1.0) -> float:
    """Exposure that would have hit ``target_vol`` given recent realised volatility."""
    realised = returns.dropna().iloc[-window:].std(ddof=1) * math.sqrt(TD)
    if not realised or math.isnan(realised):
        return cap
    return float(min(cap, target_vol / realised))


def allocate(capital: float, weights: pd.Series, prices: pd.Series, fractional: bool = False) -> pd.DataFrame:
    """Turn weights into dollar amounts and share counts."""
    w = weights[weights > 0]
    px = prices.reindex(w.index)
    dollars = w * capital
    shares = dollars / px if fractional else np.floor(dollars / px)
    spent = shares * px
    out = pd.DataFrame({"weight": w, "price": px, "target_$": dollars, "shares": shares, "cost_$": spent})
    out.loc["CASH", "cost_$"] = capital - spent.sum()
    return out
