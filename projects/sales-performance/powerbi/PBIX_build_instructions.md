# PBIX Build Instructions

## Target

- PBIP entry point: `dashboard/UK_Online_Retail_Sales.pbip`
- Packaged output: `UK_Online_Retail_Sales_Performance_Dashboard.pbix`
- Canonical source: `C:\PowerBI Dashboard - KhoiPort`

## Build

1. Download the complete project folder; a `.pbip` file is only an entry point.
2. Open `dashboard/UK_Online_Retail_Sales.pbip` in Power BI Desktop.
3. If refresh fails, update the source path to the included/public source documented in the README.
4. Refresh and resolve errors before changing visuals.
5. Validate the page set: UK Retail Sales, Customer Insights, Product & Returns.
6. Compare the semantic model with `model/model_inventory.md` and exact measures with `model/measures.dax`.
7. Run the QA checklist, save the PBIP, then export `UK_Online_Retail_Sales_Performance_Dashboard.pbix`.
8. Regenerate the dashboard PDF in `preview/`; portfolio images are rendered from this PDF, not from slide artwork.

## Guardrails

- Do not edit files inside `.pbi/`; they are local caches/settings.
- Do not publish secrets, credentials, private data, or local absolute paths.
- Do not rename tables or measures without updating visuals, documentation, and QA.
