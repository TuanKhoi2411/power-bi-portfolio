# Apple Financial Performance

## Management question

Are revenue growth, margin expansion, balance-sheet resilience, and operating costs moving in a sustainable direction?

## Dashboard

| Item | Detail |
|---|---|
| Power BI project | [`dashboard/Apple_Finance.pbip`](./dashboard/Apple_Finance.pbip) |
| Pages | Apple Finance · Profitability & Growth · Balance & Liquidity |
| Canvas | 1280 × 720 on every page |
| Semantic model | FactFinance + DimDate, 90 authored measures |
| Source | SEC EDGAR XBRL Company Facts for Apple Inc., forms 10-K and 10-Q |

The report moves from headline financial performance into profitability, growth consistency, balance-sheet capacity, and liquidity constraints.

## Interactive presentation

[`Finance_Performance_Interactive.html`](./Finance_Performance_Interactive.html) is the accompanying 12-slide decision story. Download it and open locally in Chrome or Edge; all ten chart images are embedded.

Controls: `←` / `→` or `Space` to navigate, `F` for fullscreen, and `O` for overview.

## Source and refresh

- Included source: [`data/sec-aapl-companyfacts.json`](./data/sec-aapl-companyfacts.json)
- Publisher: [SEC EDGAR Company Facts API](https://data.sec.gov/api/xbrl/companyfacts/CIK0000320193.json)
- Before refreshing on another computer, replace `SourcePath` in `FactFinance.tmdl` with the absolute path to the included JSON file.

## Verification and limits

- PBIP package contains the project pointer, report definition, semantic model, valid active page, and three report pages.
- The HTML deck contains 12 slides, embedded visuals, and keyboard navigation.
- Public filings can contain restatements and taxonomy changes; source-period selection should be reviewed before extending the model.
- A fresh Power BI Desktop reopen was not performed during this repository packaging step.
