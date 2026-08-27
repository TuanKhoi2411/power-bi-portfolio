from __future__ import annotations

import copy
import json
import re
import uuid
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT / "PowerBI_Project"
REPORT = PROJECT / "Apple_Finance_v2.Report"
MODEL = PROJECT / "Apple_Finance_v2.SemanticModel"
PAGES = REPORT / "definition" / "pages"
FACT = MODEL / "definition" / "tables" / "FactFinance.tmdl"
DIM_DATE = MODEL / "definition" / "tables" / "DimDate.tmdl"
MODEL_TMDL = MODEL / "definition" / "model.tmdl"
COMPONENT = MODEL / "definition" / "tables" / "FinanceComponent.tmdl"


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def write_json(path: Path, payload: dict) -> None:
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def literal(value: str) -> dict:
    return {"expr": {"Literal": {"Value": value}}}


def measure_projection(name: str, display: str | None = None) -> dict:
    return {
        "field": {
            "Measure": {
                "Expression": {"SourceRef": {"Entity": "FactFinance"}},
                "Property": name,
            }
        },
        "queryRef": f"FactFinance.{name}",
        "nativeQueryRef": display or name,
        "displayName": display or name,
    }


def column_projection(entity: str, name: str, display: str | None = None) -> dict:
    return {
        "field": {
            "Column": {
                "Expression": {"SourceRef": {"Entity": entity}},
                "Property": name,
            }
        },
        "queryRef": f"{entity}.{name}",
        "nativeQueryRef": display or name,
        "active": True,
        "displayName": display or name,
    }


def filter_item(kind: str, entity: str, name: str, filter_type: str) -> dict:
    return {
        "name": uuid.uuid4().hex[:20],
        "field": {
            kind: {
                "Expression": {"SourceRef": {"Entity": entity}},
                "Property": name,
            }
        },
        "type": filter_type,
    }


def title_text(data: dict) -> str:
    for item in data.get("visual", {}).get("visualContainerObjects", {}).get("title", []):
        raw = item.get("properties", {}).get("text", {}).get("expr", {}).get("Literal", {}).get("Value")
        if raw:
            return raw.strip("'")
    return ""


def set_title(data: dict, text: str) -> None:
    objects = data["visual"].setdefault("visualContainerObjects", {})
    title = objects.setdefault("title", [{"properties": {}}])
    props = title[0].setdefault("properties", {})
    props["show"] = literal("true")
    props["text"] = literal(f"'{text}'")


def set_alt_text(data: dict, text: str) -> None:
    objects = data["visual"].setdefault("visualContainerObjects", {})
    general = objects.setdefault("general", [{"properties": {}}])
    general[0].setdefault("properties", {})["altText"] = literal(f"'{text.replace(chr(39), chr(8217))}'")


def axis_objects(show_legend: bool = False, show_labels: bool = True) -> dict:
    result = {
        "legend": [{"properties": {"show": literal(str(show_legend).lower()), "position": literal("'Top'")}}],
        "categoryAxis": [{"properties": {"showAxisTitle": literal("false"), "fontSize": literal("9D")}}],
        "valueAxis": [{"properties": {"showAxisTitle": literal("false"), "fontSize": literal("9D")}}],
    }
    if show_labels:
        result["labels"] = [{"properties": {"show": literal("true"), "fontSize": literal("9D")}}]
    return result


def component_bar(path: Path, ratio: bool, title: str) -> None:
    data = read_json(path)
    measure = "Latest Revenue Component Ratio" if ratio else "Latest Revenue Component Amount"
    data["visual"]["visualType"] = "clusteredBarChart"
    data["visual"]["query"] = {
        "queryState": {
            "Category": {"projections": [column_projection("FinanceComponent", "Component", "Component")]},
            "Y": {"projections": [measure_projection(measure, "% of Revenue" if ratio else "Amount")]},
        },
        "sortDefinition": {
            "sort": [{"field": measure_projection(measure)["field"], "direction": "Descending"}]
        },
    }
    data["visual"]["objects"] = axis_objects(show_legend=False, show_labels=True)
    data["visual"]["objects"]["dataPoint"] = [{"properties": {"fill": {"solid": {"color": literal("'#0F766E'")}}}}]
    set_title(data, title)
    set_alt_text(data, title + ". Compares the four components that reconcile revenue to net income.")
    data["filterConfig"] = {
        "filters": [
            filter_item("Column", "FinanceComponent", "Component", "Categorical"),
            filter_item("Measure", "FactFinance", measure, "Advanced"),
        ]
    }
    write_json(path, data)


