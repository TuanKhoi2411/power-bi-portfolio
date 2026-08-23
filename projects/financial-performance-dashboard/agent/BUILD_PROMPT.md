# Agent prompt — Sports & Health Enterprise Financial Performance

## Objective

Enhance the existing Power BI report to answer:

> How can management move from a headline P&L into margin, cost, segment, and break-even drivers?

This is not a from-scratch build prompt. The repository does not currently publish the raw source or PBIP definitions.

## Required input

`../Sports_Health_Enterprise_Financial_Performance_Dashboard.pbix`

## Required deliverables

1. An updated PBIX that retains the existing model unless a requested change explicitly requires modification.
2. Four working pages: `Overview`, `Breakdown`, `Segments`, and `Breakeven`.
3. Working navigation, filters, reset behavior, and cross-filtering.
4. A clean portfolio screenshot per page if imagery is requested.
5. An updated `BUILD_AND_QA.md` describing inspection, changes, and limitations.

## Execution sequence

1. Open the PBIX and inventory tables, relationships, measures, data sources, refresh state, page names, visual types, bookmarks, and interactions.
2. Compare the live artifact with `DATA_MODEL_SPEC.md` and `REPORT_SPEC.md`; treat the PBIX as authoritative when documentation and implementation differ.
3. Implement only the requested enhancement.
4. Reconcile changed KPIs and visuals inside Power BI.
5. Save, close, reopen, and inspect every page.

## Stop condition

If the request requires data regeneration, new source fields, a refresh from unavailable source data, or a from-scratch rebuild, stop and request the missing source/PBIP instead of fabricating it.
