# Evidence on 50x Long-Term Goals in Public Equities, and the Risks of Thematic / Infrastructure-Boom Investing

*Compiled 2026-11-25. **Labels:** [PR] = peer-reviewed journal; [WP] = working paper (not peer-reviewed); [IND] = industry/practitioner research; [MEDIA] = news report; [OPINION] = commentary or forecast; [OWN CALC] = my computation from a cited dataset; [EXTRACT] = figure taken from a search-engine extract of the cited page, which could not be opened in full; [NOT RE-VERIFIED] = canonical citation from reference knowledge, link not opened this session.*

*Research limits: in this session WebFetch was blocked for jpmorgan.com, morningstar.com and brookings.edu, and downloads were blocked for Damodaran's NYU site and Shiller's Yale page. The shared web-search budget also ran out before the sections on strategies, 1920s utilities and some ETFs were finished. Index math and the strategy backtests were therefore computed directly from Robert Shiller's monthly S&P Composite data, through the public datahub GitHub mirror. That data has dividends and CPI through **June 2023**. It uses monthly-average prices, which smooth intramonth peaks and troughs.*

---

## 1. Base rates of extreme winners: how often do individual stocks become 10x / 50x / 100x, and who creates the wealth?

### Takeaway
Long-run stock returns are very positively skewed. About 55–57% of individual stocks fail to beat one-month T-bills over their listed lives, and ~52% of US stocks lost money outright from 1926 to 2023. Essentially all net stock-market wealth creation comes from the top ~2.4% (global, 1990–2020) to ~4% (US, 1926–2016) of firms. 100-baggers exist: ~365 per ~40–50-year span in two book-length studies. But they took ~26 years on average, and the 17 greatest long-lived US compounders averaged only ~13.5%/yr. So a 50x from stock picking is a right-tail outcome, not a base case.

