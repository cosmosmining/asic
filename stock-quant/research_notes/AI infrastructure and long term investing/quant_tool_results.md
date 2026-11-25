# Quant tool results (stock-quant), computed 2026-11-25

Source: the `stock-quant` Python toolkit built in this session (repo folder `stock-quant/`). Prices are Yahoo Finance daily adjusted closes through 2026-11-25 for 214 tickers; long-run index history is Robert Shiller's monthly S&P 500 data (1871–2023). Valuation flags use a Yahoo fundamentals snapshot (ratios dated 2026-11-20/23) for ~114 stocks; missing = not in snapshot.

Key caveats the report must carry:
- Suite B (AI-infrastructure backtests 2016→today) and the satellite sleeve in Suite C use a universe picked in 2026 with hindsight (survivorship bias). Treat their returns as an upper bound, not an expectation.
- Monte Carlo/lognormal probabilities depend entirely on the assumed mean and volatility; 'measured' rows use each ETF's own history.
- Screen scores are relative (percentiles within each group) and price-based: high score = strong, orderly trend, not cheapness.
- Signals are mechanical rules, not forecasts.

## Theme baskets (equal-weight, as of 2026-11-25)

| Theme | Group | N | 1y | 3y CAGR | From 1y high | Vol 1y |
|---|---|---:|---:|---:|---:|---:|
| Memory | compute | 3 | 123.6% | 84.0% | -53.4% | 70% |
| AI cybersecurity | edge_emerging | 2 | 73.2% | 43.6% | -20.0% | 53% |
| Edge AI SoC | edge_emerging | 2 | 72.7% | 36.7% | -22.9% | 49% |
| Analog/edge | edge_emerging | 2 | 35.7% | 20.5% | -21.3% | 44% |
| Accelerators | compute | 2 | 30.6% | 47.6% | -36.4% | 55% |
| Networking | compute | 2 | 29.0% | 36.7% | -22.3% | 43% |
| Servers & racks | compute | 4 | 25.0% | 56.4% | -46.5% | 66% |
| Optical | compute | 5 | 24.8% | 71.0% | -62.0% | 89% |
| ALL AI compute, networking & data centers | compute | 50 | 18.9% | 59.8% | -45.8% | 56% |
| Data-center REIT | compute | 2 | 18.7% | 9.7% | -13.6% | 26% |
| Semicap | compute | 4 | 18.4% | 29.7% | -51.3% | 61% |
| Gas midstream | power_grid | 3 | 16.3% | 25.5% | -8.4% | 20% |
| Utilities | power_grid | 6 | 13.1% | 19.6% | -3.0% | 16% |
| Edge AI IP | edge_emerging | 2 | 11.1% | 18.5% | -58.4% | 75% |
| Power semis | edge_emerging | 5 | 11.0% | 4.4% | -61.6% | 71% |
| On-site power | power_grid | 3 | 9.6% | 62.3% | -46.0% | 55% |
| Custom silicon & networking | compute | 2 | 8.1% | 40.2% | -45.7% | 61% |
| Copper | power_grid | 2 | 8.0% | 14.9% | -37.1% | 51% |
| ALL Edge AI & emerging themes | edge_emerging | 38 | 7.5% | 37.3% | -36.1% | 42% |
| DC cooling | power_grid | 4 | 3.2% | 26.8% | -32.0% | 44% |
| Electrical equipment | power_grid | 3 | -0.3% | 15.7% | -28.3% | 36% |
| Hyperscaler | compute | 4 | -1.2% | 20.4% | -14.4% | 26% |
| DC construction | power_grid | 4 | -2.6% | 61.7% | -51.8% | 62% |
| DC power & cooling | power_grid | 2 | -3.2% | 39.7% | -47.2% | 60% |
| Gas turbines & grid | power_grid | 3 | -5.8% | 97.0% | -39.0% | 37% |
| Advanced packaging | compute | 3 | -8.5% | 9.3% | -55.4% | 72% |
| Connectivity | compute | 2 | -9.4% | n/a | -59.9% | 96% |
| Grid EPC | power_grid | 4 | -12.2% | 31.4% | -52.3% | 53% |
| ALL AI power, grid & cooling | power_grid | 57 | -12.9% | 43.1% | -36.2% | 35% |
| IPP power | power_grid | 3 | -23.7% | 51.5% | -30.7% | 51% |
| AI software | edge_emerging | 2 | -26.3% | 42.1% | -29.7% | 54% |
| Neocloud | compute | 2 | -32.0% | n/a | -66.5% | 105% |
| Space | edge_emerging | 2 | -38.1% | 103.8% | -74.4% | 96% |
| Miner-to-AI hosting | compute | 7 | -45.0% | 38.3% | -69.6% | 91% |
| Uranium | power_grid | 2 | -45.8% | 6.7% | -63.2% | 61% |
| Quantum | edge_emerging | 3 | -67.1% | 93.3% | -71.4% | 93% |
| SMR developer | power_grid | 3 | -80.1% | 47.3% | -80.5% | 87% |
| Storage | power_grid | 2 | -84.7% | -8.3% | -87.4% | 100% |

