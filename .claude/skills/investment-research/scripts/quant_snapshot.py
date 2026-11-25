#!/usr/bin/env python3
"""Price-based quant snapshot for stocks/ETFs: trend, momentum, risk and a peer score.

Usage
-----
  python quant_snapshot.py NVDA AVGO --peers AMD TSM MRVL --bench SPY
  python quant_snapshot.py VRT --years 5 --json /tmp/vrt.json
  python quant_snapshot.py GEV ETN --fundamentals      # adds yfinance valuation (needs open internet)

What it prints for each ticker
------------------------------
* trend state (strong uptrend / pullback / recovering / weakening / downtrend /
  pinned-to-a-deal), returns over 1m/3m/12m, 12-1 momentum, distance from the
  52-week high and from the 200-day average
* risk: 1y volatility, worst 1y drop, beta and correlation to the benchmark,
  and the worst drawdown in its full history with peak/trough/recovery dates
* N-year window stats: CAGR, volatility, Sharpe, max drawdown vs the benchmark
* a 0-100 composite score ranked against the tickers + peers you pass
  (strong, orderly trend = high; it says nothing about valuation)

Data: Yahoo Finance daily adjusted closes (public chart endpoint, yfinance as a
fallback), cached in $STOCKQUANT_CACHE (default <tmp>/stockquant-cache).
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

import pandas as pd  # noqa: E402

from stockquant import metrics as M  # noqa: E402
from stockquant import signals as S  # noqa: E402
from stockquant.data import PriceStore  # noqa: E402


def pct(x, d=1):
    return "n/a" if x is None or (isinstance(x, float) and math.isnan(x)) else f"{x * 100:+.{d}f}%"


def num(x, d=2):
    return "n/a" if x is None or (isinstance(x, float) and math.isnan(x)) else f"{x:.{d}f}"


def fundamentals(ticker: str) -> dict:
    try:
        import yfinance as yf

        info = yf.Ticker(ticker).info or {}
    except Exception as exc:  # noqa: BLE001
        return {"error": f"{type(exc).__name__}: {exc}"[:200]}
    keys = {
        "marketCap": "market_cap", "forwardPE": "fwd_pe", "trailingPE": "trailing_pe",
        "enterpriseToRevenue": "ev_sales", "revenueGrowth": "rev_growth", "grossMargins": "gross_margin",
        "operatingMargins": "op_margin", "freeCashflow": "fcf", "totalDebt": "debt", "totalCash": "cash",
    }
    return {v: info.get(k) for k, v in keys.items()}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("tickers", nargs="+", help="Yahoo symbols, e.g. NVDA BRK-B 6501.T")
    ap.add_argument("--peers", nargs="*", default=[], help="extra tickers to rank against")
    ap.add_argument("--bench", default="SPY")
    ap.add_argument("--preset", default="balanced", choices=list(S.PRESETS))
    ap.add_argument("--years", type=float, default=5.0, help="window for CAGR/Sharpe/drawdown stats")
    ap.add_argument("--fundamentals", action="store_true", help="add yfinance valuation fields")
    ap.add_argument("--cache-dir", help="where downloaded prices are cached (default <tmp>/stockquant-cache)")
    ap.add_argument("--json", help="also write results to this JSON file")
    args = ap.parse_args()
    if args.cache_dir:
        os.environ["STOCKQUANT_CACHE"] = args.cache_dir

    store = PriceStore()
    names = list(dict.fromkeys(args.tickers))
    universe = list(dict.fromkeys(names + args.peers + [args.bench]))
    px = store.prices(universe, calendar=args.bench)
    if px.empty:
        print("No price data could be fetched. Errors:", json.dumps(store.errors, indent=1))
        print("Fall back to web sources for prices and say the quant snapshot was unavailable.")
        return 2
    close = store.panel(universe, "close")
    vol = store.panel(universe, "volume")
    bench = args.bench if args.bench in px.columns else None
    feat = S.features_table(px, bench=bench, volume=vol, close=close)
    pool = [t for t in names + args.peers if t in feat.index]
    scored = S.composite_scores(feat.loc[pool], args.preset) if pool else feat.iloc[0:0]

    out = {"asof": str(px.index[-1].date()), "bench": bench, "preset": args.preset, "errors": store.errors, "tickers": {}}
    print(f"Quant snapshot as of {out['asof']} (benchmark {bench or 'none'}, score preset '{args.preset}', ranked among {len(pool)} names)\n")
    for t in names:
        if t not in px.columns:
            print(f"## {t}: no price data ({store.errors.get(t, 'unknown error')})\n")
            continue
        s = px[t].dropna()
        f = scored.loc[t] if t in scored.index else feat.loc[t]
        start = s.index[-1] - pd.DateOffset(years=args.years)
        win = s.loc[start:]
        st = M.summarize(win, bench=px[bench].loc[start:] if bench else None)
        dd_all = M.max_drawdown_info(s)
        rank = int(list(scored.index).index(t)) + 1 if t in scored.index else None
        rec = {
            "last_close_date": f.get("last_date"), "price": f.get("price"), "history_years": f.get("history_years"),
            "trend_state": f.get("trend_state"), "extended_above_200d": f.get("extended"), "pinned_to_deal": f.get("pinned"),
            "ret_1m": f.get("ret_1m"), "ret_3m": f.get("ret_3m"), "ret_12m": f.get("ret_12m"), "mom_12_1": f.get("mom_12_1"),
            "dd_from_52w_high": f.get("dd_from_high"), "gap_to_200d": f.get("sma200_gap"),
            "vol_1y": f.get("vol_1y"), "maxdd_1y": f.get("maxdd_1y"), "beta_1y": f.get("beta_1y"), "corr_1y": f.get("corr_1y"),
            "rel_strength_12m": f.get("rel_strength_12m"), "cagr_3y": f.get("cagr_3y"), "cagr_5y": f.get("cagr_5y"),
            "score": f.get("score"), "grade": f.get("grade"), "rank": rank, "of": len(pool),
            "window": {k: st.get(k) for k in ("start", "end", "years", "cagr", "vol", "sharpe", "max_drawdown", "beta", "up_capture", "down_capture")},
            "worst_drawdown_full_history": dd_all,
        }
        if args.fundamentals:
            rec["fundamentals"] = fundamentals(t)
        out["tickers"][t] = rec

        w = rec["window"]
        print(f"## {t}  close {num(rec['price'])} on {rec['last_close_date']}  ({rec['history_years']} yrs of data)")
        print(f"- Trend: {rec['trend_state']}; {pct(rec['gap_to_200d'])} vs 200-day avg; {pct(rec['dd_from_52w_high'])} from 52-week high"
              + ("; EXTENDED (>40% above 200-day)" if rec["extended_above_200d"] else "")
              + ("; PINNED near a fixed price (likely pending takeover)" if rec["pinned_to_deal"] else ""))
        print(f"- Returns: 1m {pct(rec['ret_1m'])}, 3m {pct(rec['ret_3m'])}, 12m {pct(rec['ret_12m'])}; 12-1 momentum {pct(rec['mom_12_1'])}; "
              f"vs {bench} 12m {pct(rec['rel_strength_12m'])}")
        print(f"- Risk: 1y vol {pct(rec['vol_1y'], 0)}, worst 1y drop {pct(rec['maxdd_1y'], 0)}, beta {num(rec['beta_1y'])}, corr {num(rec['corr_1y'])}")
        print(f"- {w['years']}-yr window from {w['start']}: CAGR {pct(w['cagr'])}, vol {pct(w['vol'], 0)}, Sharpe {num(w['sharpe'])}, "
              f"max drawdown {pct(w['max_drawdown'], 0)}")
        print(f"- Worst drawdown in full history: {pct(dd_all['depth'], 0)} (peak {dd_all['peak']}, trough {dd_all['trough']}, "
              f"recovered {dd_all['recovery'] or 'not yet'})")
        if rank:
            print(f"- Composite score {num(rec['score'], 1)} (grade {rec['grade']}), rank {rank} of {len(pool)}")
        if args.fundamentals:
            fu = rec["fundamentals"]
            if "error" in fu:
                print(f"- Fundamentals unavailable: {fu['error']}")
            else:
                print(f"- Valuation (yfinance): fwd P/E {num(fu.get('fwd_pe'), 1)}, EV/sales {num(fu.get('ev_sales'), 1)}, "
                      f"revenue growth {pct(fu.get('rev_growth'))}, op margin {pct(fu.get('op_margin'))}")
        print()
    if store.errors:
        print("Skipped tickers:", json.dumps(store.errors))
    if args.json:
        Path(args.json).write_text(json.dumps(out, indent=1, default=str))
        print(f"JSON -> {args.json}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
