from pathlib import Path
import json, re

ROOT = Path(__file__).resolve().parents[1]

PROJECTS = {
    "sales-performance": dict(title="UK Online Retail — Sales Performance", question="Where is growth coming from, which customers and products matter, and how do returns affect sales quality?", pbix="UK_Online_Retail_Sales_Performance_Dashboard.pbix", pbip="UK_Online_Retail_Sales.pbip", source="UCI Online Retail workbook", grain="transaction line", pages=[("UK Retail Sales","scale, trend, and sales quality"),("Customer Insights","customer value and concentration"),("Product & Returns","product contribution and return leakage")]),
    "marketing-performance": dict(title="Portuguese Bank — Marketing Performance", question="Which audiences and campaign conditions are associated with stronger subscription conversion?", pbix="Portuguese_Bank_Marketing_Performance_Dashboard.pbix", pbip="Portuguese_Bank_Marketing.pbip", source="UCI Bank Marketing CSV", grain="campaign contact", pages=[("Bank Marketing","volume, conversion, and channel direction"),("Audience Segmentation","audience mix and response"),("Campaign Effectiveness","campaign conditions and conversion drivers")]),
    "finance-performance": dict(title="Apple Inc. — Financial Performance", question="Are growth, margins, liquidity, and cost structure moving sustainably?", pbix="Apple_Inc_Financial_Performance_Dashboard.pbix", pbip="Apple_Finance.pbip", source="Apple SEC filing data", grain="reported financial metric by period", pages=[("Overview","headline scale and direction"),("Profitability & Growth","growth and margin structure"),("Balance & Liquidity","assets, liabilities, cash, and resilience")]),
    "credit-risk-performance": dict(title="FinTech Credit Risk — Portfolio Performance", question="Where is credit risk concentrated, how should pricing respond, and which borrower segments require action?", pbix="FinTech_Credit_Risk_Dashboard.pbix", pbip="FinTech_Credit_Risk.pbip", source="Lending Club public loan data", grain="loan application", pages=[("Overview","portfolio scale, grade mix, and loss direction"),("Borrower Risk","borrower attributes and risk concentration"),("Pricing & Returns","rate, return, and recovery trade-offs"),("Risk Drivers & Actions","model drivers and operational action rules")]),
}

def tmdl_files(folder):
    return sorted((folder / "dashboard").rglob("*.tmdl"))

def extract_measures(folder):
    out=[]
    for path in tmdl_files(folder):
        text=path.read_text(encoding="utf-8",errors="ignore")
        for match in re.finditer(r"^\s*measure\s+(.+?)\s*=\s*(.+?)(?=^\s*(?:measure|column|partition|hierarchy|annotation)\s|\Z)",text,re.M|re.S):
            name=match.group(1).strip().strip("'")
            expr=match.group(2).strip()
            out.append((name,expr,path.name))
    return out

def model_inventory(folder):
    tables=[]
    for path in tmdl_files(folder):
        text=path.read_text(encoding="utf-8",errors="ignore")
        m=re.search(r"^table\s+(.+)$",text,re.M)
        if m: tables.append(m.group(1).strip().strip("'"))
    return sorted(set(tables))