## Leverage illustration: Nasdaq-100 (QQQ) 1x vs simulated daily-reset 2x/3x since March 1999

| Leverage | CAGR | Max drawdown | 2000–02 drawdown | Multiple |
|---|---:|---:|---:|---:|
| 1x | 10.2% | -83.0% | -83.0% | 14.7x |
| 2x | 9.1% | -98.9% | -98.7% | 11.3x |
| 3x | 1.4% | -100.0% | -100.0% | 1.5x |

## Contribution plan simulation: $10,000 now + $500/month rising 3%/yr for 30 years (20,000 paths)

| Scenario | Contributed | 10th pct | Median | 90th pct | P(≥10x contributions) | P(≥50x contributions) | Median worst drawdown |
|---|---:|---:|---:|---:|---:|---:|---:|
| US stocks, forward-looking (6.5% mean, 16% vol) | $295,452 | $358,873 | $681,134 | $1,391,669 | 0.6% | 0.0% | -40% |
| US stocks, long-run history (11.8% mean, 19.5% vol) | $295,452 | $696,750 | $1,626,874 | $4,141,136 | 20.6% | 0.1% | -38% |
| Nasdaq-100-like growth (14% mean, 24% vol) | $295,452 | $763,536 | $2,170,444 | $6,932,928 | 36.3% | 2.0% | -45% |
| Diversified AI-infra basket (20% mean, 35% vol) | $295,452 | $1,025,908 | $4,673,404 | $25,003,657 | 64.4% | 18.9% | -57% |
| Single high-flyer stock (25% mean, 60% vol) | $295,452 | $381,894 | $3,313,788 | $45,463,827 | 52.3% | 23.0% | -83% |

## Bootstrap (12-month blocks of real monthly returns, 20,000 paths): P(lump sum ≥ 50x)

| Series | Hist CAGR | Hist vol | Years of data | 10y | 15y | 20y | 25y | 30y | 35y | 40y |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| S&P 500 (SPY, since 1993) | 10.6% | 15% | 33.8 | 0% | 0% | 0% | 4% | 17% | 37% | 57% |
| Nasdaq-100 (QQQ, since 1999) | 10.1% | 23% | 27.7 | 0% | 0% | 4% | 12% | 23% | 35% | 47% |
| Semiconductors (SMH, since 2000) | 9.3% | 32% | 26.4 | 0% | 3% | 13% | 26% | 41% | 54% | 65% |
| Sector momentum rule (since 2000) | 9.2% | 14% | 26.8 | 0% | 0% | 0% | 0% | 3% | 13% | 33% |

## Model portfolio allocations (illustrative)

- **Steady compounder**: VTI 60%, QQQM 15%, VXUS 20%, BND 5%
- **Growth tilt**: VTI 45%, QQQM 20%, SMH 10%, VXUS 10%, AI satellite (screen picks) 15%
- **Aggressive AI-infra**: VTI 35%, QQQM 20%, SMH 15%, AI satellite (screen picks) 30%

---

# Full tool summary (generated file output/SUMMARY.md)

# stock-quant summary — data as of 2026-11-25

_Generated by `python -m stockquant report`. Educational research output, not financial advice._

