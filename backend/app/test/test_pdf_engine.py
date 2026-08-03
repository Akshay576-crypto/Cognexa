from pathlib import Path

from pypdf import PdfReader

from app.presentations.pdf_engine import PDFEngine


def create_presentation_spec():

    return {
        "type": "presentation_specification",
        "title": "Indian Electric Vehicle Market",
        "slides": [
            {
                "slide_number": 1,
                "slide_type": "title",
                "title": "Indian Electric Vehicle Market",
                "content": {
                    "subtitle": (
                        "EV market intelligence presentation."
                    )
                },
                "sources": [],
            },
            {
                "slide_number": 2,
                "slide_type": "overview",
                "title": "Market Overview",
                "content": {
                    "description": (
                        "Indian EV market analysis."
                    )
                },
                "sources": [],
            },
            {
                "slide_number": 3,
                "slide_type": "kpi",
                "title": "Market Growth",
                "content": {
                    "name": "Market Growth",
                    "value": 32.5,
                    "unit": "%",
                },
                "sources": [
                    {
                        "source": "Example Research",
                        "source_url": "https://example.com",
                    }
                ],
            },
            {
                "slide_number": 4,
                "slide_type": "chart",
                "title": "EV Market Growth",
                "content": {
                    "chart_type": "line",
                    "data": [
                        {
                            "period": 2023,
                            "value": 100,
                        },
                        {
                            "period": 2024,
                            "value": 130,
                        },
                    ],
                },
                "sources": [
                    {
                        "source": "Example Research",
                        "source_url": "https://example.com",
                    }
                ],
            },
            {
                "slide_number": 5,
                "slide_type": "table",
                "title": "Top EV Companies",
                "content": {
                    "columns": [
                        "Company",
                        "Market Share",
                    ],
                    "rows": [
                        ["Company A", 35],
                        ["Company B", 28],
                    ],
                },
                "sources": [],
            },
            {
                "slide_number": 6,
                "slide_type": "map",
                "title": "EV Market Share by State",
                "content": {
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
                "slide_number": 7,
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
                "slide_number": 8,
                "slide_type": "sources",
                "title": "Sources & References",
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


def test_pdf_generation():

    engine = PDFEngine()

    output_path = (
        "generated/test_ev_market.pdf"
    )

    result = engine.generate(
        presentation_spec=create_presentation_spec(),
        output_path=output_path,
    )

    assert result["type"] == "pdf"
    assert result["slide_count"] == 8
    assert result["theme_id"] == (
        "cognexa_aurora"
    )

    file_path = Path(output_path)

    assert file_path.exists()
    assert file_path.stat().st_size > 0

    reader = PdfReader(
        str(file_path)
    )

    assert len(reader.pages) == 8

    print("\nPDF GENERATION TEST PASSED")
    print(result)


def test_custom_pdf_theme():

    engine = PDFEngine()

    output_path = (
        "generated/test_custom_pdf.pdf"
    )

    result = engine.generate(
        presentation_spec=create_presentation_spec(),
        output_path=output_path,
        theme_id="light_professional",
    )

    assert result["type"] == "pdf"
    assert result["theme_id"] == (
        "light_professional"
    )

    file_path = Path(output_path)

    assert file_path.exists()
    assert file_path.stat().st_size > 0

    reader = PdfReader(
        str(file_path)
    )

    assert len(reader.pages) == 8

    print("\nCUSTOM PDF THEME TEST PASSED")


def test_invalid_spec():

    engine = PDFEngine()

    try:

        engine.generate(
            presentation_spec={},
            output_path="generated/invalid.pdf",
        )

        assert False, "Expected ValueError"

    except ValueError:

        pass

    print("\nPDF VALIDATION TEST PASSED")


def test_invalid_theme():

    engine = PDFEngine()

    try:

        engine.generate(
            presentation_spec=create_presentation_spec(),
            output_path="generated/invalid_theme.pdf",
            theme_id="unknown_theme",
        )

        assert False, "Expected ValueError"

    except ValueError:

        pass

    print("\nPDF THEME VALIDATION TEST PASSED")


if __name__ == "__main__":

    test_pdf_generation()
    test_custom_pdf_theme()
    test_invalid_spec()
    test_invalid_theme()

    print("\nALL PDF ENGINE TESTS PASSED")
