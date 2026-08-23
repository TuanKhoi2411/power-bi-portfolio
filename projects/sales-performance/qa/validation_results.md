# Validation results — UK Online Retail Sales

## Current automated structural result

- Status: **PASS**
- Pages: 3
- Canvas: 1280×720 on every page
- Report visuals: 28 per page, 84 total
- Measures: 74
- PBIP pointer: present
- Report folder: present
- Semantic-model folder: present
- Source workbook: present
- Active page: resolves
- Page order: resolves

Machine-readable evidence: `structural_validation.json`.

## Independent source read during documentation update

| Check | Result |
|---|---:|
| Source rows | 541,909 |
| Gross Sales transformation | £10,666,684.54 |
| Return Amount transformation | £896,812.49 |
| Signed Net Sales transformation | £9,747,747.93 |
| Distinct non-cancelled orders | 20,728 |
| Missing CustomerID rows | 135,080 |
| Missing Description rows | 1,454 |

Gross, return, and signed net transformations intentionally have different validity/classification rules. Validate each independently and explain residual exceptions rather than forcing a simple subtraction identity.

## Scope of this result

The automated result validates repository structure, JSON readability, page metadata, visual presence, measure count, and required artifacts. It does **not** prove a new refresh, numeric reconciliation, interaction behavior, or Power BI Desktop reopen after the latest documentation update.

## Recorded Desktop history

The source creation task recorded a successful Desktop load/refresh during development, including 541,909 Sales rows, and subsequent report/measure corrections. This history is provenance, not a substitute for a fresh Desktop test after future model changes.

## Required next validation after implementation changes

Complete `qa_checklist.md`, record refresh/reconciliation totals, save/reopen the PBIX, and update this file with date, tester, application version, and unresolved issues.
