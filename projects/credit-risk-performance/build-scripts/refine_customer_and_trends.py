from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(r"C:\Users\ADMIN\Downloads\CP2 - New\FinTech_Credit_Risk_PBIP")
PAGES = ROOT / "FinTech_Credit_Risk.Report" / "definition" / "pages"
sys.path.insert(0, str(ROOT))
import align_report_to_lark as base  # noqa: E402


def load(page: str, visual: str):
    path = PAGES / page / "visuals" / visual / "visual.json"
    return path, json.loads(path.read_text(encoding="utf-8"))


def save(path: Path, obj):
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def common_axis_objects():
    return {
        "legend": [{"properties": {"showTitle": {"expr": {"Literal": {"Value": "false"}}}, "fontSize": {"expr": {"Literal": {"Value": "8D"}}}}}],
        "categoryAxis": [{"properties": {"gridlineShow": {"expr": {"Literal": {"Value": "false"}}}, "showAxisTitle": {"expr": {"Literal": {"Value": "false"}}}, "fontSize": {"expr": {"Literal": {"Value": "8D"}}}}}],
        "valueAxis": [{"properties": {"gridlineShow": {"expr": {"Literal": {"Value": "true"}}}, "showAxisTitle": {"expr": {"Literal": {"Value": "false"}}}, "fontSize": {"expr": {"Literal": {"Value": "8D"}}}}}],
    }


def set_combo(page: str, visual: str, column_measure: str, line_measure: str, title: str):
    path, obj = load(page, visual)
    obj["visual"]["visualType"] = "lineClusteredColumnComboChart"
    obj["visual"]["query"] = {
        "queryState": {
            "Category": {"projections": [base.column("DimDate", "Year", "Year", True)]},
            "Y": {"projections": [base.measure(column_measure, "Applications")]},
            "Y2": {"projections": [base.measure(line_measure, "Bad Rate")]},
        }
    }
    objects = common_axis_objects()
    objects["lineStyles"] = [{"properties": {"strokeShow": {"expr": {"Literal": {"Value": "true"}}}, "areaShow": {"expr": {"Literal": {"Value": "false"}}}, "strokeWidth": {"expr": {"Literal": {"Value": "2D"}}}, "showMarker": {"expr": {"Literal": {"Value": "true"}}}, "markerSize": {"expr": {"Literal": {"Value": "4D"}}}}}]
    objects["dataPoint"] = [
        {"properties": {"fill": {"solid": {"color": {"expr": {"Literal": {"Value": "'#5B6C8F'"}}}}}}},
        {"properties": {"fill": {"solid": {"color": {"expr": {"Literal": {"Value": "'#C94C4C'"}}}}}}, "selector": {"metadata": f"Measure.{line_measure}"}},
    ]
    obj["visual"]["objects"] = objects
    obj.pop("filterConfig", None)
    base.set_title(obj, title)
    save(path, obj)


def set_term_comparison(page: str, visual: str):
    path, obj = load(page, visual)
    obj["isHidden"] = True
    obj["visual"]["visualType"] = "clusteredBarChart"
    obj["visual"]["query"] = {
        "queryState": {
            "Category": {"projections": [base.column("FactLoans", "TermMonths", "Loan Term (Months)", True)]},
            "Y": {"projections": [base.measure("Seasoned Bad Loan Rate", "Seasoned Bad Rate")]},
        },
        "sortDefinition": {
            "sort": [
                {
                    "field": {"Column": {"Expression": {"SourceRef": {"Entity": "FactLoans"}}, "Property": "TermMonths"}},
                    "direction": "Ascending",
                }
            ]
        },
    }
    objects = common_axis_objects()
    objects["legend"] = [{"properties": {"show": {"expr": {"Literal": {"Value": "false"}}}}}]
    objects["dataPoint"] = [
        {"properties": {"fill": {"solid": {"color": {"expr": {"Literal": {"Value": "'#D98324'"}}}}}}},
        {"properties": {"fill": {"solid": {"color": {"expr": {"Literal": {"Value": "'#C94C4C'"}}}}}}, "selector": {"data": [{"scopeId": {"Comparison": {"ComparisonKind": 0, "Left": {"Column": {"Expression": {"SourceRef": {"Entity": "FactLoans"}}, "Property": "TermMonths"}}, "Right": {"Literal": {"Value": "60L"}}}}}]}},
    ]
    objects["labels"] = [{"properties": {"show": {"expr": {"Literal": {"Value": "true"}}}, "fontSize": {"expr": {"Literal": {"Value": "10D"}}}}}]
    obj["visual"]["objects"] = objects
    obj.pop("filterConfig", None)
    base.set_title(obj, "Seasoned Bad Loan Rate by Term | 36M vs 60M")
    save(path, obj)

    grade_path, grade = load(page, "Chart3")
    grade["position"] = {
        "x": 189.5,
        "y": 235,
        "z": 21000,
        "height": 205,
        "width": 1065.5,
        "tabOrder": 21000,
    }
    save(grade_path, grade)


