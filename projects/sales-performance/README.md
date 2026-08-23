# UK Online Retail — Sales Performance

Power BI portfolio project for commercial performance, customer concentration, product contribution, and return-quality analysis.

## Review in 60 seconds

| Question | Answer |
|---|---|
| Management question | Where is commercial growth coming from, which customers and products drive the result, and how do returns affect sales quality? |
| What I built | A three-page Power BI report, semantic model, packaged PBIX, and a 12-slide management story. |
| Evidence | UCI Online Retail transactions covering 1 December 2010 to 9 December 2011. |
| Status | PBIX, PBIP, source workbook, and HTML story are published. |

## Goal

Build a sales review product that helps management:

- Establish sales direction and transaction quality.
- Identify valuable customers and concentration risk.
- Compare product contribution and return behavior.
- Move from headline performance into evidence-backed commercial action.

## Dashboard pages

| Page | Decision lens |
|---|---|
| UK Retail Sales | Establish scale, trend, sales quality, and overall direction. |
| Customer Insights | Identify customer value, concentration, and behavior. |
| Product & Returns | Compare product contribution and investigate return patterns. |

## Key portfolio signals

- Three report pages at 1280 × 720.
- `FactSales` plus a dedicated `DimDate` table.
- 74 authored measures.
- Public, source-backed transactional data.
- Separate report and semantic-model definitions in PBIP format.

## Main artifacts

| Artifact | Use |
|---|---|
| [`UK_Online_Retail_Sales_Performance_Dashboard.pbix`](./UK_Online_Retail_Sales_Performance_Dashboard.pbix) | Fastest way to inspect the imported model and interactive report. |
| [`dashboard/UK_Online_Retail_Sales_Performance_Dashboard.pbip`](./dashboard/UK_Online_Retail_Sales_Performance_Dashboard.pbip) | Entry point for the source-controlled Power BI project. |
| [`UK_Online_Retail_Sales_Performance_Interactive.html`](./UK_Online_Retail_Sales_Performance_Interactive.html) | Standalone 12-slide management story; download and open in Chrome or Edge. |
| [`data/Online Retail.xlsx`](./data/Online%20Retail.xlsx) | Raw public source workbook used by the model. |

## Data and model

- Publisher: [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/352/online+retail).
- Grain: transaction-line sales records.
- Model: `FactSales` related to `DimDate`.
- The PBIP query retains the original local `SourcePath`. Before refreshing on another computer, replace it in `FactSales.tmdl` with the absolute path to the included workbook.

## How to review

1. Open the HTML story for the executive narrative.
2. Open the PBIX in Power BI Desktop for immediate interaction.
3. Use the PBIP only after downloading the complete `dashboard/` directory.
4. Review customer and product pages after establishing the overall direction on the first page.

HTML controls: `←` / `→` or `Space` to navigate, `F` for fullscreen, and `O` for overview.

## QA status and limits

- The PBIP contains a report, semantic model, three pages, and a valid active-page reference.
- The HTML story contains 12 slides, embedded visuals, and keyboard navigation.
- The source task validated the dashboard definitions; a fresh Power BI Desktop reopen was not performed during repository packaging.
- Historical transactions describe the supplied period and should not be treated as a current commercial forecast.

## Portfolio talking points

- Connects sales scale with customer concentration, product contribution, and return quality.
- Demonstrates Power BI modeling, DAX, navigation, and management storytelling.
- Publishes both a reviewer-friendly PBIX and a source-controlled PBIP structure.

## Agent build package

To rebuild or extend this dashboard with an agent, start with the [full creation prompt](./BI_Dashboard_Creation_Prompt.md) and [project instructions](./AGENTS.md). The package also includes [exact DAX](./model/measures.dax), [measure catalog](./model/measure_catalog.csv), [data dictionary](./model/data_dictionary.md), [Power Query](./powerbi/PowerQuery_M.txt), [PBIX build instructions](./powerbi/PBIX_build_instructions.md), [creation history](./docs/creation_history.md), and [QA results](./qa/validation_results.md).
