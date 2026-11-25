# Researching one stock or ETF

Work through these in order. Each step says what to collect and why it matters.
Keep a running list of facts with date and source link.

## 1. Snapshot (numbers first)

Run `python quant_snapshot.py TICKER --peers <3-6 close competitors> --years 5`.
Record: trend state, distance from 52-week high, 12-month and 12-1 momentum,
1-year volatility, worst 1-year drop, beta, the full-history worst drawdown with
its recovery date, and the peer rank.

Why: the trend and drawdown history tell the investor what holding this will feel
like. A 70% volatility name will likely drop 40%+ at some point in any year.

## 2. What the business does and how it makes money

- Segments and the share of revenue and profit from each. Who pays and why.
- Where it sits in its value chain (supplier, integrator, platform, end user) and
  who has pricing power over whom.
- Customer concentration. Any customer above 10% of revenue is named in filings
  (10-K, "major customers"). AI suppliers often depend on 3–5 hyperscalers.

## 3. Latest results (most recent quarter, with the date)

- Revenue growth year over year, gross and operating margin, and their trend over
  4–8 quarters.
- Guidance: raised, held or cut? Guidance changes move stocks more than beats.
- Orders, backlog or remaining performance obligations for equipment and
  infrastructure businesses. A book-to-bill above 1 means growing demand.
- Free cash flow, net debt, interest coverage, share count change (dilution) and
  stock-based compensation as a share of revenue.

## 4. Valuation (see valuation-cheatsheet.md)

- Forward P/E, EV/sales, EV/EBITDA and FCF yield, compared with its own 5-year
  range, its peers and its growth.
- Run the cyclical check: memory, semicap, energy, materials and commodity-linked
  names look cheapest at the peak.
- Reverse-DCF sanity check: what growth for how long is the price assuming? Is that
  plausible against the market size?

## 5. Moat and durability

Ask what stops a competitor or customer from taking the profits: switching costs,
scale, network effects, IP, regulation, unique assets. Look for evidence such as
stable or rising margins through a downturn and pricing power, not adjectives.

## 6. Risks and bear case

- The single most likely way this loses 50%: overbuild, a cyclical downturn, a
  customer bringing work in-house, regulation, dilution, a financing squeeze or
  key-person risk.
- Balance-sheet stress: debt maturities, covenants, refinancing yields. CoreWeave
  bonds yielding 16%+ in Nov 2026 is the kind of signal to look for.
- For ETFs: expense ratio, top-10 concentration, overlap with what the user already
  owns, index rules, liquidity (assets, spread) and launch date (see the thematic
  ETF evidence in evidence-base-rates.md).

## 7. Catalysts and review triggers

List 2–4 dated events (earnings, product ramps, regulatory decisions) and what
outcome would upgrade or downgrade the verdict.

## 8. Verdict and sizing

Choose one class from SKILL.md (core, satellite, watchlist or speculative only).
Give a size range, an entry plan (lump sum, thirds, or wait for a trigger) and the
bear case in one sentence.

## For ETFs specifically

Replace steps 2–5 with: what index or rules it follows, holdings and weights, cost,
assets and spread, tracking versus its index, how its top holdings score on steps
3–4, and overlap with the user's core (for example, SMH and QQQ share NVDA, AVGO and
AMD).
