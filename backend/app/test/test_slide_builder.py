import pytest

from app.presentations.slide_builder import SlideBuilder


@pytest.fixture
def builder():
    return SlideBuilder()


# ============================================================
# BASIC VALIDATION
# ============================================================

def test_empty_slide_plan(builder):

    with pytest.raises(ValueError, match="Slide plan cannot be empty"):
        builder.build_slide({})


def test_missing_slide_type(builder):

    with pytest.raises(ValueError, match="Slide type is required"):
        builder.build_slide({
            "title": "Test Slide"
        })


def test_unsupported_slide_type(builder):

    with pytest.raises(
        ValueError,
        match="Unsupported slide type"
    ):
        builder.build_slide({
            "slide_type": "invalid",
            "title": "Test Slide"
        })


def test_missing_slide_title(builder):

    with pytest.raises(
        ValueError,
        match="Slide title cannot be empty"
    ):
        builder.build_slide({
            "slide_type": "title"
        })


# ============================================================
# TITLE SLIDE
# ============================================================

def test_title_slide(builder):

    result = builder.build_slide({
        "slide_number": 1,
        "slide_type": "title",
        "title": "Indian EV Market",
        "purpose": "Introduction",
        "description": "Overview of the Indian EV market."
    })

    assert result["slide_number"] == 1
    assert result["slide_type"] == "title"
    assert result["title"] == "Indian EV Market"
    assert result["purpose"] == "Introduction"

    assert result["content"]["subtitle"] == (
        "Overview of the Indian EV market."
    )

    assert result["sources"] == []


# ============================================================
# EXECUTIVE SUMMARY
# ============================================================

def test_executive_summary_slide(builder):

    kpis = [
        {
            "name": "Market Growth",
            "value": 32.5,
            "unit": "%"
        }
    ]

    sources = [
        {
            "source": "Example Research",
            "source_url": "https://example.com"
        }
    ]

    result = builder.build_slide({
        "slide_number": 2,
        "slide_type": "executive_summary",
        "title": "Executive Summary",
        "components": {
            "kpis": kpis,
            "sources": sources
        }
    })

    assert result["content"]["kpis"] == kpis
    assert result["sources"] == sources


# ============================================================
# OVERVIEW
# ============================================================

def test_overview_slide(builder):

    result = builder.build_slide({
        "slide_number": 3,
        "slide_type": "overview",
        "title": "Market Overview",
        "description": "Indian EV market overview."
    })

    assert result["content"]["description"] == (
        "Indian EV market overview."
    )


# ============================================================
# KPI
# ============================================================

def test_kpi_slide(builder):

    result = builder.build_slide({
        "slide_number": 4,
        "slide_type": "kpi",
        "title": "Market Growth",
        "component": {
            "name": "Market Growth",
            "value": 32.5,
            "unit": "%",
            "source": "Example Research",
            "source_url": "https://example.com"
        }
    })

    assert result["content"] == {
        "name": "Market Growth",
        "value": 32.5,
        "unit": "%"
    }

    assert result["sources"] == [
        {
            "source": "Example Research",
            "source_url": "https://example.com"
        }
    ]


# ============================================================
# CHART
# ============================================================

def test_chart_slide(builder):

    chart_data = [
        {"period": 2023, "value": 100},
        {"period": 2024, "value": 130}
    ]

    result = builder.build_slide({
        "slide_number": 5,
        "slide_type": "chart",
        "title": "EV Market Growth",
        "component": {
            "type": "line",
            "data": chart_data,
            "source": "Example Research",
            "source_url": "https://example.com"
        }
    })

    assert result["content"]["chart_type"] == "line"
    assert result["content"]["data"] == chart_data

    assert len(result["sources"]) == 1
    assert result["sources"][0]["source"] == (
        "Example Research"
    )


# ============================================================
# TABLE
# ============================================================

def test_table_slide(builder):

    columns = ["Company", "Market Share"]
    rows = [
        ["Company A", 35],
        ["Company B", 28]
    ]

    result = builder.build_slide({
        "slide_number": 6,
        "slide_type": "table",
        "title": "Top EV Companies",
        "component": {
            "columns": columns,
            "rows": rows,
            "source": "Example Research",
            "source_url": "https://example.com"
        }
    })

    assert result["content"]["columns"] == columns
    assert result["content"]["rows"] == rows

    assert result["sources"] == [
        {
            "source": "Example Research",
            "source_url": "https://example.com"
        }
    ]


# ============================================================
# MAP
# ============================================================

def test_map_slide(builder):

    map_data = [
        {
            "location": "Maharashtra",
            "value": 32
        },
        {
            "location": "Gujarat",
            "value": 24
        }
    ]

    result = builder.build_slide({
        "slide_number": 7,
        "slide_type": "map",
        "title": "EV Market Share by State",
        "component": {
            "location_type": "region",
            "metric": "Market Share",
            "unit": "%",
            "data": map_data,
            "source": "Example Research",
            "source_url": "https://example.com"
        }
    })

    assert result["content"]["location_type"] == "region"
    assert result["content"]["metric"] == "Market Share"
    assert result["content"]["unit"] == "%"
    assert result["content"]["data"] == map_data


