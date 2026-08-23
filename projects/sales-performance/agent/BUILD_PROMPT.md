# Agent build prompt — UK Online Retail Sales Performance

## Objective

Build or enhance a three-page Power BI Sales dashboard that answers:

> Where is growth coming from, which customers and products matter, and how do returns affect sales quality?

Use only the included UCI Online Retail source and the existing PBIP definitions. Do not invent records, KPIs, targets, or findings.

## Required inputs

- `../data/Online Retail.xlsx`
- `../dashboard/UK_Online_Retail_Sales_Performance_Dashboard.pbip`
- `DATA_MODEL_SPEC.md`
- `REPORT_SPEC.md`
- `BUILD_AND_QA.md`

## Required deliverables

1. A refreshable PBIP with the existing report and semantic-model folders intact.
2. A packaged `UK_Online_Retail_Sales_Performance_Dashboard.pbix`.
3. Three working pages: `UK Retail Sales`, `Customer Insights`, and `Product & Returns`.
4. Working page navigation, slicers, reset action, cross-filtering, and readable 1280×720 layouts.
5. Reconciled Sales, returns, order, unit, customer, country, and product measures.
6. An updated QA/status record in `BUILD_AND_QA.md` if implementation changes artifact truth.

## Execution sequence

1. Profile the workbook and confirm columns, types, grain, date span, missing customer IDs, cancellations, non-positive quantities, and non-positive prices.
2. Update the `SourcePath` used by the `FactSales` partition.
3. Refresh and validate `FactSales` and `DimDate`; keep the active `FactSales[SalesDate]` → `DimDate[Date]` relationship.
4. Preserve or intentionally update the existing 74 measures in `FactSales.tmdl`.
5. Implement the page blueprint in `REPORT_SPEC.md`.
6. Complete all checks in `BUILD_AND_QA.md`.
7. Open the final PBIX in Power BI Desktop and visually inspect every page before claiming completion.

## Acceptance criteria

- No unresolved refresh, relationship, DAX, or visual errors.
- Gross sales, returns, and net sales reconcile using the documented sign logic.
- Top-N visuals are sorted by numeric measures, not formatted text.
- Customer analysis discloses incomplete customer identification.
- PBIP and PBIX names remain stable so portfolio links do not break.
