from pathlib import Path

import pytest
from pptx import Presentation

from app.presentations.ppt_engine import PPTEngine


def create_presentation_spec():

    return {
        "type": "presentation_specification",
        "title": "Indian Electric Vehicle Market",
        "slide_count": 9,
        "slides": [
            {
                "slide_number": 1,
                "slide_type": "title",
                "title": "Indian Electric Vehicle Market",
                "content": {
                    "subtitle": "Market Intelligence Report"
                },
                "sources": [],
            },
            {
                "slide_number": 2,
                "slide_type": "executive_summary",
                "title": "Executive Summary",
                "content": {
                    "kpis": [
                        {
                            "name": "Market Growth",
                            "value": 32.5,
                            "unit": "%",
                        }
                    ]
                },
                "sources": [
                    {
                        "source": "Example Research",
                        "source_url": "https://example.com",
                    }
                ],
            },
            {
                "slide_number": 3,
                "slide_type": "overview",
                "title": "Market Overview",
                "content": {
                    "description": "Indian EV market overview."
                },
                "sources": [],
            },
            {
                "slide_number": 4,
                "slide_type": "kpi",
                "title": "Market Growth",
                "content": {
                    "name": "Growth",
                    "value": 32.5,
                    "unit": "%",
                },
                "sources": [],
            },
            {
                "slide_number": 5,
                "slide_type": "chart",
                "title": "EV Market Growth",
                "content": {
                    "chart_type": "line",
                    "data": [
                        {"period": 2023, "value": 100},
                        {"period": 2024, "value": 130},
                    ],
                },
                "sources": [],
            },
            {
                "slide_number": 6,
                "slide_type": "table",
                "title": "Company Comparison",
                "content": {
                    "columns": ["Company", "Share"],
                    "rows": [
                        ["Company A", 35],
                        ["Company B", 28],
                    ],
                },
                "sources": [],
            },
            {
                "slide_number": 7,
                "slide_type": "map",
                "title": "Regional Market Share",
                "content": {
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
                },
                "sources": [],
            },
            {
                "slide_number": 8,
                "slide_type": "analysis",
                "title": "Market Analysis",
                "content": {
                    "kpis": [{}],
                    "charts": [{}],
                    "tables": [{}],
                    "maps": [{}],
                },
                "sources": [],
            },
            {
                "slide_number": 9,
                "slide_type": "sources",
                "title": "Sources",
                "content": {
                    "sources": [
                        {
                            "source": "Example Research",
                            "source_url": "https://example.com",
                        }
                    ]
                },
                "sources": [],
            },
        ],
    }


def test_ppt_generation(tmp_path):

    engine = PPTEngine()

    output_path = tmp_path / "test_presentation.pptx"

    result = engine.generate(
        presentation_spec=create_presentation_spec(),
        output_path=str(output_path),
    )

    assert result["type"] == "pptx"

    assert result["title"] == (
        "Indian Electric Vehicle Market"
    )

    assert result["slide_count"] == 9

    assert result["theme_id"] == "cognexa_aurora"

    assert output_path.exists()

    assert output_path.is_file()


def test_generated_pptx_is_valid(tmp_path):

    engine = PPTEngine()

    output_path = tmp_path / "valid_presentation.pptx"

    engine.generate(
        presentation_spec=create_presentation_spec(),
        output_path=str(output_path),
    )

    presentation = Presentation(
        str(output_path)
    )

    assert len(presentation.slides) == 9


def test_custom_theme_generation(tmp_path):

    engine = PPTEngine()

    output_path = tmp_path / "custom_theme.pptx"

    result = engine.generate(
        presentation_spec=create_presentation_spec(),
        output_path=str(output_path),
        theme_id="executive_dark",
    )

    assert result["theme_id"] == "executive_dark"

    assert output_path.exists()


def test_empty_specification(tmp_path):

    engine = PPTEngine()

    with pytest.raises(ValueError):

        engine.generate(
            presentation_spec={},
            output_path=str(
                tmp_path / "test.pptx"
            ),
        )


def test_invalid_specification_type(tmp_path):

    engine = PPTEngine()

    specification = create_presentation_spec()

    specification["type"] = "invalid"

    with pytest.raises(ValueError):

        engine.generate(
            presentation_spec=specification,
            output_path=str(
                tmp_path / "test.pptx"
            ),
        )


def test_empty_slides(tmp_path):

    engine = PPTEngine()

    specification = {
        "type": "presentation_specification",
        "title": "Test",
        "slides": [],
    }

    with pytest.raises(ValueError):

        engine.generate(
            presentation_spec=specification,
            output_path=str(
                tmp_path / "test.pptx"
            ),
        )


def test_invalid_theme(tmp_path):

    engine = PPTEngine()

    with pytest.raises(ValueError):

        engine.generate(
            presentation_spec=create_presentation_spec(),
            output_path=str(
                tmp_path / "test.pptx"
            ),
            theme_id="does_not_exist",
        )


def test_unsupported_slide_type(tmp_path):

    engine = PPTEngine()

    specification = create_presentation_spec()

    specification["slides"] = [
        {
            "slide_number": 1,
            "slide_type": "unsupported",
            "title": "Invalid Slide",
        }
    ]

    with pytest.raises(ValueError):

        engine.generate(
            presentation_spec=specification,
            output_path=str(
                tmp_path / "test.pptx"
            ),
        )


def test_invalid_hex_color():

    engine = PPTEngine()

    with pytest.raises(ValueError):

        engine._hex_to_rgb("#12345")