### Cited Findings
**Bessembinder: US and global evidence**
- [PR] Bessembinder (2018), "Do stocks outperform Treasury bills?", *Journal of Financial Economics* 129(3): 440–457 (DOI 10.1016/j.jfineco.2018.06.004). A majority of CRSP common stocks since 1926 have lifetime buy-and-hold returns below one-month T-bills. The best-performing 4% of listed companies explain the net gain of the entire US stock market since 1926, while the other stocks collectively matched T-bills. — [EconPapers abstract](https://econpapers.repec.org/RePEc:eee:jfinec:v:129:y:2018:i:3:p:440-457); [ASU W. P. Carey faculty research page](https://wpcarey.asu.edu/department-finance/faculty-research/do-stocks-outperform-treasury-bills)
- Bessembinder, interviewed: only about 43% of stocks, "roughly three out of seven", beat Treasury bills. That means about four of seven underperformed. — [Morningstar, "Hendrik Bessembinder: Do Stocks Outperform Treasury Bills?"](https://www.morningstar.com/personal-finance/hendrik-bessembinder-do-stocks-outperform-treasury-bills)
- ASU summary of the 2018 paper: all of the ~$35 trillion of wealth created above T-bill returns from 1926 to 2016 is attributable to 1,092 companies, 4.3% of nearly 26,000 stocks. — [ASU News, 2018-12-12](https://news.wpcarey.asu.edu/20181212-research-shows-most-stocks-haven%E2%80%99t-outperformed-treasury-bills)
- [PR, practitioner journal] Bessembinder, Chen, Choi & Wei (2023), "Long-Term Shareholder Returns: Evidence from 64,000 Global Stocks", *Financial Analysts Journal* 79(3): 33–63. The sample is more than 64,000 common stocks from January 1990 to December 2020.
  - 55.2% of US stocks and 57.4% of non-US stocks underperform one-month US T-bills in compound return over the full sample.
  - The top-performing **2.4%** of firms account for all **US$75.7 trillion** of net global wealth creation.
  - Outside the US, **1.41%** of firms account for the US$30.7 trillion of net wealth creation.
  - The ASU page gives the sample period as 1991–2020, while the journal abstract says January 1990. Prefer the abstract.
  - Sources: [CFA Institute Research & Policy Center](https://rpc.cfainstitute.org/research/financial-analysts-journal/2023/long-term-shareholder-returns-evidence-from-64000-global-stocks); [IDEAS/RePEc](https://ideas.repec.org/a/taf/ufajxx/v79y2023i3p33-63.html)
- [WP] Bessembinder (2024), "Which U.S. Stocks Generated the Highest Long-Term Returns?", SSRN 4897069. The sample is 29,078 CRSP common stocks from December 1925 to December 2023.
  - **51.6% had negative cumulative returns**.
  - **17 stocks** had cumulative returns above 5,000,000%, i.e. more than $50,000 per $1 invested. Altria led at about 265 million percent.
  - Those top 17 averaged only **~13.47%/yr**. The paper credits long holding periods, not extreme annual returns.
  - The highest annualized compound return for any stock with at least 20 years of data was **Nvidia at 33.38%**. Emerson Electric compounded at 13.57% for 79 years.
  - Sources: [SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4897069); figures via [Edward Conard summary](https://www.edwardconard.com/macro-roundup/hendrik-bessembinder-finds-that-from-1925-to-2023-51-6-of-equities-had-a-negative-return-however-17-stocks-had-cumulative-returns-greater-than-50000-per-dollar-invested-led-by-altria-group-with-a/?view=detail) and [A Wealth of Common Sense, July 2024](https://awealthofcommonsense.com/2024/07/the-biggest-winners-in-the-stock-market/) [EXTRACT]
- [WP, secondary] A 2026 Bessembinder working paper, "One Hundred Years in the U.S. Stock Markets", reportedly extends the sample to 1926–2025 with 29,754 stocks. A summary page gives Altria's top annualized return as 16.53%. Figures differ by sample period, so check which period a number refers to. — [summary page](https://cgodlewski.github.io/100-US-stock-markets/) [EXTRACT]

**J.P. Morgan concentrated-stock studies**
- [IND] J.P. Morgan Private Bank / Michael Cembalest, "The Agony & the Ecstasy: The risks and rewards of a concentrated stock position". Editions: Sept 2014, a 2021 "v2.0", and an Oct 2, 2024 update on catastrophic declines.
  - More than **40%** of all companies ever in the Russell 3000 since 1980 suffered a "catastrophic stock price loss", defined as a ≥70% decline from peak that is not recovered.
  - In the 2014 edition, the median stock underperformed the Russell 3000 by **54%** over its lifetime, about **two-thirds** of stocks had negative lifetime excess returns versus the index, and **40%** had negative absolute returns.
  - A concentrated single-stock position underperformed a diversified Russell 3000 position about two-thirds of the time.
  - One secondary source says ~10% of stocks met the "megawinner" definition.
  - Sources: [J.P. Morgan 2021 PDF](https://privatebank.jpmorgan.com/content/dam/jpm-pb-aem/global/en/documents/eotm/agony-ecstasy-2021.pdf); [2014 edition PDF](https://www.chase.com/content/dam/privatebanking/en/mobile/documents/eotm/eotm_2014_09_02_agonyescstasy.pdf); [Irish Times coverage](https://www.irishtimes.com/business/personal-finance/extreme-winners-take-it-all-while-40-of-stocks-suffer-catastrophic-declines-1.1970035); [The Irrelevant Investor, 2021-03-23](https://theirrelevantinvestor.com/2021/03/23/the-agony-the-ecstasy/); [J.P. Morgan Oct 2024 update page](https://privatebank.jpmorgan.com/nam/en/insights/latest-and-featured/eotm/the-agony-the-ecstasy1) [EXTRACT]

**100-bagger and multibagger studies**
- [Book; secondary summaries] Thomas Phelps, *100 to 1 in the Stock Market* (1972), listed **365** investments that rose at least 100x between 1932 and 1971. — [Stablebread, "What 1,275 Multibagger Stocks Had in Common"](https://stablebread.com/multibagger-stock-studies/)
- [Book; secondary summaries] Christopher Mayer, *100 Baggers* (2015), repeated the study with 1962–2014 data and dividends reinvested.
  - He found **365** stocks that returned at least 100x.
  - The average time to 100x was **~26 years**, about 19%/yr. Only **20 of 365** did it in under 10 years.
  - The median 100-bagger started with ~$170M of annual sales and ~$500M of market value.
  - Sources: [Stablebread](https://stablebread.com/multibagger-stock-studies/); [The Pender Pulse](https://thependerpulse.substack.com/p/the-hunt-for-100-baggers); [The Investor's Podcast interview with Mayer](https://www.theinvestorspodcast.com/millennial-investing/finding-100-bagger-stocks/)
- [WP, not peer-reviewed] Anna Yartseva (2025), "The Alchemy of Multibagger Stocks: An empirical investigation of factors that drive outperformance in the stock market", CAFÉ Working Paper No. 33, Birmingham City University. The sample is **464** stocks listed on major US exchanges that rose at least **10x during 2009–2024**.
  - Size, value and profitability (Fama-French factors) remain significant predictors.
  - Free-cash-flow-to-price was reported as the most important driver. Earnings growth was *not* a significant predictor.
  - Multibaggers loaded *negatively* on 3- and 6-month momentum, and stocks near their 12-month highs tended to underperform. Secondary summaries disagree on 1-month momentum.
  - Winners came from many industries; technology was important but did not dominate.
  - Sources: [BCU open-access PDF](https://www.open-access.bcu.ac.uk/16180/1/The%20Alchemy%20of%20Multibagger%20Stocks%20-%20Anna%20Yartseva%20-%20CAFE%20Working%20Paper%2033%20%282025%29.pdf); [IDEAS](https://ideas.repec.org/p/akf/cafewp/33.html); [Quantseeker](https://www.quantseeker.com/p/how-multibaggers-really-happen); [Stockopedia](https://www.stockopedia.com/content/multibaggers-what-a-new-us-study-confirms-about-our-uk-findings-1036614) [EXTRACT; details mostly from secondary write-ups]

**Mauboussin / Counterpoint Global base-rate work**
- [IND] Mauboussin & Callahan (Counterpoint Global, Morgan Stanley IM), "Total Shareholder Return: Linking the Drivers of Total Returns to Fundamentals".
  - S&P 500 total shareholder return (TSR) for 2012–2021 was 16.6%/yr. 44% of it came from EPS growth and 42% from multiple expansion.
  - The present value of growth opportunities (PVGO) correlated only −0.26 with subsequent 10-year TSR.
  - The lowest-PVGO quartile averaged 11.6% annualized 10-year returns.
  - Sources: [Morgan Stanley PDF](https://www.morganstanley.com/im/publication/insights/articles/article_totalshareholderreturns.pdf); [Edward Conard summary](https://www.edwardconard.com/macro-roundup/between-2012-21-the-total-shareholder-return-for-the-sp-500-was-16-6-with-44-of-the-return-driven-by-earnings-per-share-growth-and-multiple-expansion-contributing-42-mjmauboussin/?view=detail) [EXTRACT]
- [IND] Mauboussin & Callahan, *The Base Rate Book* (Credit Suisse, Sept 2016), is the main repository of base rates for sales growth and TSR distributions. The specific 10-year TSR probabilities could not be extracted. — [PDF copy](https://sorfis.com/wp-content/uploads/2021/09/The-Base-Rate-Book-Integrating-the-Past-to-Better-Anticipate-the-Future-September-2016.pdf)
- [IND] Counterpoint Global, "Drawdowns and Recoveries": Nvidia fell ~90% in 2002 and took **4.1 years** (Oct 2002 to Nov 2006) after its bottom to regain the prior peak. — [Morgan Stanley PDF](https://www.morganstanley.com/im/publication/insights/articles/article_drawdownsandrecoveries_ltr.pdf) [EXTRACT]

### Inferences
- **Rough frequency.** Mayer's 365 100-baggers over 1962–2014, against the ~26,000 stocks Bessembinder counts in CRSP over 1926–2016, puts 100-baggers on the order of **1–2% of all listed names** over a ~50-year span. This is my rough estimate; the denominators and periods differ.
- **10-baggers over 15 years.** If the 2009 US-listed universe was roughly 4,000–5,000 common stocks, Yartseva's 464 implies roughly a ~10% 15-year 10-bagger rate. The denominator is not given in the sources I could access.
- **CAGRs implied by the cited winners [OWN CALC]:**
  - 100x in 26 years = **19.4%/yr**. At that pace, 50x takes **22.1 years**.
  - The top-17 average of 13.47%/yr compounds to **44.3x in 30 years** and needs **31.0 years** for 50x. Emerson's 13.57%/yr needs **30.7 years**.
  - Only a Nvidia-class outlier (33.38%/yr) reaches 50x in about **13.6 years**.
  - So a single-stock 50x over ~30 years requires picking, and *holding*, something comparable to the top 17 of 29,078 US stocks in a century.
- **What predicted the winners.** In Yartseva's working paper, multibaggers looked like cheap, cash-generative, smaller companies, often *out* of favor (negative short-term momentum). They did not look like consensus hot-theme stocks. This conflicts with the "buy the hottest theme" approach.
- **Skewness.** A concentrated portfolio has a *lower median* outcome than the index even when its *expected* value is similar.

### Gaps
- I found no source giving denominator-based frequencies of 10x / 50x / 100x outcomes over fixed 10-, 20- and 30-year windows. No 50x-specific frequency study was found.
- The tables in Mauboussin's *Base Rate Book* (10-year TSR distribution) could not be read.
- The exact median lifetime return in Bessembinder (2018) was not verified.
- The 2024 J.P. Morgan update figures could not be retrieved because jpmorgan.com was blocked.
- Yartseva's statistics come from secondary summaries; the PDF was not opened.

---

## 2. Index math: S&P 500 long-run CAGR, rolling 20/30/40-year multiples, and years to 50x

### Takeaway
The S&P 500 total return compounded at about **10.2% nominal / 7.0% real** from Jan 1926 to Jun 2023. At that rate, **50x nominal is roughly a 40-year index outcome**: the median 40-year multiple was 46x across all windows since 1871 and 65x for windows starting from 1926. But **50x real has required 50+ years**. Since 1926, no 20-year window reached 50x, only ~1% of 30-year windows did (nominal), and no 40-year window did in real terms.

### Cited Findings
*All rows are [OWN CALC] on [Shiller monthly S&P Composite data, datahub mirror](https://raw.githubusercontent.com/datasets/s-and-p-500/main/data/data.csv) (original: [Shiller data page](http://www.econ.yale.edu/~shiller/data.htm)). Total return is computed as monthly (Pₜ₊₁ + Dₜ/12)/Pₜ, real values are deflated by CPI, and dividends/CPI end in June 2023.*

**Long-run CAGRs (to June 2023)**

| Start | Years | Nominal TR multiple | Nominal CAGR | Real TR multiple | Real CAGR |
|---|---|---|---|---|---|
| Jan 1871 | 152.4 | 634,681x | 9.16% | 25,919x | 6.90% |
| Jan 1926 | 97.4 | 12,286x | **10.15%** | 721x | **6.99%** |
| Jan 1928 | 95.4 | 8,037x | 9.88% | 456x | 6.63% |
| Mar 1957 (S&P 500 launch) | 66.2 | 661x | **10.30%** | 60x | **6.38%** |
| Jan 1980 | 43.4 | 116x | 11.58% | 30x | 8.12% |
| Jan 2000 | 23.4 | 5x | 6.82% | 2.6x | 4.16% |

- Cross-check: a secondary summary of Bessembinder (2024) cites ~**10.3%/yr** for the S&P 500 from 1926 to 2023. The small difference reflects Shiller's monthly averaging and index construction. — [A Wealth of Common Sense](https://awealthofcommonsense.com/2024/07/the-biggest-winners-in-the-stock-market/)

**Rolling-window total-return multiples (all monthly start points, 1871 to Jun 2023)**

| Horizon | Nominal: worst / median / best (start date) | Share ≥10x | Share ≥50x | Real: worst / median / best | Real share ≥50x |
|---|---|---|---|---|---|
| 10y | 0.67x (Aug 1929) / 2.3x / 6.8x (Jun 1949) | 0% | 0% | 0.54x (Mar 1999, −5.9%/yr) / 2.0x / 6.2x | 0% |
| 20y | 1.50x (Sep 1929) / 4.7x / **27.1x (Apr 1980, 17.9%/yr)** | 20.4% | **0%** | 0.96x (Jun 1901) / 3.7x / 12.8x | 0% |
| 30y | 2.92x (Jun 1902) / 16.9x / **55.1x (Jul 1970, 14.3%/yr)** | 69.0% | **0.6%** | 1.75x / 7.0x / 23.8x (Jun 1932) | 0% |
| 40y | 6.77x (Jun 1892) / **45.8x** / 141x (Jun 1932) | 97.3% | **44.3%** | 3.50x / 12.1x / 50.0x (Aug 1921, single best case) | ~0% |
| 50y | 10.8x (Jun 1882) / 98.4x / 623x (Jun 1949) | 100% | 71.5% | 8.1x (Sep 1929) / 21.2x / 89.6x (Jun 1949) | **10.2%** |

**Same statistics, starts from Jan 1926 onward only**
- **20y:** 930 windows. Nominal worst 1.50x (Sep 1929), median **8.0x** (11.0%/yr), best 27.1x. **0%** reached 50x. Real median 3.8x.
- **30y:** 810 windows. Nominal worst 9.1x (Sep 1929, 7.6%/yr), median **21.4x** (10.75%/yr), best 55.1x (Jul 1970). **1.1%** reached 50x nominal. Real median 8.0x, best 23.8x, 0% reached 50x.
- **40y:** 690 windows, with starts running only through mid-1983. Nominal worst 20.6x (Sep 1929, 7.85%/yr), median **65.1x** (11.0%/yr), best 141x (Jun 1932). **71.9%** reached 50x nominal. Real median 13.4x, best 46.0x, **0%** reached 50x real.

**Years needed to reach a multiple at a given CAGR [OWN CALC: ln(M)/ln(1+r)]**

| CAGR | 10x | **50x** | 100x |
|---|---|---|---|
| 5% | 47.2y | 80.2y | 94.4y |
| 7% (≈ index real) | 34.0y | **57.8y** | 68.1y |
| 10% (≈ index nominal) | 24.2y | **41.0y** | 48.3y |
| 12% | 20.3y | 34.5y | 40.6y |
| 15% | 16.5y | **28.0y** | 33.0y |
| 20% | 12.6y | **21.5y** | 25.3y |
| 25% | 10.3y | 17.5y | 20.6y |
| 30% | 8.8y | **14.9y** | 17.6y |
| 40% | 6.8y | 11.6y | 13.7y |

- **CAGR required for 50x [OWN CALC]:**

  | Horizon | Required CAGR |
  |---|---|
  | 10 years | 47.9% |
  | 15 years | 29.8% |
  | 20 years | **21.6%** |
  | 25 years | 16.9% |
  | 30 years | **13.9%** |
  | 40 years | **10.3%** |
  | 50 years | 8.1% |

- **Index drawdowns and recovery times [OWN CALC, monthly-average data, which understates daily extremes]:**
  - 1929–32: **−81.7%** nominal (Sep 1929 to Jun 1932). The nominal total return did not recover until **Dec 1944 (15.2 years)**. Real: −76.7%, recovered Nov 1936 thanks to deflation.
  - 1973–74: −39.2% nominal, but **−50.1% real**. The real recovery took until **Jan 1985 (12 years)**.
  - 2000–2009: the real total return fell **−51.8%** from Aug 2000 to Mar 2009 and recovered only in **May 2013 (12.8 years)**. The worst 10-year real window started Mar 1999, at **−5.9%/yr**.

### Inferences
- **Nominal versus real matters enormously.** 50x nominal in ~40 years has been near the historical *median* for a US index investor who stayed fully invested and reinvested dividends. It held in ~44% of all 40-year windows since 1871 and ~72% of those since 1926. 50x real needs ~58 years at 7%. Only 10% of 50-year windows achieved it.
- **50x in 20 years needs 21.6%/yr.** That exceeds the *best* 20-year index window ever (17.9%/yr from 1980). It cannot come from broad beta alone; it requires concentration, leverage and/or luck.
- **Starting point matters.** The best windows started near valuation troughs (1932, 1949, 1980). The worst started at peaks (1929, 1999). This bears on starting a 50x plan in late 2026 during an AI-led correction from record highs (see section 5). I did not compute current valuation measures.
- **Small effective sample.** Rolling windows overlap heavily. Since 1926 there are only ~2.4 non-overlapping 40-year periods, so these "frequencies" have very wide uncertainty.
- **US survivorship.** US results are among the best of any national market (survivorship at the country level). I could not retrieve non-US base rates.

### Gaps
- Damodaran's annual S&P 500 return file (NYU) could not be downloaded for a cross-check.
- The data mirror lacks dividends and CPI after June 2023, so 2023–2026 returns are excluded. It also has no T-bill series.
- Dimson–Marsh–Staunton global long-run figures were not retrieved.

---

## 3. Volatility drag, concentration, Kelly sizing, and the drawdowns of eventual mega-winners

### Takeaway
Compounding punishes volatility: the geometric return is roughly the arithmetic return minus σ²/2. A single stock with a high *expected* return and high volatility therefore usually has a low, even negative, *median* outcome, while its mean is driven by rare outliers. That is the mechanism behind Bessembinder's skewness result. Every famous mega-winner suffered at least one **65–95% drawdown**. Holding one required surviving falls that permanently destroyed >40% of similar-looking companies.

### Cited Findings
**Skewness and concentration**
- [PR] Bessembinder (2018) attributes "most stocks underperform T-bills" to **positive skewness** in long-horizon returns, which compounding amplifies. He argues this helps explain why poorly diversified, active strategies usually underperform. This is my paraphrase of the abstract. — [EconPapers](https://econpapers.repec.org/RePEc:eee:jfinec:v:129:y:2018:i:3:p:440-457); [ASU](https://wpcarey.asu.edu/department-finance/faculty-research/do-stocks-outperform-treasury-bills)
- [IND] More than 40% of Russell 3000 stocks since 1980 had unrecovered ≥70% losses, and two-thirds lagged the index (see section 1). — [J.P. Morgan "Agony & Ecstasy" 2021](https://privatebank.jpmorgan.com/content/dam/jpm-pb-aem/global/en/documents/eotm/agony-ecstasy-2021.pdf)

**Drawdowns of eventual mega-winners**
- **Amazon:** ~**−94%** (Dec 1999 to Sep 2001, weekly data), with a low of about $5.97 in Q3 2001. It regained its 1999 high around Oct 2009, nearly 10 years later; sources differ slightly on that date. — [Complete Trader's Edge](https://completetradersedge.com/amazon-history-dot-com-crash-drawdown-aws-moat/); [Fact of the Day](https://www.factoftheday1.com/p/april-12-amazon-and-the-dot-com-bubble); [InvestWealth](https://www.investwealth.com/markets/amazon) [secondary]
- **Nvidia** (total-return data):

  | Peak | Trough | Drawdown |
  |---|---|---|
  | Jan 3, 2002 | Oct 9, 2002 | **−89.7%** |
  | Oct 17, 2007 | Nov 20, 2008 | **−85.1%** |
  | Nov 29, 2021 | Oct 14, 2022 | **−66.3%** |

  - In 2018, one article describes a 50%+ drawdown; the calendar-year 2018 return was −30.8%.
  - Counterpoint: 4.1 years to regain the 2002 peak after the bottom.
  - As of 2026-11-10, Nvidia was ~30% below its high.
  - Sources: [totalrealreturns.com](https://totalrealreturns.com/n/NVDA,AAPL,MSFT,GOOGL,AMZN,NFLX,META,TSLA); [Counterpoint "Drawdowns and Recoveries"](https://www.morganstanley.com/im/publication/insights/articles/article_drawdownsandrecoveries_ltr.pdf); [Motley Fool, 2026-11-10](https://www.fool.com/investing/2026/11/10/nvidia-is-down-30-from-its-high-history-says-this/) [EXTRACT]
- **Apple:** −81.8% (Mar 22, 2000 to Apr 17, 2003). **Microsoft:** −69.4% total return (Dec 27, 1999 to Mar 9, 2009), so it was still below its 1999 high a decade later. **Netflix:** −76.0% (Nov 17, 2021 to May 11, 2022). — [totalrealreturns.com](https://totalrealreturns.com/n/NVDA,AAPL,MSFT,GOOGL,AMZN,NFLX,META,TSLA) [EXTRACT]
- **Cisco:** after losing ~90% in the bust, it first closed above its split-adjusted record of $80.06 (Mar 27, 2000) on **Dec 10, 2025**, at $80.25. That is more than **25 years** to break even in price terms. — [CNBC, 2025-12-10](https://www.cnbc.com/2025/12/10/ciscos-stock-closes-at-record-for-first-time-since-dot-com-peak-2000.html); [Bloomberg, 2025-12-10](https://www.bloomberg.com/news/articles/2025-12-10/cisco-shares-finally-top-dot-com-record-after-more-than-25-years)

**Volatility drag: lognormal illustration** [OWN CALC; assumed parameters, not a forecast]. *μ is the arithmetic expected return; σ is log-volatility.*

| μ | σ | Horizon | Median growth/yr | Mean multiple | **Median multiple** | P(≥50x) | P(loss) |
|---|---|---|---|---|---|---|---|
| 10% | 17% (index-like) | 30y | 8.4% | 17.4x | 11.3x | 5.5% | 0.5% |
| 15% | 30% (large-cap stock) | 30y | 9.9% | 66.2x | 17.2x | 25.8% | 4.2% |
| 15% | **45%** (typical single growth stock) | 30y | 3.9% | 66.2x | **3.2x** | 13.2% | **32.0%** |
| 15% | 60% (speculative) | 30y | −3.9% | 66.2x | 0.3x | 6.0% | 64.3% |
| 20% | 60% | 20y | 0.2% | 38.3x | 1.0x | 7.5% | 49.3% |

- Real single stocks also carry delisting and bankruptcy jumps. Their left tail is therefore fatter than the lognormal model above.

**Kelly sizing** [OWN CALC using standard continuous-time results; references Kelly (1956), *Bell System Technical Journal* 35(4), and Thorp's work on the Kelly criterion, NOT RE-VERIFIED]
- Full-Kelly fraction = (μ − r)/σ².
  - Index-like asset (excess return 6%, σ 18%): **1.85x** capital (leveraged).
  - Single stock (excess return 8%, σ 50%): **0.32x** capital at full Kelly, **0.16x** at half Kelly.
- Betting a fraction c of Kelly earns c(2 − c) of the maximum excess growth. Half Kelly therefore keeps **75% of the growth with 50% of the volatility**.
- The probability of *ever* falling to a fraction x of starting wealth is x^(2/c − 1):
  - Full Kelly: **50%** chance of being halved at some point, and 20% chance of losing 80%.
  - Half Kelly: **12.5%** chance of being halved, and 0.8% chance of losing 80%.
  - Quarter Kelly: 0.8% chance of being halved.

### Inferences
- **Holding through is the hard part.** A 50x single-stock outcome almost always passes through at least one 50–90% drawdown: Amazon −94%, Nvidia −90% / −85% / −66%, Apple −82%, Microsoft −69% with a decade under water. Whoever *sizes* such a position must be able to survive the drawdown financially and psychologically.
- **A drawdown is not a buy signal.** The same drawdown pattern describes the >40% of stocks that never recovered (J.P. Morgan). Survivorship bias makes "hold through −90%" look easier in hindsight than it was.
- **The median argument for diversification.** With realistic single-stock volatility (40–60%), the *median* 30-year outcome is roughly 0.3x to 3x even when the *mean* is 66x. Diversifying across many such bets, or sizing each at ≤ half Kelly, is what turns favorable expected values into a decent median.
- **Kelly parameters are optimistic.** The inputs above assume known parameters. In practice μ is highly uncertain and usually overestimated, which argues for quarter to half Kelly at most. Even with an optimistic 8% edge, that means single positions of roughly **≤8–16%** of capital.

### Gaps
- The 2011 Netflix drawdown and Microsoft's exact recovery date to its 1999 high (believed to be ~2016) were not verified.
- No cross-sectional study of drawdown base rates among *eventual* winners was retrieved; Counterpoint's "Drawdowns and Recoveries" summary statistics were not extracted.
- The Kelly references were not re-opened this session.

---

## 4. Thematic investing evidence: specialized/thematic ETFs and hot-theme funds after peaks

### Takeaway
Thematic and specialized funds tend to launch when a theme's stocks are most overvalued and most talked about, and then underperform. Peer-reviewed evidence (Ben-David et al., RFS 2023) and Morningstar's survivorship data agree: fewer than **1 in 10** thematic funds survived *and* beat global equities over 15 years, and ~60% closed. The flagship hot-theme fund of the 2020–21 cycle (ARKK) lost ~77–81% from peak and was still ~56–58% below it in 2026.

### Cited Findings
- [PR] Ben-David, Franzoni, Kim & Moussawi (2023), "Competition for Attention in the ETF Space", *Review of Financial Studies* 36(3): 987–1042 (originally NBER WP 28369, Jan 2021).
  - Specialized ETFs track niche, attention-grabbing themes and charge high fees.
  - Providers cater to investors' extrapolative beliefs.
  - The poor post-launch performance is driven by the **overvaluation of the underlying stocks at launch**.
  - Sources: [EconPapers (RFS)](https://econpapers.repec.org/RePEc:oup:rfinst:v:36:y:2023:i:3:p:987-1042.); [NBER WP PDF](https://www.nber.org/system/files/working_papers/w28369/revisions/w28369.rev2.pdf); [Swiss Finance Institute](https://www.sfi.ch/en/publications/competition-for-attention-in-the-etf-space); [DePaul behavioral-finance blog](https://blogs.depaul.edu/behavioral-finance/?p=173)
- [IND] Morningstar, *Global Thematic Funds Landscape 2024* (data to June 2024):
  - Only **9%** of thematic funds both survived and outperformed global equities over the **15 years** to June 2024.
  - **60%** of thematic funds closed in that period.
  - The 1-year success rate, the highest of any horizon, was 18%.
  - The benchmark is the Morningstar Global Target Market Exposure Index.
  - Sources: [Morningstar 2024 report PDF](https://assets.contentstack.io/v3/assets/blt4eb669caa7dc65b2/bltdcc1650217a6ca47/6716663877dcca724419a5b0/Morningstar_Global_Thematic_Funds_Landscape_2024.pdf); [Behavioural Investment, "Thematic Funds: Double Trouble", 2024-11-26](https://behaviouralinvestment.com/2024/11/26/thematic-funds-double-trouble/) [EXTRACT]
- [IND] Morningstar, *Global Thematic Funds Landscape* (May 2021): the 15-year success rate was **22%**, with **57%** of thematic funds closed. A later Morningstar guide using data through December 2021 put the 15-year rate near **one in ten**. — [2021 report PDF](https://www.investmentofficer.nl/sites/default/files/Global-Thematic-Funds-Landscape-May-2021.pdf); [Morningstar's Guide to Thematic Funds, Apr 2022](https://assets.contentstack.io/v3/assets/blt4eb669caa7dc65b2/blt49d8aa8626f0a97e/625ef5f82e17474fc7b94d8d/Guide_To_Thematic_Funds_04.18.22.pdf) [EXTRACT]
- [IND] Morningstar, *Global Thematic Fund Landscape 2025* (with a November 2025 update):
  - Fewer than **one in ten** thematic funds managed to both survive and outperform global equities over the long term. The window was not stated in the extract.
  - Global thematic assets reached a 3-year high of **US$779bn in Q3 2025**, still **15% below the 2021 peak**.
  - **82** new thematic funds launched in the first three quarters of 2025.
  - Sources: [Morningstar landing page](https://www.morningstar.com/lp/global-thematic-fund-landscape); [Morningstar Australia column](https://www.morningstar.com.au/etfs/young-invested-why-these-etfs-are-likely-disappoint-investors); [2025 report PDF](https://www.morningstar.com/content/cs-assets/v3/assets/blt9415ea4cc4157833/bltc6f6a4f03788229c/6920b163c3599fc9658f86a0/Global_Thematic_Fund_Landscape_2025_(2).pdf) [EXTRACT; PDF could not be opened]
- **ARK Innovation ETF (ARKK).**
  - Peak: February 2021. One tracker dates the total-return high to Feb 12, 2021; another gives a $159.70 peak on Feb 16, 2021.
  - Maximum drawdown to December 2022, which differs by measure:

    | Measure | Drawdown |
    |---|---|
    | Ben Felix | −77% |
    | Nominal total return | −80.9% |
    | Inflation-adjusted, to Dec 28, 2022 | −83.1% |

  - Still −63% from the peak as of March 2024 and **−55.9% as of Feb 18, 2026**. A tracker showed about −58% in late November 2026.
  - Sources: [Ben Felix (LinkedIn)](https://www.linkedin.com/posts/benjaminwfelix_the-ark-innovation-etf-arkk-had-a-maximum-activity-7186811281390149633-9arf); [totalrealreturns ARKK vs SPY](https://totalrealreturns.com/s/ARKK,SPY); [PortfoliosLab](https://portfolioslab.com/tools/stock-comparison/ARKK/SPY); [Seeking Alpha news, 2026](https://seekingalpha.com/news/4553197-five-years-later-cathie-woods-arkk-is-still-down-over-50-percent-since-its-2021-peak) [EXTRACT; figures vary by price vs. total-return basis]

### Inferences
- **Right theme, wrong price.** The themes (innovation, clean energy) were real. The losses came from entry valuations at launch or peak, which is exactly the mechanism Ben-David et al. identify. The same applies to AI-themed funds launched or bought during 2023–2026.
- **Supply follows attention.** Thematic fund supply responds to investor attention: 82 launches in nine months of 2025 even though assets were still below the 2021 peak. The pipeline of new theme products is therefore itself a sentiment indicator.
- **Survivorship flatters what remains.** The ~60% closure rate means the surviving thematic funds an investor sees today look better than the cohort's true record.

### Gaps
- The exact size of the post-launch underperformance in Ben-David et al. was not verified. A commonly cited figure is about −6%/yr risk-adjusted, roughly −30% over five years; treat it as unverified.
- Peak-to-trough figures for ICLN/TAN (clean energy), MJ (cannabis), 3D-printing stocks and ETFs, and 2020–21 de-SPACs were *not retrieved*. Searches returned nothing usable, and the search budget then ran out.
- Morningstar "Mind the Gap" investor-return gaps for thematic funds, and its "value destroyers" lists, were not verified.

---

## 5. Infrastructure-boom history (railways, electrification, telecom/fiber, dot-com) and the 2025–2026 AI-capex debate

### Takeaway
Each great infrastructure boom built durable, socially valuable capacity. Each also financed an overbuild that wiped out 65–99% of the equity value of many builders and "picks-and-shovels" suppliers, and the long-run winners were often the *users* of the then-cheap capacity. The 2025–26 AI buildout is already comparable to or larger than the telecom peak as a share of GDP (estimates range from ~1.1% to ~2.3% of GDP, with some projections to 3.6%). It shows classic late-boom markers: vendor/circular financing, credit- and SPV-funded data centers, and disputes over the useful lives of short-lived GPUs. As of **Nov 20–25, 2026, a live AI-led correction is under way**.

### Cited Findings
**British Railway Mania (1840s)**
- [WP/academic] Odlyzko (Univ. of Minnesota), "Collective Hallucinations and Inefficient Markets: The British Railway Mania of the 1840s":
  - Railway share prices declined relentlessly from the **summer-1845 peak to a trough at end-1849**.
  - Railway investment reached about **7% of GDP in 1847**.
  - Average dividends on ordinary railway shares were **1.83% in 1850**, against investors' hopes of about 10%.
  - The mania tripled British railway mileage and capitalization.
  - Sources: [ResearchGate](https://www.researchgate.net/publication/228291464_Collective_Hallucinations_and_Inefficient_Markets_The_British_Railway_Mania_of_the_1840s); [Odlyzko papers](https://www-users.cse.umn.edu/~odlyzko/doc/mania18.pdf); [notes by Kyle Harrison](https://www.kwharrison13.com/notes/collective-hallucinations-and-inefficient-markets-the-british-railway-mania-of-the-1840s/) [EXTRACT]
- [Academic] Queen's University Belfast paper, "Government Policy during the British Railway Mania and the 1847 Commercial Crisis": railway construction ran at **5.7%, 6.7% and 4.7% of GDP** in 1846, 1847 and 1848. — [QUB PDF](https://pureadmin.qub.ac.uk/ws/files/18161511/RailwayCrisis.pdf) [EXTRACT]
- [Academic] Odlyzko also documents an earlier British railway mania (1830s) as "a giant, wildly speculative, and *successful* investment mania". Not every mania destroys investors. — [Odlyzko, mania01.pdf](https://www-users.cse.umn.edu/~odlyzko/doc/mania01.pdf)

**US railroads**
- [MEDIA] By 1873 the US railroad boom had built some of the largest fortunes in American history. The crash then bankrupted **more than 100 railroads** and brought a five-year depression. — [Yahoo Finance](https://finance.yahoo.com/economy/articles/1873-railroad-boom-had-built-112630347.html)
- Estimates of railroad spending as a share of GDP vary with source and window:

  | Source | Railroad share of GDP |
  |---|---|
  | Brookings / Van Nieuwerburgh | ~**2.2%/yr** for 1870–1890 |
  | Noah Smith | some data put the peak near **5.4%** |
  | Paul Kedrosky | ~**6%** for late-1800s railroads |
  | UBS | **3.8–4.7%** for railroad booms |

  - Sources: [Brookings, "The $10 trillion question: Financing the AI buildout"](https://www.brookings.edu/articles/the-10-trillion-question-financing-the-ai-buildout/); [Noahpinion, "AI vs. the railroads"](https://www.noahpinion.blog/p/ai-vs-the-railroads); [Advisor Perspectives, 2025-10-09](https://www.advisorperspectives.com/articles/2025/10/09/ai-spending-boom-massive-not-unprecedented); [Pareto Investor](https://paretoinvestor.substack.com/p/who-keeps-the-value-ai-infrastructure-boom) [EXTRACT]

**Telecom / fiber (1996–2002) and dot-com**
- **Fiber utilization.** In 2002 only **~2.7%** of installed US fiber was in use. Commonly cited lit-fiber figures range from **2.7% to 5%**. Another estimate says less than 5% of cable laid between 1999 and 2004 was lit. — [The Timeless Investor](https://thetimelessinvestor.substack.com/p/they-buried-a-trillion-dollars-underground); [Opus Interactive](https://www.opusinteractive.com/opus-blog/post/the-telecom-overbuild-that-built-the-cloud-lessons-from-fiber-glut-to-hyperscale-success/); [HostDir](https://hostdir.net/blog/fiber-optic-glut-dark-fiber) [secondary]
- **Market losses and bandwidth prices.** From 2000 to 2002, global telecom stocks lost **more than $2 trillion** of market value. Bandwidth prices fell by **~90%**. — [The Bubble Bubble](https://www.thebubblebubble.com/telecom-bubble/); [94040 Substack](https://94040.substack.com/p/edition-2-lessons-from-history-telecom) [secondary]
- [MEDIA] **Equipment vendors** ("picks and shovels"):
  - At their peaks, Lucent, Nortel and JDS Uniphase each had market caps **above $200bn**, and Corning's was above $100bn.
  - By September 2002 the **combined value of all four was about $11bn**.
  - JDSU: split-adjusted close of **$146.35 on Mar 6, 2000**, falling to about **$2.91 by July 2003**, roughly −98%.
  - Lucent had lost more than 90% in two years by late 2001.
  - Nortel had fallen to 7.2% of its year-earlier value by September 2001. It later declined ~99% and went bankrupt in 2009.
  - Sources: [CNN Money, "The $1 telecom club", 2002-09-23](https://money.cnn.com/2002/09/23/pf/investing/q_lucent/index.htm); [CNN Money, "Telecom turmoil", 2001-12-18](https://money.cnn.com/2001/12/18/technology/q_yearend_telecom/); [Motley Fool, 2003-07-29](https://www.fool.com/news/2003/07/29/jds-uniphases-telecosmic-trip.aspx); [Optics & Photonics News, Oct 2016, "Boom, Bubble, Bust: Fiber Optic Mania"](https://internethistory.org/wp-content/uploads/2020/01/OSA_Boom.Bubble.Bust_Fiber.Optic_.Mania_.pdf) [EXTRACT; the per-number attribution across these four sources could not be checked page by page]
- [MEDIA] **Cisco**, the highest-quality survivor, fell ~90% (market cap bottomed near $60bn in late 2002). It regained its Mar 27, 2000 record close only on **Dec 10, 2025**. — [CNBC](https://www.cnbc.com/2025/12/10/ciscos-stock-closes-at-record-for-first-time-since-dot-com-peak-2000.html); [Yahoo Finance, "Cisco's 25-Year Journey Back to Its Dot-Com Peak Offers a Cautionary Tech Lesson"](https://finance.yahoo.com/news/cisco-25-journey-back-dot-122222711.html)
- **Who later benefited.** The overbuilt "dark" fiber later carried the cloud and hyperscale era (Opus Interactive's account: "the telecom overbuild that built the cloud"). Amazon, which itself fell −94%, became a long-run winner partly as a *user* of cheap infrastructure. — [Opus Interactive](https://www.opusinteractive.com/opus-blog/post/the-telecom-overbuild-that-built-the-cloud-lessons-from-fiber-glut-to-hyperscale-success/); see section 3 for the Amazon drawdown.

**AI capex scale versus past booms (2024–2026 debate)**
- [OPINION/IND] David Cahn (Sequoia), "AI's $200B Question" (Sept 2023) and "**AI's $600B Question**" (June 20, 2024).
  - Method: take Nvidia's run-rate data-center revenue, double it for total data-center cost, and double again for a 50% end-user gross margin. The result is the revenue AI must eventually generate.
  - Cahn also wrote that AI "is likely to be the next transformative technology wave".
  - In Goldman Sachs Research's report "AI: In a Bubble" (date not retrieved), Cahn argues there is a capex bubble but significant long-term opportunity, especially at the application layer.
  - Sources: [Cahn's Substack](https://dcahn.substack.com/p/ais-600b-question); [Goldman Sachs, "AI: In a Bubble"](https://www.goldmansachs.com/pdfs/insights/goldman-sachs-research/ai-in-a-bubble/report.pdf) [EXTRACT]
- [OPINION] **Paul Kedrosky** (reported 2025-10-09): AI capex was ~**1.2% of US GDP**, versus ~1% at the telecom peak (the extract says "2020", evidently a typo for 2000) and ~6% for late-1800s railroads. — [Advisor Perspectives](https://www.advisorperspectives.com/articles/2025/10/09/ai-spending-boom-massive-not-unprecedented)
- [IND] **Brookings, Stijn Van Nieuwerburgh** (publication date not retrieved): data-center buildout projected at about **3.6% of GDP per year through 2032**, versus ~2.2% for 1870–1890 railroads and ~1.1% for telecom/fiber. Hence the "$10 trillion question" of how the buildout will be financed. Noah Smith notes the comparison uses different time spans. — [Brookings](https://www.brookings.edu/articles/the-10-trillion-question-financing-the-ai-buildout/); [Noahpinion](https://www.noahpinion.blog/p/ai-vs-the-railroads) [EXTRACT]
- [IND, secondary] **UBS** projected AI capex at ~1.1% of GDP. **Meridian Report** (2026) put 2026 capex by the big four hyperscalers at ~**2.3% of US GDP**, versus ~1.2% for telecom in 2000. Meridian flags that it divides *global* company spending by *US* GDP, which flatters the ratio. — [Pareto Investor](https://paretoinvestor.substack.com/p/who-keeps-the-value-ai-infrastructure-boom); [Meridian Report, "The $733 billion year"](https://meridianreport.org/article/ai-infrastructure-capex-report-2026)
- [IND/MEDIA] **Contribution to growth:**
  - Renaissance Macro estimated that AI data-center spending added more to **2025** US GDP growth than all consumer spending. — [Yahoo Finance / Fortune](https://finance.yahoo.com/news/spending-ai-data-centers-massive-150110727.html)
  - Harvard's **Jason Furman** said AI investment accounted for nearly **92% of US GDP growth in H1 2025**. This is secondhand; the original methodology was not seen. — [Yahoo Finance](https://finance.yahoo.com/news/most-us-growth-now-rides-213011552.html)
- [OPINION] **Sam Altman**, OpenAI CEO (Aug 2025): "Are we in a phase where investors as a whole are overexcited about AI? My opinion is yes." — [Yahoo Finance](https://finance.yahoo.com/news/most-us-growth-now-rides-213011552.html) [secondary quote]

**GPU depreciation lives**
- [OPINION] **Michael Burry**, X post, ~Nov 10, 2025:
  - Hyperscalers will **understate depreciation by ~$176bn over 2026–2028** by assigning 5–6-year useful lives to Nvidia-class servers whose economic cycle he puts at 2–3 years.
  - By 2028, he estimates Oracle's earnings will be overstated by **26.9%** and Meta's by **20.8%**.
  - Burry called extending useful lives "one of the more common frauds of the modern era".
  - Sources: [Burry on X](https://x.com/michaeljburry/status/1987918650104283372); [Yahoo Finance](https://finance.yahoo.com/technology/ai/articles/michael-burry-says-could-heard-055211614.html)
- **Reconstructions of Burry's figure:** assuming true 4-year lives adds ~**$132bn** of depreciation over 2026–28, and 3-year lives add ~**$263bn**. Burry never published his model. — [CapexCat Substack](https://capexcat.substack.com/p/michael-burry-depreciation-math); [Dave Friedman](https://davefriedman.substack.com/p/the-176-billion-accounting-question)
- **Company changes in 2025:**
  - **Amazon** shortened the useful life of a subset of servers from 6 to 5 years, citing the pace of AI/ML development. The change cost ~$700m of operating income, with ~$920m of accelerated depreciation.
  - **Meta** extended server lives to 5.5 years, cutting depreciation expense by ~$2.9bn.
  - Counterpoint: valuations based on free cash flow or EBITDA are unaffected by these choices.
  - Sources: [Level Headed Investing](https://www.levelheadedinvesting.com/p/are-ai-chips-useful-lives-creating-useless-earnings); [Luminix](https://www.useluminix.com/reports/industry-analysis/gpu-depreciation-debate) [secondary]

**Circular and vendor financing**
- [Government analysis] Congressional Research Service In Focus IF13349, "The Role of Circular Finance in Funding AI Investment":
  - Nvidia reportedly pledged up to **$100bn** of investment in OpenAI (reported autumn 2025).
  - Later reports said the deal was being significantly downsized. A secondary source puts Nvidia's actual investment at $30bn in an OpenAI round that closed Mar 31, 2026.
  - Sources: [Congress.gov](https://www.congress.gov/crs-product/IF13349); [Columbia Business School note](https://blogs.cuit.columbia.edu/gjb2124/circular-financing/) [EXTRACT]
- **AMD and Oracle:**
  - AMD granted OpenAI warrants for up to **160 million AMD shares** tied to deploying **6 GW** of AMD GPUs by 2030.
  - OpenAI's compute commitment to **Oracle** is about **$300bn**; some sources say $317bn.
  - Oracle reportedly paid up to **8.65%** to borrow $10bn.
  - Sources: [Alatirok explainer](https://alatirok.com/ai-circular-financing-explained/); [Gecko](https://www.geckomode.ai/blog/ai-debt-machine-circular-financing) [secondary]
- [WP] Solanki (SSRN), "The AI Circular Economy: Systemic Risk, Vendor Financing, and the Keystone Problem", identifies **seven circular financing loops** totaling **more than $1.4 trillion** of committed future spending. — [SSRN](https://papers.ssrn.com/sol3/Delivery.cfm/6672478.pdf?abstractid=6672478&mirid=1)
- [OPINION/unverified] Burry also says five hyperscalers carry **$1.65 trillion** of off-balance-sheet obligations and that Nvidia's CDS spread doubled in two months. Secondary sources further report that Nvidia guarantees up to **$105bn** of OpenAI leases (reported Aug 2026). — [Yahoo Finance](https://finance.yahoo.com/technology/ai/articles/michael-burry-sounds-alarm-again-144154784.html); [AIStockWire, Nov 2026](https://aistockwire.com/blog/circular-financing-explained-fed-nvidia-openai-nscale-coreweave-november-2026) [not verified against filings]

**Market events, Sept–Nov 2026 (dated)**
- [OPINION] **2026-09-28**, Forbes (Peter Cohan), bust scenario: Nvidia −25–35%, Oracle −30–40% given its reliance on OpenAI contracts, and CoreWeave −40–60%. This is a scenario, not a forecast. — [Forbes](https://www.forbes.com/sites/petercohan/2026/09/28/what-could-pop-the-ai-bubble-and-which-stocks-stand-to-lose/)
- [MEDIA] **2026-11-10:** Nvidia was ~30% below its high. — [Motley Fool](https://www.fool.com/investing/2026/11/10/nvidia-is-down-30-from-its-high-history-says-this/)
- [IND/MEDIA] **2026-11-17**, Bank of America November Global Fund Manager Survey:
  - Managers cut tech allocations by the **most since June 2006**.
  - **52%** expect at least one AI hyperscaler to announce a capex cut within six months.
  - **Goldman Sachs** estimates AI has pushed profits ~**25% above trend**. It expects hyperscaler capex to keep growing in 2027 but more slowly, and sees the net boost from AI investment falling to ~9 points in 2027 and turning into a ~5-point drag in 2028 (units as reported).
  - Source: [Fortune, 2026-11-17](https://fortune.com/2026/11/17/ai-bubble-popping-bofa-fund-manager-survey-largest-cut-since-2006/)
- [MEDIA] **2026-11-20:** the S&P 500 fell **3.6%**, its seventh straight decline and longest losing streak since Feb 2020. The **S&P 500 and the Dow entered correction** (more than 10% below record closes), and the Nasdaq turned negative for the year. — [Breitbart, 2026-11-20](https://www.breitbart.com/economy/2026/11/20/stocks-plunge-as-ai-selloff-pushes-sp-500-and-dow-into-correction/); [Yahoo Finance / Reuters](https://finance.yahoo.com/markets/stocks/articles/wall-st-futures-slip-anthropic-104746137.html)
- [MEDIA] **2026-11-25:**
  - The Nasdaq 100 fell **more than 4% intraday** and briefly entered a **bear market**, 20% below its early-October 2026 peak, before paring losses. CNN reported a close of −0.62%.
  - The Nasdaq and S&P 500 were on track for their **worst November since 2008**.
  - The newly listed **Anthropic** traded below its **$83 IPO price**, and its market value dipped below $1 trillion for the first time since listing.
  - Causes cited: doubts over whether AI spending will pay off and how it will be financed as interest rates climb, plus new tariff proposals.
  - Sources: [Irish Times](https://www.irishtimes.com/business/2026/11/25/us-stocks-sell-off-deepens-as-ai-trade-cracks/); [CNN](https://www.cnn.com/2026/11/25/business/ai-sell-off-despite-huang-nvidia-return); [CNBC](https://cnbc.com/2026/11/25/nvidia-ai-stock-tech-selloff.html); [Korea Times / Reuters](https://www.koreatimes.co.kr/world/20261126/nasdaq-sinks-about-4-as-ai-rout-fresh-trump-tariffs-spook-wall-st)
- [MEDIA, single extract, not cross-verified] OpenAI's latest round was reported at **$15bn at a $1.25tn valuation**, against an initial target of up to $30bn at $1.4tn (CNBC, as summarized in a search extract). FT reportedly said the target was trimmed by $10bn. — [CNBC](https://cnbc.com/2026/11/25/nvidia-ai-stock-tech-selloff.html) [unverified]
- [IND/OPINION] **2027 capex estimates** vary: "analyst construction" puts Big-5 capex at **$1.2–1.3tn**, while JPMorgan reportedly forecasts **$1.7tn** against a $1.4tn consensus. — [AL Capital Advisory](https://alcapitaladvisory.com/research/intelligence/ai-infrastructure.html) [secondary]

### Inferences
- **The recurring boom template** (railways 1840s and 1870s–90s, telecom 1996–2002):
  1. A genuinely transformative technology arrives.
  2. Capex surges to ~1–7% of GDP.
  3. It is financed with leverage and novel structures.
  4. Capacity overshoots near-term demand (UK rail dividends 1.83% versus 10% hoped; fiber 2.7–5% lit).
  5. Prices for the capacity collapse (bandwidth −90%).
  6. Builders' and suppliers' equity falls 85–99%, and several go bankrupt.
  7. Later *users* of the cheap capacity capture much of the value.
  - This matches Carlota Perez's "installation, frenzy, turning point, deployment" framework in *Technological Revolutions and Financial Capital* (2002) and Chancellor's *Devil Take the Hindmost* (1999). Both are NOT RE-VERIFIED this session.
- **Quality does not rescue a peak entry price.** Cisco was the strongest picks-and-shovels survivor and still needed 25 years to break even from its 2000 peak. Buying excellent suppliers at peak valuations can mean zero nominal price return for decades.
- **What is new about AI:**
  - Core AI assets (GPUs) have economic lives of roughly 3–6 years, versus decades for rail and fiber. An AI overbuild leaves less durable "cheap capacity" for later users, though data-center shells, power and grid connections do last. It also makes the depreciation debate central to whether reported earnings are real.
  - Much hyperscaler spending is funded from operating cash flow, unlike debt-funded 1990s carriers. But vendor financing, SPVs, private credit and Oracle/neocloud debt are where the telecom-style fragility sits. In Forbes' bust scenario, the most-levered names (CoreWeave, Oracle) are expected to fall furthest.
- **The 2026 correction resolves nothing yet.** The Nov 2026 correction (S&P/Dow −10%+, Nasdaq 100 briefly −20%, Nvidia ~−30%) is consistent with the boom template's "turning point" phase. It is too early to tell whether it is a mid-cycle correction (like 1998) or a 2000-style peak.

### Gaps
- **1920s electrification and utilities** were not retrieved (search budget ran out): Insull's holding-company collapse, the size of the 1929–32 decline in utility stocks, and the Public Utility Holding Company Act of 1935.
- The share of US railroad mileage in receivership after the 1893 panic was not verified.
- The exact percentage fall in UK railway share prices from 1845 to 1849 was not given in the extracts.
- The Meta "Hyperion" / Blue Owl SPV financing (reported ~US$27bn), Oracle CDS levels, Morgan Stanley's ~$1.5tn financing-gap estimate and JPMorgan's ~$5tn AI-infrastructure estimate (all 2025) were *not verified*.
- The conclusions of the June 2026 arXiv paper "Boom, Bubble, or Buildout?" ([arXiv 2606.01575](https://arxiv.org/pdf/2606.01575)) were not retrieved.
- These unverified narratives appeared only in low-quality sources and should not be used without confirmation: an "October 2026 tech selloff" with OpenAI revenue at ~$50bn (trading blogs), a post-midterm "data-center regulation" scare that wiped out ~$2tn in a day (newsletters), and news about Nvidia CEO Jensen Huang's "exit" and "return" (Trefis 2026-11-20; CNN 2026-11-25 headline).
- Dimson–Marsh–Staunton work on new-industry returns (e.g., railroads versus later industries) was not retrieved.

---

## 6. Evidence-based strategies that improve long-run odds or reduce ruin

### Takeaway
No well-documented strategy reliably turns the index's ~10% nominal into the 14–22%/yr a 30- to 20-year 50x goal requires. Several have strong evidence for improving *risk-adjusted* returns or cutting the drawdowns that cause ruin or capitulation:
- momentum, if its crash risk is managed;
- trend filters, which in my backtests cut the worst drawdown from −82% to roughly −46% to −51% (1926–2023) at a cost of 0 to 1.6 points of CAGR before taxes and costs;
- quality / profitability / free-cash-flow tilts;
- minimal fees, tax deferral, and lump-sum investing over dollar-cost averaging.

### Cited Findings
**Momentum and its crash risk**
- [PR] Daniel & Moskowitz (2016), "Momentum crashes", *Journal of Financial Economics* (sample 1927–2013).
  - The two worst months for a long-winners / short-losers momentum strategy were **July and August 1932**, at about **−61% and −74%** (roughly −90% compounded). Over those two months the loser decile rose **~232%**, winners ~32% and the market ~82%.
  - In **Mar–May 2009**, losers rose **~163%**, winners ~8% and the market ~26%.
  - Crashes occur in "panic" states after market declines, when volatility is high and the market rebounds.
  - Sources: [Kent Daniel, JFE PDF](https://www.kentdaniel.net/papers/published/jfe_16.pdf); [working-paper version](https://www.kentdaniel.net/papers/published/mom12.pdf); [RSL-List summary](https://rsl-list.com/en/wissen/momentum-crashs-und-schwankung) [EXTRACT]
- [PR, NOT RE-VERIFIED] Jegadeesh & Titman (1993), "Returns to Buying Winners and Selling Losers", *Journal of Finance* 48(1): 65–91. The 6-month formation / 6-month holding strategy earned a compounded excess return of about **12.01%/yr** over 1965–1989, with part of it dissipating over the following two years. — [DOI 10.1111/j.1540-6261.1993.tb04702.x](https://doi.org/10.1111/j.1540-6261.1993.tb04702.x)
- [PR, NOT RE-VERIFIED] Moskowitz, Ooi & Pedersen (2012), "Time series momentum", *Journal of Financial Economics* 104(2): 228–250. Significant time-series momentum appears in all **58** liquid futures instruments studied (equity indexes, currencies, commodities, bonds). Returns persist over 1–12 months and partly reverse over longer horizons. A diversified time-series momentum (TSMOM) portfolio performs best in extreme markets. — [DOI 10.1016/j.jfineco.2011.11.003](https://doi.org/10.1016/j.jfineco.2011.11.003)
- [PR, NOT RE-VERIFIED] Barroso & Santa-Clara (2015), "Momentum has its moments", *JFE* 116(1): 111–120. Scaling momentum exposure by its own recent volatility substantially reduces crash risk and improves the Sharpe ratio. — [DOI 10.1016/j.jfineco.2014.11.010](https://doi.org/10.1016/j.jfineco.2014.11.010)

**Trend filters**
- [Practitioner journal, NOT RE-VERIFIED] Faber (2007), "A Quantitative Approach to Tactical Asset Allocation", *Journal of Wealth Management*. A 10-month simple-moving-average (SMA) timing rule, tested on US equities since 1900 and on multiple asset classes since 1973, produced "equity-like returns with bond-like volatility and drawdown" in a tactical-allocation portfolio. — [SSRN 962461](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=962461)

**My backtests of trend rules on the S&P 500** [OWN CALC on [Shiller data](https://raw.githubusercontent.com/datasets/s-and-p-500/main/data/data.csv); signal uses a one-month lag to avoid look-ahead; no transaction costs or taxes]
- The rules are invested only when the price is above its 10-month SMA (**10M SMA**), or when the trailing 12-month total return is positive (**12M TSMOM**).
- No T-bill series was available, so cash is shown at two bounds: **0%** (lower bound) and the **10-year Treasury yield/12** (an upper-bound proxy for T-bills).

| Period | Strategy | Nominal CAGR | Real CAGR | Vol | **Max drawdown** (nominal / real) | Time invested |
|---|---|---|---|---|---|---|
| 1926–2023 | Buy & hold | 10.15% | 6.99% | 15.3% | **−81.7% / −76.7%** | 100% |
| 1926–2023 | 10M SMA, cash 0% | 8.53% | 5.42% | 10.4% | −51.3% / −40.0% | 68% |
| 1926–2023 | 10M SMA, cash at 10y yield | 10.23% | 7.07% | 10.3% | −46.6% / −38.1% | 68% |
| 1926–2023 | 12M TSMOM, cash 0% | 8.27% | 5.17% | 11.0% | −48.5% / −56.7% | 75% |
| 1926–2023 | 12M TSMOM, cash at 10y yield | 9.59% | 6.44% | 11.0% | −45.8% / −53.3% | 75% |
| 1957–2023 | Buy & hold | 10.30% | 6.38% | 12.4% | −49.0% / −51.8% | 100% |
| 1957–2023 | 10M SMA, cash 0% / 10y yield | 8.10% / 10.08% | 4.26% / 6.17% | 8.9% | −26.3% / −25.0% (nominal) | 70% |
| 1990–2023 | Buy & hold | 10.12% | 7.28% | 12.6% | −49.0% / −51.8% | 100% |
| 1990–2023 | 10M SMA, cash 0% / 10y yield | 8.66% / 9.86% | 5.85% / 7.02% | 9.0% | −18.9% / −18.9% | 74% |

**Lump sum versus dollar-cost averaging** [OWN CALC, same data; 12-month DCA; start months from 1926]
- With a **10-year horizon**, lump sum beat DCA in **66.4–72.9%** of 1,049 start months. The median lump-sum advantage was 3.4–5.4%, with the range depending on the cash bound.
- With a 1-year horizon, lump sum won in **66.0–73.6%** of start months.

**Quality and profitability** [PR, NOT RE-VERIFIED]
- Novy-Marx (2013), "The other side of value: The gross profitability premium", *JFE* 108(1): 1–28. Gross profits-to-assets has about as much power as book-to-market in predicting the cross-section of returns, and profitable firms earn higher returns despite higher valuations. — [DOI 10.1016/j.jfineco.2013.01.003](https://doi.org/10.1016/j.jfineco.2013.01.003)
- Asness, Frazzini & Pedersen (2019), "Quality minus junk", *Review of Accounting Studies* 24(1): 34–112. A long-quality / short-junk factor earns significant risk-adjusted returns in the US and internationally. High-quality stocks trade at higher prices, but not high enough. — [DOI 10.1007/s11142-018-9470-2](https://doi.org/10.1007/s11142-018-9470-2)
- Consistent with this, Yartseva (2025, WP) finds profitability, value and FCF yield predicted the 2009–2024 10-baggers (see section 1).

**Fees and taxes** [OWN CALC, illustrative: 10% gross return]
- Fees over **40 years** cut the terminal multiple:

  | Annual fee | Terminal multiple | Change versus 45.3x gross |
  |---|---|---|
  | 0.05% | **44.4x** | −2% |
  | 0.75% | **34.4x** | −24% |
  | 1% | **31.4x** | −31% |
  | 2% | **21.7x** | −52% |

- Over **30 years**, a 1% fee cuts 17.4x to 13.3x (−24%) and a 2% fee cuts it to 10.1x (−42%).
- Taxes over 40 years at 10%/yr:

  | Tax treatment | Terminal multiple |
  |---|---|
  | Untaxed | 45.3x |
  | Deferred, 20% tax paid once at the end | **36.4x** |
  | Taxed annually at 20% (high turnover, long-term rates) | **21.7x** |
  | Taxed annually at 37% (short-term rates) | **11.5x** |

**Core-satellite / barbell arithmetic** [OWN CALC]
- With 90% in an index core and 10% in a satellite, the satellite must return the following for the whole portfolio to reach 50x:
  - **~348x** over 30 years if the core earns the 1871+ median (16.9x).
  - **~307x** over 30 years if the core earns the 1926+ median (21.4x).
  - **~88x** over 40 years if the core earns the 1871+ median (45.8x).
  - Nothing over 40 years if the core earns the 1926+ median (65.1x): the core alone gives 0.9 × 65.1 = 58.6x.
  - **~391x** for a *real* 50x over 40 years.
- If the 10% satellite goes to zero, the portfolio loses only 10%.

### Inferences
- **Value of trend and momentum rules is survival, not return.** They lower the *variance* of outcomes and cut the depth of the worst drawdowns roughly in half (1926–2023). That matters most for concentrated or leveraged portfolios, where a −80% drawdown is fatal, and for an investor's ability to stay invested. With costs and taxes, they likely trail buy-and-hold slightly. Their whipsaw costs were real: 126 switches over 97 years for 10M SMA.
- **Two kinds of momentum.** Cross-sectional stock momentum has a crash problem (−90% in two months in 1932). Yartseva's multibaggers also loaded *negatively* on short-term momentum *before* their runs. Momentum may help more in *holding* winners ("let winners run") than in *finding* future 50-baggers.
- **The highest-certainty levers are mechanical:**
  - Fees: 1%/yr costs about a third of a 40-year 50x.
  - Tax deferral: annual taxation at 20% roughly halves the 40-year multiple.
  - Lump sum over DCA: wins about two-thirds of the time.
  - Avoiding forced selling: no leverage that can be margin-called through a −50% index drawdown.
- **Barbell logic.** With a broad index core, a 50x *nominal* over 40 years historically depended mainly on time in the market. A ≤10–20% satellite of concentrated or thematic bets can raise the odds of beating that while capping the cost of failure at 10–20%. Over 20–30 years, however, the satellite would need ~300x+ to matter, which is extreme right-tail territory (see sections 1 and 3).

### Gaps
- These items were not verified this session because the search budget ran out:
  - SPIVA active-fund underperformance rates;
  - Morningstar "Mind the Gap" investor-return gaps;
  - Vanguard's 2023 update on cost averaging;
  - Faber's published performance numbers;
  - Antonacci, *Dual Momentum Investing* (McGraw-Hill, 2014; backtest-based, not peer-reviewed), which combines relative and absolute (trend) momentum;
  - Vanguard (2012), "Dollar-cost averaging just means taking risk later", widely cited as finding lump sum beat DCA about two-thirds of the time in US, UK and Australian data. My backtest (lump sum won 66–73% of start months) is consistent with this;
  - rebalancing-bonus studies;
  - after-cost evidence on trend following.
- The papers marked NOT RE-VERIFIED are canonical, but their links and numbers should be spot-checked before publication.
- No study was found estimating the probability of a 50x outcome under specific evidence-based strategies.

---

## 7. Implications for a 50x goal

### Takeaway
A 50x goal is realistic mainly as a ~40-year, nominal, low-cost, tax-deferred broad-equity outcome; historically that has been close to the median. Compressing it into 20–30 years, or demanding 50x *after inflation*, moves it into right-tail territory. That territory is reached only through concentration, which empirically has a poor *median* and requires surviving 65–95% drawdowns. Entering through hot themes or boom-era "picks and shovels" has historically lowered, not raised, the odds.

### Cited Findings (evidence-backed takeaways)
1. **Time is the main lever; 50x nominal is roughly a 40-year index outcome.**
   - Index evidence [OWN CALC, Shiller data]:
     - The S&P 500 total return delivered ≥50x in **~72%** of 40-year windows starting 1926 or later. The median was 65x (46x across all windows since 1871).
     - It delivered ≥50x in only **~1%** of 30-year windows and **0%** of 20-year windows.
     - At ~10%/yr, 50x takes ~41 years.
   - Implication: define the goal's horizon first. — [Shiller data](https://raw.githubusercontent.com/datasets/s-and-p-500/main/data/data.csv)
2. **Separate nominal from real.**
   - At the index's ~7% real CAGR, 50x real takes **~58 years**. No 40-year window since 1926 achieved 50x real; only ~10% of 50-year windows did [OWN CALC].
   - Implication: a "50x" plan should state whether inflation is included.
3. **The required CAGR rises steeply as the horizon shortens:** **21.6%/yr for 20 years**, 13.9% for 30 and 10.3% for 40 [OWN CALC]. The index's best-ever 20-year window was 17.9%/yr. A 20-year 50x is outside anything the market itself has delivered.
4. **Single-stock base rates are poor.**
   - **51.6%** of US stocks had negative lifetime returns from 1926 to 2023 ([Bessembinder 2024](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4897069)).
   - 55–57% of US and global stocks lagged T-bills from 1990 to 2020, and **2.4%** of firms created all net global wealth ([Bessembinder et al., FAJ 2023](https://rpc.cfainstitute.org/research/financial-analysts-journal/2023/long-term-shareholder-returns-evidence-from-64000-global-stocks)).
   - More than **40%** of Russell 3000 names suffered unrecovered ≥70% losses ([J.P. Morgan](https://privatebank.jpmorgan.com/content/dam/jpm-pb-aem/global/en/documents/eotm/agony-ecstasy-2021.pdf)).
5. **Even the great winners compounded at "only" 13–19%/yr and needed decades.**
   - The 17 best long-lived US stocks averaged **~13.5%/yr**, i.e. ~31 years to 50x ([Bessembinder 2024](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4897069)).
   - Mayer's 100-baggers averaged **~26 years**, about 19%/yr ([Stablebread summary](https://stablebread.com/multibagger-stock-studies/)).
   - Implication: a sub-15-year 50x requires a once-a-generation outlier such as Nvidia's 33%/yr.
6. **Every path to 50x includes brutal drawdowns, so size positions to survive them.**
   - Amazon −94%; Nvidia −90%, −85% and −66%; Apple −82%; Microsoft −69% and under water for a decade; Cisco 25 years to regain its 2000 peak ([totalrealreturns](https://totalrealreturns.com/n/NVDA,AAPL,MSFT,GOOGL,AMZN,NFLX,META,TSLA); [CNBC](https://www.cnbc.com/2025/12/10/ciscos-stock-closes-at-record-for-first-time-since-dot-com-peak-2000.html)).
   - Full Kelly carries a **50%** chance of being halved at some point; half Kelly cuts that to 12.5% [OWN CALC]. Keep any single position at roughly ≤ half Kelly, which in practice means about **~8–16%** of capital (quarter to half Kelly, even with an optimistic 8% edge).
7. **Volatility drag makes concentrated bets' median outcomes poor.** A stock with a 15% expected return and 45% volatility has a mean 30-year multiple of 66x but a **median of 3.2x**, a ~13% chance of reaching 50x and a **~32% chance of losing money** [OWN CALC]. Diversifying across many independent bets is what rescues the median.
8. **Don't buy themes after they are hot.**
   - Specialized ETFs launch when their holdings are overvalued and then underperform ([Ben-David et al., RFS 2023](https://econpapers.repec.org/RePEc:oup:rfinst:v:36:y:2023:i:3:p:987-1042.)).
   - Only **9%** of thematic funds survived and beat global equities over 15 years, and **60%** closed ([Morningstar 2024](https://assets.contentstack.io/v3/assets/blt4eb669caa7dc65b2/bltdcc1650217a6ca47/6716663877dcca724419a5b0/Morningstar_Global_Thematic_Funds_Landscape_2024.pdf)).
   - ARKK fell ~77–81% and was still ~56% below its peak five years later ([Seeking Alpha](https://seekingalpha.com/news/4553197-five-years-later-cathie-woods-arkk-is-still-down-over-50-percent-since-its-2021-peak)).
9. **Infrastructure booms reward the technology more than the builders' shareholders.**
   - Telecom equipment leaders lost ~90–99%; four companies once worth more than $700bn combined were worth ~$11bn by 2002 ([CNN Money](https://money.cnn.com/2002/09/23/pf/investing/q_lucent/index.htm)).
   - Only ~2.7–5% of the fiber built was lit ([The Timeless Investor](https://thetimelessinvestor.substack.com/p/they-buried-a-trillion-dollars-underground)).
   - UK railway dividends were 1.83% in 1850 against ~10% hoped ([Odlyzko](https://www.researchgate.net/publication/228291464_Collective_Hallucinations_and_Inefficient_Markets_The_British_Railway_Mania_of_the_1840s)).
   - Implication: for AI, the long-run winners may be *users* of cheap compute as much as today's suppliers.
10. **The AI trade now shows classic late-boom markers. Treat AI infrastructure as a sized satellite, not a core bet.**
    - Capex is ~1.2–2.3% of GDP, at or above the telecom peak ([Advisor Perspectives](https://www.advisorperspectives.com/articles/2025/10/09/ai-spending-boom-massive-not-unprecedented); [Meridian](https://meridianreport.org/article/ai-infrastructure-capex-report-2026)).
    - Circular financing loops total more than $1.4tn ([SSRN](https://papers.ssrn.com/sol3/Delivery.cfm/6672478.pdf?abstractid=6672478&mirid=1)).
    - GPU useful-life accounting is disputed: Burry estimates $176bn of understated depreciation ([X](https://x.com/michaeljburry/status/1987918650104283372)).
    - A correction is under way (S&P 500 and Dow in correction on 2026-11-20; Nasdaq 100 briefly in a bear market on 2026-11-25) ([Irish Times](https://www.irishtimes.com/business/2026/11/25/us-stocks-sell-off-deepens-as-ai-trade-cracks/)).
    - None of this proves AI will disappoint. It means entry valuation and balance-sheet risk dominate the outcome.
11. **Bank the mechanical edges first.**
    - Low fees: 1%/yr turns a 45x 40-year outcome into ~31x.
    - Tax deferral: annual taxation at 20% gives ~22x instead of ~36x deferred.
    - Lump sum over DCA: wins ~66–73% of the time.
    - No margin leverage that could force selling in an index fall of −50% to −82%.
    - All from [OWN CALC, Shiller data](https://raw.githubusercontent.com/datasets/s-and-p-500/main/data/data.csv).
12. **Use evidence-based tilts and risk controls for the risky sleeve.**
    - Prefer quality, profitability and FCF-yield characteristics; these are what predicted 10-baggers in [Yartseva 2025](https://ideas.repec.org/p/akf/cafewp/33.html).
    - Use trend or volatility filters to avoid −80% outcomes: −82% fell to −46% to −51% (1926–2023) [OWN CALC].
    - Respect momentum crash risk: a ~−90% two-month loss in 1932 ([Daniel & Moskowitz](https://www.kentdaniel.net/papers/published/jfe_16.pdf)).
    - Rebalance a 90/10 or 80/20 core-satellite so that a failed satellite costs ≤10–20%.

### Inferences
- **Recommended framing for the report.** "50x nominal in ~40 years via a low-cost, tax-deferred broad-equity core" is the evidence-based base case, at roughly a coin flip or better historically. "50x in 15–25 years" requires a right-tail outcome; give it a probability in single digits to the low teens even under generous assumptions, and design the portfolio so that missing it is survivable.

### Gaps
- No direct empirical study estimating the probability of 50x for concentrated, thematic or factor portfolios was found.
- The probabilities in this section combine index history with lognormal illustrations, and should be presented as such.
