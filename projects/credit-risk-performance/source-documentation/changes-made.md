# Changes Made

- Built a new PBIP project without editing `CreditRisk_Dashboard_backup.pbix`.
- Replaced the reused technical skeleton's retail model with a loan-level Credit Risk semantic model sourced from `CreditRisk_Data.csv`.
- Applied a Deep Navy / Teal / Coral risk-control theme and a consistent 1280×720 grid across all pages.
- Added a header/date slicer, left page-navigation and filter rail, five KPI cards with trend context, and a balanced comparison/composition/trend/detail chart zone on every page.
- Added and surfaced measures for Bad Loan Rate, Recovery Rate, Expected Loss, Low Recovery Exposure, Funding Rate, Income Verification Rate, High Risk Rule Rate, 60M Bad Loan Rate and period-over-period movement.
- Implemented the Lark Good/Neutral/Bad logic using recovery rate and loan seasoning against the dataset's December 2014 analysis horizon.
- Moved all calculations into a dedicated `Measure` table with 135 measures and display folders, matching the discoverable measure-catalog pattern used by the reference dashboard.
- Added Portfolio ROI, raw default rate/count, good-loan rate, bad-loan funded amount, investor funds, term 36M/60M mix, average delinquencies, public-record rate and their relevant movement measures.
- Replaced categorical `YearMonth` axes with the continuous `MonthStart` date field across 18 trend visuals. This removes horizontal truncation and makes the full 2007–2014 trend visible.
- Added an explicit seasoning layer using the December 2014 analysis horizon: `Seasoned >40%` and `Early-stage <=40%`. The report now shows both the overall bad-loan rate and the seasoned bad-loan rate so the assignment's "under consideration" condition is transparent rather than silently imposed.
- Added seasoned application, Good/Bad rate, recovery, coverage, period variance, 36M/60M term-gap, high-risk-rule rate/lift and model-evidence measures, and placed them in decision-useful visuals.
- Trained a reproducible random-forest/decision-tree analysis on the same CSV using origination-time borrower and loan attributes only. The holdout AUC is 0.698; top feature importance is led by interest rate (25.2%) and credit grade (22.8%).
- Added `risk_driver_importance.csv` and `risk_rule_summary.csv` as traceable derived tables. The assignment hypothesis (income < $30K, interest >17%, grade E/F/G) has a 15.8% seasoned bad rate and 2.79x lift; the 60M + grade C example has an 11.7% rate and 2.06x lift.
- Reframed the three pages as `Portfolio Overview`, `Borrower Risk`, and `Risk Drivers & Actions`. The first page now answers the 2007–2014 quality trend and seasoning question; the second compares borrower characteristics; the third surfaces feature importance, rule lift, term/grade risk and action thresholds.
- Refreshed and saved the PBIP in Power BI Desktop through MCP. All three pages rendered without unresolved report-definition or data-load errors.
- Reworked `Borrower Risk` into a customer-analysis page with five customer KPIs (customers, average delinquency, public-record rate, average interest rate, and average DTI), plus purpose, income-level, and home-ownership profiles.
- Replaced the marketplace-dependent decomposition tree with two native Power BI visuals: `Customer Loan Quality Mix by Purpose` and `Seasoned Bad Loan Rate by Income Level`. This preserves the customer journey analysis while avoiding import/render failures.
- Replaced the hard-to-interpret `Strategy Rules` table with a ranked horizontal bar chart, `Where Seasoned Bad Loans Concentrate | Purpose`, so risk concentration is directly actionable.
- Rebuilt the two unclear percentage trends as paired native views: loan-quality area distribution and Applications + Seasoned Bad Rate combo on Overview; 60M Applications + 60M Seasoned Bad Rate combo on Risk Drivers. Percentage axes now display as percentages rather than `M%` units.
- Added customer KPI display and movement measures for average delinquencies, public-record rate, and average DTI, and used them in the report rather than leaving them model-only.
- Reopened the PBIP through the Power BI Desktop MCP, refreshed all source tables, visually checked all three pages, and saved successfully at 03:11 on 24 Aug 2026.
- Replaced the cluttered multi-series `Customer Loan Quality Mix by Purpose` column chart with a ranked horizontal bar chart, `Highest-Risk Loan Purposes | Top 8 Seasoned Bad Rate`. Added `Purpose Seasoned Bad Rate Rank` and `Top 8 Purpose Seasoned Bad Rate` so only the eight decision-relevant purposes appear, sorted from highest to lowest risk with readable labels.
- Verified the revised Customer page in Power BI Desktop through MCP, refreshed the model, and saved successfully at approximately 03:25 on 24 Aug 2026.
- Removed the redundant term-comparison chart from `Risk Drivers & Actions` instead of replacing it with another visual or table. Expanded `Grade Action | Tighten approval for weak grades` across the full analysis row so the page has one clear decision view rather than overlapping term-risk signals.
- Reopened the PBIP through MCP, confirmed the hidden term visual no longer renders, refreshed all data, and saved successfully at 01:41 on 24 Aug 2026. The reference backup was not modified.
- Replaced the previous navy/teal/coral styling with an original `Plum Copper Editorial` theme across all three pages: plum `#4B2142` structure, copper `#D98324` emphasis, smoky blue `#5B6C8F`, sage `#6E9674`, warm ivory `#FAF7F2`, and charcoal-plum text `#2B2230`.
- Recolored page canvases, headers, navigation states, KPI sparklines/deltas, slicers, chart series, borders, shadows, and risk-state accents rather than changing only the theme palette. Added `apply_plum_copper_theme.py` so the design can be reproduced safely.
- Visually checked `Portfolio Overview`, `Borrower Risk`, and `Risk Drivers & Actions` in Power BI Desktop, refreshed the model without errors, and saved successfully at 01:49 on 24 Aug 2026.
- Refined the Borrower Risk composition to match the reference's decision density: `Applications by Purpose` now uses a ranked Top 5 application measure, removing the long tail of unreadable columns.
- Consolidated annual-income bands into three readable levels (`Low <30K`, `Medium 30K–90K`, `High >90K`) and consolidated home ownership into `Mortgage`, `Rent`, `Own`, and `Other`; both donut charts now show complete bottom legends and data labels.
- Removed the duplicated full-width grade-risk chart from `Risk Drivers & Actions`. Replaced it with paired term views: `Seasoned Bad Loan Rate by Term` and `Seasoned Recovery Rate by Term`, showing the risk/collection trade-off for 36-month versus 60-month loans.
- Added `Purpose Application Rank`, `Top 5 Purpose Applications`, and `HomeOwnershipGroup` to support the revised visuals. Verified all new visuals in Power BI Desktop with no TMDL/report-definition errors on 26 Aug 2026.
# 2026-08-26 — Term comparison and readable driver labels

