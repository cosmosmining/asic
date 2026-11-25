"""End-to-end research run: screens, theme analysis, backtests, goal math.

``build_report()`` writes:

* ``output/results.json``   everything, machine-readable (feeds the dashboard)
* ``output/screen_<group>.csv``
* ``output/SUMMARY.md``     human-readable digest
"""
from __future__ import annotations

import json
import logging
import math
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

from . import goal as G
from . import metrics as M
from . import signals as S
from . import strategies as ST
from . import universe as U
from .backtest import BacktestResult, leveraged_equity, run_backtest
from .data import PKG_ROOT, PriceStore

log = logging.getLogger(__name__)

OUTPUT_DIR = PKG_ROOT / "output"
FUNDAMENTALS_CSV = PKG_ROOT / "data" / "fundamentals.csv"

SCREEN_PRESET = {
    "core": "balanced",
    "sector": "balanced",
    "thematic_etf": "balanced",
    "compounder": "balanced",
    "power_grid": "balanced",
    "compute": "balanced",
    "edge_emerging": "balanced",
}

SCREEN_COLUMNS = [
    "name", "theme", "stage", "score", "grade", "trend_state", "price",
    "ret_1m", "ret_3m", "ret_6m", "ret_12m", "mom_12_1", "risk_adj_mom", "vol_1m", "vol_1y", "maxdd_1y",
    "dd_from_high", "sma200_gap", "extended", "pinned", "cagr_3y", "cagr_5y", "beta_1y", "rel_strength_12m",
    "history_years", "adv_3m_usd", "valuation_flag", "fwd_pe", "ev_sales", "rev_growth", "op_margin", "mcap_usd_bn", "fund_as_of",
    "s_risk_adj_mom", "s_mom_6_1", "s_trend", "s_rel_strength", "s_low_vol", "s_dd_resilience", "s_long_term",
    "coverage", "note", "last_date",
]


