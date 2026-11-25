#!/usr/bin/env python3
"""How realistic is a money goal, and what does it take?

Usage
-----
  python goal_plan.py --initial 15000 --monthly 800 --years 25 --target-multiple 50
  python goal_plan.py --initial 50000 --monthly 1000 --raise 0.03 --years 20 --target-amount 1000000
  python goal_plan.py ... --scenario "My 80/20 mix" 0.09 0.15        # add your own (mean, volatility)
  python goal_plan.py ... --backtest-mix VTI=0.6 VXUS=0.2 QQQM=0.2  # replay a real ETF mix (needs internet)
  python goal_plan.py ... --json /tmp/plan.json

Targets
-------
--target-amount is a dollar goal. --target-multiple M means M times the money
you put in (initial + all contributions); with no monthly contributions that
is simply M times the starting amount.

Output (markdown)
-----------------
1. The math: the yearly return this exact plan needs; what the plan grows to at
   common return levels.
2. History: replay of the plan through every monthly start date of the S&P 500
   total-return series since 1926 (Shiller data bundled in ../assets), nominal
   and after inflation.
3. Monte Carlo per scenario: money in, 10th/50th/90th percentile outcome,
   chance of reaching the target, typical worst drawdown, chance of ending
   below the money put in.
4. Sizing: growth-optimal (Kelly) fraction per scenario and the quarter/half
   versions used in practice, as a ceiling for how much a risky bet deserves.
All returns are before taxes and fees unless you pass --fee.
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

from stockquant import goal as G  # noqa: E402
from stockquant import history as Hs  # noqa: E402

SHILLER = HERE.parent / "assets" / "shiller_sp500.csv"

DEFAULT_SCENARIOS = [
    ("Balanced 60/40 stocks/bonds", 0.070, 0.10),
    ("US stocks, cautious forecast", 0.065, 0.16),
    ("US stocks, long-run history", 0.118, 0.195),
    ("Nasdaq-100-like growth", 0.14, 0.24),
    ("AI-infrastructure basket, optimistic", 0.20, 0.35),
    ("Single high-flyer stock", 0.25, 0.60),
]


def money(v: float) -> str:
    a = abs(v)
    if a >= 1e9:
        return f"${v / 1e9:,.2f}B"
    if a >= 1e6:
        return f"${v / 1e6:,.2f}M"
    if a >= 1e4:
        return f"${v / 1e3:,.0f}K"
    return f"${v:,.0f}"


def pct(x: float, d: int = 1) -> str:
    return "n/a" if x is None or (isinstance(x, float) and math.isnan(x)) else f"{x * 100:.{d}f}%"


def contributions(monthly: float, raise_pct: float, months: int) -> np.ndarray:
    return np.array([monthly * (1 + raise_pct) ** (m // 12) for m in range(months)])


def fv_at(rate: float, initial: float, contrib: np.ndarray) -> float:
    rm = (1 + rate) ** (1 / 12) - 1
    w = initial
    for c in contrib:
        w = (w + c) * (1 + rm)
    return w


def required_rate(target: float, initial: float, contrib: np.ndarray) -> float:
    lo, hi = -0.5, 3.0
    if fv_at(hi, initial, contrib) < target:
        return float("inf")
    for _ in range(200):
        mid = (lo + hi) / 2
        if fv_at(mid, initial, contrib) >= target:
            hi = mid
        else:
            lo = mid
    return hi


def history_replay(initial: float, contrib: np.ndarray, target: float) -> dict | None:
    if not SHILLER.exists():
        return None
    df = Hs.load_shiller(SHILLER)
    nominal, real = Hs.total_return_index(df)
    out = {"source": Hs.SHILLER_URL, "span": f"{df.index[0].date()} to {df.index[-1].date()}"}
    months = len(contrib)
    for label, idx in (("nominal", nominal), ("real (after inflation)", real)):
        r = (idx / idx.shift(1) - 1).loc["1926-01-01":].to_numpy()[1:]
        n = len(r) - months + 1
        if n <= 0:
            continue
        terminals = np.empty(n)
        for s in range(n):
            w = initial
            seg = r[s:s + months]
            for m in range(months):
                w = (w + contrib[m]) * (1 + seg[m])
            terminals[s] = w
        out[label] = {
            "start_months": int(n),
            "share_reaching_target": float(np.mean(terminals >= target)),
            "median": float(np.median(terminals)),
            "worst": float(terminals.min()),
            "best": float(terminals.max()),
        }
    return out


def backtest_mix(spec: list[str]) -> tuple[dict, np.ndarray] | None:
    from stockquant import metrics as M
    from stockquant import strategies as ST
    from stockquant.backtest import run_backtest
    from stockquant.data import PriceStore

    weights = {}
    for item in spec:
        t, w = item.split("=")
        weights[t.strip()] = float(w)
    tot = sum(weights.values())
    weights = {k: v / tot for k, v in weights.items()}
    store = PriceStore()
    px = store.prices(list(weights) + ["SPY"], calendar="SPY")
    missing = [t for t in weights if t not in px.columns]
    if missing:
        print(f"(could not fetch {missing}: {store.errors})")
        return None
    start = max(px[t].first_valid_index() for t in weights)
    res = run_backtest(px, ST.fixed_weights(weights), start=start, freq="M", cost_bps=5, name="mix", bench=px["SPY"])
    mr = M.monthly_returns(res.equity).to_numpy()
    return {"weights": weights, **{k: res.stats.get(k) for k in ("start", "years", "cagr", "vol", "max_drawdown", "sharpe", "multiple")}}, mr


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--initial", type=float, default=10_000)
    ap.add_argument("--monthly", type=float, default=0.0)
    ap.add_argument("--raise", dest="raise_pct", type=float, default=0.0, help="yearly growth of contributions, e.g. 0.03")
    ap.add_argument("--years", type=int, required=True)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--target-amount", type=float)
    g.add_argument("--target-multiple", type=float)
    ap.add_argument("--scenario", nargs=3, action="append", metavar=("NAME", "MEAN", "VOL"), help="extra scenario, e.g. 'My mix' 0.09 0.15")
    ap.add_argument("--only-custom", action="store_true", help="skip the default scenarios")
    ap.add_argument("--backtest-mix", nargs="*", metavar="TICKER=WEIGHT")
    ap.add_argument("--fee", type=float, default=0.0, help="yearly cost (expense ratio + advice), e.g. 0.002")
    ap.add_argument("--rf", type=float, default=0.035, help="cash yield for the Kelly calculation")
    ap.add_argument("--paths", type=int, default=20_000)
    ap.add_argument("--json")
    a = ap.parse_args()

    months = a.years * 12
    contrib = contributions(a.monthly, a.raise_pct, months)
    paid = a.initial + contrib.sum()
    target = a.target_amount if a.target_amount else a.target_multiple * paid
    tdesc = money(target) + ("" if a.target_amount else f" ({a.target_multiple:g}x the {money(paid)} you put in)")
    out: dict = {"inputs": vars(a), "money_in": paid, "target": target}

    print(f"# Goal plan: {tdesc} in {a.years} years\n")
    print(f"Plan: {money(a.initial)} now + {money(a.monthly)}/month" + (f" rising {pct(a.raise_pct)} a year" if a.raise_pct else "")
          + f" = {money(paid)} put in over {a.years} years." + (f" Costs: {pct(a.fee, 2)} a year." if a.fee else "") + "\n")

    # 1. deterministic math
    req = required_rate(target, a.initial, contrib)
    out["required_return"] = req
    print("## 1. The math\n")
    print(f"- This plan needs a steady **{pct(req)} a year** (after costs) to reach the target." if math.isfinite(req)
          else "- No realistic return reaches this target with this plan.")
    if a.monthly == 0 and a.target_multiple:
        print(f"- For comparison, {a.target_multiple:g}x on a lump sum takes {G.years_to_multiple(a.target_multiple, 0.07):.0f} years at 7%, "
              f"{G.years_to_multiple(a.target_multiple, 0.10):.0f} at 10%, {G.years_to_multiple(a.target_multiple, 0.15):.0f} at 15%.")
    print("\n| Steady yearly return | Plan grows to | Times money put in | Reaches target? |\n|---:|---:|---:|---|")
    table1 = []
    for r in (0.04, 0.07, 0.10, 0.12, 0.15, 0.20):
        v = fv_at(r - a.fee, a.initial, contrib)
        table1.append({"rate": r, "value": v})
        print(f"| {pct(r, 0)} | {money(v)} | {v / paid:.1f}x | {'yes' if v >= target else 'no'} |")
    out["deterministic"] = table1

    # 2. history replay
    hist = history_replay(a.initial, contrib, target)
    out["history"] = hist
    print("\n## 2. What history says (S&P 500 total return, every start month since 1926)\n")
    if not hist or "nominal" not in hist:
        print("History replay unavailable for this horizon (data covers 1926-2023).")
    else:
        print("| Basis | Start months tested | Reached target | Median result | Worst | Best |\n|---|---:|---:|---:|---:|---:|")
        for lab in ("nominal", "real (after inflation)"):
            if lab in hist:
                h = hist[lab]
                print(f"| {lab} | {h['start_months']} | {pct(h['share_reaching_target'], 0)} | {money(h['median'])} | {money(h['worst'])} | {money(h['best'])} |")
        print(f"\nSource: Shiller monthly data ({hist['span']}); index returns before fees and taxes. The real row measures the target in today's dollars.")

    # 3. Monte Carlo
    scen = [] if a.only_custom else list(DEFAULT_SCENARIOS)
    for name, m, v in a.scenario or []:
        scen.append((name, float(m), float(v)))
    mix_hist = None
    if a.backtest_mix:
        bt = backtest_mix(a.backtest_mix)
        if bt:
            info, mix_hist = bt
            out["mix_backtest"] = info
            print(f"\nYour mix {', '.join(f'{k} {w:.0%}' for k, w in info['weights'].items())} since {info['start']} ({info['years']} yrs): "
                  f"CAGR {pct(info['cagr'])}, volatility {pct(info['vol'], 0)}, worst drop {pct(info['max_drawdown'], 0)}.")
    print("\n## 3. Range of outcomes (Monte Carlo, " + f"{a.paths:,} paths)\n")
    print("| Scenario | Avg return / volatility | Typical yearly | Unlucky 1 in 10 | Median | Lucky 1 in 10 | Chance of target | Typical worst drop | Chance of losing money |")
    print("|---|---|---:|---:|---:|---:|---:|---:|---:|")
    rows = []
    sims = [(n, dict(mean=m, vol=v)) for n, m, v in scen]
    if mix_hist is not None and len(mix_hist) > 24:
        sims.append(("Your mix, replaying its own history", dict(hist_monthly=mix_hist)))
    for name, kw in sims:
        sim = G.simulate(a.initial, a.monthly, a.years, contrib_growth=a.raise_pct, fee=a.fee, n_paths=a.paths, seed=11, **kw)
        s = sim.summary()
        hit = sim.prob_at_least(target)
        mv = f"{pct(kw['mean'], 1)} / {pct(kw['vol'], 0)}" if "mean" in kw else "history"
        typ = pct(G.median_cagr(kw["mean"], kw["vol"])) if "mean" in kw else "n/a"
        rows.append({"scenario": name, "p10": s["p10"], "median": s["median"], "p90": s["p90"], "p_target": hit,
                     "median_max_drawdown": s["median_max_drawdown"], "prob_loss": s["prob_loss"]})
        print(f"| {name} | {mv} | {typ} | {money(s['p10'])} | {money(s['median'])} | {money(s['p90'])} | {pct(hit, 0)} | "
              f"{pct(s['median_max_drawdown'], 0)} | {pct(s['prob_loss'], 0)} |")
    out["monte_carlo"] = rows
    print("\nTypical yearly = median compound return after volatility drag (mean minus about half the variance).")
    if mix_hist is not None and len(mix_hist) < 25 * 12:
        print(f"Caution: your mix has only {len(mix_hist) / 12:.0f} years of history to replay. A short window that was mostly a bull market "
              "overstates the odds; compare it with the long-run rows and the 1926+ replay above.")

    # 4. sizing
    print("\n## 4. How much a risky bet deserves (Kelly ceiling)\n")
    print(f"Growth-optimal fraction = (mean - cash {pct(a.rf)}) / volatility². Real-world inputs are uncertain, so use a quarter to half of it, "
          "and never more than you could watch fall 50-90% without selling.\n")
    risky = [(n, m, v) for n, m, v in scen if v >= 0.30]
    kel = []
    if risky:
        print("| Concentrated bet | Full Kelly | Half | Quarter |\n|---|---:|---:|---:|")
        for name, m, v in risky:
            k = G.kelly_fraction(m, v, a.rf)
            kel.append({"scenario": name, "kelly": k})
            print(f"| {name} | {pct(k, 0)} | {pct(k / 2, 0)} | {pct(k / 4, 0)} |")
    else:
        print("No concentrated (30%+ volatility) scenario in this run.")
    out["kelly"] = kel
    print("\nThe table covers concentrated bets only. For diversified portfolios the formula exceeds 100%, which would mean borrowing; "
          "margin calls and daily-reset leveraged funds punish that in crashes, so treat 100% invested as the ceiling. "
          "And these inputs are guesses: if the real edge is half what you assumed, the right size is half too.")

    if a.json:
        Path(a.json).write_text(json.dumps(out, indent=1, default=str))
        print(f"\nJSON -> {a.json}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
