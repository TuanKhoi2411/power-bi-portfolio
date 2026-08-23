# BI Dashboard Creation Prompt — Portuguese Bank Marketing Performance

## Objective

Create or rebuild a complete Power BI product named **Portuguese Bank Marketing Performance Dashboard**.

Management question:

> Which audiences and campaign conditions are associated with stronger term-deposit subscription conversion?

The dashboard must support campaign review, segmentation, and experiment design without overstating causality or using unavailable cost/revenue data.

## Required inputs

- Raw source: `data/bank-additional-full.csv`
- PBIP: `dashboard/Portuguese_Bank_Marketing_Performance_Dashboard.pbip`
- Report: `dashboard/Portuguese_Bank_Marketing.Report/`
- Model: `dashboard/Portuguese_Bank_Marketing.SemanticModel/`
- Power Query: `powerbi/PowerQuery_M.txt`
- DAX: `model/measures.dax`
- Measure catalog: `model/measure_catalog.csv`
- Data dictionary: `model/data_dictionary.md`
- Relationship map: `model/relationship_map.md`
- Report blueprint: `agent/REPORT_SPEC.md`

## Source and analytical rules

- Publisher: UCI Machine Learning Repository, Bank Marketing.
- Grain: one outbound marketing contact.
- Source row count: 41,188.
- Target: term-deposit subscription outcome (`yes`/`no`).
- Preserve audience, loan/default, contact, campaign, prior-contact, outcome, and macroeconomic fields.
- Keep `unknown` as an explicit category unless a documented rule says otherwise.
- Call duration is post-contact information; display it with a leakage warning and do not present it as an unqualified pre-call targeting feature.
- The source is observational. Use “associated with,” “observed,” and “test” language rather than causal claims.
- Do not invent campaign spend, CPA, revenue, ROI, uplift, or experimental control groups.

## Agent roles

1. **Manager agent** — define campaign-review scope and acceptance criteria.
2. **Data analyst** — profile target balance, segment bases, unknowns, timing, and leakage risk.
3. **Power BI specialist** — maintain M, TMDL, DAX, PBIR, interactions, and PBIX packaging.
4. **Responsible-analysis reviewer** — flag causal overreach, small bases, leakage, and discriminatory recommendations.
5. **UI/UX reviewer** — enforce hierarchy, contrast, compact filters, and readable segment comparisons.
6. **QA reviewer** — run structure, source, measure, interaction, and Desktop tests.

## Required theme and layout

- Canvas: 1280×720.
- Visibly distinct Marketing theme: navy/dark campaign context with purple, coral, and mint/teal highlights, implemented on readable white/neutral report surfaces.
- Five KPI cards with compact movement context.
- Four concise slicers; no duplicated labels.
- Navigation/filter treatment must remain consistent across all three pages.
- Show both segment volume and conversion rate; never promote a high rate without its base size.
- Use native visuals and avoid large narrative paragraphs on the report canvas.
- Portfolio screenshots must exclude Power BI Desktop chrome.

## Required pages

### Page 01 — Bank Marketing

Purpose: establish campaign scale, conversion, channel, timing, and current context.

Required KPIs:

- Contacts
- Conversions
- Conversion Rate
- Average Contact Duration
- Average Campaign Contacts

Required analysis:

- contact and conversion context by campaign month;
- channel/outcome mix;
- audience or campaign ranking with both count and rate;
- time/context comparison;
- campaign detail table.

### Page 02 — Audience Segmentation

Purpose: locate audience groups associated with higher/lower subscription conversion while protecting base-size context.

Required analysis:

- job, age band, education, marital status, and relevant loan/default views;
- contacts and conversion rate shown together;
- audience ranking and detail table;
- prior-contact context where relevant;
- explicit `unknown` categories or disclosure.

### Page 03 — Campaign Effectiveness

Purpose: compare contact channel, month/day-of-week context, campaign frequency, and prior outcome.

Required KPIs/analysis:

- Conversion Rate, Conversions per 1K Contacts, Prior Contact Rate, Cellular Contact Share, Successful Prior Outcome Rate;
- campaign-frequency bands;
- prior-outcome comparison;
- channel and timing comparison;
- duration analysis with leakage warning;
- detail view with contact volume and rate.

## Semantic-model requirements

- Current implementation uses a single imported analytical table: `FactMarketing`.
- Current canonical measure count: **34**.
- Preserve data types, categories, derived bands, display folders, format strings, and measure names.
- The technical campaign date uses month context because the source does not provide a normal full calendar date/year. Do not imply day-level chronology.
- Regenerate exported documentation after TMDL changes:

```powershell
./scripts/export-model-documentation.ps1
```

## Required DAX families

Use exact definitions from `model/measures.dax`:

- Contacts, Conversions, Conversion Rate;
- Average Contact Duration and Average Campaign Contacts;
- Prior Contact Rate, Cellular Contact Share, Successful Prior Outcome Rate;
- Conversions per 1K Contacts;
- previous-month, MoM, and conversion-rate percentage-point movement;
- KPI display helpers.

Numeric base measures must drive charts, sorting, conditional formatting, and reconciliation. Formatted text measures are display-only.

## Power Query requirements

- Update the local `SourcePath` to `data/bank-additional-full.csv`.
- Confirm semicolon delimiter and column types.
- Preserve `unknown` values.
- Create the documented derived fields such as `Converted`, age/duration/contact-frequency bands, prior-contact flag, and campaign-date/month fields exactly as shown in `powerbi/PowerQuery_M.txt` unless an approved change is requested.
- Record row-count effects of every filter or transformation.

## Interaction requirements

- Page navigator reaches all three pages.
- Reset restores the documented default.
- Slicers filter numerator and denominator in the same context.
- Cross-highlighting must retain sample-size visibility.
- Sorting uses numeric measures.
- Small segments must not be presented as “best” without contact count.

## QA and acceptance

1. Run structural validation and confirm `qa/structural_validation.json` passes.
2. Refresh 41,188 source contacts unless a documented filter changes the count.
3. Reconcile Contacts, Conversions, Conversion Rate, prior-contact rate, and channel share.
4. Confirm all 34 measures load without errors.
5. Verify all three pages, navigation, reset, filters, cross-highlighting, and detail tables.
6. Inspect labels and small-base context at 100% and Fit to page.
7. Save PBIP and PBIX, close Desktop, reopen PBIX, and repeat a smoke test.
8. Record causal/leakage limitations and any unperformed checks.

## Final deliverables

- Updated PBIP and `Portuguese_Bank_Marketing_Performance_Dashboard.pbix`.
- Current DAX, catalog, dictionary, relationship/model notes, and Power Query.
- Structural validation JSON and QA record.
- Sharp report-canvas screenshots if visuals change.

## Copy-ready instruction

> Work on `projects/marketing-performance`. Follow both `AGENTS.md` files and read `BI_Dashboard_Creation_Prompt.md`, `agent/`, `model/`, `powerbi/`, and `qa/`. Use only the included UCI Bank Marketing data and current PBIP/TMDL. Preserve the three-page 1280×720 Marketing decision journey, exact DAX/M logic unless intentionally revised, base-size context, `unknown` categories, leakage and causal limitations. Run structural and Desktop QA, save/reopen the PBIX, and disclose tests not performed.
