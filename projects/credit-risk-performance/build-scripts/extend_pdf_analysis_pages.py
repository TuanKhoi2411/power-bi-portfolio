from __future__ import annotations

import hashlib
import json
import shutil
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


def literal(value: str):
    return {"expr": {"Literal": {"Value": value}}}


def clone_page(source: str, target: str, display_name: str) -> str:
    src = PAGES / source
    dst = PAGES / target
    if dst.exists():
        raise FileExistsError(f"Target page already exists: {dst}")
    shutil.copytree(src, dst)
    page_path = dst / "page.json"
    page = json.loads(page_path.read_text(encoding="utf-8"))
    page_id = hashlib.sha1(target.encode("utf-8")).hexdigest()[:20]
    page["name"] = page_id
    page["displayName"] = display_name
    save(page_path, page)
    for visual_path in (dst / "visuals").glob("*/visual.json"):
        visual = json.loads(visual_path.read_text(encoding="utf-8"))
        visual["name"] = hashlib.sha1(f"{target}:{visual_path.parent.name}".encode("utf-8")).hexdigest()[:20]
        visual.pop("isHidden", None)
        save(visual_path, visual)
    return page_id


def position(obj, x, y, width, height, z=22000):
    obj["position"] = {
        "x": x,
        "y": y,
        "z": z,
        "height": height,
        "width": width,
        "tabOrder": z,
    }


def axis_objects(legend=True):
    return {
        "legend": [{"properties": {
            "show": literal("true" if legend else "false"),
            "showTitle": literal("false"),
            "position": literal("'Top'"),
            "fontSize": literal("8D"),
        }}],
        "categoryAxis": [{"properties": {
            "gridlineShow": literal("false"),
            "showAxisTitle": literal("false"),
            "fontSize": literal("8D"),
        }}],
        "valueAxis": [{"properties": {
            "gridlineShow": literal("true"),
            "showAxisTitle": literal("false"),
            "fontSize": literal("8D"),
        }}],
    }


def set_area(page: str, visual: str, measure_name: str, title: str, x, y, width, height, color: str):
    path, obj = load(page, visual)
    position(obj, x, y, width, height)
    obj["visual"]["visualType"] = "areaChart"
    obj["visual"]["query"] = {
        "queryState": {
            "Category": {"projections": [base.column("DimDate", "Year", "Year", True)]},
            "Y": {"projections": [base.measure(measure_name)]},
        },
        "sortDefinition": {"sort": [{
            "field": {"Column": {"Expression": {"SourceRef": {"Entity": "DimDate"}}, "Property": "Year"}},
            "direction": "Ascending",
        }]},
    }
    objects = axis_objects(False)
    objects["lineStyles"] = [{"properties": {
        "strokeShow": literal("true"),
        "areaShow": literal("true"),
        "strokeWidth": literal("3D"),
        "lineChartType": literal("'smooth'"),
        "showMarker": literal("true"),
        "markerSize": literal("5D"),
    }}]
    objects["dataPoint"] = [
        {"properties": {"transparency": literal("78D")}},
        {"properties": {"fill": {"solid": {"color": literal(f"'{color}'")}}}, "selector": {"metadata": f"Measure.{measure_name}"}},
    ]
    objects["labels"] = [{"properties": {"show": literal("true"), "fontSize": literal("8D")}}]
    obj["visual"]["objects"] = objects
    obj.pop("filterConfig", None)
    base.set_title(obj, title)
    save(path, obj)


def set_line(page: str, visual: str, measures: list[tuple[str, str]], title: str, x, y, width, height):
    path, obj = load(page, visual)
    position(obj, x, y, width, height)
    obj["visual"]["visualType"] = "lineChart"
    obj["visual"]["query"] = {
        "queryState": {
            "Category": {"projections": [base.column("DimDate", "Year", "Year", True)]},
            "Y": {"projections": [base.measure(name, label) for name, label in measures]},
        },
        "sortDefinition": {"sort": [{
            "field": {"Column": {"Expression": {"SourceRef": {"Entity": "DimDate"}}, "Property": "Year"}},
            "direction": "Ascending",
        }]},
    }
    objects = axis_objects(True)
    objects["lineStyles"] = [{"properties": {
        "strokeShow": literal("true"),
        "areaShow": literal("false"),
        "strokeWidth": literal("3D"),
        "lineChartType": literal("'smooth'"),
        "showMarker": literal("true"),
        "markerSize": literal("5D"),
    }}]
    palette = ["#C94C4C", "#2F7D6E", "#D98324"]
    objects["dataPoint"] = [
        {"properties": {"fill": {"solid": {"color": literal(f"'{palette[i]}'")}}}, "selector": {"metadata": f"Measure.{name}"}}
        for i, (name, _) in enumerate(measures)
    ]
    objects["labels"] = [{"properties": {"show": literal("true"), "fontSize": literal("8D")}}]
    obj["visual"]["objects"] = objects
    obj.pop("filterConfig", None)
    base.set_title(obj, title)
    save(path, obj)


