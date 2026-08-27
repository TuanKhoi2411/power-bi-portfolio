from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(r"C:\Users\ADMIN\Downloads\CP2 - New\FinTech_Credit_Risk_PBIP")
PAGES = ROOT / "FinTech_Credit_Risk.Report" / "definition" / "pages"


def load(page: str, visual: str):
    path = PAGES / page / "visuals" / visual / "visual.json"
    return path, json.loads(path.read_text(encoding="utf-8"))


def save(path: Path, obj):
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def column(entity: str, prop: str, display: str | None = None, active: bool = False):
    out = {
        "field": {"Column": {"Expression": {"SourceRef": {"Entity": entity}}, "Property": prop}},
        "queryRef": f"{entity}.{prop}",
        "nativeQueryRef": display or prop,
        "displayName": display or prop,
    }
    if active:
        out["active"] = True
    return out


def measure(prop: str, display: str | None = None):
    return {
        "field": {"Measure": {"Expression": {"SourceRef": {"Entity": "Measure"}}, "Property": prop}},
        "queryRef": f"Measure.{prop}",
        "nativeQueryRef": display or prop,
        "displayName": display or prop,
    }


def set_title(obj, title: str):
    title_obj = obj["visual"].setdefault("visualContainerObjects", {}).setdefault("title", [{}])[0]
    props = title_obj.setdefault("properties", {})
    props["show"] = {"expr": {"Literal": {"Value": "true"}}}
    props["text"] = {"expr": {"Literal": {"Value": f"'{title}'"}}}


def set_header(page: str, visual: str, text: str):
    path, obj = load(page, visual)
    runs = obj["visual"]["objects"]["general"][0]["properties"]["paragraphs"][0]["textRuns"]
    runs[0]["value"] = text
    save(path, obj)


def set_card(page: str, visual: str, prop: str, label: str):
    path, obj = load(page, visual)
    obj["visual"]["query"] = {"queryState": {"Data": {"projections": [measure(prop, label)]}}}
    obj["visual"]["objects"]["label"][0]["properties"]["text"]["expr"]["Literal"]["Value"] = f"'{label}'"
    save(path, obj)


def set_delta(page: str, visual: str, prop: str, display: str = "vs PM"):
    path, obj = load(page, visual)
    obj["visual"]["query"] = {"queryState": {"Data": {"projections": [measure(prop, display)]}}}
    save(path, obj)


def set_spark(page: str, visual: str, prop: str, category_entity="DimDate", category_prop="MonthStart", category_display="Month"):
    path, obj = load(page, visual)
    obj["visual"]["query"] = {
        "queryState": {
            "Category": {"projections": [column(category_entity, category_prop, category_display, True)]},
            "Y": {"projections": [measure(prop)]},
        }
    }
    save(path, obj)


def set_bar(page: str, visual: str, entity: str, prop: str, value: str, title: str, category_label=None, value_label=None):
    path, obj = load(page, visual)
    obj["visual"]["query"] = {
        "queryState": {
            "Category": {"projections": [column(entity, prop, category_label or prop, True)]},
            "Y": {"projections": [measure(value, value_label or value)]},
        },
        "sortDefinition": {
            "sort": [
                {
                    "field": {"Measure": {"Expression": {"SourceRef": {"Entity": "Measure"}}, "Property": value}},
                    "direction": "Descending",
                }
            ]
        },
    }
    obj.pop("filterConfig", None)
    set_title(obj, title)
    save(path, obj)


def set_donut(page: str, visual: str, entity: str, prop: str, value: str, title: str):
    path, obj = load(page, visual)
    obj["visual"]["query"] = {
        "queryState": {
            "Category": {"projections": [column(entity, prop, prop, True)]},
            "Y": {"projections": [measure(value)]},
        }
    }
    obj.pop("filterConfig", None)
    set_title(obj, title)
    save(path, obj)


def set_line(page: str, visual: str, entity: str, prop: str, values: list[str], title: str, category_label=None):
    path, obj = load(page, visual)
    obj["visual"]["query"] = {
        "queryState": {
            "Category": {"projections": [column(entity, prop, category_label or prop, True)]},
            "Y": {"projections": [measure(v) for v in values]},
        }
    }
    obj.pop("filterConfig", None)
    set_title(obj, title)
    save(path, obj)


