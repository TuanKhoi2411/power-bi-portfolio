# Metric definitions — Marketing

Exact formulas and formats are in `measures.dax` and `measure_catalog.csv`.

| Metric | Business definition | Filter behavior / caution |
|---|---|---|
| Contacts | Count of contact records in filter context | One source row equals one contact |
| Conversions | Contacts whose subscription outcome is `yes` | Must reconcile to target mapping |
| Conversion Rate | Conversions divided by Contacts | Always show contact/base volume for segments |
| Conversions per 1K Contacts | Conversion rate expressed per 1,000 contacts | Efficiency view, not incremental lift |
| Average Contact Duration | Average call duration in seconds | Post-contact variable; leakage risk for targeting |
| Average Campaign Contacts | Average number of contacts during the campaign | Context for contact pressure/frequency |
| Prior Contact Rate | Share of contacts with prior campaign contact | Historical association only |
| Cellular Contact Share | Share of contacts using cellular channel | Channel mix, not causal effectiveness |
| Successful Prior Outcome Rate | Share associated with a prior successful outcome | Small-base and selection effects may apply |
| MoM / variance pp | Month-context movement in count/rate | Technical month sequence; not a complete daily chronology |
