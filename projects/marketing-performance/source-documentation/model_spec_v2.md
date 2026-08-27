# Data and semantic-model specification

## Source contract

| Item | Contract |
|---|---|
| Publisher | UCI Machine Learning Repository — Bank Marketing |
| Local file | `../data/bank-additional-full.csv` |
| Observation grain | One outbound marketing contact |
| Published row count | 41,188 contacts |
| Target | Term-deposit subscription outcome (`yes`/`no`) |
| Quality conditions | `unknown` categories, class imbalance, post-contact duration, historical macro variables |

## Model contract

The current semantic model uses a single analytical fact table, `FactMarketing`, with measures stored on that table. Canonical definition:

`../dashboard/Portuguese_Bank_Marketing.SemanticModel/definition/tables/FactMarketing.tmdl`

Required fields include:

- contact identity and profile: `ContactId`, `Age`, `Job`, `MaritalStatus`, `Education`, `CreditDefault`, `HousingLoan`, `PersonalLoan`;
- campaign context: `ContactChannel`, `CampaignMonth`, `CampaignNumber`, `ContactDayOfWeek`, `DurationSeconds`, `CampaignContacts`, `DaysSincePriorContact`, `PriorContacts`, `PriorOutcome`;
- economic context: `EmploymentVariationRate`, `ConsumerPriceIndex`, `ConsumerConfidenceIndex`, `Euribor3Month`, `NumberEmployed`;
- outcomes and derived groups: `SubscriptionOutcome`, `Converted`, `AgeBand`, `DurationBand`, `ContactFrequencyBand`, `PriorContacted`, `CampaignDate`.

## Measure contract

`FactMarketing.tmdl` currently contains 34 measures.

Core numeric measures:

- Contacts, Conversions, Conversion Rate
- Average Contact Duration, Average Campaign Contacts
- Prior Contact Rate, Cellular Contact Share, Successful Prior Outcome Rate
- Conversions per 1K Contacts
- Previous-month, month-over-month, and variance-percentage-point measures

Display measures are formatting helpers; keep numeric base measures available for charts, sorting, tooltips, and QA.

## Refresh requirement

Replace any machine-specific CSV `SourcePath` with the repository file or a documented project-root parameter. Confirm the semicolon delimiter and data types before applying transformations.

## Minimum reconciliation

- Contacts equals source row count after documented filters.
- Conversions equals rows whose target is `yes`.
- Conversion Rate equals Conversions / Contacts in the same filter context.
- Category totals reconcile to the overall population.
- Time-based views do not imply a real day-level chronology when only month/day-of-week context exists.

## Analytical limitations

- This is observational campaign data; associations do not establish causality.
- Call duration is observed after contact and can create target leakage in a predictive or pre-call targeting use case.
- Historical campaign context may not generalize to current customers, channels, regulation, or macro conditions.

## v2 contract addendum

- Campaign month is categorical; CampaignDate is a technical sort key only.
- Headline audience rate rankings require at least 500 contacts.
- Sample Size Status must accompany investigative views below the threshold.
- Duration remains post-contact evidence and carries an explicit leakage warning.
