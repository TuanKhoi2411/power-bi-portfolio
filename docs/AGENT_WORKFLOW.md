# Agent workflow for Power BI projects

This document makes the portfolio actionable for a coding or computer-use agent. It describes what an agent must inspect, change, verify, and report.

## 1. Select exactly one project

Work inside one `projects/<project-name>/` directory unless the request explicitly covers multiple projects. Read its `AGENTS.md` and `agent/BUILD_PROMPT.md` before editing.

## 2. Establish artifact truth

Confirm which artifacts actually exist:

- raw source file;
- PBIP entry point;
- `.Report` definition;
- `.SemanticModel` definition;
- packaged PBIX;
- standalone HTML story.

Do not infer that a missing artifact exists. The Sports & Health project is intentionally classified as an in-place PBIX enhancement because its raw source and PBIP are not published.

## 3. Validate source and model

Before changing the report:

1. Confirm the source publisher, file, grain, date coverage, and row-count assumptions in `agent/DATA_MODEL_SPEC.md`.
2. Inspect Power Query partitions and replace any stale local `SourcePath` value.
3. Confirm table roles, keys, relationships, data types, formatting, and sort-by columns.
4. Reconcile core measures against source totals or a documented control calculation.
5. Keep display measures separate from numeric measures used for aggregation and sorting.

## 4. Implement the report blueprint

Use `agent/REPORT_SPEC.md` as the acceptance blueprint. Preserve:

- 1280×720 page canvas for PBIP projects;
- page names and decision-specific page roles;
- navigation, slicers, reset behavior, KPI definitions, and drill path;
- the project's existing visual language unless redesign is requested.

Every visual must answer a stated business question. Decorative changes must not hide source quality, uncertainty, or limitations.

## 5. Build in Power BI Desktop

For PBIP projects:

1. Open the complete `.pbip` entry point, not an isolated report folder.
2. Update the source parameter/path and refresh.
3. Resolve model, DAX, or visual errors.
4. Save the PBIP.
5. Save or export the packaged PBIX using the existing project filename.

For the Sports & Health project, open the existing PBIX and make in-place changes only. A from-scratch rebuild requires the user to provide the source dataset and/or PBIP.

## 6. QA before claiming completion

Complete the project checklist in `agent/BUILD_AND_QA.md`:

- source and refresh;
- model relationships and measure reconciliation;
- page content, navigation, slicers, reset, and cross-filtering;
- 100% and Fit-to-page visual review;
- PBIX reopen test;
- artifact names and links;
- limitation disclosure.

If Desktop QA cannot be performed, say exactly what was and was not verified.

Run the repository structure check before handoff:

```powershell
./scripts/validate-agent-packages.ps1
```

## 7. Handoff format

Report:

1. files changed;
2. model or measure changes;
3. page and interaction changes;
4. validation performed and results;
5. remaining limitations;
6. exact PBIP/PBIX/HTML paths for review.

## Reusable request pattern

Use this with any capable agent:

> Work on `<project path>`. Follow the repository and project `AGENTS.md` files. Read all files in `agent/`, inspect the canonical PBIP/PBIX and source data, implement the requested change, run the documented QA, and report limitations without inventing evidence.
