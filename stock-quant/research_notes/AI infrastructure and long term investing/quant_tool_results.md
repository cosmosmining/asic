# Quant tool results (stock-quant), computed 2026-11-25

Source: the `stock-quant` Python toolkit built in this session (repo folder `stock-quant/`). Prices are Yahoo Finance daily adjusted closes through 2026-11-25 for 214 tickers, aligned to SPY's trading days; long-run index history is Robert Shiller's monthly S&P 500 data (1871–2023). Valuation flags use a Yahoo fundamentals snapshot (ratios dated 2026-11-20/23) for ~114 stocks; missing = not in snapshot.

Key caveats the report must carry:
- Suite B (AI-infrastructure backtests 2016→today) and the satellite sleeve in Suite C use a universe picked in 2026 with hindsight (survivorship bias). Treat their returns as an upper bound, not an expectation.
- Monte Carlo/lognormal probabilities depend entirely on the assumed mean and volatility; 'measured' rows use each ETF's own history.
- Screen scores are relative (percentiles within each group) and price-based: high score = strong, orderly trend, not cheapness.
- Signals are mechanical rules, not forecasts.

## Theme baskets (equal-weight, as of 2026-11-25)

| Theme | Group | N | 1y | 3y CAGR | From 1y high | Vol 1y |
|---|---|---:|---:|---:|---:|---:|
| Memory | compute | 3 | 140.6% | 89.2% | -53.5% | 70% |
| Edge AI SoC | edge_emerging | 2 | 102.4% | 44.3% | -22.9% | 49% |
| AI cybersecurity | edge_emerging | 2 | 81.0% | 51.9% | -20.0% | 53% |
| Analog/edge | edge_emerging | 2 | 56.5% | 24.4% | -21.3% | 45% |
| Optical | compute | 5 | 41.7% | 82.9% | -62.0% | 90% |
| Networking | compute | 2 | 33.9% | 39.9% | -22.3% | 43% |
| Servers & racks | compute | 4 | 32.8% | 58.5% | -46.5% | 66% |
| Accelerators | compute | 2 | 31.5% | 52.3% | -36.4% | 55% |
| Semicap | compute | 4 | 30.2% | 33.0% | -51.3% | 61% |
| ALL AI compute, networking & data centers | compute | 50 | 30.0% | 69.4% | -45.9% | 56% |
| Power semis | edge_emerging | 5 | 28.8% | 9.1% | -61.6% | 71% |
| On-site power | power_grid | 3 | 23.6% | 70.2% | -46.0% | 56% |
| Edge AI IP | edge_emerging | 2 | 22.7% | 24.7% | -58.4% | 75% |
| ALL Edge AI & emerging themes | edge_emerging | 38 | 21.0% | 42.9% | -36.1% | 43% |
| Gas midstream | power_grid | 3 | 20.7% | 26.2% | -8.4% | 20% |
| Copper | power_grid | 2 | 19.7% | 21.2% | -37.1% | 51% |
| Custom silicon & networking | compute | 2 | 19.5% | 45.2% | -45.7% | 61% |
| Data-center REIT | compute | 2 | 19.3% | 10.6% | -13.6% | 27% |
| Advanced packaging | compute | 3 | 11.4% | 15.6% | -55.4% | 72% |
| Utilities | power_grid | 6 | 9.8% | 21.1% | -3.0% | 17% |
| Electrical equipment | power_grid | 3 | 4.8% | 19.8% | -28.3% | 36% |
| DC power & cooling | power_grid | 2 | 4.3% | 44.4% | -47.2% | 60% |
| Connectivity | compute | 2 | 3.3% | n/a | -59.9% | 96% |
| DC cooling | power_grid | 4 | 2.9% | 32.2% | -32.0% | 44% |
| Hyperscaler | compute | 4 | 2.3% | 21.7% | -14.4% | 26% |
| Gas turbines & grid | power_grid | 3 | 1.9% | 95.8% | -39.0% | 38% |
| DC construction | power_grid | 4 | 0.1% | 69.7% | -51.8% | 63% |
| Grid EPC | power_grid | 4 | -7.6% | 39.7% | -52.3% | 53% |
| ALL AI power, grid & cooling | power_grid | 57 | -7.9% | 47.8% | -36.2% | 35% |
| AI software | edge_emerging | 2 | -20.2% | 38.9% | -29.7% | 54% |
| Space | edge_emerging | 2 | -22.8% | 124.4% | -74.4% | 98% |
| Neocloud | compute | 2 | -23.0% | n/a | -66.5% | 105% |
| IPP power | power_grid | 3 | -27.2% | 57.7% | -30.7% | 51% |
| Miner-to-AI hosting | compute | 7 | -39.3% | 79.2% | -69.6% | 92% |
| Uranium | power_grid | 2 | -39.4% | 5.8% | -63.2% | 62% |
| Quantum | edge_emerging | 3 | -63.3% | 95.2% | -71.4% | 95% |
| SMR developer | power_grid | 3 | -77.2% | 55.2% | -81.0% | 89% |
| Storage | power_grid | 2 | -79.8% | -3.1% | -87.4% | 103% |

