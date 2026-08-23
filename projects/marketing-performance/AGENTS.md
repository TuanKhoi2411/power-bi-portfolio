# Portuguese Bank Marketing agent instructions

This project is a rebuildable Marketing analytics product based on the public UCI Bank Marketing dataset.

## Read first

- `README.md`
- every document in `agent/`

## Canonical artifacts

- Source: `data/bank-additional-full.csv`
- PBIP: `dashboard/Portuguese_Bank_Marketing_Performance_Dashboard.pbip`
- Report: `dashboard/Portuguese_Bank_Marketing.Report/`
- Semantic model: `dashboard/Portuguese_Bank_Marketing.SemanticModel/`
- PBIX: `Portuguese_Bank_Marketing_Performance_Dashboard.pbix`
- Story: `Portuguese_Bank_Marketing_Performance_Interactive.html`

## Guardrails

- Preserve one-contact-per-row grain and the 41,188-row public dataset.
- Treat conversion patterns as associations, not causal proof.
- Do not present contact duration as a deployable pre-call targeting variable without leakage disclosure.
- Keep demographic and financial-condition attributes descriptive and avoid discriminatory recommendations.
- Update the local CSV source path before refresh.
- Preserve the three-page 1280×720 journey unless redesign is requested.
