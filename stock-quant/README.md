# stock-quant

A small, transparent quant toolkit for a long-term investor who wants to find
durable core holdings, size bets on emerging AI-infrastructure themes (power
grid, nuclear, cooling, networking/optics, memory, edge AI, neoclouds) and see
honest odds for big goals like "50x".

> Research and education only. Nothing here is personal financial advice, and
> no tool can guarantee returns. Backtests on a universe chosen today are
> biased upward (see Caveats).

## What it does

| Command | What you get |
|---|---|
| `python -m stockquant fetch` | Downloads daily adjusted prices for ~210 tickers into `data/cache/` |
| `python -m stockquant screen --group compute` | Ranks a group by a 0–100 trend-quality score, with trend state and valuation flags |
| `python -m stockquant backtest --group ai --top 10 --core VTI --satellite 0.3` | Backtests a rule (momentum, equal weight, inverse vol, trend filter), optionally as a core-satellite blend |
| `python -m stockquant goal --initial 10000 --monthly 500 --years 30 --mean 0.118 --vol 0.195` | Monte Carlo of your plan: median, bad/good cases, odds of 10x/50x, typical worst drawdown |
| `python -m stockquant goal --bootstrap SPY ...` | Same, replaying real SPY monthly history in 12-month blocks |
| `python -m stockquant metrics NVDA VRT GEV --start 2024-01-01` | CAGR, volatility, Sharpe, Sortino, drawdowns, beta, capture ratios |
| `python -m stockquant fundamentals` | Refreshes the valuation snapshot (`data/fundamentals.csv`) with yfinance |
| `python -m stockquant report` | Runs everything into `output/results.json`, `output/SUMMARY.md` and `output/screen_*.csv` |
| `python -m stockquant.dashboard_export` | Splits results into `output/dashboard/*.json` datasets for the interactive dashboard |

Add `--offline` before the command to use cached prices only.

## Install

```bash
cd stock-quant
python -m pip install -r requirements.txt
python -m stockquant fetch && python -m stockquant report
python -m pytest -q tests
```

Prices come from Yahoo Finance's public chart endpoint, with `yfinance` as a
fallback. On a normal internet connection both work; `fundamentals` needs
`yfinance`.

## Modules

| Module | Purpose |
|---|---|
| `data.py` | Price download + per-ticker CSV cache; split/dividend-adjusted closes |
| `universe.csv` / `universe.py` | Editable universe: core ETFs, sectors, thematic ETFs, AI power & grid, AI compute & data centers, edge AI & emerging, quality compounders |
| `metrics.py` | Performance and risk statistics |
| `signals.py` | Momentum / trend / volatility / drawdown features, composite score presets, takeover-pin detection, valuation flags |
| `backtest.py` | Daily-marked, monthly-rebalanced engine with costs and cash yield; no look-ahead (decide at the close, trade next day); leveraged-ETF simulator |
| `strategies.py` | Momentum top-N (with trend and absolute-momentum filters), trend filter, dual momentum, inverse vol, equal weight, blends |
| `portfolio.py` | Risk parity, inverse-vol caps, volatility targeting, share allocation |
| `goal.py` | 50x math, lognormal and bootstrap Monte Carlo with contributions, Kelly fraction |
| `history.py` | S&P 500 total-return base rates since 1926 from Shiller's monthly data |
| `report.py` | Orchestrates screens, theme baskets, backtests, goal tables and current signals |

## How the score works

Within each group, every name is ranked (percentiles) on: risk-adjusted 12-1
momentum, 6-1 momentum, trend (distance above the 200-day average, 50/200
cross, rising 200-day), 12-month strength vs SPY, low volatility, shallow
1-year drawdown and 3–5 year CAGR. Presets (`balanced`, `momentum`,
`defensive`) weight these differently. Young listings get a small penalty;
stocks pinned to a pending takeover price get a large one. A high score means a
strong, orderly trend. It says nothing about value: see the valuation flags
(stretched, premium, peak-cycle risk, speculative).

## Caveats

* **Hindsight bias.** The AI-infrastructure universe was picked in November
  2026. Backtesting it from 2016 includes only survivors that are famous today,
  so those results are an upper bound, not an expectation. The long-history
  suite (index and sector ETFs since 2000) is the honest benchmark.
* **Model risk.** Monte Carlo odds depend on the assumed return and volatility.
  The bootstrap table replays history as a cross-check.
* **Snapshot data.** `data/fundamentals.csv` is a dated snapshot (Nov 2026);
  refresh it before relying on valuations. `data/evidence.json` holds sourced
  research findings used by the dashboard.

## Study

The written study is in `reports/` and the research notes behind it in
`research_notes/`.

## Claude skills built on this toolkit

Two project skills live in `.claude/skills/` at the repository root, so Claude
sessions on this branch pick them up automatically:

| Skill | Use it for |
|---|---|
| `investment-research` | Researching a stock, ETF, sector or theme (e.g. AI power, edge AI): quant snapshot, fundamentals, valuation, bubble checklist, base rates, sizing |
| `portfolio-goal-planner` | Turning a goal ("50x", "$1M by 45") into required-return math, 1926+ history replay, Monte Carlo odds and a core-satellite allocation |

Each skill bundles a copy of `stockquant/` so it also works when installed into
a Claude profile. After changing the toolkit, run `./sync_skills.sh` to refresh
those copies.