## Market regime now

| Index | From 52w high | 1m | YTD | 12m | 1m vol (ann.) | Above 10m avg |
|---|---:|---:|---:|---:|---:|---|
| SPY | -8.0% | -6.9% | 5.9% | 5.7% | 31% | no |
| QQQ | -16.6% | -12.1% | 3.5% | 1.8% | 47% | no |
| SMH | -36.8% | -24.3% | 17.3% | 16.3% | 92% | no |
| VTI | -7.9% | -6.5% | 6.2% | 5.8% | 30% | no |
| EFA | -8.9% | -4.3% | 4.9% | 7.1% | 25% | no |
| GRID | -24.5% | -10.2% | -1.3% | -1.4% | 45% | no |
| XLU | -6.7% | 1.8% | 4.3% | 3.6% | 14% | no |
| XLE | -13.0% | -10.7% | 38.9% | 36.4% | 30% | yes |

VIX 28.3 on 2026-11-25 (1y median 17.1, 1y max 35.9).

Breadth (share of names above their 200-day average): AI power, grid & cooling 9%, AI compute, networking & data centers 2%, Edge AI & emerging themes 26%, Quality compounders 100%, US sector ETFs 67%, Thematic ETFs 9%

## Current rule-based signals

Trend filters (price above ~10-month average): SPY ❌, QQQ ❌, SMH ❌, VTI ❌, EFA ❌, GRID ❌

AI-infra momentum sleeve (top 10, inverse-vol, 15% cap):

| Ticker | Weight | Theme |
|---|---:|---|
| SO | 15.0% | Utilities |
| D | 15.0% | Utilities |
| AEP | 15.0% | Utilities |
| AAPL | 14.7% | Edge AI devices |
| MSFT | 11.8% | Hyperscaler |
| SYNA | 7.4% | Edge AI IoT |
| TXN | 6.3% | Analog/edge |
| PANW | 5.2% | AI cybersecurity |
| CRWD | 5.1% | AI cybersecurity |
| NET | 4.6% | Edge cloud |

Cash in sleeve: 0.0%

Sector momentum (top 3): XLE, XLK, XLB

Dual momentum: EFA

## Screen — Core ETFs (top 12)

| # | Ticker | Score | Trend | 12m | Vol | MaxDD 1y | Valuation |
|---:|---|---:|---|---:|---:|---:|---|
| 1 | DGRO | 88.6 | strong uptrend | 16.6% | 10% | -6% |  |
| 2 | SCHD | 87.4 | strong uptrend | 31.8% | 12% | -7% |  |
| 3 | VIG | 79.5 | strong uptrend | 11.5% | 11% | -8% |  |
| 4 | RSP | 76.9 | strong uptrend | 14.2% | 12% | -8% |  |
| 5 | AVUV | 74.8 | weakening | 16.4% | 15% | -11% |  |
| 6 | QUAL | 74.5 | uptrend (pullback) | 9.2% | 13% | -9% |  |
| 7 | SPYM | 65.5 | weakening | 5.7% | 15% | -11% |  |
| 8 | VOO | 65.2 | weakening | 5.7% | 15% | -11% |  |
| 9 | IVV | 64.0 | weakening | 5.7% | 15% | -11% |  |
| 10 | SPY | 53.8 | weakening | 5.7% | 15% | -11% |  |
| 11 | VTI | 53.3 | weakening | 5.8% | 15% | -11% |  |
| 12 | VGT | 49.3 | weakening | 7.3% | 29% | -25% |  |

## Screen — US sector ETFs (top 12)

| # | Ticker | Score | Trend | 12m | Vol | MaxDD 1y | Valuation |
|---:|---|---:|---|---:|---:|---:|---|
| 1 | XLV | 83.3 | strong uptrend | 21.9% | 17% | -10% |  |
| 2 | XLE | 76.7 | uptrend (pullback) | 36.4% | 23% | -15% |  |
| 3 | XLP | 68.3 | strong uptrend | 20.9% | 16% | -10% |  |
| 4 | XLF | 65.0 | strong uptrend | 6.9% | 15% | -15% |  |
| 5 | XLB | 57.8 | recovering | 18.2% | 19% | -12% |  |
| 6 | XLK | 45.0 | weakening | 6.8% | 31% | -26% |  |
| 7 | XLI | 40.0 | downtrend | 6.6% | 19% | -16% |  |
| 8 | XLU | 39.4 | downtrend | 3.6% | 15% | -16% |  |
| 9 | XLY | 24.4 | recovering | -1.1% | 20% | -15% |  |

