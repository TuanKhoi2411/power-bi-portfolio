# UK Online Retail agent instructions

This project is a rebuildable Sales analytics product based on public UCI Online Retail data.

## Read first

- `README.md`
- `BI_Dashboard_Creation_Prompt.md`
- `agent/BUILD_PROMPT.md`
- `agent/DATA_MODEL_SPEC.md`
- `agent/REPORT_SPEC.md`
- `agent/BUILD_AND_QA.md`
- every file in `model/`, `powerbi/`, `qa/`, and `docs/`

## Canonical artifacts

- Source: `data/Online Retail.xlsx`
- PBIP: `dashboard/UK_Online_Retail_Sales_Performance_Dashboard.pbip`
- Report definition: `dashboard/UK_Online_Retail_Sales.Report/`
- Semantic model: `dashboard/UK_Online_Retail_Sales.SemanticModel/`
- Packaged report: `UK_Online_Retail_Sales_Performance_Dashboard.pbix`
- Management story: `UK_Online_Retail_Sales_Performance_Interactive.html`

## Guardrails

- Preserve transaction-line grain and distinguish sales from cancellations/returns.
- Do not treat gross sales as net sales.
- Keep customer IDs nullable; anonymous sales must not be silently dropped.
- Replace the local source path before refresh; do not commit a machine-specific path as the only refresh method.
- Preserve the three-page decision journey and 1280×720 canvas unless redesign is requested.
- Validate numeric measures before changing display-format measures.
