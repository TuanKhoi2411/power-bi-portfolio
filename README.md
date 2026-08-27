<div align="center">

# Power BI Analytics Portfolio

**Five decision-focused dashboard products across Sales, Marketing, Finance, Credit Risk, and FP&A**

[![Portfolio](https://img.shields.io/badge/PORTFOLIO-C7F436?style=for-the-badge)](https://tuankhoi2411.github.io/power-bi/)
[![LinkedIn](https://img.shields.io/badge/LINKEDIN-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/tuan-khoi-nguyen-324139316/)

</div>

This repository packages each dashboard as a reviewable product: the latest PBIX, source-controlled PBIP where available, exact DAX/model evidence, rebuild instructions, QA checklist, and a dashboard-only PDF preview.

## Portfolio index

| Dashboard product | Decision supported | Deliverables |
|---|---|---|
| [UK Online Retail — Sales Performance](./projects/sales-performance/README.md) | Where is growth coming from, which customers/products matter, and how do returns affect quality? | PBIX · PBIP · data · DAX · PDF |
| [Portuguese Bank — Marketing Performance](./projects/marketing-performance/README.md) | Which audiences and campaign conditions are associated with conversion? | PBIX · PBIP · data · DAX · PDF |
| [Apple Inc. — Financial Performance](./projects/finance-performance/README.md) | Are growth, margins, liquidity, and cost structure moving sustainably? | PBIX · PBIP · SEC data · DAX · PDF |
| [FinTech Credit Risk — Portfolio Performance](./projects/credit-risk-performance/README.md) | Where is risk concentrated, how should pricing respond, and which segments require action? | PBIX · PBIP · data · DAX · PDF |
| [Sports & Health Enterprise — Financial Performance](./projects/financial-performance-dashboard/README.md) | How can management move from headline P&L into margin, cost, segment, and break-even drivers? | PBIX · HTML story · PDF |

## Recruiter review path

1. Open a project README for the management question and 60-second summary.
2. Review the dashboard-only PDF in `preview/`—no Power BI Desktop chrome and no slide artwork.
3. Download the PBIX for direct interaction.
4. Inspect the PBIP, exact DAX, source notes, and QA package for reproducibility.

## Agent-ready packages

The four source-controlled PBIP projects include:

```text
projects/<project>/
├── README.md
├── AGENTS.md
├── BI_Dashboard_Creation_Prompt.md
├── *.pbix
├── dashboard/                  # current PBIP report + semantic model
├── data/                       # source/public data where distributable
├── model/                      # exact DAX, measure catalog, model inventory
├── powerbi/                    # PBIX rebuild instructions
├── qa/                         # validation checklist
├── preview/                    # PDF + dashboard page PNGs
├── source-documentation/       # current source and model notes
├── build-scripts/              # project build/documentation utilities
└── theme/                      # Power BI theme assets
```

Start with each project’s `BI_Dashboard_Creation_Prompt.md`. The DAX export and model inventory are generated from the current canonical PBIP, not reconstructed from screenshots.

## Current delivery status

| Project | PBIX | PBIP | Dashboard PDF | Agent package |
|---|---:|---:|---:|---:|
| UK Online Retail | Yes | Yes | 3 pages | Yes |
| Portuguese Bank | Yes | Yes | 3 pages | Yes |
| Apple Inc. | Yes | Yes | 3 pages | Yes |
| FinTech Credit Risk | Yes | Yes | 4 pages | Yes |
| Sports & Health Enterprise | Yes | Not published | 4 pages | Existing-PBIX workflow |

## Quality standard

- Management question before charts.
- Clear page purpose, slicer state, navigation, and reset behavior.
- Exact model/DAX evidence instead of undocumented screenshots.
- Dashboard-only PDF previews derived from current dashboard pages.
- Public or portfolio-safe data, explicit limitations, and no confidential inputs.

## Author

**Nguyen Tuan Khoi** — Finance & Data Analytics · Power BI · Process Automation

[GitHub Profile](https://github.com/TuanKhoi2411) · [Finance Case Studies](https://github.com/TuanKhoi2411/finance-analytics-case-studies) · [Email](mailto:tuankhoi24112003@gmail.com)
