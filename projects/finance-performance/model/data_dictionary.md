# Data dictionary

Auto-exported from the canonical TMDL tables. Business rules and source limitations are documented in `../agent/DATA_MODEL_SPEC.md`.

| Table | Column | Data type | Source column | Format | Summarization |
|---|---|---|---|---|---|
| DimDate | Date | dateTime | [Date] | M/d/yyyy | none |
| DimDate | Year | int64 |  | 0 | none |
| DimDate | MonthNumber | int64 |  | 0 | none |
| DimDate | Month | string |  |  | none |
| DimDate | YearMonth | string |  |  | none |
| DimDate | YearMonthSort | int64 |  | 0 | none |
| DimDate | Quarter | string |  |  | none |
| FactFinance | Company | string | Company |  | none |
| FactFinance | CIK | string | CIK |  | none |
| FactFinance | DisplayMetric | string | DisplayMetric |  | none |
| FactFinance | Concept | string | Concept |  | none |
| FactFinance | MetricClass | string | MetricClass |  | none |
| FactFinance | MetricSort | int64 | MetricSort | 0 | none |
| FactFinance | PeriodType | string | PeriodType |  | none |
| FactFinance | PeriodLabel | string | PeriodLabel |  | none |
| FactFinance | StartDate | dateTime | StartDate | mmm d, yyyy | none |
| FactFinance | EndDate | dateTime | EndDate | mmm d, yyyy | none |
| FactFinance | FiscalYear | int64 | FiscalYear | 0 | none |
| FactFinance | FiscalPeriod | string | FiscalPeriod |  | none |
| FactFinance | Value | decimal | Value | $#,0 | sum |
| FactFinance | Form | string | Form |  | none |
| FactFinance | FiledDate | dateTime | FiledDate | mmm d, yyyy | none |
| FactFinance | Frame | string | Frame |  | none |
| FactFinance | AccessionNumber | string | AccessionNumber |  | none |
