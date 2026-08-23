# Agent build prompt — Portuguese Bank Marketing Performance

## Objective

Build or enhance a three-page Power BI Marketing dashboard that answers:

> Which audiences and campaign conditions are associated with stronger term-deposit subscription conversion?

Use the included UCI dataset and existing PBIP only. Do not invent campaign costs, revenue, lift, experiments, or causal outcomes.

## Required deliverables

1. Refreshable PBIP and packaged `Portuguese_Bank_Marketing_Performance_Dashboard.pbix`.
2. Pages `Bank Marketing`, `Audience Segmentation`, and `Campaign Effectiveness`.
3. Working navigation, slicers, reset action, cross-filtering, and readable 1280×720 layouts.
4. Reconciled contact, conversion, rate, campaign-frequency, channel, prior-contact, and macro-context measures.
5. Updated QA disclosure after any implementation change.

## Execution sequence

1. Profile `../data/bank-additional-full.csv`: delimiter, 41,188 contacts, field types, `unknown` categories, target distribution, and temporal fields.
2. Update the `SourcePath` in the `FactMarketing` partition and refresh.
3. Preserve or intentionally update the 34 canonical measures in `FactMarketing.tmdl`.
4. Follow `REPORT_SPEC.md`; keep descriptive findings separate from recommendations.
5. Complete `BUILD_AND_QA.md`, save PBIP/PBIX, then close and reopen the PBIX.

## Acceptance criteria

- Contacts and conversions reconcile to source rows and target values.
- Conversion Rate uses a clearly defined numerator and denominator.
- Duration is disclosed as post-contact information and not used as unqualified targeting guidance.
- `unknown` is retained or explicitly handled; never silently imputed.
- No causal language unless supported by an experiment or causal design not currently present.
