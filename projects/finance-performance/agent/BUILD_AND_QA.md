# Build, QA, and handoff

## Build procedure

1. Open `../dashboard/Apple_Inc_Financial_Performance_Dashboard.pbip`.
2. Point `FactFinance` to `../data/sec-aapl-companyfacts.json`.
3. Refresh and inspect taxonomy mapping, units, forms, frames, period types, and duplicate-period handling.
4. Confirm the `EndDate` relationship and all 90 measures.
5. Review all three pages, save PBIP, and update `../Apple_Inc_Financial_Performance_Dashboard.pbix`.
6. Close and reopen the PBIX; verify totals, interactions, and visual state.

## QA checklist

### Source and model

- [ ] Source is the included SEC EDGAR company-facts JSON.
- [ ] Company/CIK, units, form, filed date, accession, period, and frame are preserved.
- [ ] Instant and duration facts are handled separately.
- [ ] Restated/duplicate period facts follow a documented selection rule.
- [ ] `FactFinance[EndDate]` → `DimDate[Date]` is active and appropriate.

### Measures

- [ ] Revenue, Gross Profit, Operating Income, and Net Income reconcile by period.
- [ ] Margins use matching-period Revenue.
- [ ] Assets, Liabilities, and Cash use point-in-time logic.
- [ ] Latest and YoY values reconcile to trend/detail visuals.
- [ ] Display measures are not used for numeric sorting.

### Report and delivery

- [ ] Three required pages exist at 1280×720.
- [ ] Navigation, slicers, reset, cross-filtering, and tables work.
- [ ] Units, currency scale, fiscal context, and source labels are readable.
- [ ] No investment recommendation is implied.
- [ ] PBIP and PBIX open after save/reopen.
- [ ] Screenshots exclude Desktop chrome and remain sharp.
- [ ] All unperformed tests are disclosed.

## Current artifact status

- PBIP, semantic model, report definition, SEC source, PBIX, and HTML story are published.
- The Power Query source path may need updating on a different machine.
- Every future rebuild requires a fresh Desktop reopen and visual QA before claiming completion.
