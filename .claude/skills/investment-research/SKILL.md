---
name: investment-research
description: Evidence-based research on stocks, ETFs, sectors and emerging investment themes for long-term investors, such as AI infrastructure, power grid and utilities, nuclear and uranium, data-center cooling, optical networking, memory, edge AI, robotics or quantum. Produces a dated, sourced research note with a quant snapshot (trend, momentum, drawdowns, peer score), fundamentals and valuation, a bubble and hype check, historical base rates, risks and position-sizing guidance. Use it whenever someone asks whether to buy, hold or sell a stock or ETF, what to invest in now, for a deep dive or comparison of companies or funds, what the next big investment theme is, whether something is a bubble, or how the market looks before investing, even if they never say "research".
---

# Investment research

Help a long-term investor decide with dated facts, honest base rates and explicit
uncertainty. You are not their licensed adviser and you cannot promise returns, so
say what the evidence supports, how confident it is, and what would change the view.

## Ground rules, and why

1. **Date every number and name its source.** Prices and estimates go stale in days.
   Write "as of 2026-11-25" next to figures and keep a link per fact.
2. **Separate the business from the stock.** A great company bought at a bubble or
   peak-cycle price can still lose money for a decade (Cisco took 25 years to regain
   its 2000 peak). Judge quality, then price, then trend.
3. **Lead with base rates.** Most single stocks trail T-bills over their lives, and
   hot thematic funds launched near peaks usually lag. Read
   `references/evidence-base-rates.md` before making long-run claims.
4. **Label hindsight.** A backtest of a list picked today only contains survivors.
   Call it an upper bound.
5. **Size for survival.** Eventual winners fell 60–95% along the way. Every
   recommendation carries a position size and an exit or review trigger.
6. **Say what you cannot know.** If data is missing or a source is thin, say so
   rather than filling the gap with a guess.
7. **Context beats tips.** Taxes, horizon, debt, emergency savings and existing
   concentration change the answer. Ask only when it would change the
   recommendation; otherwise state your assumptions (default: US investor,
   10+ year horizon, already holds a broad index core).

If the user's real question is "how do I reach X dollars" or "is a 50x return
realistic", use the `portfolio-goal-planner` skill too, if available, for the odds
and the allocation.

## Choose the workflow

| Request | Read | Output |
|---|---|---|
| One stock or ETF ("is VRT a buy?", "research Constellation") | `references/single-name.md` | Single-name note |
| Several names or funds ("ETN vs GEV", "best grid ETF") | `references/single-name.md` | One block per name + comparison table |
| A theme or sector ("AI power", "edge AI stocks", "next theme after GPUs") | `references/theme.md` | Theme report |
| "Is this a bubble?", hype checks | `references/bubble-checklist.md` | Scored checklist inside the note |
| "Is now a good time?", market conditions | `references/market-regime.md` | Regime summary |

Run a quick regime check for almost every request. It costs little and it changes
the entry plan: buying all at once vs in stages, and how much cash to hold back.

## Tools bundled with this skill

Python 3 with pandas, numpy and requests. Prices come from Yahoo Finance's public
chart endpoint, with yfinance as a fallback. They are cached in `$STOCKQUANT_CACHE`
(default `<tmp>/stockquant-cache`). Run the scripts from this skill's `scripts/`
folder:

```bash
cd <this-skill>/scripts
python regime_check.py --extra SMH GRID                 # market drawdowns, trend filters, VIX, breadth
python quant_snapshot.py VRT --peers ETN GEV PWR        # trend, momentum, risk, worst drawdowns, peer score
python quant_snapshot.py NVDA --fundamentals            # adds yfinance valuation if the network allows
python theme_screen.py --name "Grid equipment" --tickers GEV ETN PWR HUBB VRT POWL --compare QQQ SMH
python -m stockquant backtest --tickers GEV ETN PWR VRT --strategy momentum --top 3 --start 2020-01-31
```

- If the working repository has its own `stock-quant/` folder, prefer it: it has
  cached prices, an editable `universe.csv` of about 210 tickers, and a full report
  (`python -m stockquant report`).
