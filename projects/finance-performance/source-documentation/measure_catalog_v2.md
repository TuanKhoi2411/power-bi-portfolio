# Measure catalog v2

| Measure | Definition | Purpose | Visible use |
|---|---|---|---|
| Quarterly Gross / Operating / Net Margin | quarterly profit divided by quarterly revenue | Prevent annual filings from being mixed into quarter margin trends | Overview and Profitability trends |
| Quarterly Cost of Sales Ratio | quarterly cost of sales / quarterly revenue | Production-cost burden | Profitability cost chart |
| Quarterly Operating Expense Ratio | quarterly operating expenses / quarterly revenue | Controllable operating-cost burden | Profitability cost chart |
| Quarterly Net Income Conversion | quarterly net income / quarterly gross profit | Share of gross profit reaching the bottom line | Profitability conversion trend |
| Net Asset Ratio | (assets - liabilities) / assets | Capital cushion available after liabilities | Balance risk trend |
| Revenue Previous Year | revenue from the prior-year SEC calendar-quarter Frame | Like-for-like quarter comparison despite Apple fiscal/calendar offsets | Revenue growth chart and scorecard |
| Latest Cost of Sales Amount | latest revenue - latest gross profit | Mutually exclusive share of latest-quarter revenue consumed by cost of sales | Revenue allocation donut |
| Latest Operating Expenses Amount | latest gross profit - latest operating income | Mutually exclusive operating-cost share of latest-quarter revenue | Revenue allocation donut |
| Latest Other and Tax Amount | latest operating income - latest net income | Mutually exclusive below-operating-income share of latest-quarter revenue | Revenue allocation donut |
| Balance Value | MAX(Value) | Point-in-time aggregation | Drives Assets, Liabilities, Cash and all dependent balance visuals |
| Assets / Liabilities / Cash | Balance Value filtered by metric | Prevents multi-period summation | Balance cards/trends/tables |
| Cash to Assets | Cash / Assets | Liquidity relative to balance-sheet scale | Balance trend and sparkline |
| Latest Cash to Assets | Latest Cash / Latest Assets | Current liquidity mix | KPI 5 |
| Latest Cash to Assets PY | latest comparable prior fiscal period | Comparison base | Delta |
| Latest Cash to Assets Variance pp | current minus PY | Direction in percentage points | Delta 5 |
| KPI Cash to Assets Display | formatted latest ratio | Card-only display | KPI 5 |

Flow measures continue to use SUM only inside compatible quarter/year contexts.