# --------------------------------------------------------------------------- utils
def _clean(x):
    """Make values JSON-safe (NaN/inf -> None, numpy -> python)."""
    if isinstance(x, dict):
        return {str(k): _clean(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [_clean(v) for v in x]
    if isinstance(x, (np.floating, float)):
        f = float(x)
        return None if math.isnan(f) or math.isinf(f) else round(f, 6)
    if isinstance(x, (np.integer,)):
        return int(x)
    if isinstance(x, (np.bool_,)):
        return bool(x)
    if isinstance(x, pd.Timestamp):
        return str(x.date())
    if x is pd.NA or x is pd.NaT:
        return None
    return x


def _series_points(s: pd.Series, freq: str = "ME") -> list[list]:
    m = s.dropna().resample(freq).last().dropna()
    return [[str(d.date()), float(v)] for d, v in m.items()]


def load_fundamentals(path: Path = FUNDAMENTALS_CSV) -> pd.DataFrame | None:
    if not Path(path).exists():
        return None
    df = pd.read_csv(path)
    df["ticker"] = df["ticker"].astype(str).str.strip()
    df = df.drop_duplicates("ticker").set_index("ticker")
    if "as_of" in df.columns:
        df = df.rename(columns={"as_of": "fund_as_of"})
    for c in ("fwd_pe", "ev_sales", "rev_growth", "gross_margin", "net_debt_ebitda"):
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors="coerce")
    if "profitable" in df.columns:
        df["profitable"] = df["profitable"].map(
            lambda v: None if pd.isna(v) else str(v).strip().lower() in {"true", "1", "yes"}
        )
    return df


# --------------------------------------------------------------------------- screens
def run_screens(px, close, volume, meta, fundamentals=None, bench="SPY") -> dict[str, pd.DataFrame]:
    out = {}
    non_equity = {"Bonds", "Cash", "Gold"}
    for group in U.GROUP_LABELS:
        members = [t for t in U.tickers(group) if t in px.columns]
        if group == "core":  # rank equity funds only; cash/bonds/gold are ballast, not picks
            members = [t for t in members if meta.loc[t, "theme"] not in non_equity]
        if not members:
            continue
        cols = list(dict.fromkeys(members + [bench]))
        feat = S.features_table(px[cols], bench=bench, volume=volume, close=close).loc[members]
        scored = S.composite_scores(feat, SCREEN_PRESET.get(group, "balanced"))
        scored = S.apply_fundamentals(scored, fundamentals)
        scored = scored.join(meta[["name", "theme", "stage", "note"]], how="left")
        keep = [c for c in SCREEN_COLUMNS if c in scored.columns]
        out[group] = scored[keep]
    return out


# --------------------------------------------------------------------------- themes
def run_theme_analysis(px: pd.DataFrame, meta: pd.DataFrame, lookback_days: int = 504) -> dict:
    ai = meta[meta["group"].isin(U.AI_GROUPS)]
    themes = {}
    for (group, theme), rows in ai.groupby(["group", "theme"]):
        members = [t for t in rows.index if t in px.columns]
        if len(members) < 2:
            continue
        idx = S.theme_index(px, members, min_members=min(2, len(members)))
        if len(idx) < 260:
            continue
        themes[theme] = {"group": group, "members": members, "index": idx}
    # Broad sleeves
    for group in U.AI_GROUPS:
        members = [t for t in U.tickers(group) if t in px.columns]
        idx = S.theme_index(px, members, min_members=5)
        if len(idx):
            themes[f"ALL {U.GROUP_LABELS[group]}"] = {"group": group, "members": members, "index": idx}

    rows = {}
    for name, th in themes.items():
        idx = th["index"]
        last = idx.iloc[-1]
        ytd_base = idx.loc[: f"{idx.index[-1].year - 1}-12-31"]
        rows[name] = {
            "group": th["group"],
            "n": len(th["members"]),
            "members": ", ".join(th["members"]),
            "ret_ytd": float(last / ytd_base.iloc[-1] - 1) if len(ytd_base) else float("nan"),
            "ret_1y": float(last / idx.iloc[-253] - 1) if len(idx) > 253 else float("nan"),
            "cagr_3y": float((last / idx.iloc[-757]) ** (1 / 3) - 1) if len(idx) > 757 else float("nan"),
            "vol_1y": M.ann_vol(M.returns_from(idx).iloc[-252:]),
            "maxdd_3y": M.max_drawdown(idx.iloc[-756:]),
            "dd_now": float(last / idx.iloc[-252:].max() - 1),
        }
    table = pd.DataFrame.from_dict(rows, orient="index").sort_values("ret_1y", ascending=False)

    # Correlations of daily returns over the lookback, plus market benchmarks.
    rets = {n: M.returns_from(th["index"]) for n, th in themes.items() if not n.startswith("ALL ")}
    for b in ("SPY", "QQQ", "SMH"):
        if b in px.columns:
            rets[b] = M.returns_from(px[b])
    rdf = pd.DataFrame(rets).iloc[-lookback_days:].dropna(how="all")
    corr = rdf.corr(min_periods=120)
    return {"table": table, "corr": corr, "indices": {n: th["index"] for n, th in themes.items()}}


# --------------------------------------------------------------------------- backtests
def _bt(px, fn, name, start, bench, **kw) -> BacktestResult:
    return run_backtest(px, fn, start=start, name=name, bench=bench, **kw)


def run_backtests(px: pd.DataFrame) -> dict[str, dict]:
    """Backtest suites. Returns {suite: {"note": str, "results": [BacktestResult]}}."""
    bench = px["SPY"]
    suites: dict[str, dict] = {}
    ai_universe = [t for t in U.tickers(U.AI_GROUPS) if t in px.columns and "." not in t]  # USD listings
    sectors = [t for t in U.tickers("sector") if t in px.columns]

    # ---- Suite A: long-history, low-hindsight strategies ---------------------
    a_start = "2000-01-31"
    res_a = [
        _bt(px, ST.fixed_weights({"SPY": 1.0}), "S&P 500 buy & hold (SPY)", a_start, bench, freq=None),
        _bt(px, ST.fixed_weights({"QQQ": 1.0}), "Nasdaq-100 buy & hold (QQQ)", a_start, bench, freq=None),
        _bt(px, ST.trend_filter({"SPY": 1.0}, sma_days=210), "SPY with 10-month trend filter", a_start, bench),
        _bt(px, ST.momentum_top_n(sectors, n=3, rank_by="return", weighting="equal", max_weight=None, trend_sma=None),
            "Sector momentum: top 3 of 9 SPDR sectors", a_start, bench),
        _bt(px, ST.blend([(ST.fixed_weights({"SPY": 1.0}), 0.6), (ST.trend_filter({"QQQ": 1.0}, 210), 0.4)]),
            "60% SPY + 40% QQQ with trend filter", a_start, bench),
    ]
    if "EFA" in px.columns and "IEF" in px.columns:
        res_a.append(_bt(px, ST.dual_momentum("SPY", "EFA", "IEF", "BIL"), "Dual momentum (SPY/EFA/IEF)", "2003-08-29", bench))
    suites["A_long_history"] = {
        "title": "Long-history strategies (2000 → today)",
        "note": "Universes chosen without hindsight (broad index / sector ETFs). Includes the 2000-02 and 2008 bear markets.",
        "results": res_a,
    }

    # ---- Suite B: AI infrastructure (hindsight-biased!) ----------------------
    b_start = "2016-01-29"
    ai_mom = ST.momentum_top_n(ai_universe, n=10, rank_by="risk_adj", weighting="inv_vol", max_weight=0.15, trend_sma=200)
    res_b = [
        _bt(px, ST.fixed_weights({"SPY": 1.0}), "S&P 500 (SPY)", b_start, bench, freq=None),
        _bt(px, ST.fixed_weights({"QQQ": 1.0}), "Nasdaq-100 (QQQ)", b_start, bench, freq=None),
        _bt(px, ST.fixed_weights({"SMH": 1.0}), "Semiconductors (SMH)", b_start, bench, freq=None),
        _bt(px, ST.equal_weight(ai_universe, min_history=21), "AI-infra universe, equal weight", b_start, bench),
        _bt(px, ai_mom, "AI-infra momentum top 10 + trend filter", b_start, bench, cost_bps=15),
        _bt(px, ST.blend([(ST.fixed_weights({"VTI": 1.0}), 0.7), (ai_mom, 0.3)]),
            "Core-satellite: 70% VTI + 30% AI momentum", b_start, bench, cost_bps=10),
    ]
    suites["B_ai_infrastructure"] = {
        "title": "AI-infrastructure strategies (2016 → today)",
        "note": "WARNING: the AI universe was picked in 2026 with hindsight (survivorship bias). These returns overstate what was knowable in real time.",
        "results": res_b,
    }

    # ---- Suite C: model portfolios ------------------------------------------
    c_start = "2012-01-31"
    profiles = model_portfolio_weights()
    res_c = []
    for pname, spec in profiles.items():
        res_c.append(_bt(px, _profile_fn(spec, ai_universe), pname, c_start, bench, cost_bps=10))
    res_c.append(_bt(px, ST.fixed_weights({"SPY": 1.0}), "S&P 500 (SPY)", c_start, bench, freq=None))
    suites["C_model_portfolios"] = {
        "title": "Model portfolios (2012 → today, ETF proxies)",
        "note": "Backtests use long-history proxies (QQQ for QQQM, EFA for VXUS). Satellite sleeve is the AI momentum rule and inherits Suite B's hindsight bias.",
        "results": res_c,
    }
    return suites


def model_portfolio_weights() -> dict[str, dict]:
    """Illustrative profiles (backtest proxies). Not personalised advice."""
    return {
        "Steady compounder": {
            "etfs": {"VTI": 0.60, "QQQ": 0.15, "EFA": 0.20, "IEF": 0.05},
            "satellite": 0.0,
            "live": {"VTI": 0.60, "QQQM": 0.15, "VXUS": 0.20, "BND": 0.05},
        },
        "Growth tilt": {
            "etfs": {"VTI": 0.45, "QQQ": 0.20, "SMH": 0.10, "EFA": 0.10},
            "satellite": 0.15,
            "live": {"VTI": 0.45, "QQQM": 0.20, "SMH": 0.10, "VXUS": 0.10, "AI satellite (screen picks)": 0.15},
        },
        "Aggressive AI-infra": {
            "etfs": {"VTI": 0.35, "QQQ": 0.20, "SMH": 0.15},
            "satellite": 0.30,
            "live": {"VTI": 0.35, "QQQM": 0.20, "SMH": 0.15, "AI satellite (screen picks)": 0.30},
        },
    }


def _profile_fn(spec: dict, ai_universe: list[str]):
    parts = [(ST.fixed_weights(spec["etfs"]), 1.0)]
    if spec.get("satellite", 0) > 0:
        sat = ST.momentum_top_n(ai_universe, n=10, rank_by="risk_adj", weighting="inv_vol", max_weight=0.15, trend_sma=200)
        parts.append((sat, spec["satellite"]))
    return ST.blend(parts)


def leverage_illustration(px: pd.DataFrame) -> dict:
    """QQQ 1x vs simulated daily-reset 2x/3x since 1999 (the 2000-02 lesson)."""
    if "QQQ" not in px.columns:
        return {}
    r = M.returns_from(px["QQQ"].dropna()).dropna()
    cash = M.returns_from(px["BIL"]).dropna() * 252 if "BIL" in px.columns else None
    out = {}
    for lev in (1, 2, 3):
        eq = (1 + r).cumprod() if lev == 1 else leveraged_equity(r, lev, borrow_rate=cash.reindex(r.index).fillna(0.03) if cash is not None else 0.03)
        eq = eq / eq.iloc[0]
        out[f"{lev}x"] = {
            "stats": M.summarize(eq),
            "equity": _series_points(eq),
            "dd_2000_2002": float(eq.loc["2000-03-01":"2002-12-31"].min() / eq.loc[:"2000-03-31"].max() - 1),
        }
    return out


# --------------------------------------------------------------------------- goals
def run_goal_analysis(px: pd.DataFrame, bt_suites: dict) -> dict:
    years = [10, 15, 20, 25, 30, 35, 40]
    req = {f"{y}y": G.required_cagr(50, y) for y in years}
    yrs_to = {f"{r:.0%}": G.years_to_multiple(50, r) for r in (0.07, 0.10, 0.12, 0.15, 0.20, 0.25, 0.30, 0.40)}

    def est(t: str, start: str | None = None) -> tuple[float, float]:
        s = px[t].dropna().loc[start:]
        mr = M.monthly_returns(s)
        return float(mr.mean() * 12), float(mr.std(ddof=1) * math.sqrt(12))

    scenarios = {
        "US stocks, forward-looking (6.5% mean, 16% vol)": (0.065, 0.16),
        "US stocks, long-run history (11.8% mean, 19.5% vol)": (0.118, 0.195),
        "Nasdaq-100-like growth (14% mean, 24% vol)": (0.14, 0.24),
        "Diversified AI-infra basket (20% mean, 35% vol)": (0.20, 0.35),
        "Single high-flyer stock (25% mean, 60% vol)": (0.25, 0.60),
    }
    for t, lab in (("SPY", "SPY 1993-now (measured)"), ("QQQ", "QQQ 1999-now (measured)"), ("SMH", "SMH 2000-now (measured)")):
        if t in px.columns:
            scenarios[lab] = est(t)
    param_table = G.horizon_table(50, scenarios, horizons=years)

    # Bootstrap only histories chosen without hindsight. (Resampling the AI-universe
    # backtest would turn its survivorship bias into fake 90%+ odds of 50x.)
    hist = {}
    for t, lab in (("SPY", "S&P 500 (SPY, since 1993)"), ("QQQ", "Nasdaq-100 (QQQ, since 1999)"), ("SMH", "Semiconductors (SMH, since 2000)")):
        if t in px.columns:
            hist[lab] = M.monthly_returns(px[t].dropna()).to_numpy()
    for suite in bt_suites.values():
        for res in suite["results"]:
            if res.name == "Sector momentum: top 3 of 9 SPDR sectors":
                hist["Sector momentum rule (since 2000)"] = M.monthly_returns(res.equity).to_numpy()
    boot_table = G.bootstrap_horizon_table(hist, 50, horizons=years, n_paths=20_000)

    # Contribution example: $10k now + $500/month (+3%/yr raises) for 30 years.
    contrib = {}
    for name, (m, v) in scenarios.items():
        if "measured" in name:
            continue
        sim = G.simulate(10_000, 500, 30, mean=m, vol=v, contrib_growth=0.03, n_paths=20_000, seed=3)
        contrib[name] = {**sim.summary(), "fan": sim.pct_paths.reset_index().to_dict(orient="records")}

    kelly = {name: G.kelly_fraction(m, v, rf=0.035) for name, (m, v) in scenarios.items() if "measured" not in name}
    return {
        "required_cagr_for_50x": req,
        "years_to_50x": yrs_to,
        "scenarios": {k: {"mean": m, "vol": v, "median_cagr": G.median_cagr(m, v)} for k, (m, v) in scenarios.items()},
        "param_table": param_table,
        "bootstrap_table": boot_table,
        "contribution_sims": contrib,
        "kelly": kelly,
    }


# --------------------------------------------------------------------------- regime
def market_regime(px: pd.DataFrame, store: PriceStore | None = None) -> dict:
    """Where are we now: drawdowns, trend, breadth and volatility."""
    idx = {}
    for t in ("SPY", "QQQ", "SMH", "VTI", "EFA", "GRID", "XLU", "XLE"):
        if t not in px.columns:
            continue
        s = px[t].dropna()
        ytd_base = s.loc[: f"{s.index[-1].year - 1}-12-31"]
        r = M.returns_from(s).dropna()
        idx[t] = {
            "dd_from_52w_high": float(s.iloc[-1] / s.iloc[-252:].max() - 1),
            "above_10m_avg": bool(s.iloc[-1] > s.iloc[-210:].mean()),
            "ret_1m": float(s.iloc[-1] / s.iloc[-22] - 1),
            "ret_ytd": float(s.iloc[-1] / ytd_base.iloc[-1] - 1) if len(ytd_base) else None,
            "ret_12m": float(s.iloc[-1] / s.iloc[-253] - 1),
            "vol_1m": float(r.iloc[-21:].std(ddof=1) * math.sqrt(252)),
        }
    breadth = {}
    for group in ("power_grid", "compute", "edge_emerging", "compounder", "sector", "thematic_etf"):
        members = [t for t in U.tickers(group) if t in px.columns]
        flags = []
        for t in members:
            s = px[t].dropna()
            if len(s) >= 200:
                flags.append(bool(s.iloc[-1] > s.iloc[-200:].mean()))
        if flags:
            breadth[group] = {"pct_above_200d": float(np.mean(flags)), "n": len(flags)}
    vix = None
    if store is not None:
        try:
            v = store.history("^VIX")["close"].dropna()
            vix = {
                "last": float(v.iloc[-1]),
                "date": str(v.index[-1].date()),
                "median_1y": float(v.iloc[-252:].median()),
                "max_1y": float(v.iloc[-252:].max()),
                "long_run_median": float(v.median()),
            }
        except Exception as exc:  # noqa: BLE001
            log.warning("VIX unavailable: %s", exc)
    return {"indices": idx, "breadth": breadth, "vix": vix}


# --------------------------------------------------------------------------- signals now
def current_signals(px: pd.DataFrame, meta: pd.DataFrame) -> dict:
    today = px.index[-1]
    ai_universe = [t for t in U.tickers(U.AI_GROUPS) if t in px.columns and "." not in t]
    sectors = [t for t in U.tickers("sector") if t in px.columns]
    hist = px.loc[:today]
    ai = ST.momentum_top_n(ai_universe, n=10, rank_by="risk_adj", weighting="inv_vol", max_weight=0.15, trend_sma=200)(today, hist)
    sec = ST.momentum_top_n(sectors, n=3, rank_by="return", weighting="equal", max_weight=None, trend_sma=None)(today, hist)
    gem = ST.dual_momentum("SPY", "EFA", "IEF", "BIL")(today, hist)

    def above(t, d=210):
        s = px[t].dropna()
        return bool(s.iloc[-1] > s.iloc[-d:].mean())

    def fmt(w: pd.Series) -> list[dict]:
        return [
            {"ticker": t, "weight": float(v), "name": meta.loc[t, "name"] if t in meta.index else t,
             "theme": meta.loc[t, "theme"] if t in meta.index else ""}
            for t, v in w.sort_values(ascending=False).items()
        ]

    return {
        "asof": str(today.date()),
        "ai_momentum_top10": fmt(ai),
        "ai_momentum_cash": float(1 - ai.sum()) if len(ai) else 1.0,
        "sector_momentum_top3": fmt(sec),
        "dual_momentum": fmt(gem),
        "trend_filters": {t: above(t) for t in ("SPY", "QQQ", "SMH", "VTI", "EFA", "GRID") if t in px.columns},
    }


# --------------------------------------------------------------------------- main
def _bt_payload(res: BacktestResult) -> dict:
    stats = dict(res.stats)
    return {
        "name": res.name,
        "stats": stats,
        "equity": _series_points(res.equity),
        "yearly": {int(k): float(v) for k, v in res.yearly().items()},
        "drawdown": _series_points(M.drawdown(res.equity)),
        "last_weights": {k: float(v) for k, v in res.weights.iloc[-1].items() if abs(v) > 1e-6} if len(res.weights) else {},
    }


def build_report(store: PriceStore | None = None, out_dir: Path = OUTPUT_DIR, refresh: bool = False) -> dict:
    store = store or PriceStore()
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    meta = U.meta()
    all_t = U.tickers()
    px = store.prices(all_t, refresh=refresh)
    close = store.panel(all_t, "close")
    volume = store.panel(all_t, "volume")
    # Use the US calendar (SPY) as the master index for screens and backtests.
    us_idx = px["SPY"].dropna().index
    px = px.reindex(us_idx).ffill(limit=5)
    fundamentals = load_fundamentals()

    screens = run_screens(px, close.reindex(us_idx).ffill(limit=5), volume.reindex(us_idx), meta, fundamentals)
    themes = run_theme_analysis(px, meta)
    suites = run_backtests(px)
    goals = run_goal_analysis(px, suites)
    signals = current_signals(px, meta)
    lev = leverage_illustration(px)
    regime = market_regime(px, store)
    try:
        from . import history as H

        br = H.base_rates()
        history = {
            "source": br["source"],
            "first": br["first"],
            "last": br["last"],
            "cagr_since_1926_nominal": br["cagr_since_1926_nominal"],
            "cagr_since_1926_real": br["cagr_since_1926_real"],
            "windows": pd.concat([br["nominal"], br["real"]]).to_dict(orient="records"),
        }
    except Exception as exc:  # noqa: BLE001 - optional dataset
        log.warning("S&P 500 history unavailable: %s", exc)
        history = None

    for g, df in screens.items():
        df.to_csv(out_dir / f"screen_{g}.csv", float_format="%.4f")

    payload = {
        "generated_utc": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M"),
        "asof": str(px.index[-1].date()),
        "n_tickers": int(px.shape[1]),
        "data_errors": store.errors,
        "fundamentals_as_of": (
            str(fundamentals["fund_as_of"].dropna().max()) if fundamentals is not None and "fund_as_of" in fundamentals else None
        ),
        "group_labels": U.GROUP_LABELS,
        "screens": {g: df.reset_index(names="ticker").to_dict(orient="records") for g, df in screens.items()},
        "themes": {
            "table": themes["table"].reset_index(names="theme").to_dict(orient="records"),
            "corr": {"labels": list(themes["corr"].columns), "matrix": themes["corr"].round(3).to_numpy().tolist()},
            "indices": {n: _series_points(s / s.loc[s.index[-1] - pd.Timedelta(days=3 * 365):].iloc[0], "W-FRI")
                        for n, s in themes["indices"].items() if len(s) > 800},
        },
        "backtests": {
            k: {"title": v["title"], "note": v["note"], "results": [_bt_payload(r) for r in v["results"]]}
            for k, v in suites.items()
        },
        "goal": {
            **{k: v for k, v in goals.items() if k not in ("param_table", "bootstrap_table")},
            "param_table": goals["param_table"].reset_index(names="scenario").to_dict(orient="records"),
            "bootstrap_table": goals["bootstrap_table"].reset_index(names="series").to_dict(orient="records"),
        },
        "signals": signals,
        "regime": regime,
        "history": history,
        "leverage": lev,
        "model_portfolios": model_portfolio_weights(),
    }
    payload = _clean(payload)
    (out_dir / "results.json").write_text(json.dumps(payload, indent=1))
    (out_dir / "SUMMARY.md").write_text(render_summary(payload))
    return payload


def _pct(x, d=1):
    return "n/a" if x is None else f"{x * 100:.{d}f}%"


def render_summary(p: dict) -> str:
    L = [f"# stock-quant summary — data as of {p['asof']}", ""]
    L.append("_Generated by `python -m stockquant report`. Educational research output, not financial advice._\n")
    rg = p.get("regime") or {}
    if rg:
        L.append("## Market regime now\n")
        L.append("| Index | From 52w high | 1m | YTD | 12m | 1m vol (ann.) | Above 10m avg |\n|---|---:|---:|---:|---:|---:|---|")
        for t, v in rg["indices"].items():
            L.append(f"| {t} | {_pct(v['dd_from_52w_high'])} | {_pct(v['ret_1m'])} | {_pct(v['ret_ytd'])} | {_pct(v['ret_12m'])} | "
                     f"{_pct(v['vol_1m'], 0)} | {'yes' if v['above_10m_avg'] else 'no'} |")
        if rg.get("vix"):
            vx = rg["vix"]
            L.append(f"\nVIX {vx['last']:.1f} on {vx['date']} (1y median {vx['median_1y']:.1f}, 1y max {vx['max_1y']:.1f}).")
        L.append("\nBreadth (share of names above their 200-day average): " + ", ".join(
            f"{p['group_labels'].get(g, g)} {_pct(b['pct_above_200d'], 0)}" for g, b in rg["breadth"].items()) + "\n")
    L.append("## Current rule-based signals\n")
    s = p["signals"]
    L.append("Trend filters (price above ~10-month average): " + ", ".join(f"{k} {'✅' if v else '❌'}" for k, v in s["trend_filters"].items()))
    L.append("\nAI-infra momentum sleeve (top 10, inverse-vol, 15% cap):\n")
    L.append("| Ticker | Weight | Theme |\n|---|---:|---|")
    for r in s["ai_momentum_top10"]:
        L.append(f"| {r['ticker']} | {_pct(r['weight'])} | {r['theme']} |")
    L.append(f"\nCash in sleeve: {_pct(s['ai_momentum_cash'])}\n")
    L.append("Sector momentum (top 3): " + ", ".join(r["ticker"] for r in s["sector_momentum_top3"]))
    L.append("\nDual momentum: " + ", ".join(r["ticker"] for r in s["dual_momentum"]) + "\n")

    for g, rows in p["screens"].items():
        L.append(f"## Screen — {p['group_labels'].get(g, g)} (top 12)\n")
        L.append("| # | Ticker | Score | Trend | 12m | Vol | MaxDD 1y | Valuation |\n|---:|---|---:|---|---:|---:|---:|---|")
        for i, r in enumerate(rows[:12], 1):
            L.append(
                f"| {i} | {r['ticker']} | {r.get('score') or 'n/a'} | {r.get('trend_state') or ''} | {_pct(r.get('ret_12m'))} | "
                f"{_pct(r.get('vol_1y'), 0)} | {_pct(r.get('maxdd_1y'), 0)} | {r.get('valuation_flag') or ''} |"
            )
        L.append("")

    L.append("## Backtests\n")
    for suite in p["backtests"].values():
        L.append(f"### {suite['title']}\n\n_{suite['note']}_\n")
        L.append("| Strategy | CAGR | Vol | Sharpe | Max DD | Multiple |\n|---|---:|---:|---:|---:|---:|")
        for r in suite["results"]:
            st = r["stats"]
            L.append(f"| {r['name']} | {_pct(st['cagr'])} | {_pct(st['vol'], 0)} | {st['sharpe']:.2f} | {_pct(st['max_drawdown'], 0)} | {st['multiple']:.1f}x |")
        L.append("")

    g = p["goal"]
    h = p.get("history")
    if h:
        L.append("## How often did the S&P 500 itself deliver 50x?\n")
        L.append(f"Shiller monthly total-return data {h['first'][:4]}–{h['last'][:7]}; CAGR since 1926: "
                 f"{_pct(h['cagr_since_1926_nominal'])} nominal, {_pct(h['cagr_since_1926_real'])} real.\n")
        L.append("| Basis | Years | Windows | Share reaching 50x | Median multiple | Worst | Best |\n|---|---:|---:|---:|---:|---:|---:|")
        for r in h["windows"]:
            L.append(f"| {r['basis']} | {r['years']} | {r['windows']} | {_pct(r['share_reaching_target'])} | "
                     f"{r['median_multiple']:.1f}x | {r['worst_multiple']:.1f}x | {r['best_multiple']:.1f}x |")
        L.append("")
    L.append("## The 50x math\n")
    L.append("| Horizon | CAGR needed for 50x |\n|---|---:|")
    for k, v in g["required_cagr_for_50x"].items():
        L.append(f"| {k} | {_pct(v)} |")
    L.append("\n### Probability a lump sum reaches 50x (lognormal model)\n")
    hz = [k for k in g["param_table"][0] if k.endswith("y")]
    L.append("| Scenario | " + " | ".join(hz) + " | Median CAGR |\n|---|" + "---:|" * (len(hz) + 1))
    for r in g["param_table"]:
        L.append(f"| {r['scenario']} | " + " | ".join(_pct(r[h], 0) for h in hz) + f" | {_pct(r['median_cagr'])} |")
    L.append("")
    return "\n".join(L)