def set_donut(page: str, visual: str, entity: str, prop: str, title: str, x, y, width, height):
    path, obj = load(page, visual)
    position(obj, x, y, width, height)
    obj["visual"]["visualType"] = "donutChart"
    obj["visual"]["query"] = {"queryState": {
        "Category": {"projections": [base.column(entity, prop, prop, True)]},
        "Y": {"projections": [base.measure("Loan Applications", "Applications")]},
    }}
    obj["visual"]["objects"] = {
        "legend": [{"properties": {
            "show": literal("true"),
            "position": literal("'BottomCenter'"),
            "showTitle": literal("false"),
            "fontSize": literal("8D"),
        }}],
        "labels": [{"properties": {
            "show": literal("true"),
            "fontSize": literal("8D"),
            "labelDisplayUnits": literal("1000D"),
        }}],
    }
    obj.pop("filterConfig", None)
    base.set_title(obj, title)
    save(path, obj)


def series_color(value: str, color: str):
    return {
        "properties": {"fill": {"solid": {"color": literal(f"'{color}'")}}},
        "selector": {"data": [{"scopeId": {"Comparison": {
            "ComparisonKind": 0,
            "Left": {"Column": {"Expression": {"SourceRef": {"Entity": "FactLoans"}}, "Property": "LoanLabel"}},
            "Right": {"Literal": {"Value": f"'{value}'"}},
        }}}]},
    }


def set_quality_mix(page: str, visual: str, entity: str, prop: str, title: str, x, y, width, height, sort_by_value=True):
    path, obj = load(page, visual)
    position(obj, x, y, width, height)
    obj["visual"]["visualType"] = "clusteredColumnChart"
    query = {"queryState": {
        "Category": {"projections": [base.column(entity, prop, prop, True)]},
        "Series": {"projections": [base.column("FactLoans", "LoanLabel", "Loan Quality")]},
        "Y": {"projections": [base.measure("Loan Applications", "Applications")]},
    }}
    if sort_by_value:
        query["sortDefinition"] = {"sort": [{
            "field": {"Measure": {"Expression": {"SourceRef": {"Entity": "Measure"}}, "Property": "Loan Applications"}},
            "direction": "Descending",
        }]}
    else:
        query["sortDefinition"] = {"sort": [{
            "field": {"Column": {"Expression": {"SourceRef": {"Entity": entity}}, "Property": prop}},
            "direction": "Ascending",
        }]}
    obj["visual"]["query"] = query
    objects = axis_objects(True)
    objects["legend"][0]["properties"]["position"] = literal("'Top'")
    objects["dataPoint"] = [
        series_color("Good", "#2F7D6E"),
        series_color("Bad", "#C94C4C"),
        series_color("Neutral", "#D98324"),
    ]
    objects["labels"] = [{"properties": {
        "show": literal("true"),
        "fontSize": literal("8D"),
        "labelDisplayUnits": literal("1000D"),
    }}]
    obj["visual"]["objects"] = objects
    obj.pop("filterConfig", None)
    base.set_title(obj, title)
    save(path, obj)


def set_bar(page: str, visual: str, entity: str, prop: str, measure_name: str, title: str, x, y, width, height, color="#C94C4C"):
    path, obj = load(page, visual)
    position(obj, x, y, width, height)
    obj["visual"]["visualType"] = "clusteredBarChart"
    obj["visual"]["query"] = {
        "queryState": {
            "Category": {"projections": [base.column(entity, prop, prop, True)]},
            "Y": {"projections": [base.measure(measure_name)]},
        },
        "sortDefinition": {"sort": [{
            "field": {"Measure": {"Expression": {"SourceRef": {"Entity": "Measure"}}, "Property": measure_name}},
            "direction": "Descending",
        }]},
    }
    objects = axis_objects(False)
    objects["dataPoint"] = [{"properties": {"fill": {"solid": {"color": literal(f"'{color}'")}}}}]
    objects["labels"] = [{"properties": {"show": literal("true"), "fontSize": literal("8D")}}]
    obj["visual"]["objects"] = objects
    obj.pop("filterConfig", None)
    base.set_title(obj, title)
    save(path, obj)


def update_kpis(page: str, cards, deltas, sparks):
    for visual, measure_name, label in cards:
        base.set_card(page, visual, measure_name, label)
    for visual, measure_name in deltas:
        base.set_delta(page, visual, measure_name)
    for visual, measure_name in sparks:
        base.set_spark(page, visual, measure_name)


