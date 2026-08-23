# Build, QA, and handoff

## In-place enhancement procedure

1. Open `../Sports_Health_Enterprise_Financial_Performance_Dashboard.pbix` in Power BI Desktop.
2. Record the actual source settings, tables, relationships, measures, pages, visual counts, bookmarks, and interactions.
3. Save a recoverable copy before material model or layout changes.
4. Implement the requested edit inside the PBIX.
5. Reconcile every changed KPI/visual using the data available in the file.
6. Review Overview, Breakdown, Segments, and Breakeven at 100% and Fit to page.
7. Save, close, reopen, and repeat a smoke test.

## QA checklist

### Artifact truth

- [ ] Work was performed on the existing PBIX.
- [ ] No claim of from-scratch rebuildability was made.
- [ ] Missing source/PBIP limitations remain disclosed.

### Model and measures

- [ ] Tables, relationships, measures, and source settings were inventoried before changes.
- [ ] Changed measures reconcile to existing model data.
- [ ] No confidential or unsupported values were added.
- [ ] Format strings and numeric sorting remain correct.

### Report

- [ ] Overview, Breakdown, Segments, and Breakeven pages remain available.
- [ ] Navigation, filters, reset, bookmarks, and cross-filtering work.
- [ ] No clipped, blurred, overlapping, or empty visuals were introduced.
- [ ] Portfolio images contain the dashboard canvas rather than Desktop chrome.

### Delivery

- [ ] PBIX was saved, closed, and reopened successfully.
- [ ] HTML story and README links still work.
- [ ] Exact tests performed and remaining limitations are stated in the handoff.

## Current artifact status

- PBIX and HTML story are published and described as review-ready.
- Raw source, PBIP, TMDL, and formal reconciliation artifacts are not published.
- The project cannot be reliably automated from scratch until those missing artifacts are added.
