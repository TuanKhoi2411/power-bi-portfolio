# Semantic-model notes

## Architecture

The current model uses one analytical table, `FactMarketing`, because the source is a single contact-level campaign file and the published report does not require a separate conformed dimension model.

## Calculation layers

1. Base: Contacts and Conversions.
2. Ratio/efficiency: Conversion Rate, Conversions per 1K, average duration, average campaign contacts.
3. Context/quality: prior-contact rate, cellular share, successful prior outcome.
4. Movement: previous-month, MoM, and percentage-point change.
5. Display: formatted KPI strings for cards only.

## Important decisions

- `unknown` remains a real reported category.
- Derived age, duration, and contact-frequency bands support segmentation but do not create causal evidence.
- Call duration is post-contact and can leak outcome information in prediction/targeting use cases.
- Campaign month is converted into a technical date context for report navigation; it must not be described as a complete real-world daily timeline.
- Segment rate always needs contact-volume context.

The canonical TMDL is authoritative; `model/` files are regenerated human/agent-readable exports.
