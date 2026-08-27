# BI Dashboard Creation Prompt

## Objective

Rebuild or extend **Apple Inc. — Financial Performance** as a polished, decision-focused Power BI product. The management question is: **Are growth, margins, liquidity, and cost structure moving sustainably?**

Use the published PBIP as the source of truth. Do not invent measures, relationships, outcomes, or source facts. Preserve the current semantic model unless a requested change requires a documented migration.

## Source and grain

- Source: Apple SEC filing data.
- Grain: reported financial metric by period.
- Current model tables: DimDate, DimForm, DimMetric, DimPeriodType, FactFinance, FinanceComponent.
- Current authored measures: 141; use [`model/measures.dax`](./model/measures.dax) as the exact DAX reference.

## Required report experience

- **Overview:** headline scale and direction.
- **Profitability & Growth:** growth and margin structure.
- **Balance & Liquidity:** assets, liabilities, cash, and resilience.

Keep a consistent 16:9 canvas, visible page navigation, clear slicer state, KPI cards, decision-oriented chart titles, and a reset-filter control. Prefer a few readable visuals over dense decoration.

## Build contract

1. Open `dashboard/Apple_Finance.pbip` with the complete report and semantic-model folders present.
2. Repoint the source only when the local path differs; do not change transformation logic silently.
3. Verify relationships and date behavior before editing visuals.
4. Reconcile the headline KPIs to the underlying table or source.
5. Confirm every page, navigation button, slicer, tooltip, sort order, and interaction.
6. Save a PBIX named `Apple_Inc_Financial_Performance_Dashboard.pbix` and regenerate the PDF preview after QA.

## Acceptance criteria

- The PBIP opens without missing report/model references.
- Every page listed above is present and usable at 16:9.
- DAX definitions reconcile with `model/measures.dax`.
- Source, assumptions, refresh dependencies, and limitations remain visible in the README.
- No proprietary or confidential data is introduced.
