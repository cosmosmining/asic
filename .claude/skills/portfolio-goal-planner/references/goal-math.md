# Goal math

## Compounding

- Multiple after n years at rate r: (1 + r)^n.
- Years to a multiple M: ln(M) / ln(1 + r). For 50x: 58 years at 7%, 41 at 10%,
  28 at 15%, 21.5 at 20%, 15 at 30%.
- Rate needed for M in n years: M^(1/n) − 1. For 50x: 47.9% (10y), 29.8% (15y),
  21.6% (20y), 16.9% (25y), 13.9% (30y), 10.3% (40y).
- Rule of 72: years to double ≈ 72 / (rate in %).

## Contributions

Future value with monthly contributions c growing at g a year, monthly rate i:
FV = initial × (1+i)^N + Σ c_m × (1+i)^(N−m). `goal_plan.py` computes it exactly and
solves for the rate a target needs.

A multiple of contributions is much harder than a multiple of a lump sum, because
later dollars have little time to grow. $500 a month for 30 years at 10% makes about
5.7x the money put in, not 17x.

## Volatility drag and the median

With arithmetic mean μ and volatility σ, the typical (median) compound rate is about
μ − σ²/2. Examples:
- 10% mean, 16% vol → about 8.8% typical
- 20% mean, 35% vol → about 15%
- 25% mean, 60% vol → about 12.7%, lower than the 20%/35% case despite the
  higher average

So concentrating in a volatile bet raises the average outcome and the lucky tail,
but often lowers the typical result and greatly worsens the bad cases.

## Real vs nominal

Inflation of 2.5–3.5% a year halves purchasing power in about 20–28 years. A
"$1M in 30 years" goal is about $360–480K in today's money. State targets in today's
dollars when the goal is a lifestyle.

## Sequence risk

The same average return gives very different results depending on when the bad
years land. A crash just before the money is needed hurts most. That is why plans
add bonds or cash for money needed within about 5 years and keep contributing
through crashes during the accumulation years.

## Kelly sizing

Growth-optimal fraction f* ≈ (μ − r_f) / σ². Use a quarter to half of it: estimated
edges are noisy, and full Kelly has about a 50% chance of halving the stake at some
point. For diversified portfolios the formula exceeds 100% (leverage), which is
unwise for individuals. For a single volatile stock (25% mean, 60% vol) it gives
about 60%, so a quarter to half Kelly means 15–30%. That is still above most
practitioners' 2–5% single-stock caps once estimation error is considered.

## Costs and taxes

A 1% yearly fee takes about 30% of a 40-year lump-sum outcome, and about a quarter
of a 40-year monthly-savings plan (later dollars pay the fee for fewer years).
`goal_plan.py` prints the exact cost for the user's plan. Paying tax on gains every
year instead of deferring costs even more. Prefer low-cost index funds, tax-advantaged
accounts and low turnover.
