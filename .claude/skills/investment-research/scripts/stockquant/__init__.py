"""stockquant: a small, transparent quant toolkit for long-term investors.

Modules
-------
data        price download + cache (Yahoo chart API, yfinance fallback)
universe    curated universes (core ETFs, AI power/grid, compute, edge AI ...)
metrics     CAGR, volatility, Sharpe/Sortino, drawdowns, capture ratios
signals     momentum/trend/volatility features and a composite screen score
backtest    monthly-rebalanced, no-look-ahead backtester (+ leveraged ETF sim)
strategies  momentum top-N, trend filter, dual momentum, inverse-vol, blends
portfolio   risk parity, inverse-vol, volatility targeting, share allocation
goal        50x math, Monte Carlo with contributions, Kelly sizing
report      runs everything and writes output/results.json + markdown
"""

__version__ = "0.1.0"
