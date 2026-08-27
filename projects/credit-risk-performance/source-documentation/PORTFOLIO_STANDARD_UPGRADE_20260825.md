# Credit Risk portfolio-standard upgrade

Date: 2026-08-25

## Scope

The working PBIP project was upgraded directly. The reference file `CreditRisk_Dashboard_backup.pbix` was not modified.

Working project:

`C:\Users\ADMIN\Downloads\CP2 - New\FinTech_Credit_Risk_PBIP\FinTech_Credit_Risk.pbip`

Safety backup:

`C:\Users\ADMIN\Downloads\CP2 - New\_backup_before_portfolio_upgrade_20260825\FinTech_Credit_Risk_PBIP`

## Semantic-model changes

- Converted report-facing categorical fields to a star-schema pattern.
- Added `DimGrade`, `DimPurpose`, `DimState`, `DimIncomeBand`, `DimLoanLabel`, `DimHomeOwnership`, and `DimTerm`.
- Added seven single-direction many-to-one relationships from `FactLoans`; the existing relationship to `DimDate` remains active.
- Hidden raw fact-table category fields and technical keys from report authors while retaining them for calculations.
- Rebound report slicers and chart categories to the new dimensions.

## Measure changes

- `Seasoning Coverage Previous Month`: prior-month comparable for the seasoning-eligible portfolio.
- `Seasoning Coverage Variance pp`: percentage-point change versus the previous month.
- `Model Gini`: `2 × Model AUC − 1`, a complementary discrimination score.
- Ranking measures for State and Purpose now iterate over dimension members, so slicers and rankings share the same filter path.

## Report changes

- Replaced the duplicated `Overall Bad Rate` KPI on Portfolio Overview with `Seasoning Coverage`.
- Its delta now shows the month-over-month percentage-point change, and its sparkline shows the same metric over time.
- Replaced the duplicated AUC evidence value on Risk Drivers & Actions with Model Gini.
- Preserved the previously approved visual set and the hidden 60-month chart state.
- Added an interactive `Customer Loan Journey Flow` decomposition tree to Borrower Risk. The existing `Loan label` slicer switches the analyzed population between Good, Bad, and Neutral, while the tree explains it by Term, Purpose, Income Band, Home Ownership, and Grade.
- The two prior bottom-row borrower charts are retained as hidden visuals for reversible review.

## Validation

- All report JSON files parse successfully.
- All visual field bindings resolve to model tables, columns, or measures.
- The PBIP report retains three pages and a valid active-page definition.
- Desktop refresh is still required after opening so calculated dimensions and relationships materialize against `CreditRisk_Data.csv`.
