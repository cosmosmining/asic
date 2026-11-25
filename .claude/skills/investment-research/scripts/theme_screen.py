#!/usr/bin/env python3
"""Screen an investment theme: rank its names and measure the theme basket.

Usage
-----
  python theme_screen.py --name "Grid equipment" --tickers GEV ETN PWR HUBB VRT POWL --compare QQQ SMH
  python theme_screen.py --name "Optical interconnect" --tickers COHR LITE CIEN FN AAOI --json /tmp/optics.json

Output
------
1. Ranked table: composite score, trend state, 12m return, distance from high,
   volatility, worst 1y drop, beta, pinned/extended flags.
2. Equal-weight basket (daily rebalanced) vs benchmark(s): YTD, 1y, 3y CAGR,
   volatility, drawdown now and worst 3y drawdown, beta and correlation.
3. Breadth (share of names above their 200-day average) and crowding (average
   pairwise correlation of daily returns over 1 year: near 1 means the names
   trade as one bet).
4. Basket backtest since the date at least 3 names had a year of history.
   The list is chosen today, so this is hindsight-biased: an upper bound.
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

import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

from stockquant import metrics as M  # noqa: E402
from stockquant import signals as S  # noqa: E402
from stockquant.data import PriceStore  # noqa: E402


def pct(x, d=1):
    return "n/a" if x is None or (isinstance(x, float) and math.isnan(x)) else f"{x * 100:+.{d}f}%"


def basket_stats(idx: pd.Series, bench: pd.Series | None) -> dict:
    idx = idx.dropna()
    last = idx.iloc[-1]
    ytd_base = idx.loc[: f"{idx.index[-1].year - 1}-12-31"]
    r = M.returns_from(idx).dropna()
    out = {
        "start": str(idx.index[0].date()),
        "ret_ytd": float(last / ytd_base.iloc[-1] - 1) if len(ytd_base) else float("nan"),
        "ret_1y": float(last / idx.iloc[-253] - 1) if len(idx) > 253 else float("nan"),
        "cagr_3y": float((last / idx.iloc[-757]) ** (1 / 3) - 1) if len(idx) > 757 else float("nan"),
        "vol_1y": M.ann_vol(r.iloc[-252:]),
        "dd_now": float(last / idx.iloc[-252:].max() - 1),
        "maxdd_3y": M.max_drawdown(idx.iloc[-756:]),
    }
    if bench is not None:
        beta, corr = M.beta_corr(r.iloc[-252:], M.returns_from(bench.dropna()).dropna())
        out.update({"beta_1y": beta, "corr_1y": corr})
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--name", default="Theme")
    ap.add_argument("--tickers", nargs="+", required=True)
    ap.add_argument("--bench", default="SPY")
    ap.add_argument("--compare", nargs="*", default=["QQQ"], help="other benchmarks/ETFs to compare the basket with")
    ap.add_argument("--preset", default="balanced", choices=list(S.PRESETS))
    ap.add_argument("--cache-dir", help="where downloaded prices are cached (default <tmp>/stockquant-cache)")
    ap.add_argument("--json")
    args = ap.parse_args()
    if args.cache_dir:
        os.environ["STOCKQUANT_CACHE"] = args.cache_dir

    store = PriceStore()
    names = list(dict.fromkeys(args.tickers))
    refs = list(dict.fromkeys([args.bench] + args.compare))
    px_all = store.prices(names + refs, calendar=args.bench)
    if px_all.empty:
        print("No price data could be fetched:", json.dumps(store.errors))
        return 2
    close = store.panel(names, "close")
    vol = store.panel(names, "volume")
    bench = px_all[args.bench] if args.bench in px_all else None
    avail = [t for t in names if t in px_all.columns]
    feat = S.features_table(px_all[avail + ([args.bench] if bench is not None else [])], bench=args.bench if bench is not None else None,
                            volume=vol, close=close).loc[avail]
    scored = S.composite_scores(feat, args.preset)
    asof = str(px_all.index[-1].date())

    print(f"# {args.name}: theme screen as of {asof}\n")
    print("| # | Ticker | Score | Trend | 12m | From high | Vol 1y | Worst 1y | Beta | Flags |")
    print("|---:|---|---:|---|---:|---:|---:|---:|---:|---|")
    rows = []
    for i, (t, r) in enumerate(scored.iterrows(), 1):
        flags = ", ".join(x for x, on in (("extended", r.get("extended")), ("pinned", r.get("pinned")), ("young", (r.get("history_years") or 0) < 1)) if on)
        print(f"| {i} | {t} | {r['score']:.1f} | {r.get('trend_state')} | {pct(r.get('ret_12m'))} | {pct(r.get('dd_from_high'))} | "
              f"{pct(r.get('vol_1y'), 0)} | {pct(r.get('maxdd_1y'), 0)} | {r.get('beta_1y', float('nan')):.2f} | {flags} |")
        rows.append({"ticker": t, **{k: (None if isinstance(v, float) and math.isnan(v) else v) for k, v in r.items()}})

    idx = S.theme_index(px_all, avail, min_members=min(3, len(avail)))
    ref_stats = {}
    print("\n## Basket vs references (equal weight, daily rebalanced)\n")
    print("| Series | YTD | 1y | 3y CAGR | Vol 1y | From 1y high | Worst 3y | Beta | Corr |")
    print("|---|---:|---:|---:|---:|---:|---:|---:|---:|")
    series = {f"{args.name} basket": idx} | {t: px_all[t] for t in refs if t in px_all}
    for lab, s in series.items():
        if s is None or s.dropna().empty:
            continue
        st = basket_stats(s, bench)
        ref_stats[lab] = st
        print(f"| {lab} | {pct(st['ret_ytd'])} | {pct(st['ret_1y'])} | {pct(st['cagr_3y'])} | {pct(st['vol_1y'], 0)} | "
              f"{pct(st['dd_now'])} | {pct(st['maxdd_3y'], 0)} | {st.get('beta_1y', float('nan')):.2f} | {st.get('corr_1y', float('nan')):.2f} |")

    above = [bool(px_all[t].dropna().iloc[-1] > px_all[t].dropna().iloc[-200:].mean()) for t in avail if px_all[t].dropna().size >= 200]
    rets = px_all[avail].pct_change(fill_method=None).iloc[-252:]
    corr = rets.corr(min_periods=120).to_numpy()
    iu = np.triu_indices_from(corr, k=1)
    avg_corr = float(np.nanmean(corr[iu])) if len(avail) > 1 else float("nan")
    print(f"\nBreadth: {sum(above)}/{len(above)} names above their 200-day average. "
          f"Crowding: average pairwise 1y correlation {avg_corr:.2f} (near 1 = one bet).")

    bt = {}
    if len(idx) > 260:
        b = bench.loc[idx.index[0]:] if bench is not None else None
        st = M.summarize(idx, bench=b)
        bt = {k: st.get(k) for k in ("start", "years", "cagr", "vol", "sharpe", "max_drawdown", "multiple")}
        bst = M.summarize(b) if b is not None else {}
        print(f"\nBasket since {bt['start']} ({bt['years']} yrs): CAGR {pct(bt['cagr'])}, vol {pct(bt['vol'], 0)}, max drawdown {pct(bt['max_drawdown'], 0)}, "
              f"{bt['multiple']:.1f}x" + (f"; {args.bench} same period: CAGR {pct(bst.get('cagr'))}, max drawdown {pct(bst.get('max_drawdown'), 0)}" if bst else ""))
        print("Hindsight warning: this list was chosen today, so names that failed are missing. Treat the backtest as an upper bound.")
    if store.errors:
        print("\nSkipped tickers:", json.dumps(store.errors))
    if args.json:
        Path(args.json).write_text(json.dumps({"asof": asof, "name": args.name, "ranked": rows, "baskets": ref_stats,
                                               "breadth_above_200d": [sum(above), len(above)], "avg_pairwise_corr": avg_corr,
                                               "basket_backtest": bt, "errors": store.errors}, indent=1, default=str))
        print(f"JSON -> {args.json}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
