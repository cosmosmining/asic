# AI Power & Physical Infrastructure (generation, grid/transmission, nuclear & fuel, data-center electrical & thermal, utilities/IPPs, gas midstream, storage, copper/uranium) — state as of 25 Nov 2026

> Compiled 2026-11-25. Every figure carries an as-of date. Tags used: **[PRE-REVENUE]**, **[SPECULATIVE]**, **[HIGH VALUATION]**, **[STALE]** (older than ~6 months or predates Q3-2026 reporting), **[SECONDARY]** (aggregator/blog/summary rather than company or agency primary), **[CONFLICT]** (sources disagree), **[VERIFY]** (figure seen only through a search-engine summary of the primary document).
>
> Research limits (important for the report writer and the screener): (1) live market data could not be pulled — finviz.com and sec.gov were outside this session's allowed fetch domains, and a direct quote-API pull was denied; (2) the shared web-search budget was exhausted before market-cap / 1-year-return / forward-multiple gaps could be closed. Market caps, YTD and 1-year returns and multiples below are therefore sparse, come from dated secondary articles, and must be refreshed from a live feed. Most company numbers come from Q3-2026 releases (often SEC 8-K exhibits) as surfaced in search results; treat them as [VERIFY] unless the release itself is the cited link.

---

## 1. Demand picture: forecasts, interconnection queues, utility and hyperscaler capex, hyperscaler power deals, equipment lead times and backlogs (2026)

### Takeaway
Demand signals stayed at record strength through Q3 2026. The IEA expects data-center electricity use to roughly double to about 950–1,000 TWh by 2030. BNEF raised its 2035 US data-center forecast to 194 GW (July 2026). ERCOT's large-load queue reached about 474 GW. PJM's 2028/29 auction again cleared at the cap and came up 6.8 GW short. Equipment is now the binding constraint: GE Vernova's gas backlog plus slot reservations is 122 GW, Siemens Energy's backlog is €164bn, and large-transformer lead times run 2.5–4+ years. The main caveat is that forecasts vary widely and request-based queues and plans (more than 115 GW of behind-the-meter gas planned vs 4.9 GW operating) far exceed what can physically be built.

### Cited Findings

