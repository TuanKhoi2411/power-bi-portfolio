# UK Online Retail — Sales Performance

## Management question

Where is commercial growth coming from, which customers and products drive the result, and how do returns affect sales quality?

## Dashboard

| Item | Detail |
|---|---|
| Power BI files | [`UK_Online_Retail_Sales_Performance_Dashboard.pbix`](./UK_Online_Retail_Sales_Performance_Dashboard.pbix) and [`dashboard/UK_Online_Retail_Sales_Performance_Dashboard.pbip`](./dashboard/UK_Online_Retail_Sales_Performance_Dashboard.pbip) |
| Pages | UK Retail Sales · Customer Insights · Product & Returns |
| Canvas | 1280 × 720 on every page |
| Semantic model | FactSales + DimDate, 74 authored measures |
| Source | UCI Online Retail, transactions from 2010-12-01 to 2011-12-09 |

The report moves from overall sales direction into customer concentration, product performance, and return behavior. It is a separate Sales model rather than a cross-domain comparison.

## Interactive presentation

[`UK_Online_Retail_Sales_Performance_Interactive.html`](./UK_Online_Retail_Sales_Performance_Interactive.html) is the accompanying 12-slide decision story. Download the file and open it in Chrome or Edge; all ten chart images are embedded for offline viewing.

Controls: `←` / `→` or `Space` to navigate, `F` for fullscreen, and `O` for overview.

## Source and refresh

- Included source: [`data/Online Retail.xlsx`](./data/Online%20Retail.xlsx)
- Publisher: [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/352/online+retail)
- The PBIX is the easiest review artifact because its imported model is already packaged.
- The PBIP query retains the original local `SourcePath`. Before refreshing the PBIP on another computer, replace that value in `FactSales.tmdl` with the absolute path to the included workbook.

## Verification and limits

- Project definition contains a report, semantic model, valid active page, and three report pages.
- The HTML deck contains 12 slides, embedded visuals, and keyboard navigation.
- Dashboard definitions and files were preserved from the source task; a fresh Power BI Desktop reopen was not performed during this repository packaging step.