## Leverage illustration: Nasdaq-100 (QQQ) 1x vs simulated daily-reset 2x/3x since March 1999

| Leverage | CAGR | Max drawdown | 2000–02 drawdown | Multiple |
|---|---:|---:|---:|---:|
| 1x | 10.2% | -83.0% | -83.0% | 14.7x |
| 2x | 9.2% | -98.8% | -98.7% | 11.6x |
| 3x | 1.5% | -100.0% | -100.0% | 1.5x |

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
| Sector momentum rule (since 2000) | 9.1% | 14% | 26.8 | 0% | 0% | 0% | 0% | 2% | 10% | 29% |

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
| SPY | -8.0% | -6.9% | 5.9% | 8.3% | 31% | no |
| QQQ | -16.6% | -12.1% | 3.5% | 5.2% | 47% | no |
| SMH | -36.8% | -24.3% | 17.3% | 25.0% | 92% | no |
| VTI | -7.9% | -6.5% | 6.2% | 8.7% | 30% | no |
| EFA | -8.9% | -4.3% | 4.9% | 10.6% | 25% | no |
| GRID | -24.5% | -10.2% | -1.3% | 2.3% | 45% | no |
| XLU | -6.7% | 1.8% | 4.3% | 0.6% | 14% | no |
| XLE | -13.0% | -10.7% | 38.9% | 40.5% | 30% | yes |

VIX 28.3 on 2026-11-25 (1y median 17.1, 1y max 35.9).

Breadth (share of names above their 200-day average): AI power, grid & cooling 9%, AI compute, networking & data centers 2%, Edge AI & emerging themes 26%, Quality compounders 100%, US sector ETFs 67%, Thematic ETFs 9%

## Current rule-based signals

Trend filters (price above ~10-month average): SPY ❌, QQQ ❌, SMH ❌, VTI ❌, EFA ❌, GRID ❌

AI-infra momentum sleeve (top 10, inverse-vol, 15% cap):

| Ticker | Weight | Theme |
|---|---:|---|
| AEP | 15.0% | Utilities |
| AAPL | 15.0% | Edge AI devices |
| D | 15.0% | Utilities |
| MSFT | 14.0% | Hyperscaler |
| SYNA | 8.7% | Edge AI IoT |
| TXN | 7.4% | Analog/edge |
| PLTR | 7.2% | AI software |
| PANW | 6.2% | AI cybersecurity |
| CRWD | 6.0% | AI cybersecurity |
| NET | 5.5% | Edge cloud |

Cash in sleeve: 0.0%

Sector momentum (top 3): XLE, XLK, XLB

Dual momentum: EFA

