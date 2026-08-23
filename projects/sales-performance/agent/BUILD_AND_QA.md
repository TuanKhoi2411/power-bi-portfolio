# Build, QA, and handoff

## Build procedure

1. Download the complete project, including `dashboard/` and `data/`.
2. Open `../dashboard/UK_Online_Retail_Sales_Performance_Dashboard.pbip` in Power BI Desktop.
3. Update the `FactSales` source path to `../data/Online Retail.xlsx` or an absolute equivalent for the current machine.
4. Refresh all queries and inspect transformation errors.
5. Confirm the relationship and all 74 measures load successfully.
6. Review all three pages at 100% and Fit to page.
7. Save the PBIP and create/update `../UK_Online_Retail_Sales_Performance_Dashboard.pbix`.
8. Close and reopen the PBIX; repeat a visual and interaction smoke test.

## QA checklist

### Data

- [ ] Source file exists and publisher is cited.
- [ ] Grain and date coverage match `DATA_MODEL_SPEC.md`.
- [ ] Missing customer IDs and cancellation/return rows are profiled.
- [ ] No undocumented row filters or synthetic replacements were introduced.

### Model and measures

- [ ] `FactSales[SalesDate]` → `DimDate[Date]` is active and single-direction unless documented otherwise.
- [ ] Gross Sales, Return Amount, and Net Sales reconcile.
- [ ] Orders are distinct invoices; Customers are distinct identified IDs.
- [ ] Time-intelligence and Top-N measures return plausible results.
- [ ] Formatted KPI measures are not used for numeric sorting.

### Report

- [ ] Three required pages exist at 1280×720.
- [ ] Navigation, slicers, reset, cross-filtering, and tables work.
- [ ] Labels, currency symbols, decimal precision, and titles are readable.
- [ ] No clipped objects, overlapping text, empty visuals, or Desktop chrome in exported imagery.
- [ ] Returns/cancellations remain visually distinct from positive sales.

### Delivery

- [ ] PBIP opens from the repository structure.
- [ ] PBIX opens after close/reopen.
- [ ] README and HTML story links still resolve.
- [ ] Any unperformed test is disclosed in the handoff.

## Current artifact status

- PBIP, semantic model, report definition, raw source, PBIX, and HTML story are published.
- The model currently uses a local source-path pattern that must be updated per machine before refresh.
- The repository package was previously marked review-ready; a fresh Desktop reopen must still be performed after any future rebuild before an agent claims new completion.
