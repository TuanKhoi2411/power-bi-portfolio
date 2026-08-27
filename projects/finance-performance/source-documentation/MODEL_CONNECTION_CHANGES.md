# Finance model connection changes

- Added readable attributes to Metric, Form, and Period Type dimensions.
- Added Metric Class and hidden Metric Sort to `DimMetric`.
- Rebound all report-facing Metric, SEC Form, Period Type, and Reporting Date fields to dimensions.
- Kept fiscal-year and fiscal-period fields on the fact because they are filing-specific attributes rather than calendar attributes.
- Validation: 5 tables, 4 relationships, 108 measures, 3 pages, zero missing report references.
- Restored the populated import cache after model migration; the temporary blank report was caused by opening the PBIP without cached/processed data.
- Live-model verification: 645 fact rows, 9 metrics, full-model Revenue 7,760,200,000,000.
- 25 Aug 2026: added operating-leverage measures and replaced the mixed Revenue YoY / Net Margin chart with Revenue vs Operating Income YoY. Post-change validation: 111 measures and zero missing report references.
