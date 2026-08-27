# UK Online Retail Sales Performance v2

## Purpose

An isolated improvement package for the UK Online Retail portfolio dashboard. It answers how sales, returns, customers, countries, and products performed while keeping partial-period and anonymous-customer limitations visible.

## Open

Open `dashboard/UK_Online_Retail_Sales_Performance_v2.pbip` in Power BI Desktop. The included workbook is referenced at `C:\pbi-portfolio-v2\UK_Online_Retail_Sales_Performance_v2\data\Online Retail.xlsx`.

## Source and validation baseline

- Publisher: UCI Machine Learning Repository.
- Dataset: [Online Retail](https://archive.ics.uci.edu/dataset/352/online+retail).
- Grain: one invoice line.
- Rows: 541,909.
- Coverage: 2010-12-01 through 2011-12-09; the final month is partial.
- Validated totals: Gross Sales £10,666,684.54; Return Amount £896,812.49; Net Sales £9,747,747.93; 20,728 non-cancelled orders; 4,372 identified customers.
- Customer-ID row coverage: 75.0733%; customer-ID net-sales coverage: 85.1485%.

## v2 improvements

- Calendar now matches the fact coverage rather than extending from 2008 to 2026.
- Prior-year comparison is day-aligned when the current month is partial.
- Orders per Customer uses identified orders only.
- Customer Sales Coverage is value-based and appears on the Customer Insights KPI/sparkline.
- Gross-to-net residual is explicit: -£22,124.12 across the full dataset, reflecting administrative/invalid-price lines rather than a forced zero.

## MCP and Desktop status

No Power BI report/model MCP operations were exposed in this session. The package was built by direct PBIP/PBIR/TMDL inspection and controlled file edits. It was opened, refreshed, visually checked, and saved in Power BI Desktop; a separate close/reopen smoke test remains manual.

## Licensing and reuse

The upstream repository contains no root LICENSE file. Keep this local derivative private unless you have permission to redistribute its report assets. Verify dataset licensing and attribution requirements on the UCI source page before publication.
