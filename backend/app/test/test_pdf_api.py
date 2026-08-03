from pathlib import Path

from fastapi.testclient import TestClient

from app.main import app
from app.auth.dependencies import get_current_user
from app.api.v1.pdf import pdf_engine


client = TestClient(app)


def fake_current_user():
    return {
        "user_id": 1,
        "email": "test@example.com",
        "role": "user",
    }


def test_pdf_api():

    app.dependency_overrides[
        get_current_user
    ] = fake_current_user

    response = client.post(
        "/api/v1/pdf/",
        json={
            "presentation_spec": {
                "type": "presentation_specification",
                "title": "Indian Electric Vehicle Market",
                "slides": [
                    {
                        "slide_type": "title",
                        "title": "Indian Electric Vehicle Market",
                        "content": {
                            "subtitle": "Cognexa Research Report"
                        },
                    },
                    {
                        "slide_type": "executive_summary",
                        "title": "Executive Summary",
                        "content": {
                            "summary": [
                                "The Indian EV market is expanding.",
                                "Competition is increasing."
                            ]
                        },
                    },
                ],
            },
            "output_filename": "test_api_ev_market.pdf",
            "theme_id": "cognexa_aurora",
        },
    )

    app.dependency_overrides.clear()

    assert response.status_code == 200

    data = response.json()

    assert data["type"] == "pdf"
    assert data["title"] == "Indian Electric Vehicle Market"
    assert data["slide_count"] == 2
    assert data["theme_id"] == "cognexa_aurora"

    output_path = Path(data["output_path"])

    assert output_path.exists()
    assert output_path.stat().st_size > 0


def test_pdf_empty_spec():

    app.dependency_overrides[
        get_current_user
    ] = fake_current_user

    response = client.post(
        "/api/v1/pdf/",
        json={
            "presentation_spec": {},
            "output_filename": "invalid.pdf",
            "theme_id": "cognexa_aurora",
        },
    )

    app.dependency_overrides.clear()

    assert response.status_code == 400


def test_pdf_invalid_theme():

    app.dependency_overrides[
        get_current_user
    ] = fake_current_user

    response = client.post(
        "/api/v1/pdf/",
        json={
            "presentation_spec": {
                "type": "presentation_specification",
                "title": "Test PDF",
                "slides": [
                    {
                        "slide_type": "title",
                        "title": "Test",
                        "content": {},
                    }
                ],
            },
            "output_filename": "invalid_theme.pdf",
            "theme_id": "does_not_exist",
        },
    )

    app.dependency_overrides.clear()

    assert response.status_code == 400