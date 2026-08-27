# BI Dashboard Creation Prompt

## Objective

Rebuild or extend **FinTech Credit Risk — Portfolio Performance** as a polished, decision-focused Power BI product. The management question is: **Where is credit risk concentrated, how should pricing respond, and which borrower segments require action?**

Use the published PBIP as the source of truth. Do not invent measures, relationships, outcomes, or source facts. Preserve the current semantic model unless a requested change requires a documented migration.

## Source and grain

- Source: Lending Club public loan data.
- Grain: loan application.
- Current model tables: DimDate, DimGrade, DimHomeOwnership, DimIncomeBand, DimIncomeLevel, DimLoanLabel, DimPurpose, DimState, DimTerm, FactLoans, Measure, RiskDriverImportance, RiskRuleSummary.
- Current authored measures: 184; use [`model/measures.dax`](./model/measures.dax) as the exact DAX reference.

## Required report experience

- **Overview:** portfolio scale, grade mix, and loss direction.
- **Borrower Risk:** borrower attributes and risk concentration.
- **Pricing & Returns:** rate, return, and recovery trade-offs.
- **Risk Drivers & Actions:** model drivers and operational action rules.

Keep a consistent 16:9 canvas, visible page navigation, clear slicer state, KPI cards, decision-oriented chart titles, and a reset-filter control. Prefer a few readable visuals over dense decoration.

## Build contract

1. Open `dashboard/FinTech_Credit_Risk.pbip` with the complete report and semantic-model folders present.
2. Repoint the source only when the local path differs; do not change transformation logic silently.
3. Verify relationships and date behavior before editing visuals.
4. Reconcile the headline KPIs to the underlying table or source.
5. Confirm every page, navigation button, slicer, tooltip, sort order, and interaction.
6. Save a PBIX named `FinTech_Credit_Risk_Dashboard.pbix` and regenerate the PDF preview after QA.

## Acceptance criteria

- The PBIP opens without missing report/model references.
- Every page listed above is present and usable at 16:9.
- DAX definitions reconcile with `model/measures.dax`.
- Source, assumptions, refresh dependencies, and limitations remain visible in the README.
- No proprietary or confidential data is introduced.
