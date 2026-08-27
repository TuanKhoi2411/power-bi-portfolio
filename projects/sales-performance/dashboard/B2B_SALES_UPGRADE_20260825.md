# B2B-style sales analytics upgrade — 25 Aug 2026

## Scope

This revision improves the existing model-connected UK Online Retail report without changing the source data, visual theme, or approved three-page structure. The original working project was copied before any edit.

Backup:

`C:\pbi-portfolio-v2\UK_Online_Retail_Sales_Performance_v2\dashboard\_backup_before_b2b_measure_upgrade_20260825\UK_Online_Retail_Sales_ModelConnected`

## Model and measure changes

- Added `DimCountry[MarketGroup]` to distinguish the United Kingdom from international markets through the existing Country relationship.
- Added geographic concentration measures: `UK Net Sales` and `UK Sales Share`.
- Added customer concentration measure: `Top 10 Customer Sales Share`.
- Added product concentration measures: `Top 10 Product Sales`, `Top 10 Product Sales Share`, latest completed-month share, previous-month share, and percentage-point variance.
- Added retention-value measures: `Repeat Customer Net Sales`, `Repeat Customer Revenue Share`, latest completed-month share, previous-month share, and percentage-point variance.
- Added display measures for the new customer-retention and product-concentration KPI cards.
- The model now contains 6 tables, 5 active one-to-many relationships, and 100 explicit measures.

## Report changes

- **UK Retail Sales:** replaced the ambiguous transaction-type donut, which mixed Gross Sales and Returns in one visual, with `Core vs International Net Sales`. The new donut uses `DimCountry[MarketGroup]` and `[Net Sales]`, so it communicates geographic concentration directly.
- **Customer Insights:** replaced the duplicated customer-coverage KPI with `Repeat Revenue`, showing the latest completed month's repeat-customer revenue share, its month-over-month percentage-point movement, and a monthly sparkline.
- **Product & Returns:** replaced the low-value product-count KPI with `Top 10 Share`, showing latest completed-month product concentration, month-over-month percentage-point movement, and its monthly sparkline.
- Existing Customer Coverage remains visible in the known-versus-anonymous sales comparison, so the data-quality message is preserved without duplicating the same idea in the KPI row.

## Source-data cross-check

The calculations were independently checked against `data\Online Retail.xlsx` (541,909 rows):

- Net Sales: **£9,747,747.93**
- UK Net Sales: **£8,187,806.36** (**84.00%** of total)
- Identified-customer Net Sales: **£8,300,065.81**
- Repeat-customer Net Sales: **£7,789,363.34** (**93.85%** of identified-customer sales across the full source period)
- Merchandise Net Sales: **£10,283,210.06**
- Top-10 product sales: **£970,100.89** (**9.43%** of merchandise sales, using StockCode-level validation)

## Validation

- All report JSON files parse successfully.
- Every report field reference resolves to a table column or explicit measure.
- No duplicate measure names or lineage tags were introduced.
- No files outside the Sales project were changed.
