from app.schemas.consulting_result_schema import (
    ConsultingResult,
    ConsultingFinding,
    ConsultingKPI,
    ConsultingRecommendation,
)


def test_consulting_result_schema():

    result = ConsultingResult(
        question="Should we enter the Indian EV market?",
        executive_summary="The market shows attractive growth potential.",
        findings=[
            ConsultingFinding(
                title="Market Growth",
                description="The market is expanding.",
                evidence="Research evidence indicates strong growth.",
                importance="high",
            )
        ],
        kpis=[
            ConsultingKPI(
                name="Market Growth",
                value=18.5,
                unit="%",
                period="2026",
                trend="increasing",
            )
        ],
        recommendations=[
            ConsultingRecommendation(
                title="Conduct regional market validation",
                description="Validate demand before large-scale expansion.",
                priority="high",
                timeframe="medium-term",
            )
        ],
    )

    assert result.question
    assert len(result.findings) == 1
    assert len(result.kpis) == 1
    assert len(result.recommendations) == 1


def test_empty_collections():

    result = ConsultingResult(
        question="Test question"
    )

    assert result.findings == []
    assert result.kpis == []
    assert result.trends == []
    assert result.comparisons == []
    assert result.risks == []
    assert result.opportunities == []
    assert result.recommendations == []


def test_kpi_schema():

    kpi = ConsultingKPI(
        name="Revenue",
        value=125,
        unit="USD Million",
        period="2026",
        change=25,
        trend="increasing",
    )

    assert kpi.name == "Revenue"
    assert kpi.value == 125
    assert kpi.change == 25
    assert kpi.trend == "increasing"