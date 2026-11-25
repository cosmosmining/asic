# Researching an investment theme

A theme report answers four questions. Is the demand real and how big is it? Which
listed companies capture the profits? How much of that is already in the price? How
should someone own it, if at all?

## 1. Define the theme and map the value chain

Draw the chain from inputs to end users, for example for AI power:
fuel → generation (gas turbines, nuclear, fuel cells) → grid (transformers,
switchgear, cables, EPC contractors) → data-center electrical and cooling (UPS, busway,
liquid cooling) → data-center owners → hyperscalers and AI labs.

For each link note how scarce it is. Lead times, backlog relative to revenue and
pricing trends show where profits concentrate. In 2026 large transformers had
2.5–4 year lead times and gas-turbine slots were sold out to 2029–30.

## 2. Size the demand, with dates and sources

- Spending or volume forecasts from neutral sources (IEA, EIA, BloombergNEF,
  IDC, Gartner, TrendForce), alongside company guidance.
- The demand driver's own financing. Who pays, and can they keep paying? In 2026
  hyperscaler capex was about $730bn against negative free cash flow at several
  spenders, which made financing the key risk.
- Leading indicators: orders, backlog, book-to-bill, interconnection queues,
  pricing.

## 3. Build the universe

List 10–40 listed names with tickers, grouped by link and stage:
- **Leaders**: profitable, already large in the theme.
- **Emerging**: real revenue from the theme, growing fast.
- **Speculative**: pre-revenue or story-driven.

Add the relevant ETFs, with fee, assets, launch date and top holdings. Note the
"pure play" share: how much of each company's revenue the theme actually drives.

## 4. Real revenue versus narrative

For each sub-theme, show the evidence in the latest quarter: revenue growth, orders,
contracted backlog, named customers. Mark sub-themes as "real now", "early, with
contracts" or "narrative". Many 2025–26 favorites, such as small modular reactors,
quantum computing and humanoid robots, were narrative-heavy. Grid equipment, cooling
and memory had real revenue.

## 5. Measure the market's pricing

Run `python theme_screen.py --name "<theme>" --tickers ... --compare SPY QQQ SMH`.
Report the basket's 1-year and 3-year returns, drawdown from high, volatility, beta,
breadth and crowding (average pairwise correlation). High crowding means the names
are one bet; size them as one position.

Valuation: the median forward P/E and EV/sales of the leaders versus their own
history and the market. Flag any name with a forward P/E above 60, EV/sales above 20,
or that is unprofitable.

## 6. Bubble and hype check

Score `bubble-checklist.md`. Compare with historical analogues: the 1840s railways,
1920s utilities, the 1996–2002 telecom and fiber boom, and the 2020–21 clean-energy,
SPAC and ARKK boom. In each, the technology won while many suppliers' shareholders
lost 80–99%.

## 7. How to own it

- **Default**: a broad core plus a small, diversified satellite in the theme, either
  an ETF or an equal-weight basket of 5–10 leaders with real revenue.
- **Sizing**: the whole theme at about 5–15% of the portfolio for most people, 30% as
  an aggressive ceiling. One name at 2–5%, speculative names at 1% or less.
- **Entry**: in stages. Use trend repair (back above the 200-day average) as a
  trigger for new money after a crash, and rebalance once a year.
- **Kill criteria**: what evidence ends the thesis, for example orders falling two
  quarters in a row, customers cutting capex guidance, or financing drying up.

## 8. Watch list for the next phase

Name the 2–3 sub-themes where attention is moving and the evidence that would show
they have become real. For 2026 that was co-packaged optics, 800V DC power and
silicon-carbide or gallium-nitride power chips, and on-site generation.
