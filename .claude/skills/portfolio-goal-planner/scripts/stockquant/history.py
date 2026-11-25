"""Long-run S&P 500 base rates from Robert Shiller's monthly data.

How often did the index itself turn $1 into $50 over N years? Uses the
public mirror of Shiller's dataset (prices, dividends, CPI since 1871) and
builds a monthly total-return index (dividends reinvested, no costs/taxes).
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
import requests

from .data import PKG_ROOT, USER_AGENT

SHILLER_URL = "https://raw.githubusercontent.com/datasets/s-and-p-500/main/data/data.csv"
CACHE = PKG_ROOT / "data" / "shiller_sp500.csv"


def load_shiller(path: Path | None = None, refresh: bool = False) -> pd.DataFrame:
    p = Path(path or CACHE)
    if refresh or not p.exists():
        r = requests.get(SHILLER_URL, headers={"User-Agent": USER_AGENT}, timeout=60)
        r.raise_for_status()
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(r.content)
    df = pd.read_csv(p, parse_dates=["Date"]).set_index("Date").sort_index()
    # Later rows carry price only; keep months with dividends and CPI.
    return df[(df["Dividend"] > 0) & (df["Consumer Price Index"] > 0)]


def total_return_index(df: pd.DataFrame) -> tuple[pd.Series, pd.Series]:
    """Nominal and real (CPI-deflated) monthly total-return indices."""
    price, div = df["SP500"], df["Dividend"]
    r = (price + div / 12.0) / price.shift(1) - 1.0  # Shiller dividends are annual rates
    tr = (1.0 + r.fillna(0.0)).cumprod()
    cpi = df["Consumer Price Index"]
    real = tr / (cpi / cpi.iloc[0])
    return tr, real


def window_stats(index: pd.Series, years=(10, 20, 30, 40, 50), start: str = "1926-01-01", target: float = 50.0) -> pd.DataFrame:
    """Distribution of N-year multiples for every monthly start date from ``start``."""
    rows = []
    for y in years:
        k = 12 * y
        mult = (index.shift(-k) / index).loc[start:].dropna()
        if mult.empty:
            continue
        rows.append(
            {
                "years": y,
                "windows": int(len(mult)),
                "first_start": str(mult.index[0].date()),
                "last_start": str(mult.index[-1].date()),
                "share_reaching_target": float((mult >= target).mean()),
                "median_multiple": float(mult.median()),
                "worst_multiple": float(mult.min()),
                "best_multiple": float(mult.max()),
                "median_cagr": float(mult.median() ** (1 / y) - 1),
                "worst_cagr": float(mult.min() ** (1 / y) - 1),
                "best_cagr": float(mult.max() ** (1 / y) - 1),
            }
        )
    return pd.DataFrame(rows)


def base_rates(path: Path | None = None, refresh: bool = False, target: float = 50.0) -> dict:
    df = load_shiller(path, refresh)
    nominal, real = total_return_index(df)
    out = {"source": SHILLER_URL, "first": str(df.index[0].date()), "last": str(df.index[-1].date())}
    for label, idx in (("nominal", nominal), ("real", real)):
        tbl = window_stats(idx, target=target)
        tbl.insert(0, "basis", label)
        out[label] = tbl
        span = idx.loc["1926-01-01":]
        yrs = (span.index[-1] - span.index[0]).days / 365.25
        out[f"cagr_since_1926_{label}"] = float((span.iloc[-1] / span.iloc[0]) ** (1 / yrs) - 1)
    return out