## Screen — Core ETFs (top 12)

| # | Ticker | Score | Trend | 12m | Vol | MaxDD 1y | Valuation |
|---:|---|---:|---|---:|---:|---:|---|
| 1 | DGRO | 96.0 | strong uptrend | 19.0% | 11% | -6% |  |
| 2 | SCHD | 92.4 | strong uptrend | 35.5% | 12% | -7% |  |
| 3 | VIG | 82.4 | strong uptrend | 13.8% | 11% | -8% |  |
| 4 | RSP | 76.9 | strong uptrend | 17.5% | 13% | -8% |  |
| 5 | QUAL | 74.3 | uptrend (pullback) | 12.6% | 14% | -9% |  |
| 6 | AVUV | 70.0 | weakening | 22.8% | 15% | -11% |  |
| 7 | VOO | 66.4 | weakening | 8.4% | 15% | -11% |  |
| 8 | IVV | 65.0 | weakening | 8.4% | 15% | -11% |  |
| 9 | SPYM | 63.6 | weakening | 8.3% | 15% | -11% |  |
| 10 | SPY | 55.0 | weakening | 8.3% | 15% | -11% |  |
| 11 | VTI | 52.1 | weakening | 8.7% | 15% | -11% |  |
| 12 | VGT | 51.7 | weakening | 11.8% | 29% | -25% |  |

## Screen — US sector ETFs (top 12)

| # | Ticker | Score | Trend | 12m | Vol | MaxDD 1y | Valuation |
|---:|---|---:|---|---:|---:|---:|---|
| 1 | XLE | 77.8 | uptrend (pullback) | 40.5% | 23% | -15% |  |
| 2 | XLP | 72.2 | strong uptrend | 23.2% | 16% | -10% |  |
| 3 | XLV | 70.0 | strong uptrend | 20.3% | 17% | -10% |  |
| 4 | XLF | 63.9 | strong uptrend | 10.6% | 16% | -15% |  |
| 5 | XLB | 58.9 | recovering | 20.5% | 19% | -12% |  |
| 6 | XLK | 56.7 | weakening | 12.0% | 31% | -26% |  |
| 7 | XLI | 41.7 | downtrend | 9.9% | 19% | -16% |  |
| 8 | XLU | 36.1 | downtrend | 0.6% | 16% | -16% |  |
| 9 | XLY | 22.8 | recovering | 3.7% | 20% | -15% |  |

## Screen — Thematic ETFs (top 12)

| # | Ticker | Score | Trend | 12m | Vol | MaxDD 1y | Valuation |
|---:|---|---:|---|---:|---:|---:|---|
| 1 | CIBR | 88.0 | uptrend (pullback) | 31.6% | 32% | -20% |  |
| 2 | PAVE | 77.1 | downtrend | 10.3% | 23% | -18% |  |
| 3 | AIQ | 75.9 | weakening | 9.0% | 32% | -27% |  |
| 4 | ZAP | 74.4 | downtrend | 5.0% | 17% | -13% |  |
| 5 | QTUM | 73.4 | weakening | 12.0% | 37% | -34% |  |
| 6 | SMH | 72.8 | weakening | 25.0% | 47% | -40% |  |
| 7 | DTCR | 70.6 | downtrend | 13.7% | 27% | -31% |  |
| 8 | SOXX | 68.5 | weakening | 36.2% | 53% | -43% |  |
| 9 | VOLT | 68.4 | downtrend | 9.4% | 29% | -26% |  |
| 10 | GRID | 60.4 | downtrend | 2.3% | 27% | -27% |  |
| 11 | CHAT | 59.0 | downtrend | 8.9% | 46% | -42% |  |
| 12 | IGV | 56.0 | uptrend (pullback) | -7.0% | 33% | -32% |  |

## Screen — AI power, grid & cooling (top 12)

