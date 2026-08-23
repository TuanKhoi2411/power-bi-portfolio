# Semantic-model notes

## Architecture

The project uses a compact two-table model:

- `FactSales`: transaction-line fact table, derived quality fields, and the 74-measure library.
- `DimDate`: contiguous calendar used for time intelligence and chronological sorting.

The single active relationship is `FactSales[SalesDate]` to `DimDate[Date]`. Keep filter direction from the date dimension to the fact table.

## Calculation layers

1. **Base totals** — Gross Sales, Return Amount, Net Sales, Units, Orders, Customers.
2. **Efficiency and quality** — Average Order Value, Average Selling Price, Return Rate, Gross-to-Net, customer coverage.
3. **Movement** — previous month, MoM, previous year, YoY, percentage-point movement.
4. **Ranking** — merchandise filters, country/product/customer ranks, Top 5/Top 10 outputs.
5. **Display** — formatted KPI strings and supporting text. These are not numeric analytical measures.

## Important design decisions

- Partial December data is handled in month-movement measures so an incomplete month is not blindly compared with a complete prior month.
- Returns/cancellations are retained and modeled, not dropped.
- Anonymous customer sales remain part of company totals but are excluded from identified-customer counts/analysis where appropriate.
- Merchandise ranking excludes non-product codes such as postage, fees, adjustments, and invalid descriptions.

## Canonical implementation

The TMDL under `dashboard/UK_Online_Retail_Sales.SemanticModel/definition/` is authoritative. Files under `model/` are human/agent-readable exports and must be regenerated after TMDL changes.
