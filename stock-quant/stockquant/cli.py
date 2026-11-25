"""Command line interface: ``python -m stockquant <command> ...``"""
from __future__ import annotations

import argparse
import json
import logging
import sys

import pandas as pd

from . import goal as G
from . import metrics as M
from . import signals as S
from . import strategies as ST
from . import universe as U
from .backtest import run_backtest
from .data import PriceStore

pd.set_option("display.width", 200)
pd.set_option("display.max_columns", 30)
pd.set_option("display.max_rows", 200)


def _store(args) -> PriceStore:
    return PriceStore(offline=getattr(args, "offline", False))


def _groups(arg: str | None) -> list[str]:
    if not arg or arg == "ai":
        return U.AI_GROUPS if arg == "ai" else list(U.GROUP_LABELS)
    return [g.strip() for g in arg.split(",")]


def cmd_fetch(args) -> int:
    store = _store(args)
    tick = args.tickers or U.tickers(_groups(args.groups))
    for t in tick:
        try:
            df = store.history(t, refresh=args.refresh)
            print(f"{t:10s} {len(df):6d} rows  {df.index[0].date()} -> {df.index[-1].date()}")
        except Exception as exc:  # noqa: BLE001
            print(f"{t:10s} FAILED: {exc}")
    return 0


def cmd_screen(args) -> int:
    store = _store(args)
    members = args.tickers or U.tickers(_groups(args.group))
    cols = list(dict.fromkeys(members + ["SPY"]))
    px = store.prices(cols)
    close = store.panel(cols, "close")
    vol = store.panel(cols, "volume")
    feat = S.features_table(px, bench="SPY", volume=vol, close=close)
    feat = feat.loc[[m for m in members if m in feat.index]]
    scored = S.composite_scores(feat, args.preset)
    from .report import load_fundamentals

    scored = S.apply_fundamentals(scored, load_fundamentals())
    meta = U.meta()
    scored = scored.join(meta[["theme", "stage"]], how="left")
    show = ["theme", "stage", "score", "grade", "trend_state", "ret_12m", "mom_12_1", "vol_1y", "maxdd_1y", "dd_from_high"]
    if "valuation_flag" in scored:
        show += ["valuation_flag", "fwd_pe"]
    out = scored[[c for c in show if c in scored.columns]].head(args.top)
    fmt = {c: "{:.1%}".format for c in ("ret_12m", "mom_12_1", "vol_1y", "maxdd_1y", "dd_from_high")}
    print(out.to_string(formatters=fmt))
    if args.csv:
        scored.to_csv(args.csv)
        print(f"\nfull table -> {args.csv}")
    return 0


def cmd_backtest(args) -> int:
    store = _store(args)
    universe = args.tickers or [t for t in U.tickers(_groups(args.group)) if "." not in t]
    needed = list(dict.fromkeys(universe + ["SPY", "BIL", "VTI"]))
    px = store.prices(needed)
    px = px.reindex(px["SPY"].dropna().index).ffill(limit=5)
    if args.strategy == "momentum":
        fn = ST.momentum_top_n(universe, n=args.top, lookback=args.lookback, rank_by=args.rank_by,
                               weighting=args.weighting, max_weight=args.max_weight,
                               trend_sma=None if args.no_trend else 200)
    elif args.strategy == "equal":
        fn = ST.equal_weight(universe, min_history=21)
    elif args.strategy == "invvol":
        fn = ST.inverse_vol(universe, max_weight=args.max_weight)
    elif args.strategy == "trend":
        fn = ST.trend_filter({t: 1.0 / len(universe) for t in universe})
    else:
        raise SystemExit(f"unknown strategy {args.strategy}")
    if args.core:
        fn = ST.blend([(ST.fixed_weights({args.core: 1.0}), 1 - args.satellite), (fn, args.satellite)])
    res = run_backtest(px, fn, start=args.start, cost_bps=args.cost_bps, name=args.strategy, bench=px["SPY"])
    spy = run_backtest(px, ST.fixed_weights({"SPY": 1.0}), start=args.start, freq=None, name="SPY", bench=px["SPY"])
    table = pd.DataFrame({res.name: res.stats, "SPY": spy.stats})
    print(table.to_string())
    print("\nCalendar-year returns:")
    print(pd.DataFrame({res.name: res.yearly(), "SPY": spy.yearly()}).map(lambda x: f"{x:.1%}").to_string())
    print("\nLatest target weights:")
    print(res.weights.iloc[-1][res.weights.iloc[-1] > 1e-6].sort_values(ascending=False).map(lambda x: f"{x:.1%}").to_string())
    return 0