for slug,cfg in PROJECTS.items():
    folder=ROOT/"projects"/slug
    measures=extract_measures(folder)
    tables=model_inventory(folder)
    for sub in ["model","powerbi","qa","docs"]: (folder/sub).mkdir(parents=True,exist_ok=True)
    dax=[f"-- Extracted from the current canonical KhoiPort PBIP on 2026-08-27.\n-- {cfg['title']}\n"]
    catalog=["measure,source_file"]
    for name,expr,src in measures:
        dax.append(f"\n{name} =\n{expr}\n")
        catalog.append(f'"{name.replace(chr(34),chr(34)*2)}","{src}"')
    (folder/"model/measures.dax").write_text("".join(dax),encoding="utf-8")
    (folder/"model/measure_catalog.csv").write_text("\n".join(catalog)+"\n",encoding="utf-8")
    page_lines="\n".join(f"- **{name}:** {lens}." for name,lens in cfg["pages"])
    table_lines="\n".join(f"- `{t}`" for t in tables)
    (folder/"model/model_inventory.md").write_text(f"# Model inventory\n\nGenerated from the current PBIP.\n\n## Tables\n\n{table_lines}\n\n## Measures\n\n{len(measures)} measures are exported verbatim in [`measures.dax`](./measures.dax).\n",encoding="utf-8")
    prompt=f"""# BI Dashboard Creation Prompt

## Objective

Rebuild or extend **{cfg['title']}** as a polished, decision-focused Power BI product. The management question is: **{cfg['question']}**

Use the published PBIP as the source of truth. Do not invent measures, relationships, outcomes, or source facts. Preserve the current semantic model unless a requested change requires a documented migration.

## Source and grain

- Source: {cfg['source']}.
- Grain: {cfg['grain']}.
- Current model tables: {', '.join(tables)}.
- Current authored measures: {len(measures)}; use [`model/measures.dax`](./model/measures.dax) as the exact DAX reference.

## Required report experience

{page_lines}

Keep a consistent 16:9 canvas, visible page navigation, clear slicer state, KPI cards, decision-oriented chart titles, and a reset-filter control. Prefer a few readable visuals over dense decoration.

## Build contract

1. Open `dashboard/{cfg['pbip']}` with the complete report and semantic-model folders present.
2. Repoint the source only when the local path differs; do not change transformation logic silently.
3. Verify relationships and date behavior before editing visuals.
4. Reconcile the headline KPIs to the underlying table or source.
5. Confirm every page, navigation button, slicer, tooltip, sort order, and interaction.
6. Save a PBIX named `{cfg['pbix']}` and regenerate the PDF preview after QA.

## Acceptance criteria

- The PBIP opens without missing report/model references.
- Every page listed above is present and usable at 16:9.
- DAX definitions reconcile with `model/measures.dax`.
- Source, assumptions, refresh dependencies, and limitations remain visible in the README.
- No proprietary or confidential data is introduced.
"""
    (folder/"BI_Dashboard_Creation_Prompt.md").write_text(prompt,encoding="utf-8")
    build=f"""# PBIX Build Instructions

## Target

- PBIP entry point: `dashboard/{cfg['pbip']}`
- Packaged output: `{cfg['pbix']}`
- Canonical source: `C:\\PowerBI Dashboard - KhoiPort`

## Build

1. Download the complete project folder; a `.pbip` file is only an entry point.
2. Open `dashboard/{cfg['pbip']}` in Power BI Desktop.
3. If refresh fails, update the source path to the included/public source documented in the README.
4. Refresh and resolve errors before changing visuals.
5. Validate the page set: {', '.join(n for n,_ in cfg['pages'])}.
6. Compare the semantic model with `model/model_inventory.md` and exact measures with `model/measures.dax`.
7. Run the QA checklist, save the PBIP, then export `{cfg['pbix']}`.
8. Regenerate the dashboard PDF in `preview/`; portfolio images are rendered from this PDF, not from slide artwork.

## Guardrails

- Do not edit files inside `.pbi/`; they are local caches/settings.
- Do not publish secrets, credentials, private data, or local absolute paths.
- Do not rename tables or measures without updating visuals, documentation, and QA.
"""
    (folder/"powerbi/PBIX_build_instructions.md").write_text(build,encoding="utf-8")
    qa=f"""# QA Checklist

- [ ] PBIP entry point opens with no missing report or semantic model.
- [ ] Expected pages are present: {', '.join(n for n,_ in cfg['pages'])}.
- [ ] All navigation buttons, slicers, reset controls, and interactions work.
- [ ] KPI cards reconcile to source/model totals.
- [ ] Date filters and previous-period calculations behave correctly.
- [ ] No visual is clipped at 1280 × 720 / 16:9.
- [ ] Labels remain legible at portfolio display size.
- [ ] `{cfg['pbix']}` is the latest reviewed build.
- [ ] PDF preview is regenerated from dashboard pages.
- [ ] README, DAX export, and measure catalog match the current PBIP.
"""
    (folder/"qa/qa_checklist.md").write_text(qa,encoding="utf-8")
    readme=f"""# {cfg['title']}

## Review in 60 seconds

| Item | Current evidence |
|---|---|
| Management question | {cfg['question']} |
| What I built | A {len(cfg['pages'])}-page Power BI dashboard, source-controlled PBIP, packaged PBIX, and PDF dashboard preview. |
| Source | {cfg['source']} at {cfg['grain']} grain. |
| Model | {len(tables)} tables and {len(measures)} authored measures in the current canonical PBIP. |
| Status | Synchronized from KhoiPort and repackaged on 27 August 2026. |

## Dashboard pages

{page_lines}

## Main artifacts

| Artifact | Purpose |
|---|---|
| [`{cfg['pbix']}`](./{cfg['pbix']}) | Review-ready packaged dashboard. |
| [`dashboard/{cfg['pbip']}`](./dashboard/{cfg['pbip']}) | Source-controlled PBIP entry point. |
| [`preview/`](./preview/) | Dashboard-only PDF and readable page images used by the portfolio. |
| [`BI_Dashboard_Creation_Prompt.md`](./BI_Dashboard_Creation_Prompt.md) | Full agent brief for rebuilding or extending the product. |
| [`model/measures.dax`](./model/measures.dax) | Exact DAX extracted from the current PBIP. |
| [`powerbi/PBIX_build_instructions.md`](./powerbi/PBIX_build_instructions.md) | Rebuild and packaging procedure. |

## Model and evidence

- Tables: {', '.join('`'+t+'`' for t in tables)}.
- Exact measure catalog: [`model/measure_catalog.csv`](./model/measure_catalog.csv).
- Source and transformation documentation: [`source-documentation/`](./source-documentation/).
- Build utilities and theme: [`build-scripts/`](./build-scripts/) and [`theme/`](./theme/).

## Reviewer path

1. Open the PDF in `preview/` for a fast dashboard-page scan.
2. Download the PBIX for interaction.
3. Inspect the PBIP, DAX, model inventory, and source notes for reproducibility.
4. Use the creation prompt and QA checklist when rebuilding or extending the case.

## Limits

This is a portfolio case study, not a production system or an investment/credit recommendation. Public or portfolio-safe data is used; source limitations remain applicable.
"""
    (folder/"README.md").write_text(readme,encoding="utf-8")
    (folder/"AGENTS.md").write_text(f"# Agent instructions — {cfg['title']}\n\nRead `BI_Dashboard_Creation_Prompt.md`, `powerbi/PBIX_build_instructions.md`, `model/model_inventory.md`, `model/measures.dax`, and `qa/qa_checklist.md` before changing the project. Treat the PBIP and canonical KhoiPort copy as source of truth. Never invent data or KPI results.\n",encoding="utf-8")
    print(slug,len(tables),len(measures))
