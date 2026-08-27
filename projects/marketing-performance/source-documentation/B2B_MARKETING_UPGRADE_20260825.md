# Portuguese bank marketing analytics upgrade — 25 Aug 2026

## Backup

`C:\pbi-portfolio-v2\Portuguese_Bank_Marketing_Performance_v2\dashboard\_backup_before_b2b_measure_upgrade_20260825\Portuguese_Bank_Marketing_ModelConnected`

## Changes

- Preserved the approved three-page layout and existing marketing theme.
- Removed duplicated Overview visuals:
  - Replaced the repeated Job conversion chart with **Conversion Rate by Contact Channel**.
  - Replaced the repeated Contact Channel Mix donut with **Contact Frequency Mix**.
- Added reviewable-period conversion measures. The KPI uses the latest month with at least 500 contacts and compares it with the prior reviewable month, avoiding a misleading December result based on only 182 contacts.
- Added contact-pressure measures for customers receiving four or more campaign contacts; the new `4+ Contact %` KPI includes percentage-point movement and a monthly sparkline.
- Model totals after the upgrade: 10 tables, 9 active relationships, 52 explicit measures, and 3 report pages.

## Source-data cross-check

- Contacts: **41,188**; conversions: **4,640**; overall conversion: **11.27%**.
- Latest reviewable month: November, **4,101 contacts**, **10.14% conversion**.
- Prior reviewable month: October, **718 contacts**, **43.87% conversion**.
- Four-or-more contact share: October **4.18%**, November **10.29%**, movement **+6.11 pp**.
- Channel conversion: cellular **14.74%** vs telephone **5.23%**.
- Contact-frequency mix: one contact **42.83%**, two-to-three **38.63%**, four-to-five **10.32%**, six-plus **8.22%**.

## Validation

- All report JSON files parse successfully.
- Zero missing report field references.
- No duplicate measure names or lineage tags.