def cmd_goal(args) -> int:
    print(f"CAGR needed for {args.multiple:g}x in {args.years} years: {G.required_cagr(args.multiple, args.years):.1%}")
    if args.bootstrap:
        store = _store(args)
        s = store.prices([args.bootstrap])[args.bootstrap].dropna()
        hist = M.monthly_returns(s).to_numpy()
        sim = G.simulate(args.initial, args.monthly, args.years, hist_monthly=hist, fee=args.fee,
                         contrib_growth=args.raise_pct, n_paths=args.paths)
        print(f"Model: block bootstrap of {args.bootstrap} monthly returns ({len(hist) / 12:.0f} years of history)")
    else:
        sim = G.simulate(args.initial, args.monthly, args.years, mean=args.mean, vol=args.vol, t_df=args.t_df,
                         fee=args.fee, contrib_growth=args.raise_pct, n_paths=args.paths)
        print(f"Model: mean {args.mean:.1%}, vol {args.vol:.1%} -> median CAGR {G.median_cagr(args.mean, args.vol):.2%} "
              f"(Kelly fraction vs 3.5% cash: {G.kelly_fraction(args.mean, args.vol, 0.035):.2f})")
    s = sim.summary()
    print(f"Contributed: ${s['contributed']:,.0f}")
    for k in ("p5", "p25", "median", "p75", "p95"):
        print(f"  {k:>6}: ${s[k]:,.0f}  ({s[k] / s['contributed']:.1f}x contributions)")
    for k in (2, 5, 10, 20, 50):
        print(f"  P(>= {k}x contributions): {s[f'prob_{k}x']:.1%}")
    print(f"  P(lose money): {s['prob_loss']:.1%}   median worst drawdown: {s['median_max_drawdown']:.0%}   "
          f"P(drawdown worse than -50%): {s['prob_drawdown_worse_50pct']:.0%}")
    return 0


def cmd_metrics(args) -> int:
    store = _store(args)
    px = store.prices(list(dict.fromkeys(args.tickers + ["SPY"])))
    rows = {}
    for t in args.tickers:
        s = px[t].dropna().loc[args.start:]
        rows[t] = M.summarize(s, bench=px["SPY"].loc[args.start:])
    df = pd.DataFrame(rows)
    print(df.to_string())
    return 0


def cmd_fundamentals(args) -> int:
    """Refresh data/fundamentals.csv with yfinance (works on a normal internet connection)."""
    try:
        import yfinance as yf
    except ImportError:
        print("pip install yfinance first")
        return 1
    from datetime import date

    from .report import FUNDAMENTALS_CSV

    tick = args.tickers or [t for t in U.tickers(["power_grid", "compute", "edge_emerging", "compounder"])]
    rows = []
    for t in tick:
        try:
            info = yf.Ticker(t).info or {}
        except Exception as exc:  # noqa: BLE001
            print(f"{t:10s} FAILED: {exc}")
            continue
        op = info.get("operatingMargins")
        rows.append({
            "ticker": t,
            "fwd_pe": info.get("forwardPE"),
            "trailing_pe": info.get("trailingPE"),
            "ev_sales": info.get("enterpriseToRevenue"),
            "rev_growth": info.get("revenueGrowth"),
            "op_margin": op,
            "profitable": None if op is None else op > 0,
            "mcap_usd_bn": (info.get("marketCap") or 0) / 1e9 or None,
            "as_of": str(date.today()),
            "source": "yfinance Ticker.info",
        })
        print(f"{t:10s} fwdPE={rows[-1]['fwd_pe']} EV/S={rows[-1]['ev_sales']} growth={rows[-1]['rev_growth']}")
    if rows:
        pd.DataFrame(rows).to_csv(FUNDAMENTALS_CSV, index=False)
        print(f"{len(rows)} rows -> {FUNDAMENTALS_CSV}")
    return 0


