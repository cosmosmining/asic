#!/usr/bin/env python3
"""Market regime check: where are stocks, bonds and volatility right now?

Usage
-----
  python regime_check.py                       # default dashboard
  python regime_check.py --extra SMH GRID URA  # add theme ETFs
  python regime_check.py --json /tmp/regime.json

Prints, for each index ETF: distance from its 52-week high, 1-month, YTD and
12-month returns, whether it is above its ~10-month (210-day) average (the
classic trend filter), and 1-month realized volatility. Adds VIX, sector
breadth (share of the 11 S&P sector ETFs above their 200-day average) and a
plain-language regime label based on the S&P 500.
"""
from __future__ import annotations

import argparse
import json
import math
import os
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
os.environ.setdefault("STOCKQUANT_CACHE", str(Path(tempfile.gettempdir()) / "stockquant-cache"))

from stockquant.data import PriceStore  # noqa: E402

CORE = ["SPY", "QQQ", "IWM", "EFA", "EEM", "TLT", "GLD", "BIL"]
SECTORS = ["XLK", "XLF", "XLE", "XLV", "XLI", "XLU", "XLP", "XLY", "XLB", "XLRE", "XLC"]


def pct(x, d=1):
    return "n/a" if x is None or (isinstance(x, float) and math.isnan(x)) else f"{x * 100:+.{d}f}%"


def label(dd: float, above: bool, vix: float | None) -> str:
    if dd <= -0.20:
        base = "Bear market (S&P 500 20%+ below its high)"
    elif dd <= -0.10:
        base = "Correction (S&P 500 10-20% below its high)"
    elif dd <= -0.05:
        base = "Pullback (S&P 500 5-10% below its high)"
    else:
        base = "Near highs"
    trend = "trend filter positive" if above else "trend filter negative (below ~10-month average)"
    fear = "" if vix is None else (", high fear (VIX > 25)" if vix > 25 else ", calm (VIX < 15)" if vix < 15 else "")
    return f"{base}; {trend}{fear}"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--extra", nargs="*", default=["SMH"], help="more tickers to include")
    ap.add_argument("--json")
    args = ap.parse_args()
    store = PriceStore()
    tick = list(dict.fromkeys(CORE + args.extra))
    px = store.prices(tick + SECTORS, calendar="SPY")
    if px.empty:
        print("No price data could be fetched:", json.dumps(store.errors))
        return 2
    rows = {}
    for t in tick:
        if t not in px.columns:
            continue
        s = px[t].dropna()
        if len(s) < 260:
            continue
        ytd = s.loc[: f"{s.index[-1].year - 1}-12-31"]
        r = s.pct_change(fill_method=None).dropna()
        rows[t] = {
            "dd_from_52w_high": float(s.iloc[-1] / s.iloc[-252:].max() - 1),
            "ret_1m": float(s.iloc[-1] / s.iloc[-22] - 1),
            "ret_ytd": float(s.iloc[-1] / ytd.iloc[-1] - 1) if len(ytd) else float("nan"),
            "ret_12m": float(s.iloc[-1] / s.iloc[-253] - 1),
            "above_10m_avg": bool(s.iloc[-1] > s.iloc[-210:].mean()),
            "vol_1m": float(r.iloc[-21:].std(ddof=1) * math.sqrt(252)),
        }
    vix = None
    try:
        v = store.history("^VIX")["close"].dropna()
        vix = {"last": float(v.iloc[-1]), "median_1y": float(v.iloc[-252:].median()), "max_1y": float(v.iloc[-252:].max())}
    except Exception as exc:  # noqa: BLE001
        print(f"(VIX unavailable: {exc})")
    flags = [bool(px[t].dropna().iloc[-1] > px[t].dropna().iloc[-200:].mean()) for t in SECTORS if t in px.columns and px[t].dropna().size >= 200]
    breadth = sum(flags) / len(flags) if flags else float("nan")
    asof = str(px.index[-1].date())

    print(f"# Market regime as of {asof}\n")
    print("| Ticker | From 52w high | 1m | YTD | 12m | Above 10m avg | 1m vol |\n|---|---:|---:|---:|---:|---|---:|")
    for t, r in rows.items():
        print(f"| {t} | {pct(r['dd_from_52w_high'])} | {pct(r['ret_1m'])} | {pct(r['ret_ytd'])} | {pct(r['ret_12m'])} | "
              f"{'yes' if r['above_10m_avg'] else 'no'} | {pct(r['vol_1m'], 0)} |")
    if vix:
        print(f"\nVIX {vix['last']:.1f} (1-year median {vix['median_1y']:.1f}, 1-year high {vix['max_1y']:.1f})")
    print(f"Sector breadth: {sum(flags)}/{len(flags)} S&P sector ETFs above their 200-day average ({pct(breadth, 0)})")
    if "SPY" in rows:
        lab = label(rows["SPY"]["dd_from_52w_high"], rows["SPY"]["above_10m_avg"], vix["last"] if vix else None)
        print(f"\nRegime: {lab}")
    if args.json:
        Path(args.json).write_text(json.dumps({"asof": asof, "indices": rows, "vix": vix, "sector_breadth": breadth}, indent=1))
        print(f"JSON -> {args.json}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
