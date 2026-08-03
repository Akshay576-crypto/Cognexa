from app.dashboard.layout_engine import LayoutEngine


def test_dashboard_layout():

    engine = LayoutEngine()

    dashboard = {
        "title": "Indian Electric Vehicle Market",
        "description": "EV market intelligence dashboard.",
        "kpis": [
            {
                "name": "Market Growth",
                "value": 32.5,
                "unit": "%",
            },
            {
                "name": "Market Size",
                "value": 120,
                "unit": "Billion USD",
            },
            {
                "name": "Market Share",
                "value": 24,
                "unit": "%",
            },
            {
                "name": "Annual Sales",
                "value": 850000,
                "unit": "Units",
            },
        ],
        "charts": [
            {
                "type": "line",
                "title": "Market Growth",
            },
            {
                "type": "bar",
                "title": "Company Comparison",
            },
        ],
        "tables": [
            {
                "type": "table",
                "title": "Top Companies",
            }
        ],
        "maps": [
            {
                "type": "map",
                "title": "Market Share by State",
            }
        ],
        "sources": [
            {
                "source": "Example Research",
                "source_url": "https://example.com",
            }
        ],
    }

    result = engine.create_layout(dashboard)

    assert result["type"] == "dashboard_layout"
    assert result["grid_columns"] == 12

    # Expected rows:
    # 1 Header
    # 2 KPI
    # 3 Chart
    # 4 Chart
    # 5 Table
    # 6 Map
    # 7 Sources

    assert len(result["rows"]) == 7

    # Header
    assert result["rows"][0]["row_type"] == "header"

    # KPI row
    kpi_row = result["rows"][1]

    assert kpi_row["row_type"] == "kpi"
    assert len(kpi_row["components"]) == 4

    for component in kpi_row["components"]:
        assert component["component_type"] == "kpi"
        assert component["width"] == 3

    # Charts
    assert result["rows"][2]["row_type"] == "chart"
    assert result["rows"][3]["row_type"] == "chart"

    # Table
    assert result["rows"][4]["row_type"] == "table"

    # Map
    assert result["rows"][5]["row_type"] == "map"

    # Sources
    assert result["rows"][6]["row_type"] == "sources"

    print("\nDASHBOARD LAYOUT TEST PASSED")
    print(result)


def test_custom_grid():

    engine = LayoutEngine()

    dashboard = {
        "title": "Test Dashboard",
        "kpis": [
            {
                "name": "KPI 1",
                "value": 10,
            },
            {
                "name": "KPI 2",
                "value": 20,
            },
        ],
    }

    result = engine.create_layout(
        dashboard,
        grid_columns=8,
    )

    assert result["grid_columns"] == 8

    kpi_components = result["rows"][1]["components"]

    assert len(kpi_components) == 2
    assert kpi_components[0]["width"] == 4
    assert kpi_components[1]["width"] == 4

    print("\nCUSTOM GRID TEST PASSED")


def test_empty_dashboard_validation():

    engine = LayoutEngine()

    try:
        engine.create_layout({})

        assert False, "Expected ValueError"

    except ValueError:
        pass

    try:
        engine.create_layout(
            {
                "title": "Test",
            },
            grid_columns=0,
        )

        assert False, "Expected ValueError"

    except ValueError:
        pass

    print("\nVALIDATION TEST PASSED")


if __name__ == "__main__":

    test_dashboard_layout()
    test_custom_grid()
    test_empty_dashboard_validation()

    print("\nALL LAYOUT ENGINE TESTS PASSED")