## Screen — Thematic ETFs (top 12)

| # | Ticker | Score | Trend | 12m | Vol | MaxDD 1y | Valuation |
|---:|---|---:|---|---:|---:|---:|---|
| 1 | CIBR | 90.0 | uptrend (pullback) | 27.2% | 32% | -20% |  |
| 2 | ZAP | 83.3 | downtrend | 6.0% | 17% | -13% |  |
| 3 | PAVE | 77.9 | downtrend | 6.9% | 22% | -18% |  |
| 4 | AIQ | 77.2 | weakening | 4.0% | 32% | -27% |  |
| 5 | VOLT | 73.2 | downtrend | 6.6% | 29% | -26% |  |
| 6 | SMH | 72.9 | weakening | 16.3% | 47% | -40% |  |
| 7 | DTCR | 70.4 | downtrend | 8.2% | 27% | -31% |  |
| 8 | QTUM | 68.1 | weakening | 3.6% | 36% | -34% |  |
| 9 | SOXX | 66.0 | weakening | 24.5% | 53% | -43% |  |
| 10 | GRID | 64.5 | downtrend | -1.4% | 27% | -27% |  |
| 11 | CHAT | 59.5 | downtrend | 3.9% | 46% | -42% |  |
| 12 | IGV | 55.6 | uptrend (pullback) | -13.2% | 33% | -32% |  |

## Screen — AI power, grid & cooling (top 12)

| # | Ticker | Score | Trend | 12m | Vol | MaxDD 1y | Valuation |
|---:|---|---:|---|---:|---:|---:|---|
| 1 | ET | 93.0 | weakening | 20.1% | 18% | -14% |  |
| 2 | KMI | 87.7 | weakening | 18.4% | 22% | -12% |  |
| 3 | JCI | 82.7 | weakening | 20.5% | 34% | -18% |  |
| 4 | ETR | 82.3 | downtrend | 16.7% | 20% | -16% |  |
| 5 | WMB | 81.7 | downtrend | 9.0% | 26% | -18% |  |
| 6 | AEP | 78.9 | recovering | 11.9% | 18% | -15% |  |
| 7 | SO | 76.4 | recovering | 13.7% | 18% | -16% |  |
| 8 | D | 76.2 | recovering | 19.9% | 21% | -15% |  |
| 9 | 6501.T | 74.8 | weakening | 2.7% | 38% | -23% |  |
| 10 | PWR | 70.5 | downtrend | 22.9% | 51% | -35% |  |
| 11 | TT | 70.4 | downtrend | 1.2% | 31% | -23% |  |
| 12 | XEL | 69.4 | recovering | 8.4% | 19% | -15% |  |

## Screen — AI compute, networking & data centers (top 12)

| # | Ticker | Score | Trend | 12m | Vol | MaxDD 1y | Valuation |
|---:|---|---:|---|---:|---:|---:|---|
| 1 | HPE | 82.4 | weakening | 78.1% | 66% | -45% |  |
| 2 | AMD | 82.2 | weakening | 86.3% | 75% | -38% | reasonable |
| 3 | DELL | 80.8 | weakening | 116.1% | 84% | -53% | reasonable |
| 4 | ANET | 79.9 | weakening | 27.5% | 59% | -27% |  |
| 5 | MU | 79.4 | weakening | 153.7% | 87% | -51% | peak-cycle risk (low P/E on boom earnings) |
| 6 | EQIX | 74.7 | downtrend | 34.6% | 27% | -14% |  |
| 7 | TSM | 74.5 | weakening | 17.4% | 46% | -34% |  |
| 8 | CSCO | 72.6 | weakening | 23.1% | 38% | -30% |  |
| 9 | STX | 70.2 | downtrend | 70.4% | 78% | -58% |  |
| 10 | ASML | 69.2 | weakening | 19.2% | 50% | -36% |  |
| 11 | NVDA | 65.0 | weakening | -18.0% | 52% | -48% | peak-cycle risk (low P/E on boom earnings) |
| 12 | MSFT | 64.5 | uptrend (pullback) | 2.2% | 34% | -28% |  |