def set_table(page: str, visual: str, fields: list[tuple[str, str, str]], title: str):
    path, obj = load(page, visual)
    projections = []
    for kind, first, second in fields:
        projections.append(column(first, second) if kind == "column" else measure(first, second))
    obj["visual"]["query"] = {"queryState": {"Values": {"projections": projections}}}
    obj.pop("filterConfig", None)
    set_title(obj, title)
    save(path, obj)


def update_overview():
    page = "SalesPage"
    set_header(page, "SalesPage_Header", "FINTECH CREDIT RISK | PORTFOLIO QUALITY & SEASONING")
    cards = [
        ("SalesPage_KPI1", "KPI Seasoned Applications Display", "Seasoned Loans"),
        ("SalesPage_KPI2", "KPI Seasoned Bad Rate Display", "Seasoned Bad Rate"),
        ("SalesPage_KPI3", "KPI Seasoned Good Rate Display", "Seasoned Good Rate"),
        ("SalesPage_KPI4", "KPI Seasoned Recovery Display", "Seasoned Recovery"),
        ("SalesPage_KPI5", "KPI Bad Loan Rate Display", "Overall Bad Rate"),
    ]
    deltas = [
        ("SalesPage_Delta1", "Seasoned Loan Applications MoM"),
        ("SalesPage_Delta2", "Seasoned Bad Loan Rate Variance pp"),
        ("SalesPage_Delta3", "Seasoned Good Loan Rate Variance pp"),
        ("SalesPage_Delta4", "Seasoned Recovery Rate Variance pp"),
        ("SalesPage_Delta5", "Seasoning Bad Rate Gap"),
    ]
    sparks = [
        ("SalesPage_Spark1", "Seasoned Loan Applications"),
        ("SalesPage_Spark2", "Seasoned Bad Loan Rate"),
        ("SalesPage_Spark3", "Seasoned Good Loan Rate"),
        ("SalesPage_Spark4", "Seasoned Recovery Rate"),
        ("SalesPage_Spark5", "Bad Loan Rate"),
    ]
    for visual, prop, label in cards:
        set_card(page, visual, prop, label)
    for visual, prop in deltas:
        set_delta(page, visual, prop)
    for visual, prop in sparks:
        set_spark(page, visual, prop)
    set_bar(page, "SalesPage_Chart1", "FactLoans", "Grade", "Seasoned Bad Loan Rate", "Seasoned Bad Rate by Grade", value_label="Bad Rate")
    set_bar(page, "SalesPage_Chart2", "FactLoans", "Purpose", "Seasoned Bad Loan Rate", "Top Purposes by Seasoned Bad Rate", value_label="Bad Rate")
    set_donut(page, "SalesPage_Chart3", "FactLoans", "LoanLabel", "Seasoned Loan Applications", "Seasoned Loan Quality Mix")
    set_line(page, "SalesPage_Chart4", "DimDate", "Year", ["Seasoned Bad Loan Rate", "Bad Loan Rate"], "Bad Loan Rate Trend | 2007–2014", "Year")
    set_table(
        page,
        "SalesPage_Chart5",
        [
            ("column", "FactLoans", "State"),
            ("measure", "Seasoned Loan Applications", "Seasoned Loans"),
            ("measure", "Seasoned Bad Loan Rate", "Seasoned Bad Rate"),
            ("measure", "Bad Loan Rate", "Overall Bad Rate"),
            ("measure", "Seasoned Recovery Rate", "Recovery Rate"),
        ],
        "State Portfolio Quality Detail",
    )


