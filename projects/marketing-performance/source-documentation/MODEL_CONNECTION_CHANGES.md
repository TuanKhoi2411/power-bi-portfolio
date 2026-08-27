# Marketing model connection changes

- Added readable attributes to Job, Channel, Prior Outcome, and Age Band dimensions.
- Added `DimMaritalStatus`, `DimEducation`, `DimDayOfWeek`, and `DimContactFrequency`.
- Expanded the model from 5 to 9 active relationships.
- Rebound all report-facing categorical and campaign-date fields from `FactMarketing` to dimensions.
- Updated previous-month and conversion-contribution measures so DimDate filters do not collapse comparisons.
- Validation: 10 tables, 9 relationships, 41 measures, 3 pages, zero missing report references.
- Restored the populated import cache after model migration; the temporary blank report was caused by opening the PBIP without cached/processed data.
- Live-model verification: 41,188 contacts, 4,640 conversions, conversion rate 11.27%.
- 25 Aug 2026: removed duplicated Overview visuals, added reviewable-period conversion logic and contact-pressure measures, and connected them to KPI cards, deltas, and sparklines. Post-change validation: 52 measures and zero missing report references.