**A. Data-center electricity demand forecasts**
- IEA (Energy & AI update, 2026): global data-centre electricity use ~485 TWh in 2025 → ~950 TWh in 2030 (~3% of global electricity demand). The central projection stays close to the 2025 report's path, and the IEA sees possible upside in the mid-to-long term — [IEA executive summary](https://iea.org/reports/key-questions-on-energy-and-ai/executive-summary)
- IEA (2026): electricity use by AI-focused data centres surged ~50% in 2025, and AI-focused DC power use is "poised to triple" by 2030 — [IEA news](https://iea.org/news/data-centre-electricity-use-surged-in-2025-even-with-tightening-bottlenecks-driving-a-scramble-for-solutions)
- IEA World Energy Outlook 2026 (19 Nov 2026), via press coverage: data-centre use doubles to ~1,000 TWh by 2030 in the Stated Policies Scenario [SECONDARY] — [Euronews, 19 Nov 2026](https://www.euronews.com/2026/11/19/data-centre-energy-consumption-could-double-by-2030-straining-grids-iea-warns)
- Gartner (10 Jun 2026): global DC electricity 447 TWh (2025) → 565 TWh (2026), +26%; >1,200 TWh by 2030 — [Gartner press release](https://www.gartner.com/en/newsroom/press-releases/2026-06-10-gartner-says-data-center-electricity-demand-to-grow-26-percent-in-2026)
- TrendForce (16 Sep 2026): global DC power-demand capacity 161 GW in 2026 (+~31% YoY). It projects a global supply-demand gap of 268 GW by 2030 (as summarized) — [TrendForce](https://www.trendforce.com/presscenter/news/20260916-13237.html)
- BNEF (July 2026, via secondary reports): US DC demand 194 GW by 2035. That is +83% vs its Dec-2025 forecast of 106 GW, which was itself 36% above the Apr-2025 forecast (~78 GW), so the 2035 figure is ~2.5x higher in 15 months. DCs would be ~20% of US electricity consumption in 2035 vs 5.9% today. The record for DC capacity connected to the grid in one year is 7.1 GW, and BNEF's base case shows a 19 GW shortfall by 2035 even with on-site gas [SECONDARY] — [Bloomberg Law](https://news.bloomberglaw.com/business-and-practice/data-centers-on-track-to-suck-up-a-fifth-of-us-power-use-by-2035); [Tom's Hardware](https://www.tomshardware.com/tech-industry/data-centers/bnef-nearly-doubles-its-us-data-center-power-forecast-to-194gw); Dec-2025 figure: [Utility Dive](https://www.utilitydive.com/news/us-data-center-power-demand-could-reach-106-gw-by-2035-bloombergnef/806972/); [Bloomberg, 1 Dec 2025](https://www.bloomberg.com/news/articles/2025-12-01/what-ai-bubble-bnef-outlook-for-data-center-power-use-rises-36)
- Goldman Sachs (publication date not confirmed): US DC power demand 31 GW (2025) → 66 GW (2027). About 60% of capacity scheduled for next year is expected to arrive on time, falling to ~50% over two years — [Goldman Sachs](https://www.goldmansachs.com/insights/articles/us-data-center-power-demand-projected-to-double-by-2027)
- S&P Global 451 Research (Oct 2025) [STALE]: US DC demand 75.8 GW (2026), 108 GW (2028), 134.4 GW (2030) — [S&P Global](https://www.spglobal.com/energy/en/news-research/latest-news/electric-power/101425-data-center-grid-power-demand-to-rise-22-in-2025-nearly-triple-by-2030)
- Grid Strategies (18 Nov 2025) [STALE — no 2026 edition found]: 166 GW of US peak-load growth by 2030, of which ~90 GW is linked to data centers (~6x the "flat" 2022 forecast). The firm itself warns DC figures may be overstated, and a Feb-2026 NASEO presentation cites alternative benchmarks of ~60–65 GW — [Grid Strategies report](https://gridstrategiesllc.com/wp-content/uploads/Grid-Strategies-National-Load-Growth-Report-2025.pdf?stream=top); [NASEO presentation](https://energyoutlook2026.naseo.org/data/energymeetings/presentations/John%20Wilson.pdf); [project page](https://gridstrategiesllc.com/project/load-growth-forecast/)
- EIA STEO (10 Nov 2026):
  - Commercial-sector sales (the sector that includes DCs) +2.4% in 2026 and +4.3% in 2027, after +2.4% in 2025. West South Central (incl. Texas) commercial sales +10 BkWh (2026) and +33 BkWh (2027) — [EIA STEO electricity](https://www.eia.gov/outlooks/steo/report/elec_coal_renew.php?)
  - Total US consumption 4,216 BkWh (2025) → 4,306 (2026) → 4,371 (2027) [SECONDARY] — [energynews.pro](https://energynews.pro/en/eia-forecasts-record-us-electricity-consumption-in-2026-and-2027)
  - Utility Dive cites 2.2%/5.3% commercial growth, possibly from a different edition [CONFLICT] — [Utility Dive](https://www.utilitydive.com/news/as-coal-burn-declines-rising-power-demand-will-be-primarily-met-by-renewab/874315/)
  - Next STEO is due 8 Dec 2026 — [letsdatascience summary](https://letsdatascience.com/news/eia-forecasts-record-us-electricity-demand-through-2027-0bbee083)
- LBNL published an "August update" literature review of large-load forecasts (file dated 2026-07). It was located but not read — [LBNL PDF](https://eta-publications.lbl.gov/sites/default/files/2026-07/lbnl_lllreview_august_update_final.pdf)

**B. Interconnection queues, capacity markets, regulation**
- ERCOT large-load queue:
  - ~474 GW seeking interconnection, ~90% data centers (slide dated 28 Jul 2026) — [ERCOT Senate panel, 29 Jul 2026](https://www.ercot.com/files/docs/2026/07/29/ERCOT-Senate-July-29-Panel-1-Assessing-The-Grid.pdf)
  - Trajectory: ~63 GW (end-2024) → >233 GW (Dec 2025) → ~410 GW (Mar 2026) → 438 GW (Jun 2026). The PUCT approved a batch-study process on 18 Jun 2026 — [ERCOT batch process](https://www.ercot.com/files/docs/2026/06/18/ERCOT-Trending-Topic-New-Batch-Connection-Process-for-Large-Electricity-Users.pdf); [ERCOT Apr-2026 update](https://www.ercot.com/files/docs/2026/04/01/ERCOT_LargeLoad_Update_April2026_B-C_-Hearing.pdf); [Latitude Media](https://www.latitudemedia.com/news/ercots-large-load-queue-has-nearly-quadrupled-in-a-single-year/)
  - These are requests, not firm projects, and load requests carry no standardized transparency requirements — [Texas Tribune, Jun 2026](https://www.texastribune.org/2026/06/17/texas-ercot-data-center-energy-grid/)
- Southeast: large-load interconnection requests exceed 200 GW (~8 Bcf/d gas-equivalent), per the Kinder Morgan CEO on the Q3-2026 call (Oct 2026) — [NGI](https://naturalgasintel.com/news/kinder-morgan-backlog-surges-on-ai-data-centers-southeast-power-demand/)
- PJM 2028/29 Base Residual Auction (14 Jul 2026):
  - Cleared at the FERC-approved cap of $325/MW-day RTO-wide (2027/28 cap: $333.44); uncapped price would have been ~$554.72. Procured 138,318 MW UCAP at a total cost of $16.4bn — [PJM release](https://www.pjm.com/-/media/DotCom/about-pjm/newsroom/2026-releases/20260714-pjm-capacity-auction-procures-138318-mw-of-generation-resources.pdf)
  - 6,831 MW short of the reliability requirement (prior auction ~6,500 MW short); reserve margin 14.4% vs the 20% IRM; only 525 MW UCAP of new generation/uprates cleared — [Datacentres.com](https://www.datacentres.com/news/pjm-2028-2029-capacity-auction-short-of-reliability-requirement); [SYSO](https://www.sysotechnologies.com/2026/07/16/pjm-2028-2029-bra-results/)
  - PJM's president reportedly attributed ~38% (~$6.3bn) of the cost to data centers [SECONDARY] — same sources
- FERC (18 Jun 2026): show-cause orders to the six RTO/ISOs to "defend or revise" large-load interconnection tariffs. The orders require consideration of advanced transmission technologies and GETs, including dynamic line ratings — [FERC, Commissioner Rosner remarks](https://www.ferc.gov/news-events/news/commissioner-rosners-remarks-large-load-show-cause-orders-e-7-e-12-june-18-2026); [Renewable Energy World](https://www.renewableenergyworld.com/energy-business/policy-and-regulation/ferc-takes-historic-action-orders-us-grid-operators-to-defend-or-revise-large-load-interconnection-tariffs/)
- Utility large-load pipelines (Q3 2026):
  - Dominion: 54.9 GW of DC capacity in contracting stages (+6.3 GW vs Dec 2025): ELOA 32.8 GW, CLOA 9.8 GW, ESA 12.2 GW. ESA is the most binding stage — [Investing.com, Dominion Q3 slides](https://in.investing.com/news/stock-market-news/dominion-energy-q3-2026-slides-data-center-growth-wind-progress-93CH-5669824)
  - Southern: 21 GW signed large-load contracts plus ~7 GW in late-stage negotiation — [Yahoo Finance](https://finance.yahoo.com/energy/articles/southern-co-q3-2026-earnings-031904789.html)
  - AEP: 15 GW of new load commitments signed in Q3. Incremental contracted load is expected to reach 84 GW by 2031 [SECONDARY][VERIFY] — [Discovery Alert](https://discoveryalert.com/news/aep-capital-plan-100-billion-data-center-october-2026/)
  - NextEra: >20 GW of "advanced" large-load projects, of which >18 GW is gas-fired generation — [NEE Q3 slides](https://www.investor.nexteraenergy.com/~/media/Files/N/NEE-IR/reports-and-fillings/quarterly-earnings/2026/Q3%202026/Q3%202026%20Earnings%20Slides_v%20F.pdf)
  - Xcel: expects ESAs for +1 GW of DC load by end-2026 and +3 GW by end-2027 — [Yahoo Finance](https://finance.yahoo.com/energy/articles/xcel-energy-xel-said-q3-031404247.html)
- Attrition signal: earlier in 2026 Southern reported 14.3 GW of DC projects withdrawn, a net 6 GW queue decline [STALE: pre-Q3][VERIFY] — [SEC filing surfaced by search](https://www.sec.gov/Archives/edgar/data/92122/000009212226000021/so-20260323.htm)

**C. Utility and hyperscaler capex**
- AEP: five-year capex raised to $100bn from $78bn, incl. ~$37bn for transmission (Q3 2026, ~28 Oct). Returns still depend on pending regulatory approvals [SECONDARY] — [Discovery Alert](https://discoveryalert.com/news/aep-capital-plan-100-billion-data-center-october-2026/); [AEP Q3 8-K](https://www.sec.gov/Archives/edgar/data/4904/000000490426000069/a3q20268kpressreleaseex991.htm)
- Southern: $81bn base plan + ~$4bn incremental (≈$85bn). Management said the plan "could potentially approach $100 billion over a five-year period" (Q3 call, early Nov 2026) — [Yahoo Finance](https://finance.yahoo.com/energy/articles/southern-co-q3-2026-earnings-031904789.html); [Motley Fool transcript](https://www.fool.com/earnings/call-transcripts/2026/11/05/southern-co-so-q3-2026-earnings-call-transcript/)
- Dominion: ~$65bn five-year capex through 2030 maintained. CVOW offshore wind budget is $11.65bn, with ~$10.1bn invested through 30 Sep 2026 [SECONDARY] — [Investing.com transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-dominion-energy-tops-q3-2026-estimates-raises-outlook-93CH-4989456); [Motley Fool](https://www.fool.com/earnings/takeaways/2026/11/02/dominion-energy-3-key-takeaways-for-long-term-investors/)
- Xcel: $70bn base plan for 2027–2031 targeting ~11% rate-base CAGR, not dependent on new DC signings. More than $10bn of potential incremental investment, mostly for DCs and transmission (29 Oct 2026) — [Investing.com](https://in.investing.com/news/stock-market-news/xcel-energy-q3-2026-slides-70b-plan-targets-11-rate-base-growth-93CH-5670074); [Xcel Q3 presentation](https://s202.q4cdn.com/586283047/files/content_files/Xcel-Energy-Earnings-Presentation-Q3-2026.pdf)
- JPMorgan pegs the US grid fix at ~$1 trillion (20 Nov 2026) — [Fortune](https://fortune.com/2026/11/20/transformer-shortage-power-grid-johns-hopkins-study)
- Hyperscaler capex for calendar 2026 (guidance after Q3 reports, per third-party trackers) [SECONDARY]:
  - Amazon ~$220bn (29 Oct 2026)
  - Alphabet $195–205bn (raised from $180–190bn); the CFO said 2027 capex will "rise significantly"
  - Microsoft ~$170bn, trimmed from ~$175bn on third-party AI-chip delays that push capacity into 1H 2027. FQ1-27 capex >$50bn, and FY27 capex is expected to grow
  - Meta $135–145bn (low end raised); no 2027 figure given
  - Combined ~$720–745bn (midpoint ~$730bn). 2027 consensus is ~$934.5bn (+~28%)
  - Sources: [YieldTheory 2026 tracker](https://www.yieldtheory.app/research/hyperscaler-ai-capex-tracker-2026); [YieldTheory 2027](https://www.yieldtheory.app/research/hyperscaler-capex-2027-forecast); [Luminix](https://www.useluminix.com/reports/industry-analysis/hyperscaler-capex-q3-2026)

**D. Hyperscaler power deals**
- Nuclear, aggregate: trackers count ~9.8 GW across 13 hyperscaler nuclear projects as of mid-2026. Meta is the largest cumulative buyer (~6.6 GW), followed by Amazon, Google and Microsoft. Most new SMR capacity arrives in the early 2030s [SECONDARY] — [presenc.ai tracker](https://presenc.ai/research/hyperscaler-nuclear-ppa-tracker-2026); context: [Carnegie Endowment, Jun 2026](https://carnegieendowment.org/research/2026/06/beyond-the-hype-assessing-hyperscaler-nuclear-commitments-against-us-energy-realities)
- Meta (Jan 2026): 20-year PPA with Vistra for 2.6 GW from life extensions and uprates at Ohio/Pennsylvania nuclear plants. Meta's TerraPower and Oklo deals together could add ~4 GW of new capacity [SECONDARY] — [Carnegie](https://carnegieendowment.org/research/2026/06/beyond-the-hype-assessing-hyperscaler-nuclear-commitments-against-us-energy-realities); [presenc.ai](https://presenc.ai/research/hyperscaler-nuclear-ppa-tracker-2026)
- Amazon/AWS:
  - Vistra Comanche Peak: 20-year PPA (options to extend up to 20 more years) for 1,200 MW. Deliveries start Q4 2027 and ramp to full by 2032 (VST 10-Q, Q3 2026) — [Vistra 10-Q](https://www.sec.gov/Archives/edgar/data/0001692819/000169281926000025/vistra-20260930.htm)
  - Talen: supply up to 1.9 GW through at least 2042 — [presenc.ai](https://presenc.ai/research/hyperscaler-nuclear-ppa-tracker-2026)
  - Constellation: ~190 MW Calvert Cliffs uprate deal [SECONDARY] — same
- Microsoft–Constellation Crane (TMI-1) restart: 20-year deal, commercial operation targeted 2H 2027 (one source); "$16bn" value [SECONDARY] — [presenc.ai](https://presenc.ai/research/hyperscaler-nuclear-ppa-tracker-2026)
- Google:
  - Kairos: up to 500 MW (6–7 units), first reactor targeted 2030 [SECONDARY] — [presenc.ai](https://presenc.ai/research/hyperscaler-nuclear-ppa-tracker-2026)
  - Constellation: ~890 MW of new (uprate) capacity across 11 units; the 2026 CEG deals with Google and Amazon pay for uprates rather than restarts [SECONDARY] — same
  - NextEra Duane Arnold (615 MW) restart: on track for no later than Q1 2029; DOE loan of up to $1.9bn closed (21 Oct 2026) — [NEE Q3 slides](https://www.investor.nexteraenergy.com/~/media/Files/N/NEE-IR/reports-and-fillings/quarterly-earnings/2026/Q3%202026/Q3%202026%20Earnings%20Slides_v%20F.pdf)
- Constellation (Calpine) DC deals in 2026:
  - CyrusOne Freestone: new 380 MW agreement plus an exclusive agreement for a 380 MW Phase 2, on top of 400 MW at Thad Hill (2H 2025)
  - A 20-year, 270 MW Peak+ agreement
  - A "long-term collaboration" with Google supporting new nuclear capacity (Q3 2026)
  - Sources: [CEG Q3 10-Q](https://www.sec.gov/Archives/edgar/data/0001868275/000186827526000119/ceg-20260930.htm); [GuruFocus](https://www.gurufocus.com/news/9184733/constellation-energy-corp-reports-strong-q3-2026-gaap-eps-at-519-and-revenue-of-955-billion-exceed-estimates)
- Behind-the-meter (BTM) gas:
  - Cleanview, via MIT Technology Review (24 Nov 2026): >100 projects totaling >115 GW of BTM gas planned for DCs as of Oct 2026, but only 4.9 GW operating and 15.8 GW under construction. Very few will use combined-cycle turbines — [MIT Technology Review](https://www.technologyreview.com/2026/11/24/1149622/data-centers-natural-gas/)
  - RBC (May 2026) tallies ~101 GW announced — [RBC Capital Markets](https://www.rbccm.com/en/insights/2026/05/natural-gas-powers-the-data-center-boom)
  - xAI Colossus 1 & 2 (Memphis): ~1,500 MW of the ~2 GW of BTM capacity online as of mid-2026 [low-authority site-selection guide] — [Power Ready Sites](https://powerreadysites.com/data-center-onsite-power-and-natural-gas)
  - Pacifico Energy Fort Stockton, TX: 1,300 MW planned with 21 Siemens turbines, potentially >6 GW. Meta New Albany, OH (built by Williams): 400 MW in two 200 MW plants (per search summary of MIT TR / Industrial Info coverage) — [MIT Technology Review](https://www.technologyreview.com/2026/11/24/1149622/data-centers-natural-gas/); [Industrial Info](https://www.industrialinfo.com/news/article/behind-the-meter-power-generation-increasingly-prevalent-at-us-data-centers--358873)
- Williams "Power Innovation" (Q3 2026, 3 Nov):
  - ~$9.6bn committed across six announced power projects, plus 6+ GW of additional potential projects in the backlog
  - $5.9bn of equipment commitments
  - Blackstone-led partnership provides $5.34bn for a 49% stake in five projects
  - Socrates (Meta) phase 2 is coming online ahead of schedule and on budget
  - Sources: [Williams Q3 8-K](https://www.sec.gov/Archives/edgar/data/0000107263/000010726326000035/wmb_20260930xer.htm); [Investing.com](https://www.investing.com/news/company-news/williams-q3-2026-slides-record-ebitda-11-growth-target-through-2030-93CH-4995914); [Yahoo Finance](https://finance.yahoo.com/energy/articles/williams-companies-inc-q3-2026-133000633.html)
- Counter-signal: Mitsubishi Heavy's CEO (Nov 2026) says off-grid power costs will push data centers back to utilities — [Utility Dive](https://www.utilitydive.com/news/data-centers-mitsubishi-gas-turbines-earnings/875146/); [MLQ](https://mlq.ai/news/mitsubishi-heavy-ceo-says-off-grid-power-costs-will-push-data-centers-back-to-utilities/)
- Direct gas-supply deals:
  - Energy Transfer–CloudBurst: up to 450,000 MMBtu/d firm, subject to the customer's FID [STALE: 2025] — [ET release](https://ir.energytransfer.com/news-releases/news-release-details/energy-transfer-and-cloudburst-sign-agreement-natural-gas-supply)
  - ET has begun deliveries to an Oracle DC — [NGI](https://naturalgasintel.com/news/energy-transfer-launches-natural-gas-deliveries-to-oracle-data-center/)
  - ET supplying ~900,000 Mcf/d to three DCs (article ~late Aug 2026) [SECONDARY] — [Yahoo Finance](https://finance.yahoo.com/energy/articles/energy-transfer-quietly-becoming-one-193501261.html)
  - EQT: sole supplier to the Homer City campus, up to 665,000 MMBtu/d (agreement in principle) [STALE: 2025] — [P&GJ](https://pgjonline.com/news/2025/july/eqt-to-supply-natural-gas-for-data-center-campus-in-pennsylvania)
- Storage for DCs:
  - Xcel to install a 300 MW / 30 GWh Form Energy iron-air system for a Google DC in Pine Island, MN (phased 2028–2031 per one source) — [Energy-Storage.news](https://www.energy-storage.news/google-minnesota-data-centre-energy-deal-includes-30gwh-multi-day-iron-air-batteries-from-form-energy/)
  - Form–Crusoe: 12 GWh, deliveries from 2027 — [Energy-Storage.news](https://www.energy-storage.news/form-energy-signs-12gwh-agreement-to-supply-multi-day-iron-air-batteries-to-new-us-ai-data-centres/)

**E. Equipment backlogs and lead times**
- GE Vernova (Q3 2026, 28 Oct 2026):
  - Gas Power backlog + slot-reservation agreements rose from 116 GW to 122 GW in the quarter, with a target of ≥130 GW by year-end 2026 — [GEV Q3 release](https://www.sec.gov/Archives/edgar/data/0001996810/000199681026000162/gevpressrelease3q26.htm)
  - The Q2 release outlined production rising to a ~20 GW/yr gas-turbine run-rate by Q3 2026 and 24 GW in 2028, with actions under way toward 30 GW in 2030 (as summarized) [VERIFY] — [GEV Q2 release](https://www.sec.gov/Archives/edgar/data/0001996810/000199681026000147/gevpressrelease2q26.htm)
- Siemens Energy (FY ending Sept 2026, reported 11 Nov 2026):
  - 42 GW of gas-turbine orders in FY26 and 65 GW of firm GT backlog. About 39 GW of slot reservations is expected to convert to firm orders in FY27; it is unclear whether these sit inside or alongside the 65 GW — [Investing.com, FY26 slides](https://www.investing.com/news/company-news/siemens-energy-fy26-slides-record-results-2022-margin-target-by-2030-93CH-5018478)
  - Earlier (30 Jun 2026): GT backlog 69 GW after booking 15 GW and shipping 6 in the quarter; lead times "three years or more" — [OilPrice](https://oilprice.com/Energy/Energy-General/The-Gas-Turbine-Shortage-Just-Became-AIs-Biggest-Constraint.amp.html)
- Mitsubishi Heavy (1H FY2026, Nov 2026):
  - 8 GW of large-frame GT orders in the half, vs 16 GW in all of FY2025; large-frame backlog ~37 GW (35 GW at Q1) — [Utility Dive](https://www.utilitydive.com/news/data-centers-mitsubishi-gas-turbines-earnings/875146/); [MLQ](https://mlq.ai/news/mitsubishi-heavy-ceo-says-off-grid-power-costs-will-push-data-centers-back-to-utilities/); Q1: [Utility Dive](https://www.utilitydive.com/news/mitsubishi-gas-turbine-backlog-earnings/827761/)
  - Spending ~$3.1bn to double production capacity by 2030, mostly via automation at existing US plants. Management said it will be selective and will not immediately seek double the orders — same sources
- Supply response: Ansaldo is re-entering the US gas-turbine market as the equipment crunch widens the supplier field — [POWER](https://www.powermag.com/ansaldo-us-gas-turbine-market-equipment-crunch/)
- Caterpillar (Q3 2026): order backlog ~$78bn, almost double a year earlier. It is expanding production of large reciprocating engines and turbines for DC demand — [Utility Dive](https://www.utilitydive.com/news/caterpillar-posts-highest-sales-quarter-ever-data-centers-q3-2026/873586/)
- Cummins (Q3 2026): added generator capacity starts coming online in 2027, with most of the expansion around 2028 — [Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/cummins-q3-earnings-call-highlights-221433740.html)
- Large power transformers (LPTs):
  - Wood Mackenzie Q2-2025 survey: LPT delivery averaged 128 weeks and generator step-up units 144 weeks [STALE] — [Orban Labs summary](https://orbanlabs.com/journal/069-transformer-lead-times-4-5-years/)
  - PwC (11 May 2026): lead times for high-capacity units up to four years — [pv magazine USA](https://pv-magazine-usa.com/2026/05/11/u-s-transformer-market-faces-severe-supply-constraints-as-lead-times-extend-to-four-years/)
  - Transformer Magazine (Aug 2026): typical LPT procurement 30–36 months (vs 12–18 months historically), EHV units up to 60 months. A National Laboratory of the Rockies summary (Jul 2026, hydro-focused) gives 2.5–3 years for a 100 MVA LPT. Domestic production met only ~20% of LPT demand and ~50% of distribution-transformer demand in 2025 — [Transformer Magazine](https://transformer-magazine.com/news/transformer-shortages-challenge-us-hydropower/)
  - Johns Hopkins study (20 Nov 2026): lead times quadrupled in four years (from ~6 months to >2 years); a trade disruption could push the transformer shortfall to 25% — [Fortune](https://fortune.com/2026/11/20/transformer-shortage-power-grid-johns-hopkins-study)
  - Coil-winding labor may be the real constraint (trade-press claim) — [Manufacturing Mag](https://www.manufacturingmag.com/article/grid-transformer-shortage-three-year-backlog-coil-winding-labor)
- Switchgear and electrical distribution (Q3 2026; details in §2):
  - Eaton: Electrical Americas backlog ~$16bn (+33%); Electrical sector backlog >$20bn (+46%) — [Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/eaton-q3-earnings-call-highlights-051410047.html)
  - Powell: backlog $2.7bn (+96% YoY) at 30 Sep 2026 — [Powell release](https://www.sec.gov/Archives/edgar/data/80420/000008042026000139/ex991-powlq4xfy2026earning.htm)
- Transmission build rate: the US is building only ~10% of the power lines it needs (Nov 2026) — [ScienceDaily](https://www.sciencedaily.com/releases/2026/11/261123005339.htm). DOE's July-2026 draft National Transmission Needs Study cites DC and manufacturing load growth — [DOE](https://www.energy.gov/documents/national-transmission-needs-study-draft-july-2026)

### Inferences
- Forecast dispersion is the core analytical problem. For 2030, US DC load estimates range from ~60–65 GW (Grid Strategies' alternative benchmarks) to ~90 GW (utility-based) to ~134 GW (S&P 451, stale). For 2035, BNEF has 194 GW. Request-based queues (ERCOT 474 GW; Southeast >200 GW) and BTM plans (>115 GW) are option value, not demand. Realized growth is capped by the grid's record ~7 GW/yr of DC connections, turbine and transformer slots, and labor. The bottleneck therefore lengthens the cycle more than it raises its peak, which supports multi-year visibility for equipment OEMs and EPCs.
- Pricing power sits where capacity is sold out for years: heavy-duty gas turbines (GEV, Siemens Energy, MHI, each with 3+ year lead times), MV/HV electrical gear and transformers (ETN, HUBB, POWL, HD Hyundai Electric, ABB, Schneider), and grid EPC (PWR). Siemens Energy says DC customers are <10% of its backlog, so turbine demand is broader than AI. That should cushion an AI-capex pause, but it also means less "AI torque" than the stock narrative implies.
- Hyperscaler 2027 capex consensus (+~28% to ~$935bn) still underwrites orders into 2027–2028. Microsoft trimming its 2026 figure because of chip delays shows that timing slips can hit quarterly order flow at suppliers.
- PJM clearing at the cap twice, with a 6.8 GW shortfall and ~38% of costs attributed to DCs, is a political-economy flashpoint. Expect more pressure on cost allocation, co-location and large-load tariffs (FERC show-cause orders), which is a risk for merchant IPP upside (CEG, TLN, VST's PJM assets).
- On-site generation is real but early (4.9 GW operating vs >115 GW planned). It is OEM-constrained, which favors recips, aeroderivatives, gensets and fuel cells (CAT, CMI, BE) and midstream-integrated developers (WMB). The MHI CEO's view suggests BTM may be a bridge until grid interconnections arrive.

### Gaps
- EPRI's 2026 load/DC forecast was not retrieved. The LBNL Aug-2026 large-load review was located but not read, and LBNL "Queued Up" 2026 generation-queue statistics were not retrieved.
- No 2026 edition of Grid Strategies' national load forecast was found (latest is Nov 2025).
- The EEI aggregate investor-owned-utility capex outlook for 2026–2030 was not retrieved; an EEI Oct-2026 large-load project list exists but was not read.
- Gas-turbine pricing ($/kW) and switchgear lead times in weeks were not found for 2026.
- Goldman Sachs forecast date unconfirmed; S&P 451 forecast is from Oct 2025.
- IEA "Electricity 2026" headline numbers were not extracted ([IEA page](https://iea.org/reports/electricity-2026/executive-summary)).

---

## 2. Companies: market data, Q3-2026 results, guidance, backlog, valuation and risks

### Takeaway
Q3-2026 results were almost uniformly strong, with record orders and backlogs and guidance raises at GEV, Siemens Energy, CAT, VRT, ETN, PWR, HUBB, POWL, NVT, TT, JCI, MOD, AAON, BE, CEG, VST and TLN. Even so, the sector de-rated sharply in November 2026. The market data that could be sourced shows:
- GE Vernova: ~$201bn market cap, +17% YTD at 16 Nov, ~30–34x forward P/E (down from ~63x at the June peak)
- Bloom: +146% YTD at 3 Nov, ~39–43x forward P/E, $46–57bn market cap
- Laggards: CEG −28% YTD / −27% over one year, NRG −42% YTD, VST ~−17% YTD
- Pre-revenue SMR developers: OKLO ~−75%, SMR ~−78%, NNE ~−48% YTD
- Benchmark: S&P 500 +6.7% YTD and +12.0% over one year (24 Nov)

Fundamentals and share prices have clearly diverged.

### Cited Findings

**A. Market-data snapshot (all that could be sourced; refresh live)**

| Ticker | Price / market cap (date) | YTD 2026 (date) | 1-yr | Forward multiple (date) | Source |
|---|---|---|---|---|---|
| Benchmark S&P 500 (SPY) | — | +6.7% (24 Nov) | +12.0% (24 Nov) | — | [Trefis](https://www.trefis.com/stock/ceg/articles/628278/is-constellation-energy-stocks-fall-a-bargain-or-a-warning/2026-11-24?.tsrc=rss) |
| GEV | ~$763.57; mkt cap ~$201bn (16 Nov). Separately $699.33 after a −12.9% week (Investing.com, mid-Nov) | +16.8% (16 Nov, from $653.57); "+18%" (TIKR, Nov) | n/f | Fwd P/E 31.5x (GuruFocus, 11 Nov); ~34x (TIKR, 10 Nov); ~63x at June peak; trailing 17.8x (Investing.com) [CONFLICT on dates] | [Admiral Markets](https://admiralmarkets.com/education/articles/shares/ge-vernova-stock); [GuruFocus](https://www.gurufocus.com/term/forward-pe-ratio/GEV); [TIKR](https://www.tikr.com/blog/ge-vernova-is-up-18-in-2026-after-three-guidance-raises-take-profits-or-buy-more); [Investing.com](https://www.investing.com/news/stock-market-news/ai-data-centers-need-power-yet-ge-vernova-sank-13-this-week-5045599) |
| BE | Mkt cap $46.24bn (25 Nov page; day range $136.88–155.55); ~$56.76bn (14 Nov) [CONFLICT] | +146% (3 Nov close); "more than doubled" (14 Nov) | n/f | ~43x fwd (3 Nov); ~39x next-year EPS (14 Nov); 3-yr avg 76x; ~74x in Aug **[HIGH VALUATION]** | [TIKR](https://www.tikr.com/blog/bloom-energy-is-up-146-in-2026-take-profits-or-buy-more); [Motley Fool, 14 Nov](https://www.fool.com/investing/2026/11/14/bloom-energy-stock-has-more-than-doubled-for-2-years-running-i-d-keep-buying-it-bit-by-bit/); [Motley Fool, 25 Nov](https://fool.com/investing/2026/11/25/this-ai-power-stock-more-than-doubled-its-revenue-and-still-burned-cash-which-number-matters-more); [BigGo](https://finance.biggo.com/news/7e30b32f-88e9-48ee-81c9-653a07fe9d2e) |
| CEG | n/f | −28.3% (24 Nov); −21.5% (10 Nov) | −26.8% TR (24 Nov) | 2.6x TTM sales (23 Nov) | [Trefis, 24 Nov](https://www.trefis.com/stock/ceg/articles/628278/is-constellation-energy-stocks-fall-a-bargain-or-a-warning/2026-11-24?.tsrc=rss) |
| NRG | n/f | −42.1% (24 Nov); +11.3% on 23 Nov | n/f | 0.6x TTM sales | [Trefis](https://www.trefis.com/stock/nrg/articles/628623/why-did-nrg-stock-jump/2026-11-24) |
| VST | $120.29 close (4 Nov, −13.8% that day) | ~−17% (post-Q3, Nov) | n/f | n/f | [Bellwize](https://bellwize.com/stocks/2026-11-05-vst-democratic-sweep-power-selloff/); [TIKR](https://www.tikr.com/blog/vistra-is-still-down-17-this-year-did-earnings-just-mark-the-bottom) |
| TLN | n/f | n/f | n/f | ~10x fwd P/E (~10 Nov) [single source] | [Motley Fool](https://www.fool.com/investing/2026/11/10/constellation-and-vistra-get-the-headlines-these-2/) |
| OKLO **[PRE-REVENUE]** | ~$17.60 (25 Nov a.m.); $19.45 (25 Nov, 1:05 pm). ~$8bn mkt cap at ~$49 (Jul 2026) | ~−75% (25 Nov); −68% (early Nov) | n/f | n/m | [24/7 Wall St., 25 Nov](https://247wallst.com/investing/2026/11/25/oklo-and-nuscale-power-retreat-8-as-ai-power-selloff-deepens-energy-fuels-drops-6/); [FourWeekMBA](https://fourweekmba.com/ai-power-stocks-give-back-55-of-monday-oklo-below-friday/); [24/7 Wall St., Jul](https://247wallst.com/investing/2026/07/10/one-nuclear-energy-stock-with-a-100-upside-potential/) |
| SMR **[PRE-REVENUE]** | $3.05 (25 Nov) | ~−78% (25 Nov); −61% (9 Nov) | n/f | n/m | [24/7 Wall St., 25 Nov](https://247wallst.com/investing/2026/11/25/oklo-and-nuscale-power-retreat-8-as-ai-power-selloff-deepens-energy-fuels-drops-6/); [24/7 Wall St., 9 Nov](https://247wallst.com/investing/2026/11/09/nuscale-is-still-down-61-in-2026-did-today-mark-the-bottom-for-smr-stock/) |
| NNE **[PRE-REVENUE]** | $12.51 (9 Nov) | −48% (9 Nov) | n/f | n/m | [24/7 Wall St. (as summarized)](https://247wallst.com/investing/2026/11/09/nuscale-is-still-down-61-in-2026-did-today-mark-the-bottom-for-smr-stock/) |
| VRT | −12.9% on 4 Nov; −12% / −18% in week to 10 Nov [CONFLICT] | n/f | n/f | n/f | [Bellwize](https://bellwize.com/stocks/2026-11-05-vst-democratic-sweep-power-selloff/); [TIKR](https://www.tikr.com/blog/ge-vernova-sinks-13-vertiv-down-18-in-a-week-as-data-center-backlash-hits-ai-power) |
| NVT | $125.98 (30 Oct, −8.8% on results day) | n/f | n/f | n/f | [Investing.com](https://in.investing.com/news/stock-market-news/earnings-call-transcript-nvent-tops-q3-2026-estimates-but-shares-fall-93CH-5670029) |
| FCX / SCCO | FCX $47.73 (−3.98%); SCCO $136.85 (−4.51%) on 24 Nov, both well off August peaks | n/f | n/f | n/f | [Rio Times](https://www.riotimesonline.com/copper-markets-latam-tuesday-november-24-2026/) |

n/f = not found in this research round; n/m = not meaningful.

**B. Gas turbines, engines and on-site generation**

GE Vernova (GEV) — Q3 2026, 28 Oct
- Gas backlog plus slot reservations 116 → 122 GW; target ≥130 GW at year-end 2026 — [GEV Q3 release](https://www.sec.gov/Archives/edgar/data/0001996810/000199681026000162/gevpressrelease3q26.htm)
- A search summary of the release cites a "$42.2bn equipment backlog"; scope unclear, likely Gas Power equipment [VERIFY] — same
- Q3 orders reportedly +96% to ~$29bn, with total backlog ~$197bn [SECONDARY][VERIFY] — [Motley Fool, 10 Nov](https://www.fool.com/investing/2026/11/10/ge-vernova-vertiv-and-bloom-energy-just-lost-10-to/); [Motley Fool, 8 Nov](https://www.fool.com/investing/2026/11/08/not-bloom-energy-not-vistra-this-ai-power-stock/)
- Buyback authorization doubled to $20bn (Nov 2026) — [Investing.com](https://www.investing.com/news/stock-market-news/ai-data-centers-need-power-yet-ge-vernova-sank-13-this-week-5045599)
- Raised guidance three times in 2026 — [TIKR](https://www.tikr.com/blog/ge-vernova-is-up-18-in-2026-after-three-guidance-raises-take-profits-or-buy-more)
- Nuclear optionality: the GE Vernova Hitachi BWRX-300 at TVA Clinch River received an NRC construction permit on 29 Sep 2026 — [ANS](https://www.ans.org/news/2026-09-29/article-8445/tva-receives-construction-permit-for-clinch-river/)
- Risk: Investing.com notes the 17.8x trailing P/E only "looks cheap if profits repeat" — [Investing.com](https://www.investing.com/news/stock-market-news/ai-data-centers-need-power-yet-ge-vernova-sank-13-this-week-5045599)

Siemens Energy (ENR.DE; OTC SMEGF) — FY2026, 11 Nov
- Orders €68.1bn (+18.8% comparable); revenue €44.2bn (+15.5%); book-to-bill 1.54 for the year, 1.16 in Q4 — [Siemens Energy release](https://www.siemens-energy.com/global/en/home/press-releases/earnings-release-q4-fy-2026--siemens-energy-reports-a-record-yea.html); [Europawire](https://news.europawire.eu/siemens-energy-posts-record-fy-2026-revenue-and-e164bn-backlog-sets-2030-margin-goal-of-20-22/eu-press-release/2026/11/11/13/46/13/187248/)
- Backlog €164bn (~€71bn service); ~85% of expected FY27 revenue already covered — [Investing.com slides](https://www.investing.com/news/company-news/siemens-energy-fy26-slides-record-results-2022-margin-target-by-2030-93CH-5018478); [Investing.com call](https://www.investing.com/news/transcripts/earnings-call-transcript-siemens-energy-shares-jump-on-record-q4-2026-results-93CH-5018439)
- DC customers <10% of backlog — [GuruFocus](https://www.gurufocus.com/news/9193800/siemens-energy-ag-smegf-q4-2026-earnings-call-highlights-record-results-eur164-billion-backlog-and-an-ambitious-2030-margin-target)
- 2030 margin target 20–22%; proposed €2.30 dividend; buybacks up to €9bn through FY2030 — [Traders Agency](https://tradersagency.com/blog/siemens-energy-posts-record-fy2026-results-targets-20-22percent-margin-by-2030-expands-buyback-by-up-to-euro9-billion)
- Gas Services margin 16.4% in FY26 with an 18–20% FY27 outlook [SECONDARY][VERIFY] — [Discovery Alert](https://discoveryalert.com/analysis/siemens-energy-backlog-data-centres-november-2026/)
- Shares jumped on the results — [Investing.com](https://www.investing.com/news/transcripts/earnings-call-transcript-siemens-energy-shares-jump-on-record-q4-2026-results-93CH-5018439)
- Market cap and multiples: not found

Mitsubishi Heavy (7011.T; OTC MHVYF) — 1H FY2026
- 8 GW of large-frame GT orders; backlog ~37 GW; ~$3.1bn to double capacity by 2030 — [Utility Dive](https://www.utilitydive.com/news/data-centers-mitsubishi-gas-turbines-earnings/875146/)
- One blog reports 19 large GTs ordered in 1H and an 83-unit backlog [low-quality source] — [note.com](https://note.com/ippan_invest/n/n0975d477d73d?hl=en)
- The same blog says shares were down ~48% from their high, hitting a YTD low on reports of "curbed" defense spending; MHI is also a defense name [low-quality source][VERIFY] — same
- Separately, MHI is investing $490m in gas-turbine capacity in Savannah, GA — [Power Engineering](https://www.power-eng.com/gas/turbines/mitsubishi-power-gas-turbine-savannah-georgia/)

Caterpillar (CAT) — Q3 2026
- Total sales $20.7bn, its "highest sales quarter ever"
- Power & Energy sales $8.78bn (+18%)
- Power Generation $3,421m (+30% vs $2,634m), driven by turbines, turbine services and large recips "primarily for data centers"
- Backlog ~$78bn (≈2x YoY)
- Sources: [Utility Dive](https://www.utilitydive.com/news/caterpillar-posts-highest-sales-quarter-ever-data-centers-q3-2026/873586/); [CAT Q3 8-K](https://www.sec.gov/Archives/edgar/data/0000018230/000001823026000052/ex991toformcat3q2026earnin.htm); [CAT 10-Q](https://www.sec.gov/Archives/edgar/data/0000018230/000001823026000057/cat-20260930.htm)

Cummins (CMI) — Q3 2026, ~5 Nov
- Revenue $9.44bn (+13.5%); Power Systems $2.29bn (+15%)
- North American power-gen revenue +22%; China power equipment +42%
- 2026 global power-gen revenue growth guidance kept at +15–25%; opened a ~$100m cooling-systems facility in Wisconsin
- Sources: [Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/cummins-q3-earnings-call-highlights-221433740.html); [Motley Fool transcript](https://www.fool.com/earnings/call-transcripts/2026/11/05/cummins-cmi-q3-2026-earnings-call-transcript/)

Bloom Energy (BE) — Q3 2026, reported ~late Oct **[HIGH VALUATION]**
- Revenue $1,235.8m (+138.1%); product revenue $1,073.6m; GAAP gross margin 33.8%; non-GAAP operating income $285.7m
- GAAP EPS $0.78; non-GAAP EPS $0.94
- 2026 revenue guidance raised to $4.4–4.6bn (~+122% at the midpoint); non-GAAP EPS $3.10–3.40; gross margin ~34%
- Added to the S&P 500
- Sources: [Bloom Q3 release](https://www.sec.gov/Archives/edgar/data/0001664703/000162828026066890/ex991_q326financialresults.htm); [Yahoo Finance](https://finance.yahoo.com/energy/articles/bloom-energy-said-q3-earnings-000417384.html)
- Cash $2.5bn; negative quarterly free cash flow weighed on the shares — [Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/bloom-energy-corp-q3-2026-090451372.html); [CryptoBriefing](https://cryptobriefing.com/bloom-energy-revenue-soars-cash-flow-dips/)
- Shares fell 13.5% in a week as investors questioned a ~$60bn valuation — [BigGo](https://finance.biggo.com/news/7e30b32f-88e9-48ee-81c9-653a07fe9d2e)
- No DC order totals were disclosed in the sources found

**C. Nuclear generators and IPPs**

Constellation (CEG) — Q3 2026, 9 Nov
- GAAP EPS $5.19; adjusted operating EPS $5.06 (vs ~$3.90 estimate); revenue $9.55bn (vs $6.57bn)
- FY26 adjusted operating EPS guidance raised and narrowed to $12.50–12.80 (originally $11.00–12.00)
- Interest expense $217m vs $134m (Calpine debt)
- Sources: [CEG Q3 release](https://www.sec.gov/Archives/edgar/data/0001868275/000186827526000116/ceg-20261109991.htm); [GuruFocus](https://www.gurufocus.com/news/9184733/constellation-energy-corp-reports-strong-q3-2026-gaap-eps-at-519-and-revenue-of-955-billion-exceed-estimates); [Trefis](https://www.trefis.com/stock/ceg/articles/625688/why-did-constellation-energy-stock-jump-over-10/2026-11-17)
- Calpine closed 7 Jan 2026 for ~$21.8bn. To meet regulatory commitments CEG is selling five PJM gas plants (~4.4 GW) to LS Power for $5.0bn — [CEG Q3 10-Q](https://www.sec.gov/Archives/edgar/data/0001868275/000186827526000119/ceg-20260930.htm)
- Shares +10.5% on 9 Nov — [Trefis](https://www.trefis.com/stock/ceg/articles/625688/why-did-constellation-energy-stock-jump-over-10/2026-11-17)
- A third-party write-up claims ~8,500 MW of long-term contracts signed in 2026 [SECONDARY, unconfirmed] — [GuruFocus](https://www.gurufocus.com/news/9184733/constellation-energy-corp-reports-strong-q3-2026-gaap-eps-at-519-and-revenue-of-955-billion-exceed-estimates)

Vistra (VST) — Q3 2026, 6 Nov
- Ongoing Operations adjusted EBITDA $2,378m (+>50% YoY); GAAP net income $1,140m, including a $559m unrealized hedge gain
- 2026 guidance: adjusted EBITDA $7.1–7.5bn; FCF before growth $4.3–4.7bn
- 2027 guidance initiated: adjusted EBITDA $7.7–8.5bn; FCF before growth $4.3–5.1bn (on 2 Nov 2026 market curves)
- Sources: [VST Q3 release](https://www.sec.gov/Archives/edgar/data/0001692819/000169281926000023/vistra-20260930xearningsre.htm); [VST Q3 presentation](https://filecache.investorroom.com/mr5ir_vistracorp_ir/349/Q3_2026_Results_Presentation_vFINAL.pdf)
- Beaver Valley and the second part of Comanche Peak are still uncontracted; Comanche Peak uprate potential is not in the outlook — [Benzinga transcript](https://www.benzinga.com/news/26/11/62991016/vistra-q3-2026-earnings-call-transcript)
- The CEO said a Texas DC moratorium "would be problematic" — same
- Management says its plans always took "a more conservative view of the AI build-out" — [Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/vistra-just-dropped-16-month-071339801.html)

Talen (TLN) — Q3 2026, 3 Nov
- GAAP net income $138m; adjusted EBITDA $669m; adjusted FCF $433m; generation 23.9 TWh (vs 11.1 TWh)
- 2026 guidance reaffirmed: adjusted EBITDA $2,050–2,200m; adjusted FCF $1,225–1,325m
- 2027 guidance: adjusted EBITDA $2,500–2,850m and adjusted FCF $1,500–1,750m (~+26–27% at midpoints)
- $1.5bn accelerated share repurchase; total buyback upsized to $3.0bn through 2028
- Susquehanna is 2,247 MW, with ~300 MW of uncontracted carbon-free capacity
- Sources: [Talen release](https://ir.talenenergy.com/news-releases/news-release-details/talen-energy-reports-third-quarter-2026-results-reaffirms-2026); [Talen Q3 presentation](https://ir.talenenergy.com/static-files/06224f65-8b56-4726-8a3c-0a4fc6aa1634)

NRG
- Held 2026 guidance; its 1.2 GW DC project remains on track — [Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/vistra-just-dropped-16-month-071339801.html)
- Fell ~13.5% on 4 Nov — [Energy News Beat](https://energynewsbeat.co/finance/chip-stocks-sink-and-texas-power-stocks-slide-did-voters-really-hit-pause-on-data-centers/)

Oklo (OKLO) — Q3 2026 **[PRE-REVENUE][SPECULATIVE]**
- Revenue ~$1.86m, mostly from ARMEC and Creative Engineers (acquired Jun 2026); net loss $41.75m (vs $29.72m); non-GAAP EPS −$0.28 vs −$0.25 consensus — [MarketScreener](https://www.marketscreener.com/news/oklo-inc-reports-earnings-results-for-the-third-quarter-and-nine-months-ended-september-30-2026-ce785fd2db8df424); [GuruFocus](https://www.gurufocus.com/news/9180960/oklo-oklo-q3-earnings-beat-expectations-amidst-execution-concerns)
- Cash and marketable securities $3,130.8m at 30 Sep, plus $81.9m restricted cash — same sources
- Raised $2.3bn via at-the-market offerings in the first nine months of 2026; first commercial power from Aurora targeted for late 2027 to early 2028 — [24/7 Wall St.](https://247wallst.com/investing/2026/11/25/prediction-oklo-stock-could-have-a-huge-year-as-nuclear-energy-demand-accelerates/); [Motley Fool](https://www.fool.com/investing/2026/11/10/ge-vernova-vertiv-and-bloom-energy-just-lost-10-to/)
- Licensing: DOE PDSA approval (Jun 2026) — [ANS](https://www.ans.org/news/2026-06-12/article-8119/oklo-secures-doe-pdsa-approval/). The NRC pre-application table shows a "Q4 CY2026" licensing-plan update dated 29 Sep 2026 with "No review requested", i.e., no Aurora-INL combined license application has been docketed. The 2020 application was denied without prejudice in 2022 — [NRC](https://www.nrc.gov/reactors/new-reactors/advanced/who-were-working-with/pre-application-activities/okla-aurora-powerhouse); [NRC Aurora page](https://www.nrc.gov/reactors/new-reactors/col/aurora-oklo.html)

NuScale (SMR) — Q3 2026 **[PRE-REVENUE][SPECULATIVE]**
- Revenue ~$0.28m (vs $8.2m); cash and investments ~$1.9bn — [NuScale release](https://www.nuscalepower.com/press-releases/2026/nuscale-power-reports-third-quarter-2026-results)
- The TVA PPA is between ENTRA1 and TVA, not NuScale. Binding module sales need a separate OEM agreement between NuScale and ENTRA1 — [Benzinga transcript](https://www.benzinga.com/news/26/11/62959728/nuscale-power-q3-2026-earnings-call-transcript)
- A $507.4m ENTRA1-related charge is dated to Q3 2026 by one source and to an earlier period by NuScale's Feb-2026 release [CONFLICT] — [FourWeekMBA](https://fourweekmba.com/ai-nuscale-paid-entra1-507m-over-a-nonbinding-tva-agreement/); [NuScale Feb-2026 8-K](https://www.sec.gov/Archives/edgar/data/1822966/000182296626000016/a20260226-earningscallpr.htm)

Nano Nuclear (NNE) **[PRE-REVENUE][SPECULATIVE]**
- −48% YTD to $12.51 (9 Nov); no fundamentals retrieved — [24/7 Wall St.](https://247wallst.com/investing/2026/11/09/nuscale-is-still-down-61-in-2026-did-today-mark-the-bottom-for-smr-stock/)

**D. Nuclear fuel cycle and uranium**

Cameco (CCJ) — Q3 2026, ~30 Oct
- Net earnings $43m
- Uranium: 5.6 Mlb delivered at an average realized $91.76/lb (vs 6.1 Mlb at $85.22)
- Westinghouse (Cameco's share): net loss $24m; adjusted EBITDA $143m (vs $124m). Nine-month adjusted EBITDA $427m vs $569m, because 2025 included a Dukovany payment
- 2026 production guidance narrowed to 19.5–20.5 Mlb (from 19.5–21.5)
- Sources: [Cameco 6-K](https://www.sec.gov/Archives/edgar/data/0001009001/000119312526439858/d106072dex991.htm); [Cameco Q3](https://www.cameco.com/invest/financial-information/quarterly-reports/2026/q3); [Investing.com](https://www.investing.com/news/company-news/cameco-narrows-2026-production-guidance-reports-lower-earnings-93CH-4986807)

Centrus (LEU) — Q3 2026, 4 Nov
- Revenue $55.5m (vs $74.9m); GAAP net income $31.6m, including a $46.4m non-cash warrant gain; adjusted net loss $9.4m
- Contingent LEU/HALEU enrichment backlog $5.4bn (from $3.0bn in Q2), of which $5.1bn is under definitive agreements; total backlog ~$7bn
- Commercial HALEU production has started on the 16-centrifuge cascade
- Centrifuges are being manufactured and shipped from Oak Ridge ~2 months ahead of plan; investor day in December 2026
- Sources: [PR Newswire](https://www.prnewswire.com/news-releases/centrus-reports-third-quarter-2026-results-302929804.html); [Centrus PDF](https://www.centrusenergy.com/wp-content/uploads/2026/11/1093554456-Centrus-3Q-earnings-release-2026-pdf.pdf); [Yahoo Finance](https://finance.yahoo.com/energy/articles/centrus-q3-profit-surges-warrant-025000355.html)

BWX Technologies (BWXT) — Q3 2026
- Revenue $952.97m (+10%); diluted EPS $1.11; adjusted EPS $1.26 (beat)
- Backlog $8,556.2m (vs $8,398.1m at 30 Jun); ~46% expected to convert to revenue by end-2027; ~$500m came with the PCG acquisition
- Cambridge, Ontario expansion adds ~50% heavy-component capacity; a prototype centrifuge test is planned by end-2026
- Shares fell after hours on the results
- Sources: [TradingView 10-Q summary](https://www.tradingview.com/news/tradingview:a7359a7f36cf4:0-bwx-technologies-3q-2026-revenue-952-97m-eps-1-11-10-q-summary/); [FourWeekMBA](https://fourweekmba.com/ai-bwxt-filing-46-of-its-8-6b-backlog-due-as-revenue-by-2027/); [MarketBeat call highlights](https://www.tradingview.com/news/marketbeat:253613180094b:0-bwx-technologies-q3-earnings-call-highlights/); [Investing.com](https://www.investing.com/news/transcripts/earnings-call-transcript-bwx-technologies-posts-q3-2026-eps-beat-shares-fall-after-hours-93CH-4993167)

Uranium prices
- Spot ~$91.50/lb (16 Nov 2026, indicative) — [MeltValue](https://meltvalue.com/uranium-price)
- Futures $89.95/lb (20 Nov 2026) — [Trading Economics](https://tradingeconomics.com/commodity/uranium)
- TradeTech long-term indicator at a record $99.00/lb (31 Oct 2026), the highest since the series began in 1996; the term price has run above spot for most of 2026 — [Crux Investor](https://www.cruxinvestor.com/posts/record-us-99-uranium-contract-price-favors-miners-with-supply-left-to-sell)
- UEC signed unhedged long-term contracts with two US utilities (5 Nov 2026) — [Engineering News](https://www.engineeringnews.co.za/article/uec-signs-unhedged-long-term-sales-contracts-with-two-prominent-us-utilities-2026-11-05)

**E. Grid equipment, transmission and EPC**

Eaton (ETN) — Q3 2026, reported ~3 Nov
- Sales +28% (organic +19%, above the guidance high end)
- Electrical Americas:
  - Rolling-12-month organic orders +39%; backlog ~$16bn (+33%)
  - Data-center sales +54%; operating margin 29.8%
  - Record quarterly orders >$5bn at a 1.3 book-to-bill (per call summary)
- Electrical sector total: DC sales +65%, DC orders +101%; backlog >$20bn (+46%)
- Raised organic growth guidance; agreed to acquire COL Group
- Sources: [Morningstar/Business Wire](https://www.morningstar.com/news/business-wire/20261102754211/eaton-reports-record-third-quarter-2026-results-with-strong-organic-growth-accelerating-record-orders-and-backlog-raises-organic-growth-guidance); [Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/eaton-q3-earnings-call-highlights-051410047.html); [Eaton Q3 8-K](https://www.sec.gov/Archives/edgar/data/0001551182/000155118226000037/etn09302026exhibit99.htm)
- Market data: not found

Hubbell (HUBB) — Q3 2026, 27 Oct
- Net sales +25% (organic +11%, M&A +13%); adjusted EPS $5.91 (+14%)
- Utility Solutions sales $1,028m (+9%: ~5% organic plus ~4 pts from DMC Power)
- Data-center sales +80% organic; Electrical Solutions +22% organic; DC expected to reach ~15% of Electrical segment revenue by year-end
- Guidance: sales growth 18–19%; adjusted EPS $20.40–20.60 (from $20.25–20.55); Utility organic growth 6–7% [SECONDARY]
- Shares fell despite the beat; Utility segment margin figures conflict between sources (19.8% vs 23.5%) [CONFLICT]
- Sources: [Hubbell release](https://hubbell.gcs-web.com/news-releases/news-release-details/hubbell-reports-third-quarter-2026-results); [Investing.com slides](https://www.investing.com/news/company-news/hubbell-q3-2026-slides-datacenter-boom-drives-25-sales-growth-93CH-4976289); [Investing.com transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-hubbell-beats-q3-2026-estimates-but-shares-fall-93CH-4976246)

Quanta Services (PWR) — Q3 2026, 29 Oct
- Revenue $12.01bn (vs $7.63bn); adjusted EPS $6.06 (vs $3.33)
- Remaining performance obligations $41.8bn; total backlog a record $63.7bn (+~$10bn QoQ); Electric segment backlog $51.9bn
- FY26 guidance raised: revenue $41.3–41.6bn; adjusted EPS $17.90–18.30
- Management flagged lumpy backlog growth from the timing of large awards
- Sources: [Quanta release](https://investors.quantaservices.com/news-events/press-releases/detail/407/quanta-services-reports-third-quarter-2026-results); [Quanta 8-K](https://www.sec.gov/Archives/edgar/data/0001050915/000119312526436949/d77812dex991.htm); [GuruFocus](https://www.gurufocus.com/news/9152576/quanta-services-inc-pwr-q3-2026-earnings-call-highlights-record-64-billion-backlog-and-raised-guidance-signal-sustained-momentum)
- Quanta is the largest holding of the Defiance AI & Power Infrastructure ETF (AIPO) — [Simply Wall St](https://simplywall.st/etfs/us/nasdaq-aipo/news/the-ai-etf-betting-on-the-infrastructure-it-needs/amp)

Powell Industries (POWL) — fiscal Q4 2026, reported ~17 Nov
- Revenue ~$397m (+33%); EPS $2.23; net income ~$82m ($81.5m in one call summary) [CONFLICT, minor]
- Backlog $2.7bn (+96% YoY); quarterly orders $710m (1.8x book-to-bill); FY26 orders ~$2.6bn (~2.0x revenue)
- ~$1.3bn of backlog expected to convert in FY27, most of the remainder in 2028; the release warns orders may be cancelled or modified
- Sources: [Powell release](https://www.sec.gov/Archives/edgar/data/80420/000008042026000139/ex991-powlq4xfy2026earning.htm); [CryptoBriefing](https://cryptobriefing.com/powell-industries-earnings-q4-fiscal-2026-2026-11/); [Panabee](https://www.panabee.com/news/powell-earnings-q4-2026); [MarketBeat](https://marketbeat.com/instant-alerts/transcript-powell-industries-q4-earnings-call-highlights-2026-11-17/?amp=)

MYR Group (MYRG)
- No Q3-2026 data retrieved (gap)

ABB (ABBNY; ABBN.SW) — Q3 2026, ~mid/late Oct
- Record orders ~$12.06bn (+40%); book-to-bill 1.24
- Electrification orders +70% comparable to $7.67bn; US orders +82%
- Data-center segment grew triple digits (no figure disclosed)
- Adjusted EPS $0.69 vs $0.79 consensus (miss); capex kept near $1bn
- Sources: [ABB](https://www.abb.com/global/en/news/139696/q3-2026-results); [Futurum](https://futurumgroup.com/insights/abb-q3-fy-2026-earnings-show-record-orders-outpacing-revenue-on-data-centers/); [Investing.com](https://ca.investing.com/news/stock-market-news/abb-q3-2026-slides-record-margins-data-center-push-amid-eps-miss-93CH-4890082); [mgrid](https://mgrid.org/2026/10/20/abb-books-a-record-12-billion-quarter-with-us-orders-up-82-but-keeps-capital-spending-near-1-billion/)

Schneider Electric (SBGSY; SU.PA) — Q3 2026, reported 16 Oct per source
- Revenue €11.46bn (+16.9% organic, +17.9% reported)
- Data-center demand up triple digits, while DC sales grew "strong double digit"
- Data Center & Networks was ~30% of 2025 revenue
- Sources: [Sotkn](https://www.sotkn.com/catalyst/schneider-q3-2026-1146b-data-center-demand-triple-digit/); [DC Market Insights](https://www.dcmarketinsights.com/news/ai-data-centres-lifted-abb-orders-40-and-schneider-sales-17-siemens-energy-reports-on-11-november)

HD Hyundai Electric (267260.KS) — Q3 2026, 27 Oct
- Revenue ~₩1.18tn (+18.5%); operating profit ₩284.5bn (+15.1%); operating margin 24.1%
- Orders $980m (−19.1% YoY, against a high 1H base of $3.231bn)
- Backlog $8.843bn (+4.2% QoQ; +26.6% YoY)
- Net profit ₩184.2bn (−3.6% YoY), below the ₩226.8bn consensus
- ~₩200bn Cheongju expansion, partly for AI DCs
- Sources: [Seoul Economic Daily](https://en.sedaily.com/finance/2026/10/27/hd-hyundai-electric-posts-record-quarterly-revenue-invests); [FN News](https://en.fnnews.com/news/202610271427519882); [Asia Business Daily](https://view.asiae.co.kr/en/article/2026102714005641709); [ad-hoc-news](https://www.ad-hoc-news.de/boerse/news/nebenwerte/hd-hyundai-electric-stock-q3-profit-rises-net-income-slips/70431901)

Prysmian (PRY.MI) and Hitachi (6501.T / HTHIY)
- No Q3-2026 data retrieved (gap). The only Hitachi figure found (¥8.8tn backlog) is from FY2026/3 Q3 and unverified [STALE] — [note.com](https://note.com/noted_jacana411/n/n7fbded323288?hl=en)

**F. Data-center electrical and thermal**

Vertiv (VRT) — Q3 2026, 28 Oct
- Net sales $4,313m (+61%: +55% organic, ~+6% from acquisitions); adjusted operating margin 25.2%; adjusted EPS $2.21
- Q3 organic orders >100% YoY (Vertiv does not disclose order dollars); EMEA pipeline ~2x
- Counts only purchase orders as backlog, not capacity agreements. The last disclosed backlog was $15.0bn at Q4 2025 (+109%)
- FY26 sales guidance ~$14.65bn (+$650m at the midpoint; ~38% organic); Q4 guidance $4,413m (~50% organic)
- Expects "significant above-market organic sales growth in 2027"
- Sources: [Vertiv Q3 release](https://www.sec.gov/Archives/edgar/data/0001674101/000162828026067707/q32026exhibit991vrt10282026.htm); [Investing.com slides](https://www.investing.com/news/company-news/vertiv-q3-2026-slides-61-sales-growth-raised-guidance-across-metrics-93CH-4980229); [Investing.com transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-vertiv-tops-q3-2026-estimates-and-raises-outlook-93CH-4980196); [Q4-2025 release](https://www.sec.gov/Archives/edgar/data/1674101/000167410126000006/exhibit991vrt02112026.htm)
- Vertiv has published an 800 V power and cooling reference architecture — [Savrn](https://savrn.com/blog/800-vdc-data-center-power-guide)

nVent (NVT) — Q3 2026, 30 Oct
- Sales ~$1.5bn (+44% reported and organic); adjusted EPS $1.52 (+67%)
- Backlog $2.6bn; orders up low double digits; Infrastructure +~90% on data centers
- Taking orders for modular liquid-cooling products
- FY guidance raised: sales growth +38–39% (from +32–34%); adjusted EPS $5.36–5.39 (from $5.00–5.10)
- Shares fell 8.8% on results day
- Sources: [nVent release](https://www.sec.gov/Archives/edgar/data/1720635/000162828026068391/q32026nvtpressrelease.htm); [Motley Fool transcript](https://www.fool.com/earnings/call-transcripts/2026/10/30/nvent-electric-nvt-q3-2026-earnings-call-transcript/); [Investing.com](https://in.investing.com/news/stock-market-news/earnings-call-transcript-nvent-tops-q3-2026-estimates-but-shares-fall-93CH-5670029)

Modine (MOD) — fiscal Q2 2027, quarter to 30 Sep 2026, reported ~4 Nov
- Data Centers segment sales $439.7m (+95%, hyperscale North America); total sales $994.4m (+35%)
- DC orders >$1bn in the quarter, a first
- FY growth guidance: Data Centers +80–90%; Commercial HVAC +10–15%
- Net earnings $30.3m (−32%); diluted EPS $0.56 (−33%)
- Sources: [Modine IR](https://investors.modine.com/news/news-details/2026/Modine-Reports-Second-Quarter-Fiscal-2027-Results/default.aspx); [StockTitan](https://www.stocktitan.net/news/MOD/modine-reports-second-quarter-fiscal-2027-3khyf8cqs3he.html); [Motley Fool transcript](https://www.fool.com/earnings/call-transcripts/2026/11/04/modine-mod-q2-2027-earnings-call-transcript/)
- The IR site is branded "Modexus Solutions", which may indicate a rename or separation — verify ticker continuity — [Modine IR](https://investors.modine.com/financials/quarterly-results/default.aspx)

Trane Technologies (TT) — Q3 2026, 29 Oct
- Bookings $7,248m (+21%; organic +20%); backlog $12.5bn, of which >$8bn is scheduled for 2027 and beyond
- Global applied Commercial HVAC bookings +>40%
- Tracking ~1,700 large projects (vs 1,400 the prior quarter), >90% data centers; DC orders described as "lumpy"
- Raised FY revenue guidance, reaffirmed EPS; margins under pressure
- Book-to-bill reported as 107% and 101% in different sources [CONFLICT]
- Sources: [Trane release](https://s2.q4cdn.com/950394465/files/content_files/Q3-2026-Earnings-Release-FINAL.pdf); [Investing.com](https://www.investing.com/news/company-news/trane-q3-2026-slides-bookings-surge-20-as-margins-face-pressure-93CH-4984598); [Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/trane-technologies-tt-said-q3-061358823.html)

Johnson Controls (JCI) — fiscal Q4 2026, late Oct
- Orders +44%; backlog $23bn (+43%), led by data centers
- Americas: orders +58%; backlog $17.8bn (+54%)
- Systems revenue +13%
- Order definitions changed in Q1 FY26, so comparisons are not fully like-for-like
- Sources: [JCI release](https://www.sec.gov/Archives/edgar/data/0000833444/000083344426000101/q4exh991xq4fy26earningsrel.htm); [Investing.com](https://www.investing.com/news/company-news/johnson-controls-q4-2026-slides-record-backlog-fuels-growth-outlook-93CH-4975920)

AAON — Q3 2026
- Net sales a record $707.4m (+84.1%)
- BASX-branded (data-center) sales $397.2m (+218.3%); AAON-branded $310.2m (+19.6%)
- Gross margin 26.7% (vs 27.8%), hurt by less mature, lower-utilization BASX plants; diluted EPS $0.83
- Source: [AAON release](https://www.sec.gov/Archives/edgar/data/0000824142/000082414226000083/liveaaonpressreleaseexs.htm)

**G. Utilities with data-center load**

NextEra (NEE) — Q3 2026, 21 Oct
- Energy Resources added 3.7 GW to backlog (incl. 2.4 GW of storage), bringing it to ~36.7 GW after 1.8 GW entered service
- Launched a data-center "hub" origination channel (>20 GW across Federal Hubs and Paducah Hub)
- Potential upside of 6–11 GW of additional storage at hub sites
- Duane Arnold restart by Q1 2029 at the latest
- Adjusted EPS $1.24 vs $1.13 per the slides; Investing.com reports $0.99 and a revenue miss [CONFLICT]
- Sources: [NEE slides](https://www.investor.nexteraenergy.com/~/media/Files/N/NEE-IR/reports-and-fillings/quarterly-earnings/2026/Q3%202026/Q3%202026%20Earnings%20Slides_v%20F.pdf); [Investing.com](https://www.investing.com/news/transcripts/earnings-call-transcript-nextera-energy-posts-mixed-q3-2026-results-93CH-4963447); [Industrial Info](https://www.industrialinfo.com/news/article/nextera-eyes-strong-backlog-data-center-hub-strategy--364064)

Dominion (D) — Q3 2026
- Beat estimates and raised its outlook; DC pipeline and capex as in §1 — [Investing.com](https://www.investing.com/news/transcripts/earnings-call-transcript-dominion-energy-tops-q3-2026-estimates-raises-outlook-93CH-4989456)

Southern (SO) — Q3 2026, ~5 Nov
- 21 GW signed plus 7 GW late-stage large load; capex $81–85bn and possibly approaching ~$100bn — [Yahoo Finance](https://finance.yahoo.com/energy/articles/southern-co-q3-2026-earnings-031904789.html)
- One summary says 2026 EPS was lifted to $4.70, a guidance increase was flagged, and DC usage rose 59% [SECONDARY] — [BigGo](https://finance.biggo.com/news/US_SO_2026-11-05)

AEP — Q3 2026
- Capex $100bn; 15 GW of new load commitments (see §1) [SECONDARY]

Xcel (XEL) — Q3 2026, 29 Oct
- $70bn base plan; 11% rate-base CAGR; >$10bn upside (see §1)

Entergy (ETR)
- No Q3-2026 data retrieved (gap; the only figures found were ~1 year old and are excluded as [STALE])

**H. Gas midstream**

Williams (WMB) — Q3 2026, 3 Nov
- Adjusted EBITDA $2.039bn (+6%); AFFO $1.589bn (+10%)
- Tracking the upper half of 2026 adjusted EBITDA guidance of $8.3–8.5bn; growth capex $7.3–7.9bn
- 11%+ EBITDA CAGR target through 2030; year-end leverage ~3.75x
- Power Innovation details in §1
- Sources: [Williams Q3 8-K](https://www.sec.gov/Archives/edgar/data/0000107263/000010726326000035/wmb_20260930xer.htm); [Investing.com](https://www.investing.com/news/company-news/williams-q3-2026-slides-record-ebitda-11-growth-target-through-2030-93CH-4995914)

Kinder Morgan (KMI) — Q3 2026, ~21 Oct (record quarter)
- Expansion backlog $14.4bn (+$4.7bn QoQ), >75% tied to power generation and LDC demand
- Creekside Lateral (~$235m; >750 MMcf/d) for Central Texas data center and industrial customers
- Sources: [KMI Q3 8-K](https://www.sec.gov/Archives/edgar/data/0001506307/000150630726000130/kmi2026q38-kex991.htm); [NGI](https://naturalgasintel.com/news/kinder-morgan-backlog-surges-on-ai-data-centers-southeast-power-demand/); [Yahoo Finance](https://finance.yahoo.com/energy/articles/kinder-morgan-reports-record-third-200500013.html)
- IEEFA argues KMI's Southeast DC load projections far exceed NERC's — [IEEFA](https://ieefa.org/resources/excessive-forecasts-data-center-growth-are-behind-push-build-two-large-natural-gas)

Energy Transfer (ET) and EQT
- DC supply deals are listed in §1. Q3-2026 results were not retrieved (gap)

**I. Storage**

Fluence (FLNC) — fiscal Q4 2026, 24 Nov
- Q4 revenue $744m vs ~$967m expected; FY revenue $2.3bn
- Houston contract-manufacturing delays cost ~$90m in penalties
- Record Q4 orders $3.5bn; FY orders $6.2bn
- Backlog ~$8.9bn (+39% QoQ; +68% YoY from $5.3bn), with no debookings; roughly one-third expected to convert in each of the next three fiscal years (~$3bn in FY27)
- No FY27 guidance until February 2027
- Liquidity $855m, incl. $379m cash; no external capital expected to be needed in FY27
- Interim CEO Axel Meier
- Sources: [Investing.com slides](https://www.investing.com/news/company-news/fluence-fy-2026-slides-record-89b-backlog-amid-execution-woes-93CH-5048565); [Investing.com transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-fluence-energy-misses-q4-2026-estimates-93CH-5048527); [GuruFocus](https://www.gurufocus.com/news/9218986/fluence-energy-flnc-reports-q4-revenue-of-744m-amid-manufacturing-delays); [Motley Fool transcript](https://www.fool.com/earnings/call-transcripts/2026/11/24/fluence-flnc-q4-2026-earnings-call-transcript/)

Tesla Energy (TSLA) — Q3 2026
- Storage deployments 13.7 GWh (vs 12.5 GWh in Q3 2025 and 13.5 GWh in Q2; record is 14.2 GWh in Q4 2025); below ~15.9 GWh expected
- Energy revenue $2.88bn (−16% YoY, partly tariff-related customer refunds); energy gross margin 33.1% (vs 20.4% in Q2)
- Nine-month deployments 36 GWh (+11%); nine-month energy revenue $8.43bn (−6%)
- Record order rate and backlog; Megapacks "almost sold out"; Megafactory Texas started production
- Sources: [Energy-Storage.news](https://www.energy-storage.news/tesla-q3-2026-energy-storage-revenues-fall-despite-second-highest-quarterly-deployments/); [Drive Tesla Canada](https://driveteslacanada.ca/news/tesla-megapack-almost-sold-out-q3-2026/); [FourWeekMBA](https://fourweekmba.com/ai-tesla-storage-orders-hit-record-as-energy-revenue-falls-16/)

Eos Energy (EOSE)
- No Q3-2026 data retrieved (gap)

**J. Copper**

Freeport-McMoRan (FCX) — Q3 2026, 27 Oct
- Copper production ~830 Mlb
- Grasberg: mill throughput ~67% of pre-Sep-2025 rates; Production Block 1S restart targeted mid-2027; ~80% of capacity by mid-2027 and near-full by end-2027
- Copper sales guidance cut ~2% for 2026 and ~2.5% for 2027 (2028 unchanged); 2027 copper sales still projected up >20%
- 2026 unit net cash cost $1.90/lb; 2027 capex ~$400m above prior guidance
- Sources: [FCX Q3 8-K](https://www.sec.gov/Archives/edgar/data/0000831259/000083125926000045/a3q2026exhibit991.htm); [FCX operational update](https://investors.fcx.com/investors/news-releases/news-release-details/2026/Freeport-Provides-Third-Quarter-2026-Operational-Update/default.aspx); [Yahoo Finance](https://finance.yahoo.com/markets/commodities/articles/freeport-mcmoran-inc-fcx-q3-210558373.html); [BigGo](https://finance.biggo.com/news/US_FCX_2026-10-27)
- Grasberg mud-rush disruption (force majeure from 8 Sep 2025) estimated at ~591k t of lost copper through end-2026 [SECONDARY] — [Startup Fortune](https://startupfortune.com/copper-hits-a-record-683-a-pound-as-mine-disasters-choke-supply/)

Southern Copper (SCCO)
- No Q3-2026 data retrieved (gap)

Copper price [CONFLICT across sources and dates]
- ~$5.32/lb on 25 Nov 2026 (−0.95%), near the lowest since Dec 2025 — [Kalkine](https://kalkine.com/news/mining/copper-slips-toward-an-11-month-low-freeport-mcmoran-nysefcx-and-southern-copper-nysescco)
- LME ~$13,876/t on 12 Nov 2026 — [copper.com.au](https://copper.com.au/news/mining/copper-weekly-brief-to-12-november-2026/)
- A record of $6.83/lb was reported earlier in 2026 — [Startup Fortune](https://startupfortune.com/copper-hits-a-record-683-a-pound-as-mine-disasters-choke-supply/)
- The copper futures fund fell 3.87% to $32.50, a six-month low, on 24 Nov amid "AI doubts and Fed bets" — [Rio Times](https://www.riotimesonline.com/copper-markets-latam-tuesday-november-24-2026/)

### Inferences
Derived ratios (author's arithmetic on the cited figures):
- Quanta: backlog ($63.7bn) is ~1.5x 2026 revenue guidance (~$41.5bn midpoint).
- Powell: backlog ($2.7bn) is ~2x annual revenue (FY orders ≈2.0x revenue), implying FY26 revenue of ~$1.3bn.
- Fluence: backlog ($8.9bn) is ~3.9x FY26 revenue ($2.3bn).
- Vertiv: the FY26 sales guide ($14.65bn) is roughly equal to its last disclosed backlog ($15.0bn at Q4 2025).
- Bloom: at a $46–57bn market cap on a $4.4–4.6bn revenue guide, it trades at ~10–13x 2026 sales and ~39–43x forward EPS. That is the richest profitable name in the set **[HIGH VALUATION]**.
- Vistra: the 2027 EBITDA guide midpoint ($8.1bn) is ~+11% over the 2026 midpoint ($7.3bn).
- Talen: the 2027 guide implies ~+26% EBITDA and ~+27% adjusted FCF growth at the midpoints. On a reported ~10x forward P/E (single source), it looks cheap relative to growth. The discount likely reflects PJM regulatory risk and its concentration in Pennsylvania.

Three tiers by fundamental momentum vs price action (Nov 2026):
- (i) Order-book compounders with record backlogs: GEV, Siemens Energy, ETN, PWR, HUBB, POWL, VRT, NVT, TT, JCI, MOD, AAON, CAT, BWXT, LEU. Fundamentals accelerating; shares hit in November on sentiment and policy.
- (ii) Merchant power/IPPs: CEG, VST, TLN, NRG. Earnings growth and buybacks continue, but the equities de-rated hard (−17% to −42% YTD) on Texas/PJM politics and AI-capex doubts. This is where valuation compression is greatest relative to guided 2027 growth.
- (iii) Pre-revenue nuclear: OKLO, SMR, NNE. Collapsed 48–78% YTD. Oklo's ~$3.1bn cash may now be close to its market value. If the July-2026 share count (≈$8bn ÷ ~$49 ≈ ~163m shares) still applies, a ~$17.60 price implies ~$2.9bn — but ATM issuance may have changed the share count, so verify before relying on this.

Other observations:
- The turbine oligopoly (GEV ~122 GW incl. slot reservations; Siemens Energy 65 GW firm; MHI ~37 GW) reports well over 200 GW of combined backlog on non-comparable definitions. Combined with the MHI/GEV capacity expansions (GEV 30 GW/yr by 2030; MHI 2x by 2030) and new entrants (Ansaldo), the pricing cycle could peak around 2028–2030. This is a key long-horizon risk for GEV, Siemens Energy and MHI multiples.
- HD Hyundai Electric's Q3 orders fell 19% YoY while backlog still rose. Lumpy large orders mean quarterly order prints are poor signals for transformer makers; track backlog and margin instead.

### Gaps
- Market capitalization, YTD and 1-year returns and forward P/E or EV/EBITDA were **not retrieved** for most names: VRT, ETN, HUBB, PWR, MYRG, POWL, NVT, MOD, TT, JCI, AAON, CAT, CMI, CCJ, LEU, BWXT, NEE, D, SO, ETR, AEP, XEL, WMB, KMI, EQT, ET, FLNC, EOSE, TSLA, FCX, SCCO, Siemens Energy, MHI, ABB, Schneider, Prysmian, HD Hyundai Electric and Hitachi. Pull these from a live feed.
- No Q3-2026 results retrieved for MYR Group, Entergy, Energy Transfer, EQT, Eos Energy, Southern Copper, Prysmian, Hitachi/Hitachi Energy or Nano Nuclear.
- The GEV total backlog/orders figures ($197bn / $29bn) are secondary and need verification against the 8-K.
- Siemens Energy's slot-reservation vs firm-backlog definitions are ambiguous.
- Bloom's DC-specific order figures were not disclosed in the sources found.
- Oklo: no post-July-2026 outcome found on whether its DOE pilot reactor reached criticality.

---

## 3. Emerging "next topic" sub-themes: real orders/revenue vs hype, and purest listed exposure

### Takeaway
Three sub-themes show real, reported revenue in 2026:
- On-site/BTM generation: Bloom revenue +138%; CAT Power Generation +30%; Williams $9.6bn committed.
- SiC/GaN power semis for AI racks: DC revenue doubling at onsemi, Infineon and Wolfspeed, though still small in absolute terms.
- Long-duration storage: contracts are real (Form Energy >80 GWh, Google/Xcel 30 GWh), but the leaders are private.

Others are still mostly pre-commercial:
- 800 VDC / solid-state transformers: native 800 VDC arrives with Nvidia's Kyber, targeted for 2027 and reportedly slipping to 2028; SST-based facilities around 2029.
- SMRs: three NRC construction permits in 2026, but first commercial power is ~2030+, and Oklo has not yet docketed an NRC license application.
- HVDC: no confirmed 2026 US orders found.
- GETs: a FERC policy push, but few listed pure plays.

### Cited Findings

**800 VDC data-center power architecture and solid-state transformers (SST)** — sources are mostly secondary newsletters and blogs [SECONDARY]
- Today's GB200/GB300 racks use 54 V. Native 800 VDC arrives with Vera Rubin/Kyber, which Nvidia has tied to 2027 production, with a design target of ~600 kW per rack — [Savrn](https://savrn.com/blog/800-vdc-data-center-power-guide); [LeCompute](https://lecompute.fr/en/silicon/800-vdc-ai-data-center-power/); [InsideDeepTech](https://www.insidedeeptech.com/800-vdc-power-distribution-ai-data-centers-full-guide/)
- SemiAnalysis reported Kyber slipping more than a year to 2028 because the midplane is hard to manufacture; Nvidia says its roadmap is intact — [SemiAnalysis](https://newsletter.semianalysis.com/p/inside-the-800vdc-revolution-part); [Macroplane](https://macroplane.com/blog/800-vdc-stocks)
- Interim products: an Nvidia hybrid power rack (2H 2026) and row power center (2027); Delta has shown a 660 kW in-row 800 V power rack; Vertiv has published an 800 V reference architecture — [Savrn](https://savrn.com/blog/800-vdc-data-center-power-guide); [Informic](https://electroniccomponent.com/800vdc-power-architecture-ai-factories-power-electronics-2)
- Named Nvidia 800 VDC partners include Delta, LITEON, Flex, Bizlink, Megmeet and Lead Wealth (private). Being a named partner signals compatibility, not confirmed orders. Nvidia reportedly held talks with LS Electric, HD Hyundai Electric and Hyosung — [Macroplane](https://macroplane.com/blog/800-vdc-stocks); [manishklach](https://manishklach.github.io/writings/nvidia-800v-dc-ai-data-center-power-semiconductors.html)
- SST:
  - A joint Nvidia/Google/Microsoft OCP effort includes an SST specification; sources date it Mar, Jul or 11 Aug 2026 [CONFLICT]
  - Nvidia's roadmap targets SST-based facilities around 2029
  - DG Matrix (private) is described as the only SST in Nvidia's MGX reference architecture, with UL certification targeted for end-Q2 2026
  - No UL-listed 800 VDC system is yet operating in a US data center
  - Sources: [mgrid](https://mgrid.org/2026/05/15/how-moving-ai-data-centers-to-800-vdc-distribution-and-solid-state-transformers-sidesteps-phase-imbalance-entirely/); [InsideDeepTech](https://www.insidedeeptech.com/800-vdc-power-distribution-ai-data-centers-full-guide/); [Savrn](https://savrn.com/blog/800-vdc-data-center-power-guide)

**SiC/GaN power semiconductors**
- Infineon: FY2026 data-center revenue ~€2.2bn, incl. ~€1.7bn AI, with a €4bn target for FY2027 [SECONDARY]. An earlier estimate put AI revenue at >€1.6bn, using a different definition [CONFLICT] — [CMC Aureon Substack](https://cmcaureon.substack.com/p/three-power-chip-plays-behind-ai); [Six Sigma Research](https://sixsigmaresearch.com/p/power-semiconductors-primer-how-ai)
- onsemi: Q3-2026 data-center revenue $180m (+175% YoY) [SECONDARY]; AI DC revenue expected to more than double in 2026 — [CMC Aureon Substack](https://cmcaureon.substack.com/p/three-power-chip-plays-behind-ai); [DataM Intelligence](https://www.datamintelligence.com/blogs/ai-data-center-power-semiconductors-infineon-onsemi-stmicroelectronics)
- Wolfspeed: AI data-center revenue more than doubled in FY2026 and grew ~20% QoQ in Q4. The company calls it a "moderate but growing" part of the business — [Wolfspeed Q4 FY26 8-K](https://www.sec.gov/Archives/edgar/data/0000895419/000089541926000049/ex991q4-26.htm)
- Navitas: 2025 revenue $45.92m, with high-power applications (incl. AI DC) the majority for the first time. It estimates a $1.4–2.5bn AI-DC serviceable market by 2030 **[SPECULATIVE; small revenue base]** — [24/7 Wall St.](https://247wallst.com/investing/2026/04/21/the-behind-the-scenes-ai-chip-stock-few-investors-know-but-every-hyperscaler-will-soon-need/); [Yahoo Finance](https://finance.yahoo.com/sectors/technology/articles/big-could-ai-data-center-162400998.html)
- Content per kW: Infineon estimates $100–250 of power semiconductors per kW of AI compute. SiC is used at high-voltage stages and GaN nearer the board — [SemiconductorX](https://semiconductorx.com/spotlight-data-center.html)

**Behind-the-meter / on-site generation and fuel cells**
- Planned vs built: >115 GW of BTM gas planned vs 4.9 GW operating and 15.8 GW under construction (Oct 2026) — [MIT Technology Review](https://www.technologyreview.com/2026/11/24/1149622/data-centers-natural-gas/)
- Revenue evidence:
  - Bloom Q3 revenue +138%, FY26 guide $4.4–4.6bn — [Bloom release](https://www.sec.gov/Archives/edgar/data/0001664703/000162828026066890/ex991_q326financialresults.htm)
  - CAT Power Generation +30%, driven by turbines and large recips primarily for DCs — [Utility Dive](https://www.utilitydive.com/news/caterpillar-posts-highest-sales-quarter-ever-data-centers-q3-2026/873586/)
  - Cummins North American power gen +22% — [Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/cummins-q3-earnings-call-highlights-221433740.html)
  - Williams ~$9.6bn committed across six projects — [Williams 8-K](https://www.sec.gov/Archives/edgar/data/0000107263/000010726326000035/wmb_20260930xer.htm)
- Skeptic view: the MHI CEO argues off-grid costs will push DCs back to utilities — [Utility Dive](https://www.utilitydive.com/news/data-centers-mitsubishi-gas-turbines-earnings/875146/)

**SMR / advanced-nuclear commercialization milestones (2026)**
- TerraPower Kemmerer 1 (Natrium, WY): NRC construction permit on 4 Mar 2026, the first commercial reactor construction permit in nearly a decade. Completion targeted for 2030 and operation for 2031. TerraPower is private — [NRC](https://www.nrc.gov/sites/default/files/cdn/doc-collection-news/2026/26-028.pdf); [ANS](https://www.ans.org/news/article-7818/nrc-approves-terrapower-construction-permit/); [WNA](https://world-nuclear.org/our-association/publications/world-nuclear-outlook-report/united-states-of-america---world-nuclear-outlook-report)
- TVA Clinch River (GE Vernova Hitachi BWRX-300, 300 MW): construction permit on 29 Sep 2026, after a ~14-month review. Construction must be complete by 30 Sep 2032; no construction start announced — [ANS](https://www.ans.org/news/2026-09-29/article-8445/tva-receives-construction-permit-for-clinch-river/); [Autonocion](https://www.autonocion.com/us/first-small-reactor-construction-permit/)
- X-energy/Dow Long Mott (four Xe-100s, TX): construction permit ~Nov 2026, the third advanced-reactor permit of 2026. Dow has not made a final decision and expects to weigh a preliminary investment decision in 2027. X-energy is private — [Daily Caller, 22 Nov 2026](https://dailycaller.com/2026/11/22/nrc-reactor-permits-long-mott-dow-texas-democrats-congress-nuclear-oversight/)
- Blue Energy submitted part one of a BWRX-300 construction permit application (Sep 2026) — [WNA](https://world-nuclear.org/our-association/publications/world-nuclear-outlook-report/united-states-of-america---world-nuclear-outlook-report)
- DOE Reactor Pilot Program: the goal of 3 reactors critical by 4 Jul 2026 was reportedly met [CONFLICT on which companies]
  - ANS names Antares, Valar Atomics and Deployable Energy
  - DOE lists Antares (4 Jun 2026), Valar (18 Jun 2026) and Aalo (6 Jul 2026)
  - The program does not specify cold vs full-power criticality
  - Oklo had hoped for criticality by end-July (outcome not found)
  - Sources: [ANS](https://www.ans.org/news/article-8178/the-deadline-arrives-checking-in-on-the-reactor-pilot-program/); [DOE](https://www.energy.gov/ne/us-department-energy-reactor-pilot-program); [Partnership for Global Security](https://partnershipforglobalsecurity.org/status-of-the-doe-reactor-pilot-project/)
- Oklo: DOE PDSA approved (Jun 2026); the NRC combined license application for Aurora-INL has not been docketed (pre-application status at 29 Sep 2026) — [ANS](https://www.ans.org/news/2026-06-12/article-8119/oklo-secures-doe-pdsa-approval/); [NRC](https://www.nrc.gov/reactors/new-reactors/advanced/who-were-working-with/pre-application-activities/okla-aurora-powerhouse)
- NuScale: no binding module order. The TVA PPA sits with ENTRA1 — [Benzinga](https://www.benzinga.com/news/26/11/62959728/nuscale-power-q3-2026-earnings-call-transcript)
- Policy shift: reactor permits "pile up under Trump" as Democrats prepare to take over nuclear oversight in Congress (22 Nov 2026) — [Daily Caller](https://dailycaller.com/2026/11/22/nrc-reactor-permits-long-mott-dow-texas-democrats-congress-nuclear-oversight/)

**Long-duration energy storage (LDES)**
- Form Energy (private):
  - More than 80 GWh under agreement vs ~2 GWh/yr of current production capacity — [MIT Technology Review](https://www.technologyreview.com/2026/10/06/1145020/2026-climate-tech-companies-to-watch-form-energy-iron-batteries/)
  - Raised $750m (Aug 2026) to expand its West Virginia factory — [TechCrunch](https://techcrunch.com/2026/08/12/form-energy-raises-750m-to-build-more-100-hour-batteries-for-the-grid)
  - Contracts: Google/Xcel 300 MW / 30 GWh and Crusoe 12 GWh — [Energy-Storage.news](https://www.energy-storage.news/google-minnesota-data-centre-energy-deal-includes-30gwh-multi-day-iron-air-batteries-from-form-energy/)
- Caveats on iron-air: lower round-trip efficiency than lithium-ion or flow batteries; about one acre per 2–3 MW — [MIT Technology Review](https://www.technologyreview.com/2026/10/06/1145020/2026-climate-tech-companies-to-watch-form-energy-iron-batteries/)
- Listed lithium-ion storage evidence:
  - Fluence: record $3.5bn of Q4 orders and $8.9bn backlog — [Investing.com](https://www.investing.com/news/company-news/fluence-fy-2026-slides-record-89b-backlog-amid-execution-woes-93CH-5048565)
  - NextEra: 2.4 GW of storage originated in Q3, with 6–11 GW of DC-hub storage upside — [NEE slides](https://www.investor.nexteraenergy.com/~/media/Files/N/NEE-IR/reports-and-fillings/quarterly-earnings/2026/Q3%202026/Q3%202026%20Earnings%20Slides_v%20F.pdf)
  - Tesla: Megapacks "almost sold out" — [Drive Tesla Canada](https://driveteslacanada.ca/news/tesla-megapack-almost-sold-out-q3-2026/)

**Geothermal**
- Fervo Energy IPO:
  - Priced at $27 on 12 May 2026 (upsized); shares rose ~33–35% on day one — [Yahoo Finance](https://finance.yahoo.com/news/geothermal-startup-fervo-energy-pops-174220777.html); [Canary Media](https://www.canarymedia.com/articles/geothermal/fervo-energy-ipo-milestone)
  - Gross proceeds ~$1.89bn base, or ~$2.2bn including the over-allotment [CONFLICT/definition] — [VKTR](https://www.vktr.com/ai-news/fervo-energy-raises-19b-in-ipo-01/); [Fervo 8-K](https://www.sec.gov/Archives/edgar/data/0001853868/000162828026055942/exhibit991earningsrelease8.htm)
  - Q2-2026 net loss $55.9m; aims for >1 GW online by the end of the decade; a Nevada pilot helps power a Google DC; demand comes from utilities and hyperscale developers **[UNPROFITABLE]** — [Fervo 8-K](https://www.sec.gov/Archives/edgar/data/0001853868/000162828026055942/exhibit991earningsrelease8.htm)
- Ormat (ORA): valued at ~$7.5bn, "slightly below Fervo's initial valuation"; Google deal for up to 150 MW in Nevada — [Canary Media](https://www.canarymedia.com/articles/geothermal/fervo-energy-ipo-milestone)
- Policy: geothermal escaped the administration's renewable crackdown (Mar 2026) — [Energy Connects](https://www.energyconnects.com/news/renewables/2026/march/geothermal-escapes-trump-s-renewable-crackdown-boosts-fervo-s-ipo-bid/)

**HVDC transmission**
- SunZia began full operational deliveries in Jun 2026 with ~3.0 GW of HVDC transfer capability [SECONDARY; partly garbled source] — [Energy Resources Insights](https://www.energyresourcesinsights.com/energy-power-insights/hvdc-transmission-project-pipeline-2026)
- DOE's draft National Transmission Needs Study (Jul 2026) cites DC and manufacturing load growth — [DOE](https://www.energy.gov/documents/national-transmission-needs-study-draft-july-2026)
- No confirmed 2026 US HVDC orders or contract awards were found in this round

**Grid-enhancing technologies (GETs) and grid software**
- FERC's 18 Jun 2026 large-load show-cause orders require RTOs to consider GETs, including dynamic line ratings — [FERC](https://www.ferc.gov/news-events/news/commissioner-rosners-remarks-large-load-show-cause-orders-e-7-e-12-june-18-2026)
- FERC Chair Laura Swett created a task force on supporting GETs, possibly through incentives — [Utility Dive](https://www.utilitydive.com/news/ferc-grid-enhancing-technology-incentives-atts-senate-hearing/825992/)
- A reported draft executive order (May 2026) would push FERC to identify where advanced transmission could replace new lines; FERC is independent and not bound by it — [Latitude Media](https://www.latitudemedia.com/news/scoop-trump-is-sitting-on-an-executive-order-pushing-advanced-transmission/)

### Inferences
Evidence vs hype, and purest listed exposure. Tickers marked "(verify)" come from general knowledge, not this round's sources.

| Sub-theme | Evidence level (Nov 2026) | Purest listed exposure | Notes |
|---|---|---|---|
| On-site/BTM power and fuel cells | **Real revenue now** | BE; CAT, CMI (gensets/recips/turbines); WMB (developer-owner) | BE is the purest but **[HIGH VALUATION]**, with negative FCF in Q3. BTM is OEM-constrained and possibly a bridge to the grid |
| SiC/GaN for 800 V AI power | Real but small revenue (doubling) | ON, IFNNY/IFX.DE (verify), WOLF, NVTS **[SPECULATIVE]** | DC is still a minority of revenue for all; auto/industrial cycles dominate |
| 800 VDC and SST | Mostly roadmap (2027–2029); partners ≠ orders | VRT, ETN (verify 800 VDC products), Delta 2308.TW (verify), LITEON 2301.TW (verify), FLEX (verify), HD Hyundai Electric 267260.KS, LS Electric 010120.KS (verify) | SST leaders (e.g., DG Matrix) are private. Kyber timing risk (2027 vs 2028) |
| SMRs and advanced nuclear | Permits real (3 construction permits in 2026); power ~2030+ | Picks-and-shovels with revenue: GEV (BWRX-300), BWXT, LEU, CCJ. Developers: OKLO, SMR, NNE **[PRE-REVENUE]** | TerraPower, X-energy and Kairos are private. The developer equities are option value, not cash flow |
| Long-duration storage | Contracts real; listed pure plays thin | EOSE (no data this round) **[SPECULATIVE]**; FLNC/TSLA (Li-ion, not LDES) | Form Energy (private) leads on contracts |
| Geothermal | IPO plus hyperscaler PPAs; small MW today | ORA; Fervo (listed since May 2026, ticker not verified in this research) | Fervo is unprofitable |
| HVDC | Policy and need evidence; no US orders found | Siemens Energy, Hitachi (6501.T), Prysmian (PRY.MI), GEV (verify HVDC books) | Order evidence missing this round |
| GETs and grid software | Policy push (FERC); limited revenue evidence | Few listed pure plays identified | Gap |

Two further points:
- The AI-specific piece most likely to move from hype to orders in 2027 is 800 VDC power distribution (VRT, ETN, Delta, LITEON). Watch Kyber timing: a slip to 2028 would push the revenue inflection out a year.
- The SMR "next topic" has bifurcated. Licensing progress is real (TerraPower, TVA, X-energy) but is mostly accruing to private developers and to GEV, BWXT and the fuel cycle (LEU, CCJ). The listed pure-play developers have de-rated 48–78% YTD.

### Gaps
- No 2026 orders/revenue evidence retrieved for listed SST or 800 VDC component vendors (Delta, LITEON, Flex) or for Eaton's 800 VDC products.
- No listed GETs/advanced-conductor/DLR pure plays identified.
- No 2026 US HVDC order data.
- Eos Energy's Q3-2026 status, Fervo's ticker and post-IPO performance, and AMSC/Hyosung/LS Electric data were not retrieved.
- Whether Oklo reached pilot-reactor criticality after July 2026 is unknown.
- NuScale's US460 design-approval status was not re-verified this round.

---

## 4. Valuation and bubble risk: extreme multiples, pre-revenue names, and what could break the thesis

### Takeaway
November 2026 brought a sharp de-rating driven by policy and sentiment rather than by fundamentals. Triggers:
- The 3 Nov midterms (a Democratic sweep of Congress)
- A Texas governor-elect who campaigned on pausing new data centers
- A SoftBank charge tied to power-equipment procurement
- Hot inflation, new tariff proposals, and doubts about how AI capex is financed

Extremes are concentrated in:
- Pre-revenue SMR developers (OKLO, SMR, NNE), still valued on option value after falling 48–78% YTD
- Bloom (~39–43x forward EPS, ~10x+ sales)
- GE Vernova (~30–34x forward EPS, down from ~63x in June)

The main thesis-breakers are demand overstatement and queue attrition; Texas, PJM and FERC policy; AI-capex slowdowns or financing stress; supplier capacity additions eroding pricing; and execution failures.

### Cited Findings
- **Political trigger (3–4 Nov 2026):**
  - Democrats took both houses of Congress, raising the prospect of more scrutiny of AI-linked industries — [Yahoo Finance](https://finance.yahoo.com/energy/articles/ai-data-center-stocks-dip-113427491.html); [Bellwize](https://bellwize.com/stocks/2026-11-05-vst-democratic-sweep-power-selloff/)
  - Texas elected Gina Hinojosa governor on a platform that included pausing new data centers; her term starts in January — [Protocol7 Substack](https://protocol7ai.substack.com/p/texas-may-freeze-data-centers-plugs); [Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/vistra-fell-14-texas-election-133542031.html)
  - Wells Fargo estimates Texas is ~27% of planned US data-center gigawatts — [Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/vistra-sinks-10-constellation-down-150042182.html)
  - Moves on 4 Nov: VST −13.8%, NRG ~−13.5%, CEG ~−6.7%, VRT ~−12.9% — [Bellwize](https://bellwize.com/stocks/2026-11-05-vst-democratic-sweep-power-selloff/); [Energy News Beat](https://energynewsbeat.co/finance/chip-stocks-sink-and-texas-power-stocks-slide-did-voters-really-hit-pause-on-data-centers/)
  - The pace of DC cancellations was already rising before the vote — [Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/vistra-fell-14-texas-election-133542031.html)
- **Follow-on selloff:**
  - GEV, VRT and BE lost 10–24% in a week — [Motley Fool, 10 Nov](https://www.fool.com/investing/2026/11/10/ge-vernova-vertiv-and-bloom-energy-just-lost-10-to/)
  - GEV −12.9% for the week to $699.33 and −15.4% over a month — [Investing.com](https://www.investing.com/news/stock-market-news/ai-data-centers-need-power-yet-ge-vernova-sank-13-this-week-5045599)
  - A $3.7bn SoftBank charge tied to power-equipment procurement was cited as a trigger [low-quality source][VERIFY] — [NaturalNews](https://www.naturalnews.com/2026-11-12-ai-power-stocks-fall-after-softbank-write-down.html)
  - Hot inflation, tariff proposals and AI-financing worries were also cited — [Motley Fool](https://www.fool.com/investing/2026/11/10/ge-vernova-vertiv-and-bloom-energy-just-lost-10-to/)
  - 24–25 Nov: nine AI power stocks gave back a median 54.8% of Monday's gains by 1:05 pm ET on 25 Nov; Oklo was the only one below its Friday close — [FourWeekMBA](https://fourweekmba.com/ai-power-stocks-give-back-55-of-monday-oklo-below-friday/)
  - Oklo and NuScale −8% on 25 Nov — [24/7 Wall St.](https://247wallst.com/investing/2026/11/25/oklo-and-nuscale-power-retreat-8-as-ai-power-selloff-deepens-energy-fuels-drops-6/)
- **Valuation extremes (dated):**
  - BE ~43x forward (3 Nov) and ~39x next-year EPS (14 Nov); 3-year average 76x; ~74x in Aug — [TIKR](https://www.tikr.com/blog/bloom-energy-is-up-146-in-2026-take-profits-or-buy-more); [Motley Fool](https://www.fool.com/investing/2026/11/14/bloom-energy-stock-has-more-than-doubled-for-2-years-running-i-d-keep-buying-it-bit-by-bit/)
  - GEV forward P/E ~31.5–34x (10–11 Nov) vs ~63x at the June peak — [GuruFocus](https://www.gurufocus.com/term/forward-pe-ratio/GEV); [Admiral Markets](https://admiralmarkets.com/education/articles/shares/ge-vernova-stock)
  - Oklo has no meaningful revenue; first commercial power from Aurora is targeted for late 2027 to early 2028 — [Motley Fool](https://www.fool.com/investing/2026/11/10/ge-vernova-vertiv-and-bloom-energy-just-lost-10-to/)
  - NuScale Q3 revenue ~$0.28m — [NuScale](https://www.nuscalepower.com/press-releases/2026/nuscale-power-reports-third-quarter-2026-results)
- **Demand-risk evidence:**
  - Grid Strategies says DC load figures may be overstated (alternative benchmarks ~60–65 GW vs ~90 GW by 2030) — [NASEO presentation](https://energyoutlook2026.naseo.org/data/energymeetings/presentations/John%20Wilson.pdf)
  - Goldman: only ~60% of next-year DC capacity is expected on time, ~50% over two years — [Goldman Sachs](https://www.goldmansachs.com/insights/articles/us-data-center-power-demand-projected-to-double-by-2027)
  - Southern: 14.3 GW of DC projects withdrawn earlier in 2026 [VERIFY] — [SEC filing](https://www.sec.gov/Archives/edgar/data/92122/000009212226000021/so-20260323.htm)
  - IEEFA calls KMI's Southeast forecasts excessive vs NERC — [IEEFA](https://ieefa.org/resources/excessive-forecasts-data-center-growth-are-behind-push-build-two-large-natural-gas)
  - Microsoft trimmed 2026 capex to ~$170bn on chip delays [SECONDARY] — [YieldTheory](https://www.yieldtheory.app/research/hyperscaler-ai-capex-tracker-2026)
- **Market-structure and policy risk:**
  - PJM 2028/29 capacity price capped at $325/MW-day (uncapped ~$554.72), limiting merchant upside; ~38% of capacity cost attributed to DCs, a political target — [PJM](https://www.pjm.com/-/media/DotCom/about-pjm/newsroom/2026-releases/20260714-pjm-capacity-auction-procures-138318-mw-of-generation-resources.pdf); [Datacentres.com](https://www.datacentres.com/news/pjm-2028-2029-capacity-auction-short-of-reliability-requirement)
  - FERC large-load tariff show-cause orders (Jun 2026) — [Renewable Energy World](https://www.renewableenergyworld.com/energy-business/policy-and-regulation/ferc-takes-historic-action-orders-us-grid-operators-to-defend-or-revise-large-load-interconnection-tariffs/)
  - A shift in nuclear oversight with a Democratic Congress — [Daily Caller](https://dailycaller.com/2026/11/22/nrc-reactor-permits-long-mott-dow-texas-democrats-congress-nuclear-oversight/)
  - The Vistra CEO said a Texas moratorium would be "problematic" — [Benzinga](https://www.benzinga.com/news/26/11/62991016/vistra-q3-2026-earnings-call-transcript)
- **Supply response and pricing risk:**
  - Barclays warns that added capacity may squeeze AI data-center suppliers [SECONDARY] — [TokenPost](https://www.tokenpost.com/news/business/36057)
  - MHI is doubling GT capacity by 2030, and Ansaldo is re-entering the US — [Utility Dive](https://www.utilitydive.com/news/data-centers-mitsubishi-gas-turbines-earnings/875146/); [POWER](https://www.powermag.com/ansaldo-us-gas-turbine-market-equipment-crunch/)
  - Cummins and CAT are adding capacity, with most new capacity arriving 2027–2028 — [Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/cummins-q3-earnings-call-highlights-221433740.html); [Utility Dive](https://www.utilitydive.com/news/caterpillar-posts-highest-sales-quarter-ever-data-centers-q3-2026/873586/)
- **Execution risk:**
  - Fluence: ~$90m of penalties and a revenue miss — [GuruFocus](https://www.gurufocus.com/news/9218986/fluence-energy-flnc-reports-q4-revenue-of-744m-amid-manufacturing-delays)
  - Tesla energy revenue −16% YoY — [Energy-Storage.news](https://www.energy-storage.news/tesla-q3-2026-energy-storage-revenues-fall-despite-second-highest-quarterly-deployments/)
  - Bloom's negative quarterly FCF — [CryptoBriefing](https://cryptobriefing.com/bloom-energy-revenue-soars-cash-flow-dips/)
  - AAON gross-margin compression from new plants — [AAON](https://www.sec.gov/Archives/edgar/data/0000824142/000082414226000083/liveaaonpressreleaseexs.htm)
  - Modine EPS −33% — [StockTitan](https://www.stocktitan.net/news/MOD/modine-reports-second-quarter-fiscal-2027-3khyf8cqs3he.html)
- **Commodity and macro:**
  - Copper near an 11-month low (~$5.32/lb on 25 Nov) — [Kalkine](https://kalkine.com/news/mining/copper-slips-toward-an-11-month-low-freeport-mcmoran-nysefcx-and-southern-copper-nysescco)
  - "AI doubts and Fed bets" weighed on copper and miners (24 Nov) — [Rio Times](https://www.riotimesonline.com/copper-markets-latam-tuesday-november-24-2026/)
- **Counter-evidence (thesis intact):**
  - GEV orders reportedly +96% in Q3 [SECONDARY] — [Motley Fool](https://www.fool.com/investing/2026/11/10/ge-vernova-vertiv-and-bloom-energy-just-lost-10-to/)
  - Siemens Energy DC exposure is <10% of a €164bn backlog, so demand is diversified — [GuruFocus](https://www.gurufocus.com/news/9193800/siemens-energy-ag-smegf-q4-2026-earnings-call-highlights-record-results-eur164-billion-backlog-and-an-ambitious-2030-margin-target)
  - NRG held guidance and its DC project is on track — [Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/vistra-just-dropped-16-month-071339801.html)
  - Hyperscaler 2027 capex consensus +~28% [SECONDARY] — [YieldTheory](https://www.yieldtheory.app/research/hyperscaler-capex-2027-forecast)

### Inferences
- **Most fragile names**, ranked by fragility to a demand or sentiment shock:
  1. Pre-revenue SMR developers (OKLO, SMR, NNE): equity funds the whole path to first power (2027–2030+); dilution risk; NRC and political timing.
  2. BE: high multiple on fast but cash-consuming growth.
  3. Small/mid-cap DC thermal names with margin pressure (MOD, AAON).
  4. Merchant IPPs with Texas or PJM policy exposure (VST, NRG, TLN, CEG). Their multiples are already compressed, so the risk is more political than valuation-driven.
- **Most resilient:** backlog-rich electrical and grid names whose demand is broader than AI (ETN, HUBB, PWR, Siemens Energy, ABB, Schneider) and regulated utilities with rate-base growth (SO, AEP, D, XEL, NEE). Utilities face affordability and regulatory-lag risk instead.
- **Thesis-breaker checklist** for the study:
  - A hyperscaler capex cut or a sharp drop in the 2027 consensus (watch Q4 calls in late Jan/early Feb 2027)
  - A Texas DC pause or moratorium legislation in the 2027 session
  - PJM/FERC rules on co-location and DC cost allocation
  - Rising rates or inflation raising utility funding costs
  - Turbine and transformer capacity additions plus new entrants pressuring pricing from ~2028
  - Large-load queue attrition (Southern-type withdrawals)
  - Nvidia Kyber/800 VDC slippage
  - Copper/uranium price reversals for the miners
- Efficiency gains (better models or chips per watt) are a plausible long-run demand risk. No 2026-dated source quantifying them was retrieved (see Gaps).

### Gaps
- No sourced 2026 data on interest-rate moves, the Fed path, or utility funding-cost effects.
- No 2026 source quantifying AI efficiency gains (DeepSeek-type shocks, chips per watt, PUE) as a demand risk.
- The SoftBank charge detail comes from a low-quality source; it needs Reuters/Bloomberg confirmation.
- Forward multiples for most names are missing, so a systematic "extreme multiple" screen could not be run. The screener should compute forward P/E, EV/EBITDA and EV/sales live.

---

## 5. ETFs: power, grid, nuclear/uranium, utilities, copper, and 2025–2026 launches

### Takeaway
PAVE is the largest and cheapest broad play (0.47%, ~$12.3bn net assets, 1-yr NAV +12% to 31 Oct 2026). ZAP is the small, high-momentum electrification fund (0.50%, ~$442m). Nuclear and uranium ETFs swung from triple-digit 1-year gains in spring 2026 to losses by late October (NLR −33.4% and URA −25.9% over one year to 27 Oct), even as uranium term prices hit a record. 2026 launches target the DC supply chain and AI power (VanEck RACK, Wedbush IVEP, Defiance AIPO, VegaShares COOL).

### Cited Findings

| ETF | Focus | Expense ratio | AUM (date) | Performance (date) | Sources |
|---|---|---|---|---|---|
| PAVE (Global X US Infrastructure Development) | US infrastructure / grid build-out | 0.47% | ~$12.31bn net assets (20 Nov 2026, issuer); $13.49bn (other site, undated) | 1-yr NAV +11.96%; 3-yr +23.85% annualized (31 Oct 2026) | [Global X](https://www.globalxetfs.com/funds/pave); [TipRanks](https://www.tipranks.com/etf/pave/similar-etfs) |
| GRID (First Trust Nasdaq Clean Edge Smart Grid Infrastructure) | Global smart grid / electrification | ~0.56% (0.57% and 0.70% also cited) [CONFLICT] | n/f | 1-yr TR +3.91% (undated) [CONFLICT/unreliable] | [ETFdb](https://etfdb.com/etf/GRID/); [StockAnalysis](https://stockanalysis.com/etf/grid/); [FinanceCharts](https://www.financecharts.com/etfs/GRID) |
| ZAP (Global X US Electrification) | US electrification | 0.50% | $441.75m (undated) | Trailing 1-yr +42.29% (undated) | [ETFdb](https://etfdb.com/etf/ZAP/); [KoalaGains](https://koalagains.com/etfs/NASDAQ/ZAP) |
| NLR (VanEck Uranium & Nuclear) | Reactor operators, utilities, uranium | ~0.52% | n/f | 1-yr to 27 Oct 2026: −33.4%; 5-yr annualized 13.7%. YTD +18% and 1-yr +98% (29 Apr 2026); YTD ~−12% (mid-2026) | [Four Percent Rule](https://www.fourpercentrule.com/etfs/guides/uranium); [24/7 Wall St., Apr](https://247wallst.com/investing/2026/04/29/2-nuclear-etfs-positioned-to-capture-ais-power-demand-surge-in-2026/); [Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/2-nuclear-etfs-positioned-capture-101528755.html) |
| URA (Global X Uranium) | Uranium miners plus fuel cycle | ~0.69% | n/f | 1-yr to 27 Oct 2026: −25.9%; 5-yr annualized 9.8%. YTD +15% (18 Mar 2026) | [Four Percent Rule](https://www.fourpercentrule.com/etfs/guides/uranium); [24/7 Wall St., Mar](https://247wallst.com/investing/2026/03/18/the-nuclear-etfs-powering-ai-data-centers-and-posting-triple-digit-returns/) |
| URNM (Sprott Uranium Miners) | Pure uranium miners / physical | ~0.75% | n/f | YTD +26% and 1-yr +119% (29 Apr 2026); YTD ~−3% (19 Jul 2026) | [24/7 Wall St., Apr](https://247wallst.com/investing/2026/04/29/2-nuclear-etfs-positioned-to-capture-ais-power-demand-surge-in-2026/); [24/7 Wall St., Jul](https://247wallst.com/investing/2026/07/19/5-uranium-etfs-to-buy-before-nuclear-demand-triples-by-2050/) |
| NUKZ (Range Nuclear Renaissance) | Nuclear value chain incl. SMR developers | ~0.85% | n/f | 1-yr +73% (18 Mar 2026) [STALE] | [24/7 Wall St., Mar](https://247wallst.com/investing/2026/03/18/the-nuclear-etfs-powering-ai-data-centers-and-posting-triple-digit-returns/) |
| XLU (Utilities Select Sector SPDR) | S&P 500 utilities | n/f | n/f | n/f | gap |
| COPX (Global X Copper Miners) | Copper miners | n/f | n/f | n/f | gap |

- Expense ratios for NLR, URA, URNM and NUKZ come from one guide and vary slightly by source — [Four Percent Rule](https://www.fourpercentrule.com/etfs/guides/uranium)
- Other nuclear ETFs seen: First Trust Bloomberg Nuclear Power ETF (RCTR) and Sprott Junior Uranium Miners (URNJ). An early-2026 post showed URA +8.68%, RCTR +6.21%, URNJ +6.35% and URNM +5.90% YTD [STALE] — [ETF Tracker on X](https://x.com/TheETFTracker/status/2036129346486739393)

**2025–2026 launches in AI power / data-center infrastructure**
- **RACK** (VanEck Data Center Supply Chain ETF): launched 2 Jun 2026. Tracks the MarketVector Data Center Supply Chain Index (chips, power, cooling, grid); constituents need ≥50% of revenue from DC/AI infrastructure — [VanEck](https://www.vaneck.com/us/en/press-releases/vaneck-launches-data-center-supply-chain-etf-rack-to-capture-ai-infrastructure-buildout/); [Business Wire](https://www.businesswire.com/news/home/20260602638779/en/VanEck-Launches-Data-Center-Supply-Chain-ETF-RACK-to-Capture-AI-Infrastructure-Buildout)
- **IVEP** (Dan IVES Wedbush AI Power & Infrastructure ETF): announced 8 Apr 2026. Built on the "IVES Power 30" across generation, grid, data centers, equipment and materials — [National Law Review](https://natlawreview.com/press-releases/wedbush-launches-ai-power-infrastructure-etf-energy-becomes-key-force-behind)
- **AIPO** (Defiance AI & Power Infrastructure ETF): ≥50% revenue rule; largest holding PWR; named best new thematic ETF at the 2026 ETF.com Awards — [Simply Wall St](https://simplywall.st/etfs/us/nasdaq-aipo/news/the-ai-etf-betting-on-the-infrastructure-it-needs/amp)
- **COOL** (VegaShares; thermal and power management), "extremely new and currently small"; and **AIS** (VistaShares; broad AI supercycle) — [Dividend Vision](https://www.dividendvision.com/blog/ai-power-dividend-stocks-etfs)
- **"ETFS Global AI Infrastructure and Data Centres ETF (DTCR)"** began trading 10 Nov 2026, tracking the BITA Data Centre Critical Infrastructure Index (30 companies). This looks like a non-US (likely ASX) listing; do not confuse it with the US-listed Global X fund under the same code [VERIFY] — [WiseVoter](https://wisevoter.com/world/2026/11/10/etf-launches-global-ai-data-centre-fund)
- Expense ratios, AUM and performance for RACK, IVEP, AIPO, COOL and AIS were not retrieved.

### Inferences
- **Broad grid/electrification:** PAVE (cheapest and largest; but a generalist infrastructure fund with low AI-power purity) vs ZAP (purer electrification; small AUM means liquidity and closure risk). GRID's undated, conflicting performance data makes it hard to judge.
- **Nuclear:** NLR/NUKZ and URA/URNM diverge structurally. NLR and NUKZ hold reactor operators (CEG) and SMR developers (OKLO, SMR), so they were hit by the 2026 de-rating. URNM tracks miners and spot uranium more closely. The record term price ($99/lb) vs the ETF drawdowns argues for separating "fuel" exposure (CCJ, LEU, URNM) from "developer" exposure (NUKZ) in the study.
- **New AI-power ETFs** (RACK, IVEP, AIPO) launched near the 2026 peak in sentiment. They are useful as holdings maps for the screener, but there is no performance history yet.

### Gaps
- AUM and YTD/1-yr performance as of Nov 2026 for GRID, NLR, URA, URNM, NUKZ, XLU and COPX, and all data for XLU and COPX.
- Top holdings for every ETF; only AIPO's top holding (PWR) was retrieved.
- Expense ratios and AUM for RACK, IVEP, AIPO, COOL and AIS.
- A comprehensive list of other 2025–2026 launches, e.g., any iShares, SPDR or Invesco power-infrastructure funds.

---

## Screening universe — AI power & grid

Stage: leader = scaled, profitable incumbent with reported AI/DC-driven growth; emerging = real revenue/orders but early, small-cap or margin-immature; speculative = pre-revenue or option-value. "Data gap" means this round did not retrieve Q3-2026 data or market data; pull live before use.

| Ticker (Yahoo) | Name | Sub-theme | Stage | One-line thesis | Main risk |
|---|---|---|---|---|---|
| GEV | GE Vernova | Gas turbines; grid & electrification; SMR (BWRX-300) | leader | Gas backlog plus reservations 122 GW (Q3'26), targeting ≥130 GW by YE; BWRX-300 holds the first US SMR construction permit (TVA, Sep 2026); $20bn buyback | Multiple ~30–34x fwd after de-rating; turbine pricing peak as capacity grows toward 2030; DC capex pause |
| ENR.DE | Siemens Energy (OTC SMEGF) | Gas turbines; grid technology | leader | Record FY26: €164bn backlog, book-to-bill 1.54, 42 GW GT orders, 2030 margin target 20–22%, buybacks up to €9bn | Q4 book-to-bill slowed to 1.16; DC <10% of backlog (less AI torque); EUR/FX; market data gap |
| 7011.T | Mitsubishi Heavy Industries (OTC MHVYF) | Large-frame gas turbines | leader | 8 GW of 1H FY26 GT orders; ~37 GW backlog; doubling capacity by 2030 | Deliberately selective ordering; defense-spending headlines; CEO's view that BTM demand returns to utilities |
| CAT | Caterpillar | Recips, Solar turbines, gensets (BTM) | leader | Record $20.7bn quarter; Power Generation +30%; backlog ~$78bn (~2x YoY) | Construction/mining cyclicality; BTM project slippage |
| CMI | Cummins | Backup and prime gensets | leader | North American power gen +22%; 2026 power-gen revenue +15–25%; new capacity 2027–28 | Capacity timing; truck-engine cycle dilutes exposure |
| BE | Bloom Energy | SOFC on-site power (BTM) | emerging | Q3 revenue +138%; FY26 guide $4.4–4.6bn; S&P 500 inclusion; fastest-scaling non-turbine BTM option | **[HIGH VALUATION]** ~39–43x fwd and ~10x+ sales; negative quarterly FCF; mean reversion if grid interconnects catch up |
| CEG | Constellation Energy | Nuclear fleet plus Calpine gas (IPP) | leader | FY26 EPS raised to $12.50–12.80; hyperscaler nuclear uprate/restart deals; CyrusOne Texas campuses | −28% YTD on policy and AI-capex fears; PJM price cap and co-location rules; Calpine leverage |
| VST | Vistra | IPP (ERCOT/PJM) with nuclear and gas | leader | 2027 EBITDA guide $7.7–8.5bn; AWS 1.2 GW (Comanche Peak) and Meta 2.6 GW nuclear PPAs; uncontracted upside | Texas DC-pause politics (governor-elect); ERCOT concentration |
| TLN | Talen Energy | Nuclear (Susquehanna) plus PJM gas | leader | 2027 EBITDA/FCF +26–27%; $1.5bn ASR; AWS up to 1.9 GW; ~10x fwd P/E (single source) | PJM regulatory and capacity-price risk; AWS ramp timing |
| OKLO | Oklo | Advanced fission (Aurora) | speculative | $3.13bn cash; DOE PDSA approved; first power targeted late 2027–early 2028; Meta deal | **[PRE-REVENUE]** No NRC license application docketed; −75% YTD; ATM dilution |
| SMR | NuScale Power | SMR (US460 modules) | speculative | $1.9bn cash; ENTRA1–TVA program could become the largest US nuclear deployment | **[PRE-REVENUE]** No binding module order (TVA PPA is with ENTRA1); ~$0.3m Q3 revenue; −78% YTD |
| NNE | Nano Nuclear Energy | Microreactors | speculative | Option value on portable/micro reactors | **[PRE-REVENUE]** −48% YTD (9 Nov); fundamentals not retrieved |
| CCJ | Cameco | Uranium mining plus Westinghouse | leader | Realized $91.76/lb (Q3); term price record $99/lb (31 Oct); Westinghouse adj. EBITDA growing | 2026 production guide trimmed; Westinghouse lumpiness; spot/term spread |
| LEU | Centrus Energy | LEU/HALEU enrichment | emerging | Contingent enrichment backlog $5.4bn (from $3.0bn); HALEU production started; centrifuge build ahead of plan | Funding and execution of enrichment expansion; GAAP volatility from warrants |
| BWXT | BWX Technologies | Naval/commercial nuclear components and fuel | leader | Backlog $8.56bn (~46% converts by end-2027); Cambridge capacity +50%; centrifuge prototype | Government budget dependence; valuation data gap |
| ETN | Eaton | Electrical distribution, UPS, switchgear (800 VDC) | leader | Electrical backlog >$20bn (+46%); DC orders +101%; Electrical Americas margin 29.8% | DC order lumpiness; valuation data gap |
| HUBB | Hubbell | Utility T&D components plus DC electrical | leader | DC sales +80% organic; FY EPS $20.40–20.60; heavy utility T&D exposure | Utility growth only mid-single-digit; shares fell on Q3 |
| PWR | Quanta Services | Grid and DC EPC | leader | Record $63.7bn backlog (~1.5x revenue); FY26 revenue $41.3–41.6bn; top AIPO holding | Lumpy awards; craft-labor constraints; valuation data gap |
| MYRG | MYR Group | Transmission & distribution EPC | emerging | Smaller-cap lever on utility T&D capex growth (AEP $100bn, SO up to ~$100bn) | Q3-2026 data not retrieved; contractor margin risk |
| POWL | Powell Industries | MV switchgear and e-houses | emerging | Backlog $2.7bn (+96% YoY, ~2x revenue); 1.8x book-to-bill | Order cancellation or modification; backlog conversion and capacity |
| ABBNY | ABB (ADR; ABBN.SW) | Electrification, grid, DC power | leader | Record $12.06bn orders (+40%); Electrification +70%; US +82% | EPS miss; industry capacity additions squeezing margins (Barclays) |
| SBGSY | Schneider Electric (ADR; SU.PA) | DC power and cooling, electrification | leader | Q3 revenue +16.9% organic; DC demand up triple digits; ~30% of revenue in DC & networks | DC cyclicality at ~30% of revenue; EUR/FX |
| 267260.KS | HD Hyundai Electric | Power transformers (US exports) | leader | 24.1% operating margin; backlog $8.84bn (+26.6% YoY); expanding capacity; reported Nvidia 800 VDC talks | Q3 orders −19% YoY; US tariff/trade risk; net-profit miss |
| PRY.MI | Prysmian | HV/HVDC and grid cables | leader | Cable/HVDC scarcity beneficiary as transmission build lags need | Q3-2026 data not retrieved; HVDC US order evidence absent |
| VRT | Vertiv | DC power and thermal (incl. 800 V architecture) | leader | Q3 sales +61%, organic orders >100%, FY26 guide ~$14.65bn; "above-market" 2027 growth | −12.9% on 4 Nov; highly sensitive to DC capex; competition from scaled peers |
| NVT | nVent Electric | Liquid cooling, enclosures, electrical | leader | Sales +44% organic; FY guide raised to +38–39%; modular liquid-cooling orders | Shares fell on a beat (high expectations); order growth only low double digits |
| MOD | Modine Manufacturing | DC thermal (chillers, CDUs) | emerging | DC sales +95%; first >$1bn DC order quarter; FY DC growth guide 80–90% | EPS −33% (cost/ramp); possible corporate rename/separation ("Modexus") — verify |
| TT | Trane Technologies | Chillers and DC thermal | leader | Backlog $12.5bn (>$8bn for 2027+); ~1,700 large projects tracked, >90% DC | Margin pressure; lumpy DC orders |
| JCI | Johnson Controls | DC thermal plus building systems | leader | Orders +44%; backlog $23bn (+43%); Americas backlog +54% | Order-definition changes cloud growth; execution |
| AAON | AAON | DC liquid/air cooling (BASX) | emerging | BASX sales +218% to $397m; total sales +84% | Gross-margin compression from immature plants; customer concentration |
| NEE | NextEra Energy | Utility plus renewables/storage developer; DC hubs | leader | Backlog 36.7 GW; >20 GW DC hub pipeline; Duane Arnold restart for Google | Q3 EPS reporting conflict; renewables policy; rate sensitivity |
| D | Dominion Energy | Virginia DC-load utility | leader | 54.9 GW DC pipeline incl. 12.2 GW of ESAs; ~$65bn capex | Affordability and regulation; offshore-wind cost overrun risk |
| SO | Southern Company | Southeast DC-load utility | leader | 21 GW signed plus 7 GW late-stage large load; capex $81–85bn, possibly ~$100bn | Queue attrition (14.3 GW withdrawn earlier in 2026); equity funding |
| AEP | American Electric Power | Transmission-heavy DC-load utility | leader | Capex raised to $100bn (from $78bn), ~$37bn transmission; 15 GW of new load commitments in Q3 | Regulatory approvals; financing and dilution; secondary-source figures need verification |
| WMB | Williams Companies | Gas pipelines plus BTM power developer | leader | ~$9.6bn committed across six power projects; 6+ GW pipeline; 11%+ EBITDA CAGR target to 2030 | Permitting and contract timing; leverage ~3.75x |
| KMI | Kinder Morgan | Gas pipelines (Southeast/Texas power demand) | leader | Backlog $14.4bn (+$4.7bn QoQ), >75% tied to power and LDCs; >200 GW of Southeast large-load requests | Load-forecast overstatement (IEEFA) |
| ET | Energy Transfer | Gas pipelines plus direct DC gas supply | leader | Direct DC supply deals (CloudBurst, Oracle; ~0.9 Bcf/d to three DCs, reported) | Customer final investment decisions pending; Q3-2026 data not retrieved |
| FLNC | Fluence Energy | Grid/DC battery storage | emerging | Record $3.5bn Q4 orders; backlog ~$8.9bn (+68% YoY); ~$3bn/yr conversion | Manufacturing delays and ~$90m penalties; no FY27 guidance until Feb 2027; interim CEO |
| FCX | Freeport-McMoRan | Copper | leader | Grasberg ramp to near-full by end-2027; 2027 copper sales +>20% | Copper near an 11-month low (25 Nov); Grasberg execution; 2027 capex +$400m |
| ON | onsemi | SiC power semis for 800 V AI power | emerging | Q3 DC revenue ~$180m (+175%, secondary); AI DC revenue more than doubling in 2026 | DC still a small share of revenue; auto/industrial downcycle |

Additional watchlist, beyond the 40-name cap: XEL (Xcel; $70bn plan, +1/+3 GW of DC ESAs) · ETR (Entergy; data gap) · EQT (Homer City gas supply) · EOSE (Eos; zinc LDES, [SPECULATIVE], data gap) · TSLA (Megapack; energy is a small share of Tesla's value) · SCCO (Southern Copper) · 6501.T / HTHIY (Hitachi; HVDC/transformers, data gap) · IFNNY / IFX.DE (Infineon; AI power semis) · WOLF (Wolfspeed; SiC) · NVTS (Navitas; GaN, [SPECULATIVE]) · ORA (Ormat; geothermal) · Fervo Energy (IPO May 2026; ticker not verified) · NRG (IPP; 1.2 GW DC project; −42% YTD) · UEC (Uranium Energy; unhedged US utility contracts) · ETFs: PAVE, ZAP, GRID, NLR, NUKZ, URA, URNM, XLU, COPX, RACK, AIPO, IVEP.
