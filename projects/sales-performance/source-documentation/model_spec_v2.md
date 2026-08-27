# Data and semantic-model specification

## Source contract

| Item | Contract |
|---|---|
| Publisher | UCI Machine Learning Repository — Online Retail |
| Local file | `../data/Online Retail.xlsx` |
| Observation grain | One invoice transaction line |
| Date coverage | 1 December 2010–9 December 2011 |
| Geographic scope | UK-based non-store retailer with international transactions |
| Important quality conditions | Cancellations, returns, missing customer IDs, quantity and price exceptions |

The original workbook is the source of truth. Never silently remove exceptions; document every exclusion or classification rule.

## Model contract

| Table | Role | Required key/date |
|---|---|---|
| `FactSales` | Transaction-line fact and measure home | `SalesLineId`, `SalesDate` |
| `DimDate` | Calendar dimension | `Date` |

Active relationship: `FactSales[SalesDate]` → `DimDate[Date]`.

Canonical definitions:

- `../dashboard/UK_Online_Retail_Sales.SemanticModel/definition/tables/FactSales.tmdl`
- `../dashboard/UK_Online_Retail_Sales.SemanticModel/definition/tables/DimDate.tmdl`
- `../dashboard/UK_Online_Retail_Sales.SemanticModel/definition/relationships.tmdl`

## Required fact fields

`SalesLineId`, `InvoiceNo`, `StockCode`, `Description`, `Quantity`, `InvoiceDate`, `SalesDate`, `UnitPrice`, `CustomerID`, `Country`, `IsCancellation`, `TransactionType`, `NetSalesAmount`, `GrossSalesAmount`, `ReturnAmount`, `UnitsSold`, `ReturnedUnits`, and `HasValidPrice`.

## Measure contract

`FactSales.tmdl` currently contains 74 measures. Preserve the canonical DAX unless a requested change requires revision.

Core numeric measures:

- Gross Sales, Return Amount, Net Sales
- Units Sold, Returned Units, Orders, Customers
- Average Order Value, Average Selling Price, Return Rate
- Previous-month, month-over-month, previous-year, year-over-year, and variance measures
- Merchandise Net Sales and Top-N country/product/customer measures
- Customer identification coverage, repeat customers, orders per customer, active products

Display measures prefixed with `KPI` are presentation helpers. Do not use them as numeric sort or aggregation fields.

## Refresh requirement

The current Power Query partition may contain a machine-specific `SourcePath`. Before refresh, point it to `data/Online Retail.xlsx` or replace it with a documented project-root parameter. Refresh all tables and verify that the date table covers the complete fact range.

## Minimum reconciliation

- Reconcile Gross Sales, Return Amount, and signed Net Sales independently to their Power Query definitions. Do not force `Net Sales = Gross Sales - Return Amount`: administrative, invalid-price, or exceptional rows can create a documented residual because the three measures intentionally apply different validity/classification rules.
- Order count uses distinct invoice logic.
- Customer count excludes null IDs only from identified-customer measures, not from total sales.
- Return Rate denominator is documented and stable.
- Top-N totals tie to the same base measure used by the overview.

## v2 contract addendum

- DimDate is bounded by the minimum and maximum FactSales SalesDate.
- Partial latest months use elapsed-day prior-year comparison.
- Customer frequency uses Identified Orders and Customers from the same known-ID population.
- Both row coverage and net-sales coverage remain available; the headline customer KPI uses value coverage.