- Replaced the two-category 36M/60M clustered bars on **Risk Drivers & Actions** with marker-based line comparisons:
  - **Term Risk Step-Up | 36M → 60M** — 4.7% to 12.8% seasoned bad-loan rate.
  - **Term Recovery Trade-off | 36M → 60M** — 87.6% to 70.9% seasoned recovery rate.
- Added `RiskDriverImportance[DriverLabel]` to keep feature names readable without losing business meaning (for example, `DTI Ratio`, `Ownership`, and `Verification`).
- Added `RiskRuleSummary[RuleLabel]` to replace unreadable raw decision-rule expressions with concise action labels such as `DT1 High-rate`, `Low-inc E/F/G`, and `60M Grade C`.
- Rebalanced the lower visual widths and bound the two ranked charts to the new display-label columns.
- Desktop verification: project opens successfully, both term comparison visuals render with data labels, lower chart labels show without ellipses, and the TMDL view reports **Problems 0**.
- Pre-change backup: `C:\Users\ADMIN\Downloads\CP2 - New\_backup_before_term_chart_fix_20260826\FinTech_Credit_Risk_PBIP`.
# 2026-08-26 — Axis-title cleanup across all report pages

- Disabled X- and Y-axis titles on every visible Cartesian chart across **Portfolio Overview**, **Borrower Risk**, and **Risk Drivers & Actions**.
- Specifically corrected `Seasoned Bad Rate by Grade`, `Top Purposes by Seasoned Bad Rate`, `Top 5 Loan Purposes by Applications`, `Feature Importance`, and `High-Risk Rule Combinations`, where missing object settings previously allowed Power BI defaults to display axis titles.
- Preserved category labels, scale tick labels, data labels, and tooltips; only redundant field-name titles were removed to increase usable plot area.
- Sparkline axes were already fully hidden and were left unchanged.
- Desktop verification: all visible chart-axis settings resolve to `showAxisTitle = false`, report JSON parses successfully, the project opens, and TMDL reports **Problems 0**.
- Pre-change backup: `C:\Users\ADMIN\Downloads\CP2 - New\_backup_before_axis_title_cleanup_20260826\FinTech_Credit_Risk_PBIP`.

# 2026-08-26 — KPI MoM context correction

- Saved the user's current four-page report state before changing the semantic model.
- Corrected KPI movement measures that previously compared the full 2007–2014 date range with a nearly overlapping shifted range, which flattened most cards to `0.0%`.
- Standard KPI deltas now compare the latest visible reporting month with the immediately preceding month while preserving State, Loan label, Purpose and other business filters.
- Seasoned-quality and Low-Recovery deltas now use the latest comparable month containing eligible seasoned records. Under the December 2014 analysis horizon, this is October 2013 versus September 2013; late-2014 originations are intentionally excluded because they have not reached the 40% seasoning threshold.
- Updated all movement cards on **Portfolio Overview**, **Borrower Risk**, **Pricing & Returns**, and the Low-Recovery movement card on **Risk Drivers & Actions**.
- Source-data reconciliation confirms non-zero changes, including Seasoned Applications `+9.1%`, Seasoned Bad Rate `-0.2 pp`, Seasoned Good Rate `-1.4 pp`, Seasoned Recovery `-1.6 pp`, Seasoning Coverage `-0.8 pp`, Average Loan `+4.1%`, Raw Default Rate `-1.5 pp`, and Borrowers `-58.8%`.
- Validation: report JSON parses with zero errors, semantic-model lineage tags contain zero duplicates, the PBIP reopened with a new Analysis Services workspace, and the engine log contains zero errors.
- Pre-change backup: `C:\Users\ADMIN\Downloads\CP2 - New\_backup_user_edits_before_mom_fix_20260826\FinTech_Credit_Risk_PBIP`.

