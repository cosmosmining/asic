"""Split output/results.json into small ``{rows, meta}`` JSON files.

Each file is one dataset of the interactive dashboard. ``meta`` carries the
exact functions that produced the numbers (read from disk, not retyped), the
data date and how to rerun them, so every figure on the page can be traced.

Usage: python -m stockquant.dashboard_export
"""
from __future__ import annotations

import inspect
import json
from pathlib import Path

from . import goal, metrics, report, signals, strategies
from .data import PKG_ROOT

OUT = PKG_ROOT / "output" / "dashboard"
CORR_THEMES = [
    "Accelerators", "Memory", "Semicap", "Optical", "Neocloud", "Miner-to-AI hosting",
    "Utilities", "IPP power", "Grid EPC", "DC power & cooling", "SMR developer",
    "Edge AI SoC", "Power semis", "SPY", "QQQ",
]
RERUN = "python -m stockquant fetch --refresh && python -m stockquant report && python -m stockquant.dashboard_export"


def _code(*objs) -> list[dict]:
    out = []
    for o in objs:
        mod = inspect.getmodule(o)
        label = f"{Path(mod.__file__).name}: {o.__name__}" if mod else o.__name__
        out.append({"label": label, "value": inspect.getsource(o), "type": "code", "lang": "python"})
    return out


def _meta(asof: str, extra: list[dict] | None = None, *code) -> list[dict]:
    m = [
        {"label": "Data as of", "value": asof},
        {"label": "Prices", "value": "Yahoo Finance daily adjusted closes (split & dividend adjusted), cached locally"},
        {"label": "Rerun", "value": RERUN},
    ]
    return m + (extra or []) + _code(*code)


