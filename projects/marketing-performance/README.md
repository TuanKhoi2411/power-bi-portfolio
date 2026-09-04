# Portuguese Bank — Marketing Performance

## Review in 60 seconds

| Item | Current evidence |
|---|---|
| Management question | Which audiences and campaign conditions are associated with stronger subscription conversion? |
| What I built | A 3-page Power BI dashboard, source-controlled PBIP, packaged PBIX, and PDF dashboard preview. |
| Source | UCI Bank Marketing CSV at campaign contact grain. |
| Model | 10 tables and 72 authored measures in the current canonical PBIP. |
| Status | Synchronized from KhoiPort and repackaged on 27 August 2026. |

## Dashboard pages

- **Bank Marketing:** volume, conversion, and channel direction.
- **Audience Segmentation:** audience mix and response.
- **Campaign Effectiveness:** campaign conditions and conversion drivers.

## Main artifacts

| Artifact | Purpose |
|---|---|
| [`Portuguese_Bank_Marketing_Performance_Dashboard.pbix`](./Portuguese_Bank_Marketing_Performance_Dashboard.pbix) | Review-ready packaged dashboard. |
| [`Portuguese_Bank_Marketing_Performance_Interactive.html`](./Portuguese_Bank_Marketing_Performance_Interactive.html) | Standalone interactive management story; download and open in a browser. |
| [`dashboard/Portuguese_Bank_Marketing.pbip`](./dashboard/Portuguese_Bank_Marketing.pbip) | Source-controlled PBIP entry point. |
| [`preview/`](./preview/) | Dashboard-only PDF and readable page images used by the portfolio. |
| [`BI_Dashboard_Creation_Prompt.md`](./BI_Dashboard_Creation_Prompt.md) | Full agent brief for rebuilding or extending the product. |
| [`model/measures.dax`](./model/measures.dax) | Exact DAX extracted from the current PBIP. |
| [`powerbi/PBIX_build_instructions.md`](./powerbi/PBIX_build_instructions.md) | Rebuild and packaging procedure. |

## Model and evidence

- Tables: `DimAgeBand`, `DimChannel`, `DimContactFrequency`, `DimDate`, `DimDayOfWeek`, `DimEducation`, `DimJob`, `DimMaritalStatus`, `DimPriorOutcome`, `FactMarketing`.
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
