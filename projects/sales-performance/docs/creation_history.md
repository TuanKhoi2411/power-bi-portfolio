# Creation history and provenance

## Source task

Dashboard-development task: `019f8896-46eb-7fa1-88ac-a344a69e62e5` (`Build Power BI dashboard`).

Repository-wide recovered workflow: [`../../../docs/BUILD_PROVENANCE.md`](../../../docs/BUILD_PROVENANCE.md).

This file records decisions from that task as provenance. The current PBIP/TMDL in this repository remains the implementation source of truth.

## Build sequence recovered from the task

1. A reference PBIX was inspected for layout DNA: header, navigation rail, slicer stack, KPI cards, sparklines, chart zones, spacing, and palette.
2. Three public datasets were selected for separate Sales, Finance, and Marketing products rather than a cross-domain model.
3. Sales loaded 541,909 transaction rows from UCI Online Retail.
4. An initial combined PBIP was built, then corrected for PBIR page-folder naming, `activePageName`, and report-page discovery errors.
5. The Sales model received base, MoM, YoY, variance, quality, merchandise, ranking, customer, and KPI-display measures.
6. Top-country and top-product visuals were corrected to use explicit Top 5 ranking measures and to exclude fees/postage/invalid merchandise descriptions.
7. Date filtering was changed to a calendar range appropriate for the continuous Sales date field.
8. The project was separated into its own PBIP and expanded from Overview to Customer Insights and Product & Returns.
9. Deep-dive pages were deliberately given different chart arrangements rather than duplicating the Overview grid.
10. The final Sales theme retained purple as its primary analytical accent and a clean white-card layout.

## Current implementation versus intermediate history

The task history contains intermediate combined-project measure counts. The current standalone canonical model contains **74 measures**, **3 pages**, and **84 report visuals**. Always use current TMDL and `qa/structural_validation.json` rather than an intermediate chat count.

## Rebuild intent

The repository package is designed so an agent can reproduce the model/report logic without needing the old chat. The task ID is retained only to explain design decisions and evolution.
