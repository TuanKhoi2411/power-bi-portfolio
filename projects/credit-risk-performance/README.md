# FinTech Credit Risk — Portfolio Performance

## Review in 60 seconds

| Item | Current evidence |
|---|---|
| Management question | Where is credit risk concentrated, how should pricing respond, and which borrower segments require action? |
| What I built | A 4-page Power BI dashboard, source-controlled PBIP, packaged PBIX, and PDF dashboard preview. |
| Source | Portfolio training dataset with Lending Club-style loan fields, published in this repository at loan-application grain. |
| Model | 13 tables and 184 authored measures in the current canonical PBIP. |
| Status | Synchronized from KhoiPort and repackaged on 27 August 2026. |

## Dashboard pages

- **Overview:** portfolio scale, grade mix, and loss direction.
- **Borrower Risk:** borrower attributes and risk concentration.
- **Pricing & Returns:** rate, return, and recovery trade-offs.
- **Risk Drivers & Actions:** model drivers and operational action rules.

## Main artifacts

| Artifact | Purpose |
|---|---|
| [`FinTech_Credit_Risk_Dashboard.pbix`](./FinTech_Credit_Risk_Dashboard.pbix) | Review-ready packaged dashboard. |
| [`FinTech_Credit_Risk_Performance_Interactive.html`](./FinTech_Credit_Risk_Performance_Interactive.html) | Standalone interactive management story; download and open in a browser. |
| [`dashboard/FinTech_Credit_Risk.pbip`](./dashboard/FinTech_Credit_Risk.pbip) | Source-controlled PBIP entry point. |
| [`preview/`](./preview/) | Dashboard-only PDF and readable page images used by the portfolio. |
| [`BI_Dashboard_Creation_Prompt.md`](./BI_Dashboard_Creation_Prompt.md) | Full agent brief for rebuilding or extending the product. |
| [`model/measures.dax`](./model/measures.dax) | Exact DAX extracted from the current PBIP. |
| [`powerbi/PBIX_build_instructions.md`](./powerbi/PBIX_build_instructions.md) | Rebuild and packaging procedure. |

## Model and evidence

- Tables: `DimDate`, `DimGrade`, `DimHomeOwnership`, `DimIncomeBand`, `DimIncomeLevel`, `DimLoanLabel`, `DimPurpose`, `DimState`, `DimTerm`, `FactLoans`, `Measure`, `RiskDriverImportance`, `RiskRuleSummary`.
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
