# Semantic-model notes

## Architecture

- `FactFinance`: normalized SEC company facts plus the 90-measure library.
- `DimDate`: date dimension linked by fact `EndDate`.

Relationship: `FactFinance[EndDate]` → `DimDate[Date]`.

## Calculation layers

1. Base quarterly/period values: Revenue, Cost of Sales, Gross Profit, Operating Expenses, Operating Income, Net Income.
2. Balance-sheet values: Assets, Liabilities, Cash and related point-in-time facts.
3. Ratios: gross, operating, and net margin; supported coverage/liquidity ratios.
4. Movement: latest, prior-period, YoY, and variance logic.
5. Display: KPI text/scale helpers.

## Important decisions

- `PeriodType` distinguishes instant and duration facts.
- Filing/accession metadata remains in the fact table to support deterministic fact selection and traceability.
- Point-in-time values are selected, not summed across dates.
- Flow metrics are compared on compatible duration/fiscal periods.
- SEC restatements and taxonomy evolution are explicit limitations.

Canonical TMDL is authoritative; exported `model/` files must be regenerated after changes.
