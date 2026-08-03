from app.services.dashboard_integration_service import (
    DashboardIntegrationService,
)
from app.schemas.intelligence_result_schema import (
    IntelligenceResult,
)


def create_intelligence_result():
    return IntelligenceResult(
        question="Analyze the EV market.",
        research={
            "evidence": "EV market revenue increased by 25%.",
        },
        consulting={
            "question": "Analyze the EV market.",
            "executive_summary": "The EV market is expanding.",
            "kpis": [
                {
                    "name": "Market Growth",
                    "value": 25.0,
                    "unit": "%",
                }
            ],
            "sources": [
                {
                    "source": "Market Research Report",
                    "source_url": "https://example.com/report",
                }
            ],
        },
        charts=[
            {
                "type": "line",
                "title": "EV Market Growth",
                "data": [
                    {"period": 2024, "value": 100},
                    {"period": 2025, "value": 125},
                ],
            }
        ],
        tables=[
            {
                "type": "table",
                "title": "EV Market Data",
                "columns": ["Year", "Value"],
                "rows": [
                    {"Year": 2024, "Value": 100},
                    {"Year": 2025, "Value": 125},
                ],
            }
        ],
    )


def test_build_dashboard_from_intelligence_result():

    service = DashboardIntegrationService()

    intelligence_result = create_intelligence_result()

    result = service.build_dashboard(
        intelligence_result=intelligence_result,
        title="Indian EV Market Intelligence",
        description="Executive intelligence dashboard for the Indian EV market.",
    )

    dashboard = result["dashboard"]
    layout = result["layout"]

    assert dashboard["type"] == "dashboard"

    assert dashboard["title"] == (
        "Indian EV Market Intelligence"
    )

    assert dashboard["description"] == (
        "Executive intelligence dashboard for the Indian EV market."
    )

    assert len(dashboard["kpis"]) == 1
    assert dashboard["kpis"][0]["name"] == "Market Growth"

    assert len(dashboard["charts"]) == 1
    assert dashboard["charts"][0]["title"] == (
        "EV Market Growth"
    )

    assert len(dashboard["tables"]) == 1
    assert dashboard["tables"][0]["title"] == (
        "EV Market Data"
    )

    assert dashboard["maps"] == []

    assert len(dashboard["sources"]) == 1
    assert dashboard["sources"][0]["source"] == (
        "Market Research Report"
    )

    assert layout["type"] == "dashboard_layout"


def test_build_dashboard_uses_default_theme():

    service = DashboardIntegrationService()

    intelligence_result = create_intelligence_result()

    result = service.build_dashboard(
        intelligence_result=intelligence_result,
        title="EV Intelligence",
    )

    assert result["dashboard"]["theme"]["theme_id"] == (
        "cognexa_aurora"
    )


def test_build_dashboard_without_optional_output():

    service = DashboardIntegrationService()

    intelligence_result = IntelligenceResult(
        question="Analyze the market.",
        consulting={
            "question": "Analyze the market.",
        },
    )

    result = service.build_dashboard(
        intelligence_result=intelligence_result,
        title="Market Intelligence",
    )

    dashboard = result["dashboard"]

    assert dashboard["kpis"] == []
    assert dashboard["charts"] == []
    assert dashboard["tables"] == []
    assert dashboard["maps"] == []
    assert dashboard["sources"] == []