## Screen — Edge AI & emerging themes (top 12)

| # | Ticker | Score | Trend | 12m | Vol | MaxDD 1y | Valuation |
|---:|---|---:|---|---:|---:|---:|---|
| 1 | PANW | 92.6 | uptrend (pullback) | 79.1% | 52% | -27% | stretched |
| 2 | CRWD | 90.0 | uptrend (pullback) | 63.5% | 58% | -33% | speculative (unprofitable) |
| 3 | AAPL | 87.0 | strong uptrend | 28.0% | 25% | -13% | premium |
| 4 | TXN | 83.0 | uptrend (pullback) | 51.2% | 47% | -23% | reasonable |
| 5 | 2454.TW | 81.5 | uptrend (pullback) | 162.3% | 67% | -37% | reasonable |
| 6 | ADI | 81.2 | weakening | 19.9% | 45% | -30% | reasonable |
| 7 | NET | 76.0 | uptrend (pullback) | 41.0% | 68% | -32% | speculative (unprofitable) |
| 8 | SYNA | 66.0 | strong uptrend | 50.4% | 58% | -40% | speculative (unprofitable) |
| 9 | PLTR | 65.4 | uptrend (pullback) | -10.0% | 61% | -45% | stretched |
| 10 | ROK | 63.2 | downtrend | -3.5% | 35% | -26% | reasonable |
| 11 | CGNX | 60.6 | downtrend | 22.8% | 60% | -39% | reasonable |
| 12 | STM | 60.0 | downtrend | 54.2% | 64% | -51% | reasonable |

## Screen — Quality compounders (top 12)

| # | Ticker | Score | Trend | 12m | Vol | MaxDD 1y | Valuation |
|---:|---|---:|---|---:|---:|---:|---|
| 1 | V | 85.0 | strong uptrend | 29.1% | 23% | -17% |  |
| 2 | LLY | 75.0 | strong uptrend | 38.6% | 35% | -23% |  |
| 3 | COST | 65.7 | strong uptrend | 25.6% | 20% | -18% |  |
| 4 | MA | 63.6 | strong uptrend | 21.8% | 23% | -18% |  |
| 5 | BRK-B | 60.7 | strong uptrend | 14.9% | 15% | -8% |  |
| 6 | SPGI | 25.0 | strong uptrend | -1.6% | 31% | -28% |  |
| 7 | MCO | 25.0 | strong uptrend | -1.3% | 29% | -24% |  |

## Backtests

### Long-history strategies (2000 → today)

_Universes chosen without hindsight (broad index / sector ETFs). Includes the 2000-02 and 2008 bear markets._

| Strategy | CAGR | Vol | Sharpe | Max DD | Multiple |
|---|---:|---:|---:|---:|---:|
| S&P 500 buy & hold (SPY) | 8.2% | 19% | 0.40 | -55% | 8.2x |
| Nasdaq-100 buy & hold (QQQ) | 8.3% | 26% | 0.36 | -83% | 8.4x |
| SPY with 10-month trend filter | 8.8% | 12% | 0.59 | -25% | 9.6x |
| Sector momentum: top 3 of 9 SPDR sectors | 9.2% | 17% | 0.48 | -36% | 10.7x |
| 60% SPY + 40% QQQ with trend filter | 9.1% | 16% | 0.48 | -44% | 10.2x |
| Dual momentum (SPY/EFA/IEF) | 9.1% | 16% | 0.52 | -34% | 7.6x |

### AI-infrastructure strategies (2016 → today)

_WARNING: the AI universe was picked in 2026 with hindsight (survivorship bias). These returns overstate what was knowable in real time._

