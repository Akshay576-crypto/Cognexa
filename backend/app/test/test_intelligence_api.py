from fastapi.testclient import TestClient

from app.main import app
from app.api.v1.intelligence import pipeline
from app.auth.dependencies import get_current_user
from app.schemas.intelligence_result_schema import IntelligenceResult


client = TestClient(app)


def fake_current_user():
    return {
        "user_id": 1,
        "email": "test@example.com",
        "role": "user",
    }


def fake_pipeline_run(
    question,
    document_id=None,
    top_k=5,
    sources="",
):
    return IntelligenceResult(
        question=question,
        research={
            "evidence": "Test research evidence.",
        },
        consulting={
            "question": question,
            "executive_summary": "Test consulting result.",
        },
        analytics={},
        charts=[],
        tables=[],
    )


def test_intelligence_api():

    app.dependency_overrides[
        get_current_user
    ] = fake_current_user

    original_run = pipeline.run
    pipeline.run = fake_pipeline_run

    response = client.post(
        "/api/v1/intelligence/",
        json={
            "question": "Analyze the market.",
            "document_id": 12,
            "top_k": 5,
            "sources": "Market Report",
        },
    )

    pipeline.run = original_run
    app.dependency_overrides.clear()

    assert response.status_code == 200

    data = response.json()

    assert data["question"] == "Analyze the market."

    assert (
        data["research"]["evidence"]
        == "Test research evidence."
    )

    assert (
        data["consulting"]["executive_summary"]
        == "Test consulting result."
    )

    assert data["analytics"] == {}
    assert data["charts"] == []
    assert data["tables"] == []


def test_intelligence_empty_question():

    app.dependency_overrides[
        get_current_user
    ] = fake_current_user

    response = client.post(
        "/api/v1/intelligence/",
        json={
            "question": "",
        },
    )

    app.dependency_overrides.clear()

    assert response.status_code == 422


def test_intelligence_invalid_top_k():

    app.dependency_overrides[
        get_current_user
    ] = fake_current_user

    response = client.post(
        "/api/v1/intelligence/",
        json={
            "question": "Analyze the market.",
            "top_k": 0,
        },
    )

    app.dependency_overrides.clear()

    assert response.status_code == 422