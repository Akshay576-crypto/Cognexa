from fastapi.testclient import TestClient

from app.main import app
from app.api.v1.dashboard import engine
from app.auth.dependencies import get_current_user


client = TestClient(app)


def fake_current_user():
    return {
        "user_id": 1,
        "email": "test@example.com",
        "role": "user",
    }


def fake_create_dashboard(
    title,
    description=None,
    kpis=None,
    charts=None,
    tables=None,
    maps=None,
    sources=None,
    theme_name="cognexa_aurora",
    grid_columns=12,
):
    return {
        "dashboard": {
            "type": "dashboard",
            "title": title,
            "description": description,
            "theme": {
                "theme_id": theme_name,
                "name": "Cognexa Aurora Intelligence",
                "mode": "dark",
            },
            "kpis": kpis or [],
            "charts": charts or [],
            "tables": tables or [],
            "maps": maps or [],
            "sources": sources or [],
        },
        "layout": {
            "type": "dashboard_layout",
            "grid_columns": grid_columns,
            "rows": [
                {
                    "row_type": "header",
                    "components": [
                        {
                            "component_type": "header",
                            "title": title,
                            "description": description,
                            "width": grid_columns,
                        }
                    ],
                }
            ],
        },
    }


def test_dashboard_api():

    app.dependency_overrides[
        get_current_user
    ] = fake_current_user

    original_create_dashboard = engine.create_dashboard
    engine.create_dashboard = fake_create_dashboard

    response = client.post(
        "/api/v1/dashboard/",
        json={
            "title": "Indian Electric Vehicle Market",
            "description": "EV business intelligence dashboard.",
            "kpis": [
                {
                    "name": "Market Growth",
                    "value": 32.5,
                    "unit": "%",
                }
            ],
            "charts": [
                {
                    "type": "line",
                    "title": "EV Market Growth",
                    "data": [
                        {"period": 2023, "value": 100},
                        {"period": 2024, "value": 130},
                    ],
                }
            ],
            "theme_name": "cognexa_aurora",
            "grid_columns": 12,
        },
    )

    engine.create_dashboard = original_create_dashboard
    app.dependency_overrides.clear()

    assert response.status_code == 200

    data = response.json()

    assert "dashboard" in data
    assert "layout" in data

    assert data["dashboard"]["type"] == "dashboard"
    assert data["dashboard"]["title"] == "Indian Electric Vehicle Market"

    assert len(data["dashboard"]["kpis"]) == 1
    assert len(data["dashboard"]["charts"]) == 1

    assert data["dashboard"]["theme"]["theme_id"] == "cognexa_aurora"

    assert data["layout"]["type"] == "dashboard_layout"
    assert data["layout"]["grid_columns"] == 12


def test_dashboard_empty_title():

    app.dependency_overrides[
        get_current_user
    ] = fake_current_user

    response = client.post(
        "/api/v1/dashboard/",
        json={
            "title": "",
        },
    )

    app.dependency_overrides.clear()

    assert response.status_code == 422


def test_dashboard_invalid_grid_columns():

    app.dependency_overrides[
        get_current_user
    ] = fake_current_user

    response = client.post(
        "/api/v1/dashboard/",
        json={
            "title": "Test Dashboard",
            "grid_columns": 0,
        },
    )

    app.dependency_overrides.clear()

    assert response.status_code == 422