def capital_structure(path: Path) -> None:
    data = read_json(path)
    data["visual"]["visualType"] = "hundredPercentStackedBarChart"
    data["visual"]["query"] = {
        "queryState": {
            "Y": {
                "projections": [
                    measure_projection("Latest Liabilities", "Liabilities"),
                    measure_projection("Latest Net Asset Position", "Net Assets"),
                ]
            }
        }
    }
    data["visual"]["objects"] = axis_objects(show_legend=True, show_labels=True)
    data["visual"]["objects"]["dataPoint"] = [{"properties": {"fill": {"solid": {"color": literal("'#0F766E'")}}}}]
    title = "Capital Structure | Liabilities vs Net Assets (% of Assets)"
    set_title(data, title)
    set_alt_text(data, title + ". Cash remains visible separately in the Cash KPI card.")
    data["filterConfig"] = {
        "filters": [
            filter_item("Measure", "FactFinance", "Latest Liabilities", "Advanced"),
            filter_item("Measure", "FactFinance", "Latest Net Asset Position", "Advanced"),
        ]
    }
    write_json(path, data)


def repurpose_growth_chart(path: Path) -> None:
    data = read_json(path)
    data["visual"]["visualType"] = "lineChart"
    data["visual"]["query"] = {
        "queryState": {
            "Category": {"projections": [column_projection("DimDate", "Date", "Quarter")]},
            "Y": {
                "projections": [
                    measure_projection("Revenue YoY", "Revenue YoY"),
                    measure_projection("Operating Leverage Spread", "Operating Leverage"),
                ]
            },
        }
    }
    data["visual"]["objects"] = axis_objects(show_legend=True, show_labels=False)
    title = "Growth Quality | Revenue YoY vs Operating Leverage"
    set_title(data, title)
    set_alt_text(data, title + ". Positive spread indicates operating income is growing faster than revenue.")
    data["filterConfig"] = {
        "filters": [
            filter_item("Column", "DimDate", "Date", "Categorical"),
            filter_item("Measure", "FactFinance", "Revenue YoY", "Advanced"),
            filter_item("Measure", "FactFinance", "Operating Leverage Spread", "Advanced"),
        ]
    }
    write_json(path, data)


def set_slicer(path: Path, entity: str, prop: str, title: str, group: str) -> None:
    data = read_json(path)
    data["visual"]["query"] = {"queryState": {"Values": {"projections": [column_projection(entity, prop, title)]}}}
    data["visual"]["syncGroup"] = {"groupName": group, "fieldChanges": True, "filterChanges": True}
    set_title(data, title)
    data["filterConfig"] = {"filters": [filter_item("Column", entity, prop, "Categorical")]}
    write_json(path, data)


def trim_table(path: Path, keep: list[str], title: str) -> None:
    data = read_json(path)
    values = data["visual"]["query"]["queryState"]["Values"]["projections"]
    filtered = []
    for item in values:
        field = item.get("field", {})
        node = field.get("Column") or field.get("Measure") or {}
        if node.get("Property") in keep:
            filtered.append(item)
    data["visual"]["query"]["queryState"]["Values"]["projections"] = filtered
    set_title(data, title)
    set_alt_text(data, title + ". Five decision-relevant quarterly columns are shown to avoid horizontal scrolling.")
    write_json(path, data)


def upgrade_all_visuals() -> None:
    chart_types = {
        "areaChart", "lineChart", "clusteredBarChart", "clusteredColumnChart", "stackedBarChart",
        "stackedColumnChart", "hundredPercentStackedBarChart", "hundredPercentStackedColumnChart",
        "waterfallChart", "tableEx", "matrix", "cardVisual",
    }
    for path in PAGES.glob("*/visuals/*/visual.json"):
        data = read_json(path)
        visual = data.get("visual", {})

        def walk(node):
            if isinstance(node, dict):
                for key, value in node.items():
                    if key in {"fontSize", "textSize"}:
                        raw = value.get("expr", {}).get("Literal", {}).get("Value") if isinstance(value, dict) else None
                        if isinstance(raw, str) and raw.endswith("D"):
                            try:
                                if float(raw[:-1]) < 9:
                                    value["expr"]["Literal"]["Value"] = "9D"
                            except ValueError:
                                pass
                    walk(value)
            elif isinstance(node, list):
                for item in node:
                    walk(item)

        walk(data)
        if visual.get("visualType") in chart_types:
            label = title_text(data)
            if not label:
                props = []
                for match in re.finditer(r'"Property"\s*:\s*"([^"]+)"', json.dumps(data)):
                    if match.group(1) not in props:
                        props.append(match.group(1))
                label = "Financial KPI: " + (props[0] if props else "financial metric")
            set_alt_text(data, label)
        write_json(path, data)


