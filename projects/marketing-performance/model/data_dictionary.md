# Data dictionary

Auto-exported from the canonical TMDL tables. Business rules and source limitations are documented in `../agent/DATA_MODEL_SPEC.md`.

| Table | Column | Data type | Source column | Format | Summarization |
|---|---|---|---|---|---|
| FactMarketing | ContactId | int64 | ContactId |  | none |
| FactMarketing | Age | int64 | Age | 0 | none |
| FactMarketing | Job | string | Job |  | none |
| FactMarketing | MaritalStatus | string | MaritalStatus |  | none |
| FactMarketing | Education | string | Education |  | none |
| FactMarketing | CreditDefault | string | CreditDefault |  | none |
| FactMarketing | HousingLoan | string | HousingLoan |  | none |
| FactMarketing | PersonalLoan | string | PersonalLoan |  | none |
| FactMarketing | ContactChannel | string | ContactChannel |  | none |
| FactMarketing | CampaignMonth | string | CampaignMonth |  | none |
| FactMarketing | CampaignMonthNumber | int64 | CampaignMonthNumber | 0 | none |
| FactMarketing | ContactDayOfWeek | string | ContactDayOfWeek |  | none |
| FactMarketing | DurationSeconds | int64 | DurationSeconds | 0 | none |
| FactMarketing | CampaignContacts | int64 | CampaignContacts | 0 | none |
| FactMarketing | DaysSincePriorContact | int64 | DaysSincePriorContact | 0 | none |
| FactMarketing | PriorContacts | int64 | PriorContacts | 0 | none |
| FactMarketing | PriorOutcome | string | PriorOutcome |  | none |
| FactMarketing | EmploymentVariationRate | double | EmploymentVariationRate | 0.0 | none |
| FactMarketing | ConsumerPriceIndex | double | ConsumerPriceIndex | 0.000 | none |
| FactMarketing | ConsumerConfidenceIndex | double | ConsumerConfidenceIndex | 0.0 | none |
| FactMarketing | Euribor3Month | double | Euribor3Month | 0.000 | none |
| FactMarketing | NumberEmployed | double | NumberEmployed | #,0.0 | none |
| FactMarketing | SubscriptionOutcome | string | SubscriptionOutcome |  | none |
| FactMarketing | Converted | int64 | Converted | 0 | sum |
| FactMarketing | AgeBand | string | AgeBand |  | none |
| FactMarketing | DurationBand | string | DurationBand |  | none |
| FactMarketing | ContactFrequencyBand | string | ContactFrequencyBand |  | none |
| FactMarketing | PriorContacted | string | PriorContacted |  | none |
| FactMarketing | month | string | month |  | none |
| FactMarketing | CampaignDate | dateTime | CampaignDate | M/d/yyyy | none |
