# Build, QA, and handoff

## Build procedure

1. Open `../dashboard/Portuguese_Bank_Marketing_Performance_Dashboard.pbip`.
2. Point the `FactMarketing` source to `../data/bank-additional-full.csv`.
3. Confirm delimiter, column types, category handling, and refresh.
4. Verify all 34 measures and all three 1280×720 pages.
5. Save PBIP and update `../Portuguese_Bank_Marketing_Performance_Dashboard.pbix`.
6. Close and reopen the PBIX; test navigation, slicers, reset, and key totals.

## QA checklist

### Data and model

- [ ] Source has 41,188 rows before documented exclusions.
- [ ] `Converted` maps only the published target outcome.
- [ ] `unknown` categories are retained or disclosed.
- [ ] Contacts, Conversions, and Conversion Rate reconcile.
- [ ] Numeric measures drive sorting and calculations.

### Analytical integrity

- [ ] No causal claims are made from observational comparisons.
- [ ] Duration leakage is disclosed.
- [ ] Segment rates are accompanied by population/contact volume.
- [ ] Recommendations are phrased as experiments or follow-up analysis.

### Report and delivery

- [ ] Three required pages exist at 1280×720.
- [ ] Navigation, slicers, reset, cross-filtering, and tables work.
- [ ] Text, legends, rates, and category labels are readable.
- [ ] PBIP and PBIX both open after save/reopen.
- [ ] Portfolio screenshots exclude Desktop chrome and remain sharp.
- [ ] Unperformed tests and limitations are disclosed.

## Current artifact status

- PBIP, semantic model, report definition, raw source, PBIX, and HTML story are published.
- The Power Query source path may require a machine-specific update before refresh.
- Previous packaging produced a PBIX, but every future rebuild still requires a fresh Desktop reopen and visual QA before claiming completion.
