# Apple Inc. — Financial Performance

Power BI portfolio project for public-company growth, profitability, balance-sheet resilience, and liquidity analysis.

## Review in 60 seconds

| Question | Answer |
|---|---|
| Management question | Are revenue growth, margin expansion, balance-sheet resilience, and operating costs moving sustainably? |
| What I built | A three-page Power BI report, semantic model, and a 12-slide executive story. |
| Evidence | Apple Inc. SEC EDGAR Company Facts from forms 10-K and 10-Q. |
| Status | PBIX, PBIP, SEC source JSON, and HTML story are published. |

## Goal

Build a finance review product that helps a reviewer:

- Establish the direction of growth and profitability.
- Compare margin and operating-cost behavior over time.
- Assess balance-sheet capacity and liquidity constraints.
- Trace conclusions back to public filing data.

## Dashboard pages

| Page | Decision lens |
|---|---|
| Apple Finance | Establish headline performance and current direction. |
| Profitability & Growth | Compare revenue, margins, and operating cost behavior. |
| Balance & Liquidity | Review financial capacity, liquidity, and balance-sheet resilience. |

## Key portfolio signals

- Three report pages at 1280 × 720.
- `FactFinance` plus a dedicated `DimDate` table.
- 90 authored measures.
- Source-backed SEC filing data.
- Separate profitability and balance-sheet decision lenses.

## Main artifacts

| Artifact | Use |
|---|---|
| [`Apple_Inc_Financial_Performance_Dashboard.pbix`](./Apple_Inc_Financial_Performance_Dashboard.pbix) | Packaged Power BI report for immediate review in Power BI Desktop. |
| [`dashboard/Apple_Inc_Financial_Performance_Dashboard.pbip`](./dashboard/Apple_Inc_Financial_Performance_Dashboard.pbip) | Entry point for the complete PBIP report and semantic model. |
| [`Apple_Inc_Financial_Performance_Interactive.html`](./Apple_Inc_Financial_Performance_Interactive.html) | Standalone 12-slide executive story; download and open in Chrome or Edge. |
| [`data/sec-aapl-companyfacts.json`](./data/sec-aapl-companyfacts.json) | SEC EDGAR Company Facts response retained for traceability. |

## Data and model

- Publisher: [SEC EDGAR Company Facts API](https://data.sec.gov/api/xbrl/companyfacts/CIK0000320193.json).
- Filing scope: Apple Inc. forms 10-K and 10-Q represented in the source response.
- Model: `FactFinance` related to `DimDate`.
- Before refreshing on another computer, replace `SourcePath` in `FactFinance.tmdl` with the absolute path to the included JSON file.

## How to review

1. Open the HTML story for the executive interpretation.
2. Open the PBIX for immediate dashboard interaction in Power BI Desktop.
3. For model inspection, download the complete `dashboard/` folder before opening the PBIP file.
4. Review profitability first, then use the balance and liquidity page to challenge the operating story.

HTML controls: `←` / `→` or `Space` to navigate, `F` for fullscreen, and `O` for overview.

## QA status and limits

- The PBIP contains the project pointer, report definition, semantic model, three pages, and a valid active-page reference.
- The PBIP was opened in Power BI Desktop with its visuals and data model loaded, then exported to the published PBIX.
- The HTML story contains 12 slides, embedded visuals, and keyboard navigation.
- A separate post-export reopen of the PBIX was not performed during this update.
- SEC facts can contain restatements and taxonomy changes; period selection should be reviewed before extending the model.
- This case is analytical portfolio work, not an investment recommendation.

## Portfolio talking points

- Converts XBRL filing data into an accessible management view.
- Separates operating performance from balance-sheet and liquidity analysis.
- Demonstrates source traceability, finance measures, and executive storytelling.

## Agent build package

To rebuild or extend this dashboard with an agent, start with [project instructions](./AGENTS.md), then use the [copy-ready build prompt](./agent/BUILD_PROMPT.md), [data/model contract](./agent/DATA_MODEL_SPEC.md), [report blueprint](./agent/REPORT_SPEC.md), and [build/QA checklist](./agent/BUILD_AND_QA.md).
