from app.presentations.slide_planner import SlidePlanner

def create_test_dashboard():

    return {
        "type": "dashboard",
        "title": "Indian Electric Vehicle Market",
        "description": (
            "Business intelligence dashboard "
            "for the Indian EV market."
        ),
        "kpis": [
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
        ],
        "charts": [
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
        ],
        "tables": [
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
        ],
        "maps": [
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
        ],
        "sources": [
            {
                "source": "Example Research",
                "source_url": "https://example.com",
            }
        ],
    }


def test_slide_planner():

    planner = SlidePlanner()

    dashboard = create_test_dashboard()

    result = planner.create_plan(
        title="Indian Electric Vehicle Market",
        dashboard=dashboard,
        minimum_slides=20,
    )

    assert result["type"] == "presentation_plan"

    assert result["title"] == (
        "Indian Electric Vehicle Market"
    )

    assert result["slide_count"] >= 20

    slides = result["slides"]

    assert len(slides) >= 20

    # Every slide must have a number.
    for index, slide in enumerate(slides):

        assert slide["slide_number"] == index + 1

    # First slide
    assert slides[0]["slide_type"] == "title"

    # Executive summary
    assert slides[1]["slide_type"] == "executive_summary"

    # Overview
    assert slides[2]["slide_type"] == "overview"

    # Sources should remain the final slide.
    assert slides[-1]["slide_type"] == "sources"

    # Source attribution
    assert (
        slides[-1]["sources"][0]["source_url"]
        == "https://example.com"
    )

    print("\nSLIDE PLANNER TEST PASSED")
    print(result)


def test_minimum_slide_validation():

    planner = SlidePlanner()

    dashboard = create_test_dashboard()

    try:

        planner.create_plan(
            title="Test",
            dashboard=dashboard,
            minimum_slides=0,
        )

        assert False, "Expected ValueError"

    except ValueError:

        pass

    print("\nVALIDATION TEST PASSED")


def test_empty_title_validation():

    planner = SlidePlanner()

    dashboard = create_test_dashboard()

    try:

        planner.create_plan(
            title="",
            dashboard=dashboard,
        )

        assert False, "Expected ValueError"

    except ValueError:

        pass

    print("\nTITLE VALIDATION TEST PASSED")


def test_empty_dashboard_validation():

    planner = SlidePlanner()

    try:

        planner.create_plan(
            title="Test Presentation",
            dashboard={},
        )

        assert False, "Expected ValueError"

    except ValueError:

        pass

    print("\nDASHBOARD VALIDATION TEST PASSED")


def test_custom_minimum_slides():

    planner = SlidePlanner()

    dashboard = create_test_dashboard()

    result = planner.create_plan(
        title="Compact EV Analysis",
        dashboard=dashboard,
        minimum_slides=10,
    )

    assert result["slide_count"] >= 10

    print("\nCUSTOM SLIDE COUNT TEST PASSED")


if __name__ == "__main__":

    test_slide_planner()
    test_minimum_slide_validation()
    test_empty_title_validation()
    test_empty_dashboard_validation()
    test_custom_minimum_slides()

    print("\nALL SLIDE PLANNER TESTS PASSED")

