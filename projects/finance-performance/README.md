# Apple Inc. — Financial Performance

## Review in 60 seconds

| Item | Current evidence |
|---|---|
| Management question | Are growth, margins, liquidity, and cost structure moving sustainably? |
| What I built | A 3-page Power BI dashboard, source-controlled PBIP, packaged PBIX, and PDF dashboard preview. |
| Source | Apple SEC filing data at reported financial metric by period grain. |
| Model | 6 tables and 141 authored measures in the current canonical PBIP. |
| Status | Synchronized from KhoiPort and repackaged on 27 August 2026. |

## Dashboard pages

- **Overview:** headline scale and direction.
- **Profitability & Growth:** growth and margin structure.
- **Balance & Liquidity:** assets, liabilities, cash, and resilience.

## Main artifacts

| Artifact | Purpose |
|---|---|
| [`Apple_Inc_Financial_Performance_Dashboard.pbix`](./Apple_Inc_Financial_Performance_Dashboard.pbix) | Review-ready packaged dashboard. |
| [`dashboard/Apple_Finance.pbip`](./dashboard/Apple_Finance.pbip) | Source-controlled PBIP entry point. |
| [`preview/`](./preview/) | Dashboard-only PDF and readable page images used by the portfolio. |
| [`BI_Dashboard_Creation_Prompt.md`](./BI_Dashboard_Creation_Prompt.md) | Full agent brief for rebuilding or extending the product. |
| [`model/measures.dax`](./model/measures.dax) | Exact DAX extracted from the current PBIP. |
| [`powerbi/PBIX_build_instructions.md`](./powerbi/PBIX_build_instructions.md) | Rebuild and packaging procedure. |

## Model and evidence

- Tables: `DimDate`, `DimForm`, `DimMetric`, `DimPeriodType`, `FactFinance`, `FinanceComponent`.
- Exact measure catalog: [`model/measure_catalog.csv`](./model/measure_catalog.csv).
- Source and transformation documentation: [`source-documentation/`](./source-documentation/).
- Build utilities and theme: [`build-scripts/`](./build-scripts/) and [`theme/`](./theme/).

## Reviewer path

1. Open the PDF in `preview/` for a fast dashboard-page scan.
2. Download the PBIX for interaction.
3. Inspect the PBIP, DAX, model inventory, and source notes for reproducibility.
4. Use the creation prompt and QA checklist when rebuilding or extending the case.

## Limits

This is a portfolio case study, not a production system or an investment/credit recommendation. Public or portfolio-safe data is used; source limitations remain applicable.
