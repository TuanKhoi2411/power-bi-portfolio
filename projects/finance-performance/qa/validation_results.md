# Validation results — Apple Financial Performance

## Current automated structural result

- Status: **PASS**
- Pages: 3
- Canvas: 1280×720 on every page
- Report visuals: 28 per page, 84 total
- Measures: 90
- PBIP, Report, SemanticModel, and SEC JSON: present
- Active page and page order: resolve

Evidence: `structural_validation.json`.

## Scope

This proves structural repository/PBIP/PBIR/TMDL integrity only. It does not independently re-run SEC normalization, accounting reconciliation, interaction testing, or Desktop reopen.

The source creation task recorded a Desktop refresh with 648 normalized Finance facts. After any future model/report change, complete `qa_checklist.md`, record current selected-fact counts and reconciliations, save/reopen PBIX, and update this file.

Recorded creation-task checks included latest selected quarterly Revenue of `$109,417,000,000` and Gross Margin of `50.0562%`. These values are provenance and must be revalidated after concept-selection, filing-version, or period logic changes.