def update_borrower():
    page = "CustomerInsightsPage"
    set_header(page, "Header", "FINTECH CREDIT RISK | BORROWER BEHAVIOR & QUALITY")
    set_bar(page, "Chart1", "FactLoans", "IncomeBand", "Seasoned Bad Loan Count", "Seasoned Bad Loans by Income Band", value_label="Bad Loans")
    set_bar(page, "Chart2", "FactLoans", "State", "Seasoned Bad Loan Rate", "Seasoned Bad Rate by State", value_label="Bad Rate")
    set_donut(page, "Chart3", "FactLoans", "IncomeVerification", "Seasoned Loan Applications", "Seasoned Loans by Verification Status")
    set_line(page, "Chart4", "DimDate", "MonthStart", ["Seasoned Bad Loan Rate", "Seasoned Recovery Rate"], "Monthly Borrower Quality Trend", "Month")
    set_table(
        page,
        "Chart5",
        [
            ("column", "FactLoans", "IncomeBand"),
            ("column", "FactLoans", "IncomeVerification"),
            ("measure", "Seasoned Loan Applications", "Seasoned Loans"),
            ("measure", "Average Loan Amount", "Avg Loan"),
            ("measure", "Average Interest Rate", "Avg Interest"),
            ("measure", "Average DTI", "Avg DTI"),
            ("measure", "Seasoned Bad Loan Rate", "Bad Rate"),
        ],
        "Borrower Quality Detail",
    )


def update_drivers():
    page = "ProductReturnsPage"
    page_path = PAGES / page / "page.json"
    page_obj = json.loads(page_path.read_text(encoding="utf-8"))
    page_obj["displayName"] = "Risk Drivers & Actions"
    save(page_path, page_obj)
    set_header(page, "Header", "FINTECH CREDIT RISK | MODEL DRIVERS & ACTION RULES")
    cards = [
        ("KPI1", "KPI Model AUC Display", "Model AUC"),
        ("KPI2", "KPI High Risk Rule Rate Display", "High-Risk Bad Rate"),
        ("KPI3", "KPI High Risk Lift Display", "High-Risk Lift"),
        ("KPI4", "KPI 60M Bad Rate Display", "60M Bad Rate"),
        ("KPI5", "KPI Low Recovery Exposure Display", "Low Recovery Exposure"),
    ]
    deltas = [
        ("Delta1", "Model AUC"),
        ("Delta2", "High Risk Rule Lift"),
        ("Delta3", "High Risk Rule Seasoned Loans"),
        ("Delta4", "Term Risk Gap"),
        ("Delta5", "Low Recovery Exposure MoM"),
    ]
    for visual, prop, label in cards:
        set_card(page, visual, prop, label)
    for visual, prop in deltas:
        set_delta(page, visual, prop, "Evidence")
    set_spark(page, "Spark1", "Driver Importance", "RiskDriverImportance", "Driver", "Driver")
    set_spark(page, "Spark2", "High Risk Rule Seasoned Bad Rate")
    set_spark(page, "Spark3", "Rule Lift", "RiskRuleSummary", "RuleSource", "Rule source")
    set_spark(page, "Spark4", "60M Seasoned Bad Loan Rate")
    set_spark(page, "Spark5", "Low Recovery Exposure")
    set_bar(page, "Chart1", "RiskDriverImportance", "Driver", "Driver Importance", "Feature Importance | Pricing and grade lead", value_label="Importance")
    set_bar(page, "Chart2", "RiskRuleSummary", "Rule", "Rule Bad Rate", "Rule Bad Rate | Review segments above 2× lift", value_label="Bad Rate")
    set_bar(page, "Chart3", "FactLoans", "Grade", "Seasoned Bad Loan Rate", "Grade Action | Tighten approval for weak grades", value_label="Bad Rate")
    set_line(page, "Chart4", "DimDate", "Year", ["36M Seasoned Bad Loan Rate", "60M Seasoned Bad Loan Rate"], "Term Action | Reprice and review 60M loans", "Year")
    set_table(
        page,
        "Chart5",
        [
            ("column", "RiskRuleSummary", "RuleSource"),
            ("column", "RiskRuleSummary", "Rule"),
            ("measure", "Rule Loans", "Loans"),
            ("measure", "Rule Bad Loans", "Bad Loans"),
            ("measure", "Rule Bad Rate", "Bad Rate"),
            ("measure", "Rule Lift", "Lift"),
        ],
        "Strategy Rules | Manual review >2× lift; monitor 1–2×",
    )


def main():
    update_overview()
    update_borrower()
    update_drivers()
    for path in (ROOT / "FinTech_Credit_Risk.Report").rglob("*.json"):
        json.loads(path.read_text(encoding="utf-8"))
    print("Report JSON updated and parsed successfully.")


if __name__ == "__main__":
    main()