- The composite score ranks a strong, orderly trend within the names you pass.
  It says nothing about value, so always pair it with valuation.
- If downloads fail, for example because the network blocks Yahoo, say the quant
  snapshot was unavailable and continue with sourced web data. Never invent prices.

## Research process

1. **Frame it.** Restate the question, the horizon and your assumptions in one or
   two lines.
2. **Measure first.** Run `regime_check.py` plus `quant_snapshot.py` or
   `theme_screen.py`. These numbers anchor everything after.
3. **Explain the latest move before anything else.** If the price moved sharply
   in recent weeks, spend your first searches on why: order cancellations,
   guidance cuts, policy or election news, rate moves, financing stress. The
   freshest risk is usually the one that matters most for an entry decision, and
   it is the easiest to miss when the search budget runs out.
4. **Gather fundamentals.** Use primary sources first: earnings releases, 10-Q and
   10-K filings, investor presentations, transcripts. Then reputable media. Get the
   latest quarter's revenue growth, margins, guidance, backlog or orders, free cash
   flow, debt and dilution. For a broad theme, split the research into parallel
   subagents by sub-area if you can. Web searches may share one budget across all
   agents (about 200 per turn), so give each one about 10–20 and ask for dated,
   linked facts.
5. **Value it.** Follow `references/valuation-cheatsheet.md`. Always run the
   cyclical check: a very low P/E on sales growing 75%+ often marks the top of a
   boom, not a bargain.
6. **Check for a bubble** (themes and hot stocks) with
   `references/bubble-checklist.md`, and score it.
7. **Decide.** Pick one verdict class below. Give a size range, an entry plan, a
   review trigger and the bear case in a sentence.
8. **Write it up.** Save the note as markdown (default
   `research/<topic>-<YYYY-MM-DD>.md`, unless the user names a place) using
   `references/report-templates.md`. In chat, give a short summary: verdict, the
   three numbers that matter, and the main risk. Keep the note's qualifiers in
   the summary ("reportedly", "one source", "unverified"): a summary that drops
   them states rumors as facts.

## Verdict classes

Use these instead of buy or sell ratings, because they carry sizing.

- **Core candidate.** Diversified or exceptionally durable, at a reasonable
  valuation: broad index ETFs, or quality compounders at fair prices. Can be a
  large share of a portfolio.
- **Satellite candidate.** Real growth and fundamentals, with higher volatility or
  valuation. About 2–5% per stock, and all satellites together usually 10–30%
  depending on risk tolerance.
- **Watchlist.** Interesting thesis, but the trend is broken (below its 200-day
  average), the valuation is stretched, or the evidence is immature. Name the
  trigger that would upgrade it, for example "two quarters of orders growth and
  price back above its 200-day average".
- **Speculative only.** Pre-revenue, heavy dilution or debt, a price pinned to a
  takeover offer, or a high bubble score. Only money they can afford to lose,
  about 1% or less per name.

## Entry and risk heuristics

Explain these, don't dictate them.

- **Core money.** Investing a lump sum has beaten spreading it out about two
  thirds of the time historically. Spreading it over 3–12 months is reasonable if
  it keeps the investor from panicking.
- **Satellites.** Buy in stages, for example thirds. A stock below its 200-day
  average with negative 12-month momentum often keeps falling, since momentum
  persists over months. Waiting for a base or trend repair costs a little upside
  and avoids many −60% outcomes. If you still suggest a first tranche in a name
  that is below its 200-day average, call it an exception and give the reason,
  in the note and in the chat summary, so the advice does not contradict the
  rule.
- **Rebalancing.** Trim a satellite once it exceeds about 1.5x its target weight,
  and review the thesis each quarter against named triggers. Selling because a
  stock fell is not the rule; selling because the thesis broke is.
- **Leverage.** Avoid leveraged ETFs and margin for long-horizon goals. A daily 3x
  Nasdaq-100 fund would have lost about 100% in 2000–2002.
