# Changelog v2

- Replaced the overlapping current/prior-month line chart with a waterfall of the direct net-sales change versus the preceding month.
- Added `Completed Month Net Sales MoM Change`; it suppresses the latest partial month so an incomplete period is not presented as a real decline.

- Created a standalone PBIP package; original files remain untouched.
- Renamed Report/SemanticModel pointers with a `_v2` suffix.
- Repointed Power Query to the included workbook.
- Restricted DimDate to the actual sales date range.
- Added Identified Orders, Customer Net Sales Coverage, Gross-to-Net Reconciliation Residual, and Latest Period Status.
- Revised Orders per Customer and Customer Coverage movement/display logic.
- Revised prior-year Net Sales to compare equivalent elapsed days for a partial month.
- Rebound Customer Insights coverage KPI/sparkline to value-based coverage.
- Replaced the one-point prior-year comparison with a complete month-over-month trend series.
- Replaced parallel Identified-versus-Total lines with a stacked Identified-versus-Anonymous monthly sales mix.
# 2026-08-25 — Returns and customer insight redesign

- Replaced transaction-type columns with gross-sales retention composition: Net Sales retained versus Returns.
- Replaced the scale-mismatched monthly returns line with Net Sales columns and Return Rate on a secondary axis.
- Limited the customer-base country view to the Top 5 countries to remove the scrollbar from the compact panel.
- Replaced opaque customer-ID rankings with identified-customer sales concentration: Top 10 versus all other identified customers.
- Added customer concentration and customer-country ranking measures; all are used in report visuals.

# 2026-08-27 — Customer identity and usefulness correction

- Confirmed the source workbook contains only `CustomerID`; it has no customer-name field, so synthetic labels such as `Customer 12346` are no longer shown as names.
- Replaced the Top 10 customer concentration donut with Repeat versus One-time Customers, a direct loyalty and retention view.
- Replaced the ID-level customer table with Customer Economics by Country: customer count, repeat rate, identified net sales, orders per customer, and return rate.
- Replaced the customer-ID slicer with a Customer status slicer (`Identified customer` / `Unknown customer`).
- Hid the synthetic customer-label column from the report field list while retaining `CustomerKey` for model relationships and calculations.
