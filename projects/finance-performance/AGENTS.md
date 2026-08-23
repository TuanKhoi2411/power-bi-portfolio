# Apple Financial Performance agent instructions

This project is a rebuildable Finance dashboard based on Apple Inc. SEC EDGAR company facts.

## Canonical artifacts

- Source: `data/sec-aapl-companyfacts.json`
- PBIP: `dashboard/Apple_Inc_Financial_Performance_Dashboard.pbip`
- Report: `dashboard/Apple_Finance.Report/`
- Semantic model: `dashboard/Apple_Finance.SemanticModel/`
- PBIX: `Apple_Inc_Financial_Performance_Dashboard.pbix`
- Story: `Apple_Inc_Financial_Performance_Interactive.html`

Read `README.md`, `BI_Dashboard_Creation_Prompt.md`, and all files in `agent/`, `model/`, `powerbi/`, `qa/`, and `docs/` before changing the project.

## Guardrails

- Use only sourced SEC facts; never invent missing quarters, guidance, estimates, or investment outcomes.
- Preserve accession/form/filing metadata and avoid double counting overlapping annual and quarterly facts.
- Distinguish point-in-time balance-sheet facts from duration income/cash-flow facts.
- Treat restatements, unit scales, taxonomy changes, and duplicate frames explicitly.
- This is financial analysis, not investment advice.
- Update the local JSON source path before refresh and retain the 1280×720 three-page journey.
