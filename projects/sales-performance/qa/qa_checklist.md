# QA checklist — UK Online Retail Sales

## Source and transformation

- [ ] Included UCI workbook is used.
- [ ] Source grain and 541,909-row expectation are reviewed.
- [ ] Date range is 1 Dec 2010–9 Dec 2011.
- [ ] Unknown customer IDs, cancellations, negative quantities, invalid prices, and missing descriptions are profiled.
- [ ] Transformation changes include before/after row counts and reconciliation impact.

## Semantic model and DAX

- [ ] `FactSales` and `DimDate` load.
- [ ] SalesDate-to-Date relationship is active and single direction.
- [ ] All 74 measures parse and retain format/display-folder metadata.
- [ ] Gross Sales, Return Amount, and Net Sales reconcile.
- [ ] Orders and Customers use intended distinct-count logic.
- [ ] MoM logic handles the incomplete final month intentionally.
- [ ] Top-N and merchandise exclusions return plausible rankings.
- [ ] KPI text measures are not used for numeric calculations or sorting.

## Report and interactions

- [ ] Three pages exist at 1280×720.
- [ ] Active page and page order resolve.
- [ ] Each page has navigation, reset, slicers, KPIs, analysis, and detail.
- [ ] Customer page discloses anonymous/unknown-customer limitations.
- [ ] Returns remain visibly distinct from positive sales.
- [ ] Slicers, cross-highlighting, Top-N sorting, and detail tables work.
- [ ] No visual clips, overlaps, hides data, or shows an unintended scrollbar.

## Desktop and delivery

- [ ] PBIP opens without report-definition errors.
- [ ] Refresh succeeds on the current machine.
- [ ] PBIX saves under the documented name.
- [ ] PBIX closes and reopens successfully.
- [ ] Clean screenshots exclude Desktop chrome and remain readable.
- [ ] README, story, PBIP, PBIX, source, and documentation links resolve.
- [ ] Any unperformed test is disclosed.
