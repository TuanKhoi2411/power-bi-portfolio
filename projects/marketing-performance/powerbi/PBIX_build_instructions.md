# PBIX build instructions

## Targets

- PBIP: `../dashboard/Portuguese_Bank_Marketing_Performance_Dashboard.pbip`
- PBIX: `../Portuguese_Bank_Marketing_Performance_Dashboard.pbix`
- Source: `../data/bank-additional-full.csv`

## Build steps

1. Open the complete PBIP project in Power BI Desktop.
2. Replace the local `FactMarketing` source path with the repository CSV.
3. Verify the semicolon delimiter and refresh 41,188 contact rows unless documented transformations change the count.
4. Review types, `unknown` categories, target mapping, bands, and campaign-date logic.
5. Confirm all 34 measures and all three 1280×720 pages.
6. Test page navigation, reset, audience/campaign filters, cross-highlighting, sample-size context, and tables.
7. Save PBIP; use **File → Save As** to update the packaged PBIX.
8. Close/reopen PBIX and repeat representative filters and totals.

## Documentation/validation commands

```powershell
./scripts/export-model-documentation.ps1
./scripts/validate-pbip-structure.ps1
./scripts/validate-agent-packages.ps1
```

Do not mark a changed build complete without a current Desktop refresh/reopen test.
