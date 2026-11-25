"""Goal math for "how long / how likely is a 50x?".

* Deterministic compounding: years to a multiple, required CAGR, future value
  of a lump sum plus monthly contributions.
* Monte Carlo: lognormal (optionally fat-tailed) or block-bootstrapped
  historical monthly returns, with contributions, reporting the probability
  of hitting a multiple and the drawdowns you would sit through on the way.

Parameter convention: ``mean`` is the expected *arithmetic* annual return and
``vol`` the annual standard deviation of simple returns. The median outcome
compounds at roughly ``mean - vol**2 / 2`` (volatility drag), which is why a
higher-volatility bet needs a much higher mean just to match a calmer one.
"""
from __future__ import annotations

import math
from dataclasses import dataclass

import numpy as np
import pandas as pd


def _norm_cdf(z: float) -> float:
    return 0.5 * (1.0 + math.erf(z / math.sqrt(2.0)))


def years_to_multiple(multiple: float, annual_return: float) -> float:
    if annual_return <= 0:
        return float("inf")
    return math.log(multiple) / math.log1p(annual_return)


def required_cagr(multiple: float, years: float) -> float:
    return multiple ** (1.0 / years) - 1.0


def lognormal_params(mean: float, vol: float) -> tuple[float, float]:
    """Annual log-return (mu, sigma) matching arithmetic mean/vol of gross returns."""
    g = 1.0 + mean
    sigma2 = math.log(1.0 + (vol / g) ** 2)
    return math.log(g) - sigma2 / 2.0, math.sqrt(sigma2)


def median_cagr(mean: float, vol: float) -> float:
    mu, _ = lognormal_params(mean, vol)
    return math.exp(mu) - 1.0


def prob_lump_sum_multiple(mean: float, vol: float, multiple: float, years: float) -> float:
    """P(lump sum grows >= multiple x in ``years``) under i.i.d. lognormal returns."""
    mu, sig = lognormal_params(mean, vol)
    z = (math.log(multiple) - mu * years) / (sig * math.sqrt(years))
    return float(1.0 - _norm_cdf(z))


