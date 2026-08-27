# Data dictionary

Auto-exported from the canonical TMDL tables. Business rules and source limitations are documented in `../agent/DATA_MODEL_SPEC.md`.

| Table | Column | Data type | Source column | Format | Summarization |
|---|---|---|---|---|---|
| DimDate | Date | dateTime | [Date] | M/d/yyyy | none |
| DimDate | Year | int64 |  | 0 | none |
| DimDate | MonthNumber | int64 |  | 0 | none |
| DimDate | Month | string |  |  | none |
| DimDate | YearMonth | string |  |  | none |
| DimDate | YearMonthSort | int64 |  | 0 | none |
| DimDate | Quarter | string |  |  | none |
| FactSales | CustomerStatus | string |  |  | none |
| FactSales | SalesLineId | int64 | SalesLineId |  | none |
| FactSales | InvoiceNo | string | InvoiceNo |  | none |
| FactSales | StockCode | string | StockCode |  | none |
| FactSales | Description | string | Description |  | none |
| FactSales | Quantity | int64 | Quantity |  | sum |
| FactSales | InvoiceDate | dateTime | InvoiceDate | mmm d, yyyy h:mm AM/PM | none |
| FactSales | SalesDate | dateTime | SalesDate | mmm d, yyyy | none |
| FactSales | UnitPrice | decimal | UnitPrice | £#,0.00 | average |
| FactSales | CustomerID | string | CustomerID |  | none |
| FactSales | Country | string | Country |  | none |
| FactSales | IsCancellation | boolean | IsCancellation |  | none |
| FactSales | TransactionType | string | TransactionType |  | none |
| FactSales | NetSalesAmount | decimal | NetSalesAmount | £#,0.00 | sum |
| FactSales | GrossSalesAmount | decimal | GrossSalesAmount | £#,0.00 | sum |
| FactSales | ReturnAmount | decimal | ReturnAmount | £#,0.00 | sum |
| FactSales | UnitsSold | int64 | UnitsSold |  | sum |
| FactSales | ReturnedUnits | int64 | ReturnedUnits |  | sum |
| FactSales | HasValidPrice | boolean | HasValidPrice |  | none |

## v2 measures added or revised

| Measure | Type | Description |
|---|---|---|
| Identified Orders | whole number | Non-cancelled distinct invoices with a known CustomerID |
| Customer Net Sales Coverage | percentage | Identified-customer Net Sales divided by total Net Sales |
| Gross-to-Net Reconciliation Residual | currency | Net Sales minus Gross Sales less Return Amount |
| Latest Period Status | text | Partial/complete latest-month disclosure |
| Net Sales Prior Month Trend | currency | Previous calendar-month Net Sales for the month-axis context |
| Anonymous Net Sales | currency | Net Sales attached to Unknown CustomerID |
