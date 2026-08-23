# PBIX build instructions

## Target files

- PBIP: `../dashboard/UK_Online_Retail_Sales_Performance_Dashboard.pbip`
- PBIX: `../UK_Online_Retail_Sales_Performance_Dashboard.pbix`
- Source: `../data/Online Retail.xlsx`

## Build steps

1. Download or clone the complete project; do not copy only the `.pbip` pointer.
2. Open the PBIP entry point in Power BI Desktop.
3. In Power Query, replace the existing machine-specific `SourcePath` with the absolute path to `data/Online Retail.xlsx`. The canonical transformation is in `PowerQuery_M.txt`.
4. Refresh `FactSales` and `DimDate`.
5. Confirm the active relationship and 74 measures.
6. Confirm the page metadata contains all three pages and a valid active page.
7. Review UK Retail Sales, Customer Insights, and Product & Returns.
8. Test date/country/product/transaction slicers, page navigation, reset, cross-highlighting, Top-N sorting, and detail tables.
9. Save the PBIP.
10. Use **File → Save As** and save/update the packaged PBIX using the target filename.
11. Close Power BI Desktop, reopen the PBIX, refresh if permitted, and visually inspect all pages.

## Source-path portability

The TMDL export intentionally exposes the original local source path so reviewers can see the actual dependency. Before sharing a refreshable build, replace it with the recipient's path or implement a documented project-root parameter.

## Regenerate documentation

After TMDL edits:

```powershell
./scripts/export-model-documentation.ps1
./scripts/validate-pbip-structure.ps1
./scripts/validate-agent-packages.ps1
```

## Completion rule

Structural validation alone is insufficient. Mark a new build complete only after source refresh, reconciliation, interaction testing, PBIX save, close, and reopen.