def build(results_path: Path = report.OUTPUT_DIR / "results.json", out_dir: Path = OUT) -> dict[str, int]:
    p = json.loads(Path(results_path).read_text())
    asof = p["asof"]
    out_dir.mkdir(parents=True, exist_ok=True)
    files: dict[str, dict] = {}
    labels = p["group_labels"]

    # --- market regime -------------------------------------------------------
    rg = p["regime"]
    files["regime"] = {
        "rows": [{"ticker": t, "asof": asof, **v} for t, v in rg["indices"].items()],
        "meta": _meta(asof, None, report.market_regime),
    }
    files["breadth"] = {
        "rows": [{"group": g, "label": labels.get(g, g), **v} for g, v in rg["breadth"].items()],
        "meta": _meta(asof, [{"label": "Definition", "value": "Share of names whose last price is above their 200-day average"}], report.market_regime),
    }
    if rg.get("vix"):
        files["vix"] = {"rows": [{"index": "VIX", **rg["vix"]}], "meta": _meta(asof, [{"label": "Series", "value": "^VIX daily close"}], report.market_regime)}

    # --- signals ------------------------------------------------------------
    sg = p["signals"]
    rows = []
    for sleeve, key in (("AI-infra momentum (top 10)", "ai_momentum_top10"), ("Sector momentum (top 3)", "sector_momentum_top3"), ("Dual momentum", "dual_momentum")):
        for r in sg[key]:
            rows.append({"sleeve": sleeve, **r})
    if sg.get("ai_momentum_cash", 0) > 1e-6:
        rows.append({"sleeve": "AI-infra momentum (top 10)", "ticker": "CASH", "name": "Cash (unfilled slots)", "theme": "", "weight": sg["ai_momentum_cash"]})
    files["signals"] = {"rows": rows, "meta": _meta(asof, None, report.current_signals, strategies.momentum_top_n, strategies.dual_momentum, strategies.is_pinned)}
    files["trend_filters"] = {
        "rows": [{"ticker": t, "above_10m_avg": v} for t, v in sg["trend_filters"].items()],
        "meta": _meta(asof, [{"label": "Rule", "value": "Price above its ~10-month (210 trading day) average"}], report.current_signals),
    }

    # --- screens ------------------------------------------------------------
    rows = []
    for g, recs in p["screens"].items():
        for rank, r in enumerate(recs, 1):
            rows.append({"group": g, "group_label": labels.get(g, g), "rank": rank, **r})
    files["screens"] = {
        "rows": rows,
        "meta": _meta(asof, [{"label": "Score", "value": "0-100 percentile blend within each group; presets in signals.PRESETS"}],
                      signals.ticker_features, signals.composite_scores, signals.apply_fundamentals),
    }

    # --- themes ---------------------------------------------------------------
    files["themes"] = {"rows": p["themes"]["table"], "meta": _meta(asof, None, report.run_theme_analysis, signals.theme_index)}
    cl, cm = p["themes"]["corr"]["labels"], p["themes"]["corr"]["matrix"]
    keep = [i for i, lab in enumerate(cl) if lab in CORR_THEMES]
    files["theme_corr"] = {
        "rows": [{"a": cl[i], "b": cl[j], "corr": cm[i][j]} for i in keep for j in keep],
        "meta": _meta(asof, [{"label": "Window", "value": "Daily returns of equal-weight theme baskets, last ~2 years"}], report.run_theme_analysis),
    }

    h = p.get("history")
    if h:
        from . import history as H

        files["sp500_windows"] = {
            "rows": h["windows"],
            "meta": [
                {"label": "Input", "value": h["source"]},
                {"label": "Span", "value": f"{h['first']} to {h['last']} (months with dividend and CPI data)"},
                {"label": "CAGR since 1926", "value": f"{h['cagr_since_1926_nominal']:.2%} nominal, {h['cagr_since_1926_real']:.2%} real"},
                {"label": "Rerun", "value": RERUN},
            ] + _code(H.total_return_index, H.window_stats, H.base_rates),
        }

    # --- backtests ----------------------------------------------------------
    stats_rows, curve_rows = [], []
    for sk, suite in p["backtests"].items():
        for res in suite["results"]:
            st = res["stats"]
            stats_rows.append({"suite": sk, "suite_title": suite["title"], "suite_note": suite["note"], "strategy": res["name"], **st})
            dd = dict(res["drawdown"])
            for d, v in res["equity"]:
                curve_rows.append({"suite": sk, "strategy": res["name"], "date": d, "value": v, "drawdown": dd.get(d)})
    bt_code = (report.run_backtests, report.model_portfolio_weights, strategies.momentum_top_n, strategies.trend_filter, strategies.dual_momentum, metrics.summarize)
    from . import backtest as B

    files["backtest_stats"] = {"rows": stats_rows, "meta": _meta(asof, [{"label": "Costs", "value": "10-15 bp per unit traded; cash earns BIL (3%/yr before 2007)"}], B.run_backtest, *bt_code)}
    files["equity_curves"] = {"rows": curve_rows, "meta": _meta(asof, [{"label": "Sampling", "value": "Month-end values, growth of 1"}], B.run_backtest, report._series_points)}

    lev_rows, lev_stats = [], []
    for k, v in p["leverage"].items():
        lev_stats.append({"leverage": k, "dd_2000_2002": v["dd_2000_2002"], **v["stats"]})
        for d, val in v["equity"]:
            lev_rows.append({"leverage": k, "date": d, "value": val})
    files["leverage_curves"] = {"rows": lev_rows, "meta": _meta(asof, None, report.leverage_illustration, B.leveraged_equity)}
    files["leverage_stats"] = {"rows": lev_stats, "meta": _meta(asof, None, report.leverage_illustration, B.leveraged_equity)}

    # --- goal math ----------------------------------------------------------
    g = p["goal"]
    files["goal_required"] = {
        "rows": [{"horizon_years": int(k.rstrip("y")), "required_cagr": v} for k, v in g["required_cagr_for_50x"].items()],
        "meta": _meta(asof, None, goal.required_cagr),
    }
    files["goal_years"] = {
        "rows": [{"cagr": float(k.rstrip("%")) / 100, "years_to_50x": v} for k, v in g["years_to_50x"].items()],
        "meta": _meta(asof, None, goal.years_to_multiple),
    }
    def _hz(r: dict) -> dict:  # "10y" -> "p_10y" (probability of 50x within 10 years)
        return {(f"p_{k}" if k[:-1].isdigit() and k.endswith("y") else k): v for k, v in r.items()}

    files["goal_scenarios"] = {
        "rows": [_hz({"scenario": r["scenario"], **g["scenarios"][r["scenario"]], **{k: v for k, v in r.items() if k != "scenario"}})
                 for r in g["param_table"]],
        "meta": _meta(asof, [{"label": "Model", "value": "i.i.d. lognormal annual returns matched to the arithmetic mean & volatility; P(lump sum >= 50x)"}],
                      goal.lognormal_params, goal.prob_lump_sum_multiple, goal.horizon_table, report.run_goal_analysis),
    }
    files["goal_bootstrap"] = {
        "rows": [_hz(r) for r in g["bootstrap_table"]],
        "meta": _meta(asof, [{"label": "Model", "value": "12-month block bootstrap of actual monthly returns, 20,000 paths"}], goal.bootstrap_horizon_table, goal._monthly_draws),
    }
    files["goal_contrib"] = {
        "rows": [{"scenario": k, **{kk: vv for kk, vv in v.items() if kk != "fan"}} for k, v in g["contribution_sims"].items()],
        "meta": _meta(asof, [{"label": "Plan", "value": "$10,000 now + $500/month rising 3%/yr, 30 years, 20,000 paths"}], goal.simulate, goal.SimResult.summary),
    }

    # --- model portfolios ---------------------------------------------------
    rows = []
    for prof, spec in p["model_portfolios"].items():
        for h, w in spec["live"].items():
            rows.append({"profile": prof, "holding": h, "weight": w})
    files["model_portfolios"] = {"rows": rows, "meta": _meta(asof, [{"label": "Status", "value": "Illustrative allocations, not personal advice"}], report.model_portfolio_weights)}

    ev = PKG_ROOT / "data" / "evidence.json"
    if ev.exists():
        files["evidence"] = {
            "rows": json.loads(ev.read_text()),
            "meta": [
                {"label": "Compiled", "value": "By hand from the study's research notes (Nov 2026). Each row names and links its source; 'own calculation' rows were computed from Shiller's S&P 500 data or a lognormal model."},
                {"label": "File", "value": "stock-quant/data/evidence.json"},
            ],
        }

    counts = {}
    for name, body in files.items():
        (out_dir / f"{name}.json").write_text(json.dumps(body, separators=(",", ":")))
        counts[name] = len(body["rows"])
    return counts


if __name__ == "__main__":
    for k, v in build().items():
        print(f"{k:18s} {v:6d} rows")
