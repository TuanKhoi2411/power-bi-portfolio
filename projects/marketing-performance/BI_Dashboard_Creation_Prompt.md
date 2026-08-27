# BI Dashboard Creation Prompt

## Objective

Rebuild or extend **Portuguese Bank — Marketing Performance** as a polished, decision-focused Power BI product. The management question is: **Which audiences and campaign conditions are associated with stronger subscription conversion?**

Use the published PBIP as the source of truth. Do not invent measures, relationships, outcomes, or source facts. Preserve the current semantic model unless a requested change requires a documented migration.

## Source and grain

- Source: UCI Bank Marketing CSV.
- Grain: campaign contact.
- Current model tables: DimAgeBand, DimChannel, DimContactFrequency, DimDate, DimDayOfWeek, DimEducation, DimJob, DimMaritalStatus, DimPriorOutcome, FactMarketing.
- Current authored measures: 72; use [`model/measures.dax`](./model/measures.dax) as the exact DAX reference.

## Required report experience

- **Bank Marketing:** volume, conversion, and channel direction.
- **Audience Segmentation:** audience mix and response.
- **Campaign Effectiveness:** campaign conditions and conversion drivers.

Keep a consistent 16:9 canvas, visible page navigation, clear slicer state, KPI cards, decision-oriented chart titles, and a reset-filter control. Prefer a few readable visuals over dense decoration.

## Build contract

1. Open `dashboard/Portuguese_Bank_Marketing.pbip` with the complete report and semantic-model folders present.
2. Repoint the source only when the local path differs; do not change transformation logic silently.
3. Verify relationships and date behavior before editing visuals.
4. Reconcile the headline KPIs to the underlying table or source.
5. Confirm every page, navigation button, slicer, tooltip, sort order, and interaction.
6. Save a PBIX named `Portuguese_Bank_Marketing_Performance_Dashboard.pbix` and regenerate the PDF preview after QA.

## Acceptance criteria

- The PBIP opens without missing report/model references.
- Every page listed above is present and usable at 16:9.
- DAX definitions reconcile with `model/measures.dax`.
- Source, assumptions, refresh dependencies, and limitations remain visible in the README.
- No proprietary or confidential data is introduced.