def update_model() -> None:
    model_text = MODEL_TMDL.read_text(encoding="utf-8-sig")
    if "ref table FinanceComponent" not in model_text:
        model_text = model_text.replace("ref table DimPeriodType\n", "ref table DimPeriodType\nref table FinanceComponent\n")
        MODEL_TMDL.write_text(model_text, encoding="utf-8")

    dim = DIM_DATE.read_text(encoding="utf-8-sig")
    if "column FiscalYear" not in dim:
        block = f'''\n\tcolumn FiscalYear = YEAR ( EDATE ( DimDate[Date], 3 ) )
\t\tdataType: int64
\t\tformatString: 0
\t\tlineageTag: {uuid.uuid4()}
\t\tsummarizeBy: none

\tcolumn FiscalPeriod = "Q" & FORMAT ( INT ( MOD ( MONTH ( DimDate[Date] ) + 2, 12 ) / 3 ) + 1, "0" )
\t\tdataType: string
\t\tlineageTag: {uuid.uuid4()}
\t\tsummarizeBy: none
\t\tsortByColumn: FiscalPeriodSort

\tcolumn FiscalPeriodSort = INT ( MOD ( MONTH ( DimDate[Date] ) + 2, 12 ) / 3 ) + 1
\t\tdataType: int64
\t\tisHidden
\t\tformatString: 0
\t\tlineageTag: {uuid.uuid4()}
\t\tsummarizeBy: none
'''
        dim = dim.replace("\n\tpartition DimDate = calculated", block + "\n\tpartition DimDate = calculated")
        DIM_DATE.write_text(dim, encoding="utf-8")

    if not COMPONENT.exists():
        COMPONENT.write_text(f'''table FinanceComponent
\tlineageTag: {uuid.uuid4()}

\tcolumn Component
\t\tdataType: string
\t\tisKey
\t\tlineageTag: {uuid.uuid4()}
\t\tsummarizeBy: none
\t\tsourceColumn: [Component]
\t\tsortByColumn: ComponentSort

\tcolumn ComponentSort
\t\tdataType: int64
\t\tisHidden
\t\tformatString: 0
\t\tlineageTag: {uuid.uuid4()}
\t\tsummarizeBy: none
\t\tsourceColumn: [ComponentSort]

\tpartition FinanceComponent = calculated
\t\tmode: import
\t\tsource = DATATABLE ( "Component", STRING, "ComponentSort", INTEGER, {{ {{ "Cost of Sales", 1 }}, {{ "Operating Expenses", 2 }}, {{ "Other & Tax", 3 }}, {{ "Net Income", 4 }} }} )
''', encoding="utf-8")

    fact = FACT.read_text(encoding="utf-8-sig")
    if "measure 'Latest Revenue Component Amount'" not in fact:
        measures = f'''\n\tmeasure 'Latest Revenue Component Amount' = SWITCH ( SELECTEDVALUE ( FinanceComponent[Component] ), "Cost of Sales", [Latest Cost of Sales Amount], "Operating Expenses", [Latest Operating Expenses Amount], "Other & Tax", [Latest Other and Tax Amount], "Net Income", [Latest Net Income] )
\t\tformatString: $#,0,,"M"
\t\tdisplayFolder: Finance\\Executive Composition
\t\tlineageTag: {uuid.uuid4()}

\tmeasure 'Latest Revenue Component Ratio' = DIVIDE ( [Latest Revenue Component Amount], [Latest Revenue] )
\t\tformatString: 0.0%
\t\tdisplayFolder: Finance\\Executive Composition
\t\tlineageTag: {uuid.uuid4()}

\tmeasure 'Latest Other and Tax Ratio' = DIVIDE ( [Latest Other and Tax Amount], [Latest Revenue] )
\t\tformatString: 0.0%
\t\tdisplayFolder: Finance\\Margins
\t\tlineageTag: {uuid.uuid4()}

\tmeasure 'Header As Of Label' = "As of " & FORMAT ( MAX ( DimDate[Date] ), "MMM yyyy" )
\t\tdisplayFolder: Display\\Context
\t\tlineageTag: {uuid.uuid4()}
'''
        fact = fact.replace("\n\tcolumn Company", measures + "\n\tcolumn Company")

    replacements = {
        "measure 'KPI YoY Color Latest Liabilities YoY' = VAR V = [Latest Liabilities YoY] RETURN SWITCH ( TRUE (), ISBLANK ( V ), \"#777777\", V > 0, \"#0F766E\", V < 0, \"#E05252\", \"#777777\" )":
        "measure 'KPI YoY Color Latest Liabilities YoY' = VAR V = [Latest Liabilities YoY] RETURN SWITCH ( TRUE (), ISBLANK ( V ), \"#777777\", V < 0, \"#0F766E\", V > 0, \"#E05252\", \"#777777\" )",
        "measure 'KPI YoY Color Latest Liabilities to Assets Variance pp' = VAR V = [Latest Liabilities to Assets Variance pp] RETURN SWITCH ( TRUE (), ISBLANK ( V ), \"#777777\", V > 0, \"#0F766E\", V < 0, \"#E05252\", \"#777777\" )":
        "measure 'KPI YoY Color Latest Liabilities to Assets Variance pp' = VAR V = [Latest Liabilities to Assets Variance pp] RETURN SWITCH ( TRUE (), ISBLANK ( V ), \"#777777\", V < 0, \"#0F766E\", V > 0, \"#E05252\", \"#777777\" )",
        "measure 'KPI YoY Color Latest Opex Ratio Variance pp' = VAR V = [Latest Opex Ratio Variance pp] RETURN SWITCH ( TRUE (), ISBLANK ( V ), \"#777777\", V > 0, \"#0F766E\", V < 0, \"#E05252\", \"#777777\" )":
        "measure 'KPI YoY Color Latest Opex Ratio Variance pp' = VAR V = [Latest Opex Ratio Variance pp] RETURN SWITCH ( TRUE (), ISBLANK ( V ), \"#777777\", V < 0, \"#0F766E\", V > 0, \"#E05252\", \"#777777\" )",
    }
    for old, new in replacements.items():
        fact = fact.replace(old, new)
    FACT.write_text(fact, encoding="utf-8")


