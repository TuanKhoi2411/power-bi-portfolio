# Agent build prompt — Apple Inc. Financial Performance

## Objective

Build or enhance a three-page Power BI Finance dashboard that answers:

> Are Apple Inc.'s growth, margins, liquidity, and cost structure moving sustainably according to official filings?

Use the included SEC EDGAR company-facts JSON and existing PBIP. Do not add analyst estimates, targets, market prices, forecasts, or investment recommendations unless separately sourced and explicitly requested.

## Required deliverables

1. Refreshable PBIP plus `Apple_Inc_Financial_Performance_Dashboard.pbix`.
2. Pages `Apple Finance`, `Profitability & Growth`, and `Balance & Liquidity`.
3. Reconciled revenue, gross profit, operating income, net income, assets, liabilities, cash, margins, growth, and liquidity measures.
4. Working navigation, slicers, reset, cross-filtering, and readable 1280×720 pages.
5. Explicit SEC source and analytical-limit disclosures.

## Execution sequence

1. Inspect `../data/sec-aapl-companyfacts.json` and confirm company, CIK, units, forms, filing dates, accession numbers, fiscal periods, frames, and duplicates.
2. Update the `FactFinance` `SourcePath` and refresh.
3. Validate the `FactFinance[EndDate]` → `DimDate[Date]` relationship.
4. Preserve or intentionally revise the 90 canonical measures in `FactFinance.tmdl`.
5. Implement `REPORT_SPEC.md` and complete `BUILD_AND_QA.md`.
6. Save the PBIP and PBIX, then close/reopen the PBIX for final review.

## Acceptance criteria

- Duration and instant facts are not combined incorrectly.
- Fiscal period labels, dates, forms, units, and filing versions are traceable.
- Latest-value and YoY measures use deterministic period selection.
- Revenue, gross profit, operating income, and net income trends reconcile to selected SEC facts.
- The report does not imply an investment recommendation.
