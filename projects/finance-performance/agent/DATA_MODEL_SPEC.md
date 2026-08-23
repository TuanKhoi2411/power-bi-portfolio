# Data and semantic-model specification

## Source contract

| Item | Contract |
|---|---|
| Publisher | U.S. Securities and Exchange Commission — EDGAR company facts |
| Entity | Apple Inc. |
| Local file | `../data/sec-aapl-companyfacts.json` |
| Observation grain | One reported metric fact for a period/frame, filing form, unit, and accession |
| Forms | Primarily 10-K and 10-Q facts used by the model |
| Quality conditions | Restatements, duplicate/overlapping facts, taxonomy changes, units, instant vs duration facts |

## Model contract

| Table | Role | Required key/date |
|---|---|---|
| `FactFinance` | Normalized SEC facts and measure home | metric/period/filing metadata, `EndDate` |
| `DimDate` | Calendar dimension | `Date` |

Active relationship: `FactFinance[EndDate]` → `DimDate[Date]`.

Canonical definitions:

- `../dashboard/Apple_Finance.SemanticModel/definition/tables/FactFinance.tmdl`
- `../dashboard/Apple_Finance.SemanticModel/definition/tables/DimDate.tmdl`
- `../dashboard/Apple_Finance.SemanticModel/definition/relationships.tmdl`

## Required fact fields

`Company`, `CIK`, `DisplayMetric`, `Concept`, `MetricClass`, `MetricSort`, `PeriodType`, `PeriodLabel`, `StartDate`, `EndDate`, `FiscalYear`, `FiscalPeriod`, `Value`, `Form`, `FiledDate`, `Frame`, and `AccessionNumber`.

## Measure contract

`FactFinance.tmdl` currently contains 90 measures.

Required measure families:

- Revenue, Cost of Sales, Gross Profit, Operating Expenses, Operating Income, Net Income
- Assets, Liabilities, Cash and related balance/liquidity measures
- Gross, operating, and net margins
- Latest-period values and deterministic prior-period/YoY comparisons
- Ratios and formatted KPI display measures

Do not use formatted display measures for numeric sorting, chart axes, or reconciliation.

## Fact-selection rules

- Preserve USD/unit scale.
- Select facts consistently by concept, form, fiscal period, frame, and filing/version rules.
- Avoid summing annual and quarterly duration facts in the same period context.
- For point-in-time metrics, use the value at the period end rather than summing values.
- If multiple filings report the same period, use a documented latest-filing or accession rule and preserve traceability.

## Minimum reconciliation

- Gross Profit = Revenue − Cost of Sales for matched periods when concepts permit.
- Operating and net margins use the same-period Revenue denominator.
- Balance equation direction is plausible for each selected point-in-time period.
- Latest and YoY cards reconcile to the trend series and detail table.

## Limitations

- SEC taxonomy and company reporting practices change over time.
- Reported financial facts do not alone establish future performance or valuation.
- This project is analytical evidence, not investment advice.
