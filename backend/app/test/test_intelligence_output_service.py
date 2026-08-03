from app.services.intelligence_output_service import IntelligenceOutputService
from app.schemas.consulting_result_schema import (
    ConsultingResult,
    ConsultingKPI,
    ConsultingTrend,
    ConsultingComparison,
)


service = IntelligenceOutputService()


def test_analyze_metrics():
    data = {
        "previous_value": 100,
        "current_value": 125,
        "company_value": 25,
        "total_market_value": 100,
        "values": [10, 20, 30],
    }

    result = service.analyze_metrics(data)

    assert result["input"] == data
    assert result["kpis"]["current_value"] == 125
    assert result["kpis"]["absolute_change"] == 25
    assert result["kpis"]["percentage_change"] == 25.0
    assert result["kpis"]["market_share"] == 25.0
    assert result["kpis"]["total"] == 60
    assert result["kpis"]["average"] == 20


def test_create_kpis():
    kpis = [
        {
            "name": "Revenue",
            "value": 125,
            "unit": "USD Million",
        },
        {
            "name": "Market Share",
            "value": 25,
            "unit": "%",
        },
    ]

    result = service.create_kpis(kpis)

    assert result["kpi_count"] == 2
    assert len(result["kpis"]) == 2
    assert result["kpis"][0]["name"] == "Revenue"
    assert result["kpis"][1]["name"] == "Market Share"


def test_analyze_trends():
    data = [
        {"period": 2022, "value": 100},
        {"period": 2023, "value": 120},
        {"period": 2024, "value": 150},
    ]

    result = service.analyze_trends(data)

    assert result["period_count"] == 3
    assert result["overall_direction"] == "increasing"
    assert result["overall_change"] == 50.0
    assert result["highest_period"]["period"] == 2024
    assert result["lowest_period"]["period"] == 2022


def test_compare():
    metrics = [
        {
            "metric": "Revenue",
            "value_a": 500,
            "value_b": 400,
            "unit": "USD Million",
            "higher_is_better": True,
        }
    ]

    result = service.compare(
        entity_a="Company A",
        entity_b="Company B",
        metrics=metrics,
    )

    assert result["entity_a"] == "Company A"
    assert result["entity_b"] == "Company B"
    assert result["metric_count"] == 1
    assert result["comparisons"][0]["winner"] == "Company A"


def test_create_charts():
    charts = [
        {
            "type": "bar",
            "title": "Revenue",
            "data": {
                "labels": ["2025", "2026"],
                "values": [100, 125],
            },
        }
    ]

    result = service.create_charts(charts)

    assert result["chart_count"] == 1
    assert len(result["charts"]) == 1
    assert result["charts"][0]["type"] == "bar"


def test_create_tables():
    tables = [
        {
            "type": "table",
            "title": "Revenue Table",
            "columns": ["Year", "Revenue"],
            "rows": [
                {"Year": 2025, "Revenue": 100},
                {"Year": 2026, "Revenue": 125},
            ],
        }
    ]

    result = service.create_tables(tables)

    assert result["table_count"] == 1
    assert len(result["tables"]) == 1
    assert result["tables"][0]["title"] == "Revenue Table"


def test_build_output():
    analytics_data = {
        "previous_value": 100,
        "current_value": 125,
    }

    kpis = [
        {
            "name": "Revenue",
            "value": 125,
            "unit": "USD Million",
        }
    ]

    trends = [
        {"period": 2025, "value": 100},
        {"period": 2026, "value": 125},
    ]

    charts = [
        {
            "type": "line",
            "title": "Revenue Trend",
        }
    ]

    tables = [
        {
            "type": "table",
            "title": "Revenue Data",
        }
    ]

    result = service.build_output(
        analytics_data=analytics_data,
        kpis=kpis,
        trend_data=trends,
        charts=charts,
        tables=tables,
    )

    assert result["analytics"]["kpis"]["current_value"] == 125

    assert result["kpis"]["kpi_count"] == 1

    assert result["trends"]["period_count"] == 2
    assert result["trends"]["overall_direction"] == "increasing"

    assert result["charts"]["chart_count"] == 1
    assert result["tables"]["table_count"] == 1

    assert result["comparison"] is None

def test_build_from_consulting_result():
    result = ConsultingResult(
        question="Analyze the market.",
        executive_summary="Market is growing.",
        problem_definition="Assess market performance.",
        kpis=[
            ConsultingKPI(
                name="Revenue",
                value=125,
                unit="USD Million",
                period="2026",
                change=25.0,
                trend="increasing",
            )
        ],
        trends=[
            ConsultingTrend(
                metric="Revenue",
                direction="increasing",
                description="Revenue increased.",
                data=[
                    {"period": 2025, "value": 100},
                    {"period": 2026, "value": 125},
                ],
            )
        ],
        comparisons=[
            ConsultingComparison(
                metric="Revenue",
                entity_a="Company A",
                value_a=500,
                entity_b="Company B",
                value_b=400,
                unit="USD Million",
                winner="Company A",
            )
        ],
    )

    service = IntelligenceOutputService()

    output = service.build_from_consulting_result(
        result
    )

    assert output["question"] == "Analyze the market."
    assert output["executive_summary"] == "Market is growing."

    assert len(output["kpis"]) == 1
    assert output["kpis"][0]["name"] == "Revenue"

    assert len(output["trends"]) == 1
    assert output["trends"][0]["metric"] == "Revenue"
    assert (
        output["trends"][0]["analysis"]["overall_direction"]
        == "increasing"
    )

    assert len(output["comparisons"]) == 1
    assert (
        output["comparisons"][0]["comparisons"][0]["winner"]
        == "Company A"
    )

    assert output["charts"]["chart_count"] == 1
    assert output["charts"]["charts"][0]["type"] == "line"

    assert output["tables"]["table_count"] == 1
    assert (
        output["tables"]["tables"][0]["type"]
        == "table"
    )