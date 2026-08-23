# Repository agent instructions

This repository contains four independent Power BI portfolio products. Treat each project as a separate analytical product; never merge Sales, Marketing, Apple Finance, and Sports & Health into one semantic model.

## Required reading order

1. Read the target project's `README.md`.
2. Read the target project's `AGENTS.md`.
3. Read every file in the target project's `agent/` directory.
4. Inspect the PBIP definitions under `dashboard/` when present. Those files are the canonical report and semantic-model implementation.
5. Inspect the raw source under `data/` when present.

## Non-negotiable rules

- Do not invent data, measures, outcomes, source citations, or QA results.
- Preserve the management question and decision lens before changing visuals.
- Keep source grain, date coverage, transformation assumptions, and limitations explicit.
- For PBIP projects, update source-controlled report/model definitions and the packaged PBIX consistently.
- A PBIX is not considered rebuilt until it opens in Power BI Desktop, refreshes without error, and the required pages are visually checked.
- Do not claim rebuildability for `financial-performance-dashboard`; that project currently has a PBIX but no published raw source or PBIP definition.
- Preserve the standalone HTML story unless the requested change explicitly includes the presentation.
- Record any known limitation or incomplete verification in `agent/BUILD_AND_QA.md`.

## Project routing

| Project | Mode | Primary entry point |
|---|---|---|
| `sales-performance` | Full rebuild / enhancement | `dashboard/UK_Online_Retail_Sales_Performance_Dashboard.pbip` |
| `marketing-performance` | Full rebuild / enhancement | `dashboard/Portuguese_Bank_Marketing_Performance_Dashboard.pbip` |
| `finance-performance` | Full rebuild / enhancement | `dashboard/Apple_Inc_Financial_Performance_Dashboard.pbip` |
| `financial-performance-dashboard` | In-place PBIX enhancement only | `Sports_Health_Enterprise_Financial_Performance_Dashboard.pbix` |

See `docs/AGENT_WORKFLOW.md` for the standard execution and handoff process.
