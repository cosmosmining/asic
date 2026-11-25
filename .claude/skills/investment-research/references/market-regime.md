# Market regime check

Run `python regime_check.py --extra SMH GRID <theme ETFs>`, then add macro facts from
dated sources: the policy rate and the next central-bank meeting, the 10-year yield,
the latest CPI or PCE, earnings-season tone and major policy events. Even on a tight
search budget, get the first three (one search usually covers them): rates and
inflation decide how much any valuation is worth.

## Reading it

| Signal | What it means | Practical effect |
|---|---|---|
| S&P 500 within 5% of its high, above its 10-month average | Normal uptrend | Invest new money on schedule |
| 5–10% off the high, below its 10-month average | Pullback with a broken trend | Core contributions continue. Stage satellite buys |
| 10–20% off (correction) | Elevated risk, often a good time for long-horizon core money | Keep buying the core on schedule. Satellites wait for trend repair or buy in thirds |
| 20%+ off (bear market) | Historically strong 10-year forward returns from here, but deep further drops are possible | Keep the plan. Rebalance into stocks if the plan allows. Avoid leverage |
| VIX above 25 (high fear) | Large daily swings likely | Use limit orders and smaller increments. Don't sell in panic |
| Breadth falling while the index holds up | Leadership narrowing | Check concentration risk in the core (top-10 weight) |

## Trend filters

A price above its ~10-month average is the classic rule (Faber 2007). Over 1926–2023
it cut the S&P 500's worst drawdown from about −82% to about −46% to −51%, for
0–1.6 points of annual return. It suits satellites and people who might panic-sell.
It works poorly in sideways, choppy markets (whipsaws), and it is not a reason to
stop long-term core contributions.

## What not to do

- Don't call the bottom. No regime reading predicts next month.
- Don't move the whole core to cash on a signal. Missing the best days, which
  cluster near the worst ones, costs more than most drawdowns.
- Don't treat breadth or VIX as buy or sell triggers alone. They size and pace
  decisions.
