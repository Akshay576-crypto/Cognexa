from app.dashboard.dashboard_schema import DashboardSchema


def test_dashboard_schema():

    theme = {
        "theme_id": "cognexa_aurora",
        "name": "Cognexa Aurora Intelligence",
        "mode": "dark",
    }

    dashboard = DashboardSchema(
        title="Indian Electric Vehicle Market",
        description="Business intelligence dashboard for the Indian EV market.",
        theme=theme,
    )

    kpi = {
        "name": "Market Growth",
        "value": 32.5,
        "unit": "%",
        "source": "Example Research",
        "source_url": "https://example.com",
    }

    chart = {
        "type": "line",
        "title": "EV Market Growth",
        "data": [
            {"period": 2023, "value": 100},
            {"period": 2024, "value": 130},
            {"period": 2025, "value": 165},
        ],
        "source": "Example Research",
        "source_url": "https://example.com",
    }

    table = {
        "type": "table",
        "title": "Top EV Markets",
        "columns": ["Country", "Market Size"],
        "rows": [
            ["India", 120],
            ["USA", 250],
            ["China", 300],
        ],
        "source": "Example Research",
        "source_url": "https://example.com",
    }

    map_spec = {
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

    dashboard.add_kpi(kpi)
    dashboard.add_chart(chart)
    dashboard.add_table(table)
    dashboard.add_map(map_spec)

    dashboard.add_section(
        title="Market Overview",
        component_type="mixed",
        component_ids=["kpi_1", "chart_1"],
    )

    dashboard.add_section(
        title="Geographic Analysis",
        component_type="map",
        component_ids=["map_1"],
    )

    dashboard.add_source(
        source="Example Research",
        source_url="https://example.com",
    )

    result = dashboard.to_dict()

    assert result["type"] == "dashboard"
    assert result["title"] == "Indian Electric Vehicle Market"
    assert result["description"] is not None

    assert result["theme"]["theme_id"] == "cognexa_aurora"

    assert len(result["kpis"]) == 1
    assert len(result["charts"]) == 1
    assert len(result["tables"]) == 1
    assert len(result["maps"]) == 1

    assert len(result["sections"]) == 2
    assert len(result["sources"]) == 1

    assert result["kpis"][0]["name"] == "Market Growth"
    assert result["charts"][0]["type"] == "line"
    assert result["tables"][0]["type"] == "table"
    assert result["maps"][0]["type"] == "map"

    assert result["sources"][0]["source"] == "Example Research"

    print("\nDASHBOARD SCHEMA TEST PASSED")
    print(result)


def test_empty_title_validation():

    try:
        DashboardSchema(title="")
        assert False, "Expected ValueError"

    except ValueError:
        pass

    print("\nVALIDATION TEST PASSED")


if __name__ == "__main__":

    test_dashboard_schema()
    test_empty_title_validation()

    print("\nALL DASHBOARD SCHEMA TESTS PASSED")