def set_quality_area(page: str, visual: str):
    path, obj = load(page, visual)
    obj["visual"]["visualType"] = "areaChart"
    obj["visual"]["query"] = {
        "queryState": {
            "Category": {"projections": [base.column("DimDate", "Year", "Year", True)]},
            "Series": {"projections": [base.column("FactLoans", "LoanLabel", "Loan Quality")]},
            "Y": {"projections": [base.measure("Loan Applications", "Applications")]},
        }
    }
    objects = common_axis_objects()
    objects["lineStyles"] = [{"properties": {"strokeShow": {"expr": {"Literal": {"Value": "true"}}}, "areaShow": {"expr": {"Literal": {"Value": "true"}}}, "strokeWidth": {"expr": {"Literal": {"Value": "2D"}}}, "showMarker": {"expr": {"Literal": {"Value": "true"}}}, "markerSize": {"expr": {"Literal": {"Value": "3D"}}}}}]
    objects["dataPoint"] = [
        {"properties": {"fill": {"solid": {"color": {"expr": {"Literal": {"Value": "'#6E9674'"}}}}}}, "selector": {"data": [{"scopeId": {"Comparison": {"ComparisonKind": 0, "Left": {"Column": {"Expression": {"SourceRef": {"Entity": "FactLoans"}}, "Property": "LoanLabel"}}, "Right": {"Literal": {"Value": "'Good'"}}}}}]}},
        {"properties": {"fill": {"solid": {"color": {"expr": {"Literal": {"Value": "'#C94C4C'"}}}}}}, "selector": {"data": [{"scopeId": {"Comparison": {"ComparisonKind": 0, "Left": {"Column": {"Expression": {"SourceRef": {"Entity": "FactLoans"}}, "Property": "LoanLabel"}}, "Right": {"Literal": {"Value": "'Bad'"}}}}}]}},
        {"properties": {"fill": {"solid": {"color": {"expr": {"Literal": {"Value": "'#8A6FA8'"}}}}}}, "selector": {"data": [{"scopeId": {"Comparison": {"ComparisonKind": 0, "Left": {"Column": {"Expression": {"SourceRef": {"Entity": "FactLoans"}}, "Property": "LoanLabel"}}, "Right": {"Literal": {"Value": "'Neutral'"}}}}}]}},
    ]
    obj["visual"]["objects"] = objects
    obj.pop("filterConfig", None)
    base.set_title(obj, "Applications by Loan Quality | 2007–2014")
    save(path, obj)


def set_customer_quality_chart(page: str, visual: str):
    path, obj = load(page, visual)
    obj["position"] = {"x": 189.5, "y": 455, "z": 22000, "height": 235, "width": 520, "tabOrder": 22000}
    obj["visual"]["visualType"] = "clusteredBarChart"
    obj["visual"]["query"] = {
        "queryState": {
            "Category": {"projections": [base.column("FactLoans", "Purpose", "Purpose", True)]},
            "Y": {"projections": [base.measure("Top 8 Purpose Seasoned Bad Rate", "Bad Rate")]},
        },
        "sortDefinition": {
            "sort": [
                {
                    "field": {"Measure": {"Expression": {"SourceRef": {"Entity": "Measure"}}, "Property": "Top 8 Purpose Seasoned Bad Rate"}},
                    "direction": "Descending",
                }
            ]
        },
    }
    objects = common_axis_objects()
    objects["dataPoint"] = [{"properties": {"fill": {"solid": {"color": {"expr": {"Literal": {"Value": "'#C94C4C'"}}}}}}}]
    obj["visual"]["objects"] = objects
    obj.pop("filterConfig", None)
    obj.pop("isHidden", None)
    base.set_title(obj, "Highest-Risk Loan Purposes | Top 8 Seasoned Bad Rate")
    save(path, obj)