| # | Ticker | Score | Trend | 12m | Vol | MaxDD 1y | Valuation |
|---:|---|---:|---|---:|---:|---:|---|
| 1 | ET | 93.7 | weakening | 22.4% | 18% | -14% |  |
| 2 | KMI | 89.5 | weakening | 22.6% | 22% | -12% |  |
| 3 | WMB | 82.6 | downtrend | 15.2% | 27% | -18% |  |
| 4 | JCI | 81.4 | weakening | 20.6% | 34% | -18% |  |
| 5 | ETR | 79.8 | downtrend | 15.1% | 21% | -16% |  |
| 6 | 6501.T | 76.3 | weakening | 6.5% | 38% | -23% |  |
| 7 | AEP | 74.2 | recovering | 7.8% | 19% | -15% |  |
| 8 | SCCO | 72.7 | weakening | 17.5% | 54% | -38% |  |
| 9 | ABBNY | 72.5 | downtrend | 16.4% | 35% | -30% |  |
| 10 | SO | 71.2 | recovering | 10.1% | 18% | -16% |  |
| 11 | WCC | 71.1 | weakening | 15.6% | 49% | -27% |  |
| 12 | PWR | 70.9 | downtrend | 27.8% | 51% | -35% |  |

## Screen — AI compute, networking & data centers (top 12)

| # | Ticker | Score | Trend | 12m | Vol | MaxDD 1y | Valuation |
|---:|---|---:|---|---:|---:|---:|---|
| 1 | HPE | 84.7 | weakening | 97.0% | 66% | -45% |  |
| 2 | DELL | 81.5 | weakening | 136.0% | 85% | -53% | reasonable |
| 3 | MU | 80.8 | weakening | 168.8% | 87% | -51% | peak-cycle risk (low P/E on boom earnings) |
| 4 | AMD | 78.8 | weakening | 88.8% | 75% | -38% | reasonable |
| 5 | ANET | 78.4 | weakening | 34.2% | 59% | -27% |  |
| 6 | TSM | 74.1 | weakening | 21.5% | 46% | -34% |  |
| 7 | CSCO | 73.2 | weakening | 25.8% | 38% | -30% |  |
| 8 | EQIX | 72.5 | downtrend | 31.2% | 27% | -14% |  |
| 9 | ASML | 71.0 | weakening | 32.7% | 50% | -36% |  |
| 10 | STX | 68.4 | downtrend | 87.5% | 79% | -58% |  |
| 11 | 005930.KS | 65.6 | downtrend | 81.0% | 79% | -52% | peak-cycle risk (low P/E on boom earnings) |
| 12 | MSFT | 65.3 | uptrend (pullback) | 4.2% | 34% | -28% |  |

## Screen — Edge AI & emerging themes (top 12)

| # | Ticker | Score | Trend | 12m | Vol | MaxDD 1y | Valuation |
|---:|---|---:|---|---:|---:|---:|---|
| 1 | PANW | 93.4 | uptrend (pullback) | 93.7% | 52% | -29% | stretched |
| 2 | CRWD | 87.4 | uptrend (pullback) | 65.2% | 59% | -33% | speculative (unprofitable) |
| 3 | TXN | 85.3 | uptrend (pullback) | 71.2% | 48% | -23% | reasonable |
| 4 | AAPL | 85.1 | strong uptrend | 29.3% | 25% | -14% | premium |
| 5 | ADI | 82.4 | weakening | 40.9% | 45% | -30% | reasonable |
| 6 | 2454.TW | 82.2 | uptrend (pullback) | 215.4% | 69% | -37% | reasonable |
| 7 | NET | 73.3 | uptrend (pullback) | 46.0% | 68% | -32% | speculative (unprofitable) |
| 8 | SYNA | 68.5 | strong uptrend | 78.0% | 59% | -40% | speculative (unprofitable) |
| 9 | PLTR | 65.0 | uptrend (pullback) | 0.8% | 61% | -45% | stretched |
| 10 | ROK | 63.9 | downtrend | 1.5% | 35% | -26% | reasonable |
| 11 | NXPI | 63.4 | downtrend | 29.1% | 51% | -34% | reasonable |
| 12 | STM | 62.1 | downtrend | 81.6% | 64% | -51% | reasonable |