def cmd_report(args) -> int:
    from .report import build_report

    payload = build_report(_store(args), refresh=args.refresh)
    print(f"report written: output/results.json, output/SUMMARY.md (as of {payload['asof']})")
    if payload["data_errors"]:
        print("tickers skipped:", json.dumps(payload["data_errors"], indent=1))
    return 0


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="stockquant", description="Quant research toolkit for long-term investors")
    p.add_argument("--offline", action="store_true", help="use cached prices only")
    p.add_argument("-v", "--verbose", action="store_true")
    sub = p.add_subparsers(dest="cmd", required=True)

    f = sub.add_parser("fetch", help="download/refresh price history into the cache")
    f.add_argument("--groups", help="comma list of groups (default: all); 'ai' for AI groups")
    f.add_argument("--tickers", nargs="*")
    f.add_argument("--refresh", action="store_true")
    f.set_defaults(fn=cmd_fetch)

    s = sub.add_parser("screen", help="rank a universe by the composite score")
    s.add_argument("--group", default="ai", help="core, sector, thematic_etf, power_grid, compute, edge_emerging, compounder, ai")
    s.add_argument("--tickers", nargs="*")
    s.add_argument("--preset", default="balanced", choices=list(S.PRESETS))
    s.add_argument("--top", type=int, default=25)
    s.add_argument("--csv")
    s.set_defaults(fn=cmd_screen)

    b = sub.add_parser("backtest", help="backtest a rule on a universe")
    b.add_argument("--strategy", default="momentum", choices=["momentum", "equal", "invvol", "trend"])
    b.add_argument("--group", default="ai")
    b.add_argument("--tickers", nargs="*")
    b.add_argument("--top", type=int, default=10)
    b.add_argument("--lookback", type=int, default=252)
    b.add_argument("--rank-by", default="risk_adj", choices=["risk_adj", "return"])
    b.add_argument("--weighting", default="inv_vol", choices=["inv_vol", "equal"])
    b.add_argument("--max-weight", type=float, default=0.15)
    b.add_argument("--no-trend", action="store_true", help="disable the 200-day trend filter")
    b.add_argument("--core", help="blend with a core ETF, e.g. VTI")
    b.add_argument("--satellite", type=float, default=0.3, help="satellite share when --core is used")
    b.add_argument("--start", default="2016-01-29")
    b.add_argument("--cost-bps", type=float, default=15.0)
    b.set_defaults(fn=cmd_backtest)

    g = sub.add_parser("goal", help="Monte Carlo odds of reaching a multiple")
    g.add_argument("--multiple", type=float, default=50)
    g.add_argument("--initial", type=float, default=10_000)
    g.add_argument("--monthly", type=float, default=500)
    g.add_argument("--years", type=int, default=30)
    g.add_argument("--mean", type=float, default=0.10, help="expected arithmetic annual return")
    g.add_argument("--vol", type=float, default=0.17, help="annual volatility")
    g.add_argument("--t-df", type=float, default=None, help="Student-t degrees of freedom for fat tails")
    g.add_argument("--bootstrap", help="resample this ticker's monthly history instead (e.g. SPY)")
    g.add_argument("--fee", type=float, default=0.0)
    g.add_argument("--raise-pct", type=float, default=0.03, help="annual growth of contributions")
    g.add_argument("--paths", type=int, default=20_000)
    g.set_defaults(fn=cmd_goal)

    m = sub.add_parser("metrics", help="risk/return statistics for tickers")
    m.add_argument("tickers", nargs="+")
    m.add_argument("--start", default=None)
    m.set_defaults(fn=cmd_metrics)

    fu = sub.add_parser("fundamentals", help="refresh the valuation snapshot via yfinance")
    fu.add_argument("--tickers", nargs="*")
    fu.set_defaults(fn=cmd_fundamentals)

    r = sub.add_parser("report", help="run the full research pipeline into output/")
    r.add_argument("--refresh", action="store_true")
    r.set_defaults(fn=cmd_report)

    args = p.parse_args(argv)
    logging.basicConfig(level=logging.INFO if args.verbose else logging.WARNING, format="%(levelname)s %(message)s")
    return args.fn(args)


if __name__ == "__main__":
    sys.exit(main())
