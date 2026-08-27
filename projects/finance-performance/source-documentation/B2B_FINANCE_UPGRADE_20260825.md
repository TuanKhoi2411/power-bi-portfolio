# Apple finance analytics upgrade — 25 Aug 2026

## Backup

`C:\pbi-portfolio-v2\Apple_Inc_Financial_Performance_v2\dashboard\_backup_before_b2b_measure_upgrade_20260825\Apple_Finance_ModelConnected`

## Changes

- Preserved the approved three-page layout and existing finance theme.
- Added `Quarterly Operating Income Previous Year`, `Quarterly Operating Income YoY`, and `Operating Leverage Spread`.
- Reworked the Profitability & Growth comparison from an unclear mix of Revenue YoY and Net Margin into **Revenue vs Operating Income YoY**.
- The revised chart now answers whether operating profit is scaling faster or slower than revenue; margin remains covered by the KPI row, margin-quality chart, conversion chart, and profitability table.
- Model totals after the upgrade: 5 tables, 4 active relationships, 111 explicit measures, and 3 report pages.

## Source-data cross-check

The new operating-leverage logic was independently checked against the SEC Apple company-facts JSON. Examples from the latest source quarters:

- CY2025 Q4: Revenue YoY **+15.7%**, Operating Income YoY **+18.7%**, leverage spread **+3.1 pp**.
- CY2026 Q1: Revenue YoY **+16.6%**, Operating Income YoY **+21.3%**, leverage spread **+4.7 pp**.
- CY2026 Q2: Revenue YoY **+16.4%**, Operating Income YoY **+26.6%**, leverage spread **+10.2 pp**.

## Validation

- All report JSON files parse successfully.
- Zero missing report field references.
- No duplicate measure names or lineage tags.