def future_value(
    initial: float,
    monthly: float,
    years: float,
    annual_return: float,
    contrib_growth: float = 0.0,
) -> dict:
    """Deterministic value with monthly contributions made at the start of each month."""
    months = int(round(years * 12))
    rm = (1.0 + annual_return) ** (1.0 / 12) - 1.0
    w, contributed = float(initial), float(initial)
    for m in range(months):
        c = monthly * (1.0 + contrib_growth) ** (m // 12)
        w = (w + c) * (1.0 + rm)
        contributed += c
    return {
        "final": w,
        "contributed": contributed,
        "multiple_on_contributed": w / contributed if contributed else float("nan"),
        "multiple_on_initial": w / initial if initial else float("nan"),
    }


def kelly_fraction(mean: float, vol: float, rf: float = 0.0) -> float:
    """Continuous-time growth-optimal fraction (mean - rf) / vol^2.

    It assumes the inputs are *known*; with estimation error, practitioners use
    a quarter to half of it. Values above 1 imply leverage.
    """
    return (mean - rf) / (vol**2) if vol > 0 else float("nan")


@dataclass
class SimResult:
    terminal: np.ndarray
    contributed: float
    years: int
    pct_paths: pd.DataFrame  # wealth percentiles by year
    max_dd: np.ndarray  # worst drawdown of the investment itself, per path
    params: dict

    def prob_multiple_of_contributions(self, k: float) -> float:
        return float(np.mean(self.terminal >= k * self.contributed))

    def prob_at_least(self, amount: float) -> float:
        return float(np.mean(self.terminal >= amount))

    def summary(self, multiples=(2, 5, 10, 20, 50)) -> dict:
        q = np.percentile(self.terminal, [5, 10, 25, 50, 75, 90, 95])
        out = {
            "years": self.years,
            "contributed": self.contributed,
            "p5": q[0], "p10": q[1], "p25": q[2], "median": q[3], "p75": q[4], "p90": q[5], "p95": q[6],
            "mean": float(np.mean(self.terminal)),
            "prob_loss": float(np.mean(self.terminal < self.contributed)),
            "median_max_drawdown": float(np.median(self.max_dd)),
            "prob_drawdown_worse_50pct": float(np.mean(self.max_dd <= -0.5)),
        }
        for k in multiples:
            out[f"prob_{k}x"] = self.prob_multiple_of_contributions(k)
        out.update(self.params)
        return out


def _monthly_draws(
    rng: np.random.Generator,
    n: int,
    months: int,
    mean: float | None,
    vol: float | None,
    hist_monthly: np.ndarray | None,
    block: int,
    t_df: float | None,
) -> np.ndarray:
    if hist_monthly is not None:
        h = np.asarray(hist_monthly, dtype="float64")
        h = h[~np.isnan(h)]
        if len(h) < block + 1:
            raise ValueError("historical sample too short for block bootstrap")
        n_blocks = math.ceil(months / block)
        starts = rng.integers(0, len(h) - block + 1, size=(n, n_blocks))
        offs = np.arange(block)
        idx = (starts[:, :, None] + offs[None, None, :]).reshape(n, -1)[:, :months]
        return h[idx]
    mu, sig = lognormal_params(mean, vol)
    mu_m, sig_m = mu / 12.0, sig / math.sqrt(12.0)
    if t_df and t_df > 2:
        z = rng.standard_t(t_df, size=(n, months)) / math.sqrt(t_df / (t_df - 2.0))
    else:
        z = rng.standard_normal(size=(n, months))
    return np.expm1(mu_m + sig_m * z)


def simulate(
    initial: float,
    monthly: float,
    years: int,
    *,
    mean: float | None = None,
    vol: float | None = None,
    hist_monthly: np.ndarray | pd.Series | None = None,
    block: int = 12,
    t_df: float | None = None,
    fee: float = 0.0,
    contrib_growth: float = 0.0,
    n_paths: int = 20_000,
    seed: int = 7,
    chunk: int = 5_000,
) -> SimResult:
    """Monte Carlo of wealth with monthly contributions (start of month).

    Supply either (mean, vol) for a parametric model or ``hist_monthly`` for a
    block bootstrap of historical monthly returns. ``fee`` is an annual cost.
    """
    if hist_monthly is None and (mean is None or vol is None):
        raise ValueError("give mean & vol, or hist_monthly")
    months = int(years * 12)
    rng = np.random.default_rng(seed)
    contrib = np.array([monthly * (1.0 + contrib_growth) ** (m // 12) for m in range(months)])
    fee_m = (1.0 + fee) ** (1.0 / 12) - 1.0 if fee else 0.0
    hist = None if hist_monthly is None else np.asarray(hist_monthly, dtype="float64")

    terminals, maxdds, yearly = [], [], []
    done = 0
    while done < n_paths:
        n = min(chunk, n_paths - done)
        r = _monthly_draws(rng, n, months, mean, vol, hist, block, t_df) - fee_m
        r = np.maximum(r, -1.0)
        w = np.full(n, float(initial))
        ylev = np.empty((n, years))
        for m in range(months):
            w = (w + contrib[m]) * (1.0 + r[:, m])
            if (m + 1) % 12 == 0:
                ylev[:, (m + 1) // 12 - 1] = w
        idx = np.cumprod(1.0 + r, axis=1)
        peak = np.maximum.accumulate(np.concatenate([np.ones((n, 1)), idx], axis=1), axis=1)[:, 1:]
        maxdds.append(np.min(idx / peak - 1.0, axis=1))
        terminals.append(w)
        yearly.append(ylev)
        done += n
    terminal = np.concatenate(terminals)
    max_dd = np.concatenate(maxdds)
    ymat = np.concatenate(yearly)
    pct = pd.DataFrame(
        np.percentile(ymat, [5, 25, 50, 75, 95], axis=0).T,
        index=pd.RangeIndex(1, years + 1, name="year"),
        columns=["p5", "p25", "p50", "p75", "p95"],
    )
    params = {
        "model": "bootstrap" if hist is not None else ("student-t" if t_df else "lognormal"),
        "mean": mean,
        "vol": vol,
        "initial": initial,
        "monthly": monthly,
        "fee": fee,
        "n_paths": n_paths,
    }
    return SimResult(terminal, float(initial + contrib.sum()), years, pct, max_dd, params)


def horizon_table(
    multiple: float = 50.0,
    scenarios: dict[str, tuple[float, float]] | None = None,
    horizons=(10, 15, 20, 25, 30, 35, 40),
) -> pd.DataFrame:
    """P(lump sum reaches ``multiple``) by horizon for (mean, vol) scenarios."""
    rows = {}
    for name, (m, v) in (scenarios or {}).items():
        rows[name] = {f"{h}y": prob_lump_sum_multiple(m, v, multiple, h) for h in horizons}
        rows[name]["median_cagr"] = median_cagr(m, v)
        rows[name]["years_to_50x_at_median"] = years_to_multiple(multiple, median_cagr(m, v))
    return pd.DataFrame.from_dict(rows, orient="index")


def bootstrap_horizon_table(
    hist_monthly: dict[str, np.ndarray | pd.Series],
    multiple: float = 50.0,
    horizons=(10, 15, 20, 25, 30, 35, 40),
    n_paths: int = 20_000,
    block: int = 12,
    seed: int = 11,
) -> pd.DataFrame:
    """Same as :func:`horizon_table` but resampling actual monthly histories."""
    rows = {}
    for name, h in hist_monthly.items():
        arr = np.asarray(h, dtype="float64")
        arr = arr[~np.isnan(arr)]
        rng = np.random.default_rng(seed)
        months = max(horizons) * 12
        draws = _monthly_draws(rng, n_paths, months, None, None, arr, block, None)
        logcum = np.cumsum(np.log1p(np.maximum(draws, -0.999999)), axis=1)
        row = {f"{hz}y": float(np.mean(logcum[:, hz * 12 - 1] >= math.log(multiple))) for hz in horizons}
        geo = float(np.exp(np.mean(np.log1p(arr)) * 12) - 1)
        row["hist_cagr"] = geo
        row["hist_vol"] = float(np.std(arr, ddof=1) * math.sqrt(12))
        row["sample_years"] = round(len(arr) / 12, 1)
        rows[name] = row
    return pd.DataFrame.from_dict(rows, orient="index")
