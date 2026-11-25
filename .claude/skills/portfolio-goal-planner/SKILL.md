---
name: portfolio-goal-planner
description: Turns an investing goal ("50x my money", "$1M by 45", "retire in 20 years", "how do I grow $20k a lot") into an honest, numbers-first plan. Covers the return it requires, Monte Carlo odds with monthly contributions, how often the S&P 500 achieved it since 1926, the drawdowns to expect, a core-satellite allocation of low-cost ETFs, position-size limits for risky bets, and rebalancing rules. Use it whenever someone asks how to reach a money target, whether a return goal is realistic, how much to put in stocks vs a theme or single stock, how to size a risky bet, lump sum vs dollar-cost averaging, or for a long-term investment plan, even if they only say they want their money to make a lot of money.
---

# Portfolio goal planner

People often arrive with a number ("50x", "$1M") and no sense of what it takes.
Your job is to show the math, the odds and the trade-offs plainly, then give a plan
they can follow through bad years. Never promise an outcome. A plan that survives a
50% crash beats a plan that is optimal on paper.

## 1. Capture the inputs

Ask only for what is missing and would change the answer. Otherwise assume, and say
what you assumed.

| Input | Default if not given |
|---|---|
| Starting amount | Ask: the core of the answer depends on it |
| Monthly savings, and yearly raise | 0. Offer a version with savings |
| Horizon in years | Ask, or show 10/20/30 |
| Target: a multiple or a dollar amount | As stated. A multiple means "of money put in" when there are contributions |
| Biggest drop they could sit through without selling | 35% |
| Existing holdings, debt, emergency fund | Assume a 3–6 month emergency fund exists and no high-interest debt; flag it if unknown |
| Country and account type | US, mix of retirement and taxable accounts |

High-interest debt above about 8% APR and a missing emergency fund come before
investing. Paying off a 22% card is a guaranteed 22% return.

## 2. Run the numbers

```bash
cd <this-skill>/scripts
python goal_plan.py --initial 15000 --monthly 800 --raise 0.03 --years 25 --target-multiple 50
python goal_plan.py --initial 200000 --years 15 --target-amount 2000000 --scenario "80/20 stocks/bonds" 0.09 0.15
python goal_plan.py ... --backtest-mix VTI=0.6 VXUS=0.25 QQQM=0.15   # replays a real ETF mix (needs internet)
```

The script runs offline except for `--backtest-mix`. It prints:
1. The return the exact plan needs, what it grows to at 4–20% a year, and what a 1%
   yearly fee would cost this plan.
2. A replay of the plan through every start month of S&P 500 history since 1926,
   nominal and after inflation, using the bundled Shiller data (which ends mid-2023).
3. A stress test: one 50% crash early, midway and in the final year, with and
   without a recovery. Use this table rather than building your own.
4. Monte Carlo outcomes for each scenario: 10th, 50th and 90th percentile, chance of
   the target, typical worst drop, chance of ending below the money put in. Rows
   marked "assumed" are hypothetical; never present their odds as evidence.
5. Kelly sizing limits for concentrated bets.

The toolkit in `scripts/stockquant/` also offers
`python -m stockquant goal --bootstrap SPY ...` to resample real SPY history. If the
repository has its own `stock-quant/` folder, that copy has cached prices too.

## 3. Interpret honestly

- **Compare the required return with reality.** The S&P 500 compounded about 10%
  nominal and 7% real from 1926 to 2023, and forecasts for the next decade are
  lower (about 4–7.5%). A plan needing 25% a year is a lottery ticket. Say so
  kindly, and show what is achievable.
- **Contributions are not lump sums.** "50x my money" with steady savings means 50x
  every dollar, including the last one invested a month before the deadline. That
  is far harder than 50x a lump sum. Show both framings if the user mixed them up.
- **Volatility drag.** Higher-risk scenarios have higher averages but often worse
  typical outcomes and much worse bad cases. Point to the "typical yearly" and
  "unlucky 1 in 10" columns.
- **Time is the lever that works.** The S&P 500 turned $1 into 50x in about 72% of
  40-year periods and almost never in 20-year ones. More years and more savings
  beat a riskier allocation.
- **Short histories flatter.** A mix replayed only since 2011 saw mostly a bull
  market; weigh it against the 1926+ replay.

Read `references/goal-math.md` for formulas and `references/evidence-base-rates.md`
for citations.

## 4. Design the allocation

Use `references/allocation-playbook.md`. In short:
- **Core (70–100%)**: low-cost broad index ETFs, US total market plus international,
  optionally a growth tilt. This is what makes the base case work.
- **Satellite (0–30%)**: themes or single stocks the user believes in, for example
  AI infrastructure. Cap single stocks at 2–5% each and speculative names at 1%.
  Size the satellite so that losing 70% of it leaves the plan intact.
- **Ballast**: bonds or T-bills only as needed for the drawdown tolerance and for
  money needed within about 5 years.
- **Rules**: rebalance yearly or at bands, automate contributions, and write down in
  advance what they will do in a 30% crash ("keep contributing; rebalance").

Name specific funds with their fees as examples (for example VTI, VOO or SPYM,
VXUS, QQQM, BND or SGOV), not as the only choice, and note that the user should check
the current fees and fit with their own accounts.

## 5. Stress-test, then deliver

- Use the script's stress-test table to show sequence risk, and give the dollar
  amount of the typical worst drop at the end of the horizon.
- Deliver a short summary in chat: target, required return, realistic range,
  recommended mix, and the one behavior that matters most. Lead with the honest
  answer to "is this realistic", in the user's own terms.
- Save the plan to one markdown file (default `research/goal-plan-<YYYY-MM-DD>.md`).
  Keep it focused, about 1,500 words plus the key tables, with the raw script
  output in an appendix at the end rather than in many separate files. A plan the
  user actually reads beats an exhaustive one.
- Close with what would change the plan: income changes, a much shorter horizon,
  or a large market move.
