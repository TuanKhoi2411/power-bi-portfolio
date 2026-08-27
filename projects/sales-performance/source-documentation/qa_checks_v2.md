# QA checks v2

## Automated/static checks

- [x] PBIP report path resolves to the renamed Report folder.
- [x] Report dataset path resolves to the renamed SemanticModel.
- [x] Three pages exist at 1280×720.
- [x] All visual JSON files parse.
- [x] Source workbook exists.
- [x] Source values independently reconciled with Python/pandas.
- [x] No source rows were changed.

## Expected totals after refresh

| Check | Expected |
|---|---:|
| Rows | 541,909 |
| Gross Sales | £10,666,684.54 |
| Return Amount | £896,812.49 |
| Net Sales | £9,747,747.93 |
| Orders | 20,728 |
| Identified Orders | 18,536 |
| Customers | 4,372 |
| Gross-to-Net residual | -£22,124.12 |

## Desktop checks completed

- [x] Opened the renamed PBIP in Power BI Desktop 2.156.951.0.
- [x] Refreshed the included workbook successfully; cards and charts populated.
- [x] Confirmed Product & Returns rendered without unresolved visual errors.
- [x] Saved the v2 project.
- [x] Reopened and refreshed after the chart-choice revision.
- [x] Confirmed the original shifted-line MoM comparison rendered, then superseded it with the more direct variance waterfall below.
- [x] Confirmed `Monthly Sales Mix: Identified vs Anonymous` renders as native stacked columns with no unresolved visual error.
- [x] Replaced the shifted-line MoM comparison with `Net Sales MoM Change | Complete Months`; confirmed the native waterfall renders increases, decreases, and total without the incomplete December 2011 period.

## Desktop checks still required

1. Verify Customer Sales Coverage is about 85.15% at the full-data level.
2. Test every navigation/reset/slicer/cross-highlight/table-sort path.
3. Close and reopen the saved project for a separate smoke test.
# 2026-08-25 — Returns/customer redesign review

- PASS: Net Sales and Return Rate render on separate axes in the monthly combo chart.
- PASS: the retention donut reconciles Net Sales plus Returns to Gross Sales and renders 91.57% retained / 8.43% returned in the unfiltered view.
- PASS: the customer concentration donut excludes `Unknown` and renders Top 10 identified customers at 16.5% of identified sales.
- PASS: the country panel shows five nonblank countries with no category scrollbar.