def set_customer_risk_chart(page: str, visual: str):
    path, obj = load(page, visual)
    obj["position"] = {"x": 725, "y": 455, "z": 23000, "height": 235, "width": 530, "tabOrder": 23000}
    obj["visual"]["visualType"] = "clusteredBarChart"
    obj["visual"]["query"] = {
        "queryState": {
            "Category": {"projections": [base.column("FactLoans", "IncomeBand", "Income Level", True)]},
            "Y": {"projections": [base.measure("Seasoned Bad Loan Rate", "Bad Rate")]},
        },
        "sortDefinition": {"sort": [{"field": {"Measure": {"Expression": {"SourceRef": {"Entity": "Measure"}}, "Property": "Seasoned Bad Loan Rate"}}, "direction": "Descending"}]},
    }
    obj["visual"]["objects"] = common_axis_objects()
    obj.pop("filterConfig", None)
    obj.pop("isHidden", None)
    base.set_title(obj, "Seasoned Bad Loan Rate by Income Level")
    save(path, obj)


def update_customer_page():
    page = "CustomerInsightsPage"
    base.set_header(page, "Header", "FINTECH CREDIT RISK | CUSTOMER OVERVIEW & LOAN JOURNEY")
    cards = [
        ("KPI1", "KPI Borrowers Display", "Customers"),
        ("KPI2", "KPI Average Delinquencies Display", "Avg Delinquency"),
        ("KPI3", "KPI Public Record Rate Display", "Public Record Rate"),
        ("KPI4", "KPI Avg Interest Display", "Avg Interest Rate"),
        ("KPI5", "KPI Average DTI Display", "Avg DTI Ratio"),
    ]
    deltas = [
        ("Delta1", "Borrowers MoM"),
        ("Delta2", "Average Delinquencies MoM"),
        ("Delta3", "Public Record Rate Variance pp"),
        ("Delta4", "Avg Interest MoM"),
        ("Delta5", "Average DTI MoM"),
    ]
    sparks = [
        ("Spark1", "Borrowers"),
        ("Spark2", "Average Delinquencies"),
        ("Spark3", "Public Record Rate"),
        ("Spark4", "Average Interest Rate"),
        ("Spark5", "Average DTI"),
    ]
    for visual, prop, label in cards:
        base.set_card(page, visual, prop, label)
    for visual, prop in deltas:
        base.set_delta(page, visual, prop)
    for visual, prop in sparks:
        base.set_spark(page, visual, prop)
    base.set_bar(page, "Chart1", "FactLoans", "Purpose", "Loan Applications", "Applications by Purpose", value_label="Applications")
    path, chart2 = load(page, "Chart2")
    chart2["visual"]["visualType"] = "donutChart"
    chart2["visual"]["query"] = {"queryState": {"Category": {"projections": [base.column("FactLoans", "IncomeBand", "Income Level", True)]}, "Y": {"projections": [base.measure("Loan Applications", "Applications")]}}}
    chart2["visual"].pop("sortDefinition", None)
    chart2.pop("filterConfig", None)
    base.set_title(chart2, "Applications by Income Level")
    save(path, chart2)
    base.set_donut(page, "Chart3", "FactLoans", "HomeOwnership", "Loan Applications", "Applications by Home Ownership")
    set_customer_quality_chart(page, "Chart4")
    set_customer_risk_chart(page, "Chart5")


def update_trends_and_strategy():
    set_quality_area("SalesPage", "SalesPage_Chart4")
    set_combo("SalesPage", "SalesPage_Chart5", "Seasoned Loan Applications", "Seasoned Bad Loan Rate", "Applications & Seasoned Bad Rate | 2007–2014")
    set_term_comparison("ProductReturnsPage", "Chart4")
    base.set_bar("ProductReturnsPage", "Chart5", "FactLoans", "Purpose", "Seasoned Bad Loan Count", "Where Seasoned Bad Loans Concentrate | Purpose", value_label="Bad Loans")
    path, chart5 = load("ProductReturnsPage", "Chart5")
    chart5["visual"]["visualType"] = "clusteredBarChart"
    chart5["visual"]["objects"] = common_axis_objects()
    save(path, chart5)


def main():
    update_customer_page()
    update_trends_and_strategy()
    for path in (ROOT / "FinTech_Credit_Risk.Report").rglob("*.json"):
        json.loads(path.read_text(encoding="utf-8"))
    print("Customer page, strategy replacement and trend visuals updated.")


if __name__ == "__main__":
    main()