# ============================================================
# ANALYSIS
# ============================================================

def test_analysis_slide(builder):

    kpis = [
        {
            "name": "Growth",
            "value": 32,
            "unit": "%"
        }
    ]

    charts = [
        {
            "type": "line",
            "data": [],
            "source": "Research A",
            "source_url": "https://a.com"
        }
    ]

    tables = [
        {
            "columns": ["A"],
            "rows": [["B"]],
            "source": "Research B",
            "source_url": "https://b.com"
        }
    ]

    maps = [
        {
            "location_type": "region",
            "metric": "Share",
            "unit": "%",
            "data": [],
            "source": "Research C",
            "source_url": "https://c.com"
        }
    ]

    result = builder.build_slide({
        "slide_number": 8,
        "slide_type": "analysis",
        "title": "Market Analysis",
        "components": {
            "kpis": kpis,
            "charts": charts,
            "tables": tables,
            "maps": maps
        }
    })

    assert result["content"]["kpis"] == kpis
    assert result["content"]["charts"] == charts
    assert result["content"]["tables"] == tables
    assert result["content"]["maps"] == maps

    assert len(result["sources"]) == 3


# ============================================================
# SOURCE SLIDE
# ============================================================

def test_sources_slide(builder):

    sources = [
        {
            "source": "Research A",
            "source_url": "https://a.com"
        },
        {
            "source": "Research B",
            "source_url": "https://b.com"
        }
    ]

    result = builder.build_slide({
        "slide_number": 9,
        "slide_type": "sources",
        "title": "Sources",
        "sources": sources
    })

    assert result["content"]["sources"] == sources
    assert result["sources"] == sources


# ============================================================
# SOURCE EXTRACTION
# ============================================================

def test_component_without_source(builder):

    result = builder.build_slide({
        "slide_number": 10,
        "slide_type": "kpi",
        "title": "Market Size",
        "component": {
            "name": "Market Size",
            "value": 120,
            "unit": "Billion USD"
        }
    })

    assert result["sources"] == []


def test_source_with_only_url(builder):

    result = builder.build_slide({
        "slide_number": 11,
        "slide_type": "kpi",
        "title": "Market Size",
        "component": {
            "name": "Market Size",
            "value": 120,
            "unit": "Billion USD",
            "source_url": "https://example.com"
        }
    })

    assert result["sources"] == [
        {
            "source": None,
            "source_url": "https://example.com"
        }
    ]


# ============================================================
# DUPLICATE SOURCE REMOVAL
# ============================================================

def test_duplicate_sources_are_removed(builder):

    same_source = {
        "source": "Example Research",
        "source_url": "https://example.com"
    }

    result = builder.build_slide({
        "slide_number": 12,
        "slide_type": "analysis",
        "title": "Analysis",
        "components": {
            "kpis": [
                {
                    "name": "Growth",
                    "value": 30,
                    **same_source
                }
            ],
            "charts": [
                {
                    "type": "line",
                    "data": [],
                    **same_source
                }
            ]
        }
    })

    assert len(result["sources"]) == 1


# ============================================================
# PRESENTATION BUILDING
# ============================================================

def test_empty_slide_plans(builder):

    with pytest.raises(
        ValueError,
        match="Slide plans cannot be empty"
    ):
        builder.build_presentation([])


def test_build_presentation(builder):

    slide_plans = [
        {
            "slide_number": 1,
            "slide_type": "title",
            "title": "Indian EV Market",
            "description": "Market introduction."
        },
        {
            "slide_number": 2,
            "slide_type": "overview",
            "title": "Overview",
            "description": "Market overview."
        },
        {
            "slide_number": 3,
            "slide_type": "sources",
            "title": "Sources",
            "sources": [
                {
                    "source": "Example Research",
                    "source_url": "https://example.com"
                }
            ]
        }
    ]

    result = builder.build_presentation(slide_plans)

    assert result["type"] == "presentation_specification"
    assert result["slide_count"] == 3
    assert len(result["slides"]) == 3

    assert result["slides"][0]["slide_type"] == "title"
    assert result["slides"][1]["slide_type"] == "overview"
    assert result["slides"][2]["slide_type"] == "sources"


# ============================================================
# ALL SUPPORTED SLIDE TYPES
# ============================================================

@pytest.mark.parametrize(
    "slide_type",
    [
        "title",
        "executive_summary",
        "overview",
        "kpi",
        "chart",
        "table",
        "map",
        "analysis",
        "sources",
    ]
)
def test_all_supported_slide_types(builder, slide_type):

    slide_plan = {
        "slide_number": 1,
        "slide_type": slide_type,
        "title": "Test Slide"
    }

    result = builder.build_slide(slide_plan)

    assert result["slide_type"] == slide_type
    assert result["title"] == "Test Slide"
    assert "content" in result
    assert "sources" in result