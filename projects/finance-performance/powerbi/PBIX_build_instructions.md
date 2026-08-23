# PBIX build instructions

## Targets

- PBIP: `../dashboard/Apple_Inc_Financial_Performance_Dashboard.pbip`
- PBIX: `../Apple_Inc_Financial_Performance_Dashboard.pbix`
- Source: `../data/sec-aapl-companyfacts.json`

## Build steps

1. Open the complete PBIP in Power BI Desktop.
2. Replace the local JSON `SourcePath` with the repository SEC file.
3. Refresh and inspect concept mapping, USD units, form, filing date, accession, frame, fiscal period, and instant/duration classification.
4. Confirm `FactFinance[EndDate]` → `DimDate[Date]`.
5. Confirm all 90 measures and three 1280×720 pages.
6. Reconcile representative income-statement and balance-sheet periods.
7. Test navigation, reset, slicers, cross-filtering, period compatibility, and filing detail.
8. Save PBIP; use **File → Save As** to update the PBIX.
9. Close/reopen PBIX and repeat a smoke/reconciliation test.

## Documentation/validation commands

```powershell
./scripts/export-model-documentation.ps1
./scripts/validate-pbip-structure.ps1
./scripts/validate-agent-packages.ps1
```

Structural pass is not Desktop acceptance. Record refresh/reopen and accounting reconciliation separately.
