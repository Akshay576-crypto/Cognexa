from app.schemas.intelligence_result_schema import (
    IntelligenceResult,
)


def test_intelligence_result_creation():
    result = IntelligenceResult(
        question="Analyze the market.",
        research={
            "evidence": "Market revenue increased by 25%.",
        },
        consulting={
            "question": "Analyze the market.",
            "executive_summary": "The market is expanding.",
        },
    )

    assert result.question == "Analyze the market."

    assert (
        result.research.evidence
        == "Market revenue increased by 25%."
    )

    assert (
        result.consulting.executive_summary
        == "The market is expanding."
    )

    assert result.analytics == {}
    assert result.charts == []
    assert result.tables == []