## Screen — Quality compounders (top 12)

| # | Ticker | Score | Trend | 12m | Vol | MaxDD 1y | Valuation |
|---:|---|---:|---|---:|---:|---:|---|
| 1 | V | 85.0 | strong uptrend | 29.9% | 23% | -17% |  |
| 2 | COST | 69.3 | strong uptrend | 26.8% | 20% | -18% |  |
| 3 | LLY | 66.4 | strong uptrend | 30.9% | 35% | -23% |  |
| 4 | MA | 65.0 | strong uptrend | 23.5% | 24% | -18% |  |
| 5 | BRK-B | 61.4 | strong uptrend | 14.1% | 15% | -9% |  |
| 6 | MCO | 28.6 | uptrend (pullback) | 2.4% | 29% | -24% |  |
| 7 | SPGI | 24.3 | uptrend (pullback) | 0.4% | 31% | -28% |  |

## Backtests

### Long-history strategies (2000 → today)

_Universes chosen without hindsight (broad index / sector ETFs). Includes the 2000-02 and 2008 bear markets._

| Strategy | CAGR | Vol | Sharpe | Max DD | Multiple |
|---|---:|---:|---:|---:|---:|
| S&P 500 buy & hold (SPY) | 8.2% | 19% | 0.41 | -55% | 8.2x |
| Nasdaq-100 buy & hold (QQQ) | 8.3% | 27% | 0.36 | -83% | 8.4x |
| SPY with 10-month trend filter | 8.8% | 12% | 0.60 | -25% | 9.5x |
| Sector momentum: top 3 of 9 SPDR sectors | 9.1% | 17% | 0.49 | -36% | 10.3x |
| 60% SPY + 40% QQQ with trend filter | 9.1% | 17% | 0.49 | -44% | 10.3x |
| Dual momentum (SPY/EFA/IEF) | 9.1% | 16% | 0.52 | -34% | 7.5x |

### AI-infrastructure strategies (2016 → today)

_WARNING: the AI universe was picked in 2026 with hindsight (survivorship bias). These returns overstate what was knowable in real time._

| Strategy | CAGR | Vol | Sharpe | Max DD | Multiple |
|---|---:|---:|---:|---:|---:|
| S&P 500 (SPY) | 14.7% | 18% | 0.74 | -34% | 4.4x |
| Nasdaq-100 (QQQ) | 19.0% | 22% | 0.79 | -35% | 6.6x |
| Semiconductors (SMH) | 31.0% | 34% | 0.91 | -45% | 18.7x |
| AI-infra universe, equal weight | 33.4% | 29% | 1.07 | -42% | 22.5x |
| AI-infra momentum top 10 + trend filter | 39.1% | 36% | 1.04 | -51% | 35.5x |
| Core-satellite: 70% VTI + 30% AI momentum | 22.3% | 21% | 0.95 | -35% | 8.9x |

### Model portfolios (2012 → today, ETF proxies)

_Backtests use long-history proxies (QQQ for QQQM, EFA for VXUS). Satellite sleeve is the AI momentum rule and inherits Suite B's hindsight bias._

| Strategy | CAGR | Vol | Sharpe | Max DD | Multiple |
|---|---:|---:|---:|---:|---:|
| Steady compounder | 12.6% | 16% | 0.73 | -32% | 5.8x |
| Growth tilt | 18.4% | 19% | 0.89 | -33% | 12.2x |
| Aggressive AI-infra | 22.6% | 22% | 0.97 | -33% | 20.6x |
| S&P 500 (SPY) | 14.1% | 17% | 0.78 | -34% | 7.0x |

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
