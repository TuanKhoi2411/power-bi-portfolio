# Measure catalog v2

| Measure | DAX summary | Purpose | Visible use |
|---|---|---|---|
| Completed Month Net Sales MoM Change | current month Net Sales minus prior month; blank for latest partial month | Shows direct increases/decreases without overlapping shifted lines | Overview waterfall |
| Identified Orders | Orders where CustomerID is not Unknown | Keeps customer averages on a consistent population | Drives Orders per Customer KPI/sparkline |
| Orders per Customer | Identified Orders / Customers | Correct customer frequency | Customer Insights |
| Customer Net Sales Coverage | identified-customer Net Sales / Net Sales | Shows value coverage, not only row coverage | Customer Sales Coverage KPI/sparkline |
| Net Sales Previous Year | prior-year equivalent month/day window | Comparable partial-month benchmark | UK Retail Sales trend |
| Net Sales YoY | current / comparable prior year | Comparable growth | Country detail table |
| Gross-to-Net Reconciliation Residual | Net Sales - (Gross Sales - Return Amount) | Makes administrative-line differences auditable | QA/catalog diagnostic |
| Latest Period Status | partial or complete month label | Prevents December 2011 overinterpretation | Tooltip/manual card candidate |
| Net Sales Prior Month Trend | Net Sales in the immediately preceding calendar month | Supplies a complete adjacent-period comparator on the monthly trend | UK Retail Sales trend |
| Anonymous Net Sales | Net Sales where CustomerID is Unknown | Makes the customer-identification gap visible as value | Customer Insights stacked sales mix |
| One-time Customers | identified Customers minus Repeat Customers | Separates single-purchase customers from repeat customers without exposing synthetic IDs | Customer Insights loyalty-mix donut |

The complete executable definitions are in `measures_v2.dax` and the TMDL model.
# Customer concentration and country ranking

- `Top 10 Identified Customer Sales`: aggregate sales from the ten highest-value known customers, excluding `Unknown`.
- `Other Identified Customer Sales`: remaining identified-customer sales, used with the Top 10 measure in a concentration donut.
- `Customer Country Rank` and `Top 5 Country Customers`: restrict the compact country visual to five readable markets.
