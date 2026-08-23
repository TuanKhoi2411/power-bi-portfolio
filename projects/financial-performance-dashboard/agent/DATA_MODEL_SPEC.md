# Known data and model specification

## Evidence status

The following information is documented by the existing project README and packaged PBIX, but the repository does not publish the raw source or source-controlled semantic model. An agent must inspect the PBIX to confirm implementation details before editing.

| Item | Documented state |
|---|---|
| Entity | Illustrative Sports & Health Enterprise |
| Period | 2023 portfolio case |
| Documented transaction count | 580 |
| Model shape | One fact table and six dimensions |
| Published source file | None |
| Published PBIP/TMDL | None |

## Required model inspection

Before changing the PBIX, record:

- data-source type and connection path;
- table and column inventory;
- fact grain and business keys;
- dimension keys and relationship direction/cardinality;
- all measure names, DAX, formats, display folders, and dependencies;
- date table and time-intelligence behavior;
- data categories, sort-by columns, hidden fields, and row counts.

## Expected analytical domains

The existing report is described as covering:

- revenue, cost, profit, and margin;
- segment contribution;
- operating-expense and EBIT drivers;
- break-even dynamics;
- management-oriented P&L review.

These are expectations, not permission to invent fields or measures. Use only what exists in the PBIX unless the user provides additional source data.

## Full-rebuild prerequisites

A rebuild package requires all of the following:

1. published raw source with source and usage notes;
2. documented grain, date coverage, field definitions, and data-quality profile;
3. PBIP export containing report and semantic-model definitions;
4. source-path/parameter instructions;
5. measure and relationship inventory;
6. reconciliation controls and expected outputs.

Until those artifacts exist, classify the project as `PBIX enhancement only`.