| Strategy | CAGR | Vol | Sharpe | Max DD | Multiple |
|---|---:|---:|---:|---:|---:|
| S&P 500 (SPY) | 14.7% | 17% | 0.73 | -34% | 4.4x |
| Nasdaq-100 (QQQ) | 19.0% | 22% | 0.78 | -35% | 6.6x |
| Semiconductors (SMH) | 31.0% | 33% | 0.89 | -45% | 18.7x |
| AI-infra universe, equal weight | 33.4% | 28% | 1.06 | -42% | 22.6x |
| AI-infra momentum top 10 + trend filter | 44.5% | 35% | 1.13 | -45% | 53.9x |
| Core-satellite: 70% VTI + 30% AI momentum | 23.8% | 21% | 0.99 | -35% | 10.1x |

### Model portfolios (2012 → today, ETF proxies)

_Backtests use long-history proxies (QQQ for QQQM, EFA for VXUS). Satellite sleeve is the AI momentum rule and inherits Suite B's hindsight bias._

| Strategy | CAGR | Vol | Sharpe | Max DD | Multiple |
|---|---:|---:|---:|---:|---:|
| Steady compounder | 12.6% | 16% | 0.72 | -32% | 5.8x |
| Growth tilt | 18.9% | 19% | 0.90 | -33% | 12.9x |
| Aggressive AI-infra | 23.6% | 22% | 0.99 | -33% | 23.0x |
| S&P 500 (SPY) | 14.1% | 16% | 0.77 | -34% | 7.0x |

## How often did the S&P 500 itself deliver 50x?

Shiller monthly total-return data 1871–2023-06; CAGR since 1926: 10.2% nominal, 7.0% real.

| Basis | Years | Windows | Share reaching 50x | Median multiple | Worst | Best |
|---|---:|---:|---:|---:|---:|---:|
| nominal | 10 | 1050 | 0.0% | 2.7x | 0.7x | 6.8x |
| nominal | 20 | 930 | 0.0% | 8.0x | 1.5x | 27.2x |
| nominal | 30 | 810 | 1.2% | 21.5x | 9.1x | 55.4x |
| nominal | 40 | 690 | 72.5% | 65.4x | 20.6x | 141.6x |
| nominal | 50 | 570 | 96.5% | 155.5x | 35.1x | 629.0x |
| real | 10 | 1050 | 0.0% | 2.0x | 0.5x | 5.6x |
| real | 20 | 930 | 0.0% | 3.8x | 1.1x | 12.8x |
| real | 30 | 810 | 0.0% | 8.0x | 3.3x | 23.9x |
| real | 40 | 690 | 0.0% | 13.5x | 4.5x | 46.2x |
| real | 50 | 570 | 8.6% | 21.8x | 8.2x | 90.5x |

## The 50x math

| Horizon | CAGR needed for 50x |
|---|---:|
| 10y | 47.9% |
| 15y | 29.8% |
| 20y | 21.6% |
| 25y | 16.9% |
| 30y | 13.9% |
| 35y | 11.8% |
| 40y | 10.3% |

### Probability a lump sum reaches 50x (lognormal model)

| Scenario | 10y | 15y | 20y | 25y | 30y | 35y | 40y | Median CAGR |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| US stocks, forward-looking (6.5% mean, 16% vol) | 0% | 0% | 0% | 0% | 0% | 1% | 3% | 5.3% |
| US stocks, long-run history (11.8% mean, 19.5% vol) | 0% | 0% | 1% | 4% | 14% | 30% | 48% | 10.1% |
| Nasdaq-100-like growth (14% mean, 24% vol) | 0% | 0% | 3% | 13% | 29% | 47% | 64% | 11.6% |
| Diversified AI-infra basket (20% mean, 35% vol) | 0% | 5% | 20% | 40% | 58% | 73% | 83% | 15.2% |
| Single high-flyer stock (25% mean, 60% vol) | 3% | 11% | 23% | 34% | 45% | 54% | 62% | 12.7% |
| SPY 1993-now (measured) | 0% | 0% | 0% | 1% | 8% | 26% | 49% | 10.2% |
| QQQ 1999-now (measured) | 0% | 0% | 1% | 7% | 18% | 32% | 48% | 10.1% |
| SMH 2000-now (measured) | 0% | 1% | 5% | 13% | 24% | 35% | 47% | 9.9% |