def main() -> None:
    update_model()

    component_bar(
        PAGES / "FinancePage" / "visuals" / "FinancePage_Chart1" / "visual.json",
        False,
        "Revenue Allocation | Latest Quarter (Actual $)",
    )
    component_bar(
        PAGES / "ProfitabilityGrowthPage" / "visuals" / "Chart1" / "visual.json",
        True,
        "Cost & Profit Mix | Share of Latest Revenue",
    )
    capital_structure(PAGES / "BalanceLiquidityPage" / "visuals" / "Chart1" / "visual.json")
    repurpose_growth_chart(PAGES / "FinancePage" / "visuals" / "FinancePage_Chart3" / "visual.json")

    page_prefixes = {
        "FinancePage": "FinancePage_",
        "ProfitabilityGrowthPage": "",
        "BalanceLiquidityPage": "",
    }
    for page, prefix in page_prefixes.items():
        base = PAGES / page / "visuals"
        set_slicer(base / f"{prefix}Filter1" / "visual.json", "DimDate", "FiscalYear", "Fiscal year", "Global fiscal year")
        set_slicer(base / f"{prefix}Filter2" / "visual.json", "DimPeriodType", "PeriodType", "Period type", "Global period type")
        set_slicer(base / f"{prefix}Filter3" / "visual.json", "DimForm", "Form", "SEC form", "Global SEC form")

    trim_table(
        PAGES / "FinancePage" / "visuals" / "FinancePage_Chart5" / "visual.json",
        ["Date", "Quarterly Revenue", "Revenue YoY", "Quarterly Gross Margin", "Quarterly Net Margin"],
        "Quarterly CFO Scorecard | Growth & Margin",
    )
    trim_table(
        PAGES / "ProfitabilityGrowthPage" / "visuals" / "Chart5" / "visual.json",
        ["Date", "Quarterly Revenue", "Quarterly Net Margin", "Quarterly Operating Expense Ratio", "Operating Leverage Spread"],
        "Quarterly Profitability Drivers",
    )
    trim_table(
        PAGES / "BalanceLiquidityPage" / "visuals" / "Chart5" / "visual.json",
        ["Date", "Assets", "Liabilities", "Net Asset Position", "Cash Coverage of Liabilities"],
        "Quarterly Balance-Sheet Risk Detail",
    )
    upgrade_all_visuals()
    print("Apple Finance review fixes applied to canonical v2 PBIP artifacts only.")


if __name__ == "__main__":
    main()