def build_pricing_page():
    page = "PricingVerificationPage"
    page_id = clone_page("SalesPage", page, "Pricing & Returns")
    base.set_header(page, "SalesPage_Header", "FINTECH CREDIT RISK | PRICING, VERIFICATION & RETURNS")
    update_kpis(
        page,
        [
            ("SalesPage_KPI1", "KPI Avg Loan Display", "Avg Loan"),
            ("SalesPage_KPI2", "KPI Avg Interest Display", "Interest"),
            ("SalesPage_KPI3", "KPI Income Verification Display", "Verified"),
            ("SalesPage_KPI4", "KPI Raw Default Rate Display", "Default"),
            ("SalesPage_KPI5", "KPI Portfolio ROI Display", "ROI"),
        ],
        [
            ("SalesPage_Delta1", "Avg Loan MoM"),
            ("SalesPage_Delta2", "Avg Interest MoM"),
            ("SalesPage_Delta3", "Income Verification Variance pp"),
            ("SalesPage_Delta4", "Raw Default Rate MoM"),
            ("SalesPage_Delta5", "Portfolio ROI MoM"),
        ],
        [
            ("SalesPage_Spark1", "Average Loan Amount"),
            ("SalesPage_Spark2", "Average Interest Rate"),
            ("SalesPage_Spark3", "Income Verification Rate"),
            ("SalesPage_Spark4", "Raw Default Rate"),
            ("SalesPage_Spark5", "Portfolio ROI"),
        ],
    )
    set_area(page, "SalesPage_Chart1", "Average Loan Amount", "Average Loan Amount | 2007–2014", 189.5, 235, 520, 205, "#355C7D")
    set_area(page, "SalesPage_Chart2", "Average Interest Rate", "Average Interest Rate | 2007–2014", 725, 235, 530, 205, "#D98324")
    set_donut(page, "SalesPage_Chart3", "FactLoans", "IncomeVerification", "Applications by Verification Status", 189.5, 455, 300, 235)
    set_donut(page, "SalesPage_Chart4", "FactLoans", "LoanStatus", "Applications by Loan Status", 505, 455, 300, 235)
    set_line(page, "SalesPage_Chart5", [("Raw Default Rate", "Default Rate"), ("Portfolio ROI", "Portfolio ROI")], "Default Rate vs Portfolio ROI | 2007–2014", 820, 455, 435, 235)
    return page_id


def build_mix_page():
    page = "PortfolioMixPage"
    page_id = clone_page("SalesPage", page, "Portfolio Mix")
    base.set_header(page, "SalesPage_Header", "FINTECH CREDIT RISK | PORTFOLIO COMPOSITION & LOSS MIX")
    update_kpis(
        page,
        [
            ("SalesPage_KPI1", "KPI Loan Applications Display", "Loans"),
            ("SalesPage_KPI2", "KPI Bad Loan Rate Display", "Bad Rate"),
            ("SalesPage_KPI3", "KPI Good Loan Rate Display", "Good Rate"),
            ("SalesPage_KPI4", "KPI Avg Loan Display", "Avg Loan Amount"),
            ("SalesPage_KPI5", "KPI Income Verification Display", "Verified"),
        ],
        [
            ("SalesPage_Delta1", "Loan Applications MoM"),
            ("SalesPage_Delta2", "Bad Loan Rate Variance pp"),
            ("SalesPage_Delta3", "Good Loan Rate Variance pp"),
            ("SalesPage_Delta4", "Avg Loan MoM"),
            ("SalesPage_Delta5", "Income Verification Variance pp"),
        ],
        [
            ("SalesPage_Spark1", "Loan Applications"),
            ("SalesPage_Spark2", "Bad Loan Rate"),
            ("SalesPage_Spark3", "Good Loan Rate"),
            ("SalesPage_Spark4", "Average Loan Amount"),
            ("SalesPage_Spark5", "Income Verification Rate"),
        ],
    )
    set_quality_mix(page, "SalesPage_Chart1", "DimGrade", "Grade", "Loan Quality Mix by Grade", 189.5, 235, 520, 205, False)
    set_quality_mix(page, "SalesPage_Chart2", "DimPurpose", "PurposeGroup", "Loan Quality Mix by Purpose Group", 725, 235, 530, 205, True)
    set_quality_mix(page, "SalesPage_Chart3", "DimHomeOwnership", "HomeOwnershipGroup", "Loan Quality Mix by Home Ownership", 189.5, 455, 520, 235, True)
    set_bar(page, "SalesPage_Chart4", "DimHomeOwnership", "HomeOwnershipGroup", "Bad Loan Count", "Bad Loans by Home Ownership", 725, 455, 260, 235)
    set_bar(page, "SalesPage_Chart5", "DimGrade", "Grade", "Bad Loan Count", "Bad Loans by Grade", 1000, 455, 255, 235)
    return page_id


def update_page_order(new_ids: list[str]):
    path = PAGES / "pages.json"
    meta = json.loads(path.read_text(encoding="utf-8"))
    for page_id in new_ids:
        if page_id not in meta["pageOrder"]:
            meta["pageOrder"].append(page_id)
    meta["activePageName"] = new_ids[0]
    save(path, meta)


def main():
    pricing_id = build_pricing_page()
    mix_id = build_mix_page()
    update_page_order([pricing_id, mix_id])
    for path in (ROOT / "FinTech_Credit_Risk.Report").rglob("*.json"):
        json.loads(path.read_text(encoding="utf-8"))
    print(f"Created Pricing & Returns ({pricing_id}) and Portfolio Mix ({mix_id}).")


if __name__ == "__main__":
    main()