# 2026-08-26 — Middle-page KPI error repair

- Diagnosed the broken delta cards on **Borrower Risk** and **Pricing & Returns** by querying the running local Analysis Services model directly through ADOMD/XMLA.
- The visual definitions were valid; the failure came from the DAX variable name `LastDate`, which conflicts with the reserved DAX function `LASTDATE`.
- Renamed the variable to `AnchorDate` in the nine unique movement measures used by the two pages.
- Reopened the PBIP without Computer Use and queried all 154 model measures: **0 measures in error state**.
- Live DAX results now return valid values, including Borrowers `-58.8%`, Average Loan `+4.1%`, Average Interest `-0.27 pp`, Verification `-0.06 pp`, Raw Default `-1.47 pp`, Portfolio ROI `-3.36 pp`, Public Record Rate `-1.23 pp`, and Average DTI `-0.40 pp`.
- Rechecked the remaining movement cards through the same semantic-model query: Seasoned Applications `+9.1%`, Seasoned Bad Rate `-0.20 pp`, Seasoned Good Rate `-1.42 pp`, Seasoned Recovery `-1.63 pp`, Coverage `-0.81 pp`, and Low-Recovery Exposure `+8.6%`.
# KPI title readability — 26 Aug 2026

- Updated all 20 KPI cards across Portfolio Overview, Borrower Risk, Pricing & Returns, and Risk Drivers & Actions.
- Moved each KPI label into the full-width visual title area and hid the constrained category label that produced ellipses.
- Standardized KPI titles to clear business names such as `Seasoned Recovery Rate`, `Verification Coverage`, and `Low-Recovery Exposure`.
- Preserved the existing value, delta and sparkline layers.
- Backup: `C:\Users\ADMIN\Downloads\CP2 - New\_backup_before_kpi_title_fix_20260826`.

# Internal KPI label wrapping — 26 Aug 2026

- Kept the Power BI visual Title disabled on all 20 KPI cards.
- Removed the custom text override from the existing internal category label so it follows the selected measure's semantic display name dynamically.
- Enabled native word wrapping and retained the original 11 pt semibold typography.
- Restored the label to the full internal card width (`right padding = 10`) so it can use the row above the sparkline and wrap within the existing card height.
- Did not add textboxes or external title elements and did not alter card dimensions, KPI values, MoM bindings/colors, or sparkline data/position/size.
- Validation: 20/20 titles off, 20/20 labels dynamic and wrapped, 20/20 original sparklines and delta bindings preserved, zero report JSON parse errors.
- Pre-change backup: `C:\Users\ADMIN\Downloads\CP2 - New\_backup_before_internal_label_wrap_20260826\FinTech_Credit_Risk_PBIP`.

# KPI text alignment and complete MoM indicator — 26 Aug 2026

- Lifted the internal KPI label/value block by approximately 6 px using asymmetric card padding (`top 4`, `bottom 14`) and moved the separate indicator visual from y=178 to y=172.
- Kept all 20 visual Titles disabled and retained dynamic, wrapped internal measure labels with bold styling.
- Kept every sparkline unchanged at its current lower position (`y=136`, `74×52`) with the same data, line/fill styling and colors.
- Added 15 display-only MoM measures feeding 16 temporal KPI indicators; Average Interest MoM is reused on two pages.
- MoM output is now sign-aware: `MoM: ▲ value`, `MoM: ▼ value`, or `MoM: 0.0%`, and uses `ABS()` so a down arrow is never combined with a negative sign.
- Added dynamic indicator colors: positive `#16A3B6`, negative `#E05252`, neutral `#777777`. The four non-temporal Risk Drivers annotations remain semantically unchanged.
- Validation: zero report JSON errors, zero duplicate measure names, zero duplicate lineage tags, 20/20 titles off, 20/20 sparkline geometries preserved.
- Pre-change backup: `C:\Users\ADMIN\Downloads\CP2 - New\_backup_before_kpi_text_mom_fix_20260826\FinTech_Credit_Risk_PBIP`.

# KPI card layout correction — 26 Aug 2026

- Reverted the interim container-title treatment after visual review; all 20 KPI container titles are hidden again.
- Restored one business label inside each KPI card and styled it as an 11 pt semibold accent label, matching the approved blue-dashboard card anatomy.
- Reduced the card's right padding from 82 px to 10 px. The label can now use the full card width while the independent sparkline remains in the lower-right area.
- Preserved KPI values, MoM/period deltas, sparklines, measures, filters and page geometry.
- Validated all 213 report JSON files and confirmed the corrected configuration on all 20 KPI cards.
- Pre-correction backup: `C:\Users\ADMIN\Downloads\CP2 - New\_backup_before_kpi_layout_correction_20260826`.
