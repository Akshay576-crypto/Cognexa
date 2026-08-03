from app.dashboard.dashboard_engine import DashboardEngine


def test_dashboard_engine():

    engine = DashboardEngine()

    kpis = [
        {
            "name": "Market Growth",
            "value": 32.5,
            "unit": "%",
            "source": "Example Research",
            "source_url": "https://example.com",
        },
        {
            "name": "Market Size",
            "value": 120,
            "unit": "Billion USD",
            "source": "Example Research",
            "source_url": "https://example.com",
        },
        {
            "name": "Market Share",
            "value": 24,
            "unit": "%",
            "source": "Example Research",
            "source_url": "https://example.com",
        },
        {
            "name": "Annual Sales",
            "value": 850000,
            "unit": "Units",
            "source": "Example Research",
            "source_url": "https://example.com",
        },
    ]

    charts = [
        {
            "type": "line",
            "title": "EV Market Growth",
            "data": [
                {"period": 2023, "value": 100},
                {"period": 2024, "value": 130},
                {"period": 2025, "value": 165},
            ],
            "source": "Example Research",
            "source_url": "https://example.com",
        },
        {
            "type": "bar",
            "title": "Company Comparison",
            "data": [
                {"company": "Company A", "value": 500},
                {"company": "Company B", "value": 400},
            ],
            "source": "Example Research",
            "source_url": "https://example.com",
        },
    ]

    tables = [
        {
            "type": "table",
            "title": "Top EV Companies",
            "columns": ["Company", "Market Share"],
            "rows": [
                ["Company A", 35],
                ["Company B", 28],
            ],
            "source": "Example Research",
            "source_url": "https://example.com",
        }
    ]

    maps = [
        {
            "type": "map",
            "title": "EV Market Share by State",
            "location_type": "region",
            "metric": "Market Share",
            "unit": "%",
            "data": [
                {
                    "location": "Maharashtra",
                    "value": 32,
                },
                {
                    "location": "Gujarat",
                    "value": 24,
                },
            ],
            "source": "Example Research",
            "source_url": "https://example.com",
        }
    ]

    sources = [
        {
            "source": "Example Research",
            "source_url": "https://example.com",
        }
    ]

    result = engine.create_dashboard(
        title="Indian Electric Vehicle Market",
        description="Business intelligence dashboard for the Indian EV market.",
        kpis=kpis,
        charts=charts,
        tables=tables,
        maps=maps,
        sources=sources,
        theme_name="cognexa_aurora",
    )

    dashboard = result["dashboard"]
    layout = result["layout"]

    # Dashboard
    assert dashboard["type"] == "dashboard"
    assert dashboard["title"] == "Indian Electric Vehicle Market"
    assert dashboard["description"] is not None

    # Theme
    assert dashboard["theme"]["theme_id"] == "cognexa_aurora"

    # Components
    assert len(dashboard["kpis"]) == 4
    assert len(dashboard["charts"]) == 2
    assert len(dashboard["tables"]) == 1
    assert len(dashboard["maps"]) == 1
    assert len(dashboard["sources"]) == 1

    # Source preservation
    assert dashboard["kpis"][0]["source_url"] == "https://example.com"
    assert dashboard["charts"][0]["source_url"] == "https://example.com"
    assert dashboard["tables"][0]["source_url"] == "https://example.com"
    assert dashboard["maps"][0]["source_url"] == "https://example.com"

    # Layout
    assert layout["type"] == "dashboard_layout"
    assert layout["grid_columns"] == 12

    assert len(layout["rows"]) == 7

    assert layout["rows"][0]["row_type"] == "header"
    assert layout["rows"][1]["row_type"] == "kpi"
    assert layout["rows"][2]["row_type"] == "chart"
    assert layout["rows"][3]["row_type"] == "chart"
    assert layout["rows"][4]["row_type"] == "table"
    assert layout["rows"][5]["row_type"] == "map"
    assert layout["rows"][6]["row_type"] == "sources"

    print("\nDASHBOARD ENGINE TEST PASSED")
    print(result)


def test_dashboard_without_optional_components():

    engine = DashboardEngine()

    result = engine.create_dashboard(
        title="Simple Dashboard",
    )

    dashboard = result["dashboard"]
    layout = result["layout"]

    assert dashboard["title"] == "Simple Dashboard"

    assert dashboard["kpis"] == []
    assert dashboard["charts"] == []
    assert dashboard["tables"] == []
    assert dashboard["maps"] == []
    assert dashboard["sources"] == []

    # Only header should exist.
    assert len(layout["rows"]) == 1
    assert layout["rows"][0]["row_type"] == "header"

    print("\nMINIMAL DASHBOARD TEST PASSED")


def test_custom_theme():

    engine = DashboardEngine()

    result = engine.create_dashboard(
        title="Executive Dashboard",
        theme_name="executive_dark",
    )

    dashboard = result["dashboard"]

    assert dashboard["theme"]["theme_id"] == "executive_dark"
    assert dashboard["theme"]["mode"] == "dark"

    print("\nCUSTOM THEME TEST PASSED")


def test_invalid_theme():

    engine = DashboardEngine()

    try:
        engine.create_dashboard(
            title="Invalid Dashboard",
            theme_name="unknown_theme",
        )

        assert False, "Expected ValueError"

    except ValueError:
        pass

    print("\nVALIDATION TEST PASSED")


if __name__ == "__main__":

    test_dashboard_engine()
    test_dashboard_without_optional_components()
    test_custom_theme()
    test_invalid_theme()

    print("\nALL DASHBOARD ENGINE TESTS PASSED")