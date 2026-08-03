from pathlib import Path
from typing import Any, Dict, List, Optional
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    BaseDocTemplate,
    PageBreak,
    Frame,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)

from app.presentations.pdf_theme_engine import (
    PDFThemeEngine,
)


class PDFEngine:
    """
    Deterministic PDF generation engine.

    Converts a presentation specification into a PDF document.

    Responsibilities:
    - Create PDF files
    - Apply PDF theme
    - Render supported slide/content types
    - Preserve source attribution

    Does NOT:
    - Perform research
    - Perform LLM reasoning
    - Plan presentation structure
    """

    PAGE_WIDTH, PAGE_HEIGHT = landscape(A4)

    def __init__(
        self,
        theme_engine: Optional[PDFThemeEngine] = None,
    ):
        self.theme_engine = (
            theme_engine
            or PDFThemeEngine()
        )

    def generate(
        self,
        presentation_spec: Dict[str, Any],
        output_path: str,
        theme_id: str = "cognexa_aurora",
    ) -> Dict[str, Any]:

        self._validate_spec(
            presentation_spec
        )

        theme = self.theme_engine.get_theme(
            theme_id
        )

        output = Path(output_path)

        output.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        document = BaseDocTemplate(
            str(output),
            pagesize=landscape(A4),
            leftMargin=0.55 * inch,
            rightMargin=0.55 * inch,
            topMargin=0.45 * inch,
            bottomMargin=0.45 * inch,
        )

        frame = Frame(
            document.leftMargin,
            document.bottomMargin,
            document.width,
            document.height,
            id="main_frame",
        )

        page_template = PageTemplate(
            id="cognexa_template",
            frames=[frame],
            onPage=lambda canvas, doc: (
                self._draw_page_background(
                    canvas,
                    doc,
                    theme,
                )
            ),
        )

        document.addPageTemplates(
            [page_template]
        )

        story = []

        slides = presentation_spec[
            "slides"
        ]

        for index, slide in enumerate(
            slides
        ):

            story.extend(
                self._build_slide(
                    slide,
                    theme,
                )
            )

            if index < len(slides) - 1:
                story.append(PageBreak())

        document.build(story)

        return {
            "type": "pdf",
            "title": presentation_spec.get(
                "title"
            ),
            "slide_count": len(slides),
            "output_path": str(output),
            "theme_id": theme["theme_id"],
        }

    def _validate_spec(
        self,
        presentation_spec: Dict[str, Any],
    ) -> None:

        if not presentation_spec:
            raise ValueError(
                "Presentation specification cannot be empty."
            )

        if presentation_spec.get("type") != (
            "presentation_specification"
        ):
            raise ValueError(
                "Invalid presentation specification."
            )

        slides = presentation_spec.get(
            "slides",
            [],
        )

        if not slides:
            raise ValueError(
                "Presentation must contain slides."
            )

    def _build_slide(
        self,
        slide: Dict[str, Any],
        theme: Dict[str, Any],
    ) -> List[Any]:

        slide_type = slide.get(
            "slide_type"
        )

        if not slide_type:
            raise ValueError(
                "Slide type is required."
            )

        builder = getattr(
            self,
            f"_build_{slide_type}_slide",
            None,
        )

        if builder is None:
            raise ValueError(
                f"Unsupported slide type: {slide_type}"
            )

        return builder(
            slide,
            theme,
        )

    def _build_title_slide(
        self,
        slide: Dict[str, Any],
        theme: Dict[str, Any],
    ) -> List[Any]:

        content = slide.get(
            "content",
            {},
        )

        elements = []

        elements.append(
            Spacer(
                1,
                1.55 * inch,
            )
        )

        elements.append(
            Paragraph(
                slide["title"],
                self._title_style(
                    theme,
                    center=True,
                    size=30,
                ),
            )
        )

        subtitle = content.get(
            "subtitle"
        )

        if subtitle:

            elements.append(
                Spacer(
                    1,
                    0.25 * inch,
                )
            )

            elements.append(
                Paragraph(
                    str(subtitle),
                    self._body_style(
                        theme,
                        center=True,
                        size=14,
                    ),
                )
            )

        return elements

    def _build_executive_summary_slide(
        self,
        slide: Dict[str, Any],
        theme: Dict[str, Any],
    ) -> List[Any]:

        elements = self._title_block(
            slide["title"],
            theme,
        )

        kpis = slide.get(
            "content",
            {},
        ).get(
            "kpis",
            [],
        )

        if kpis:

            data = [
                [
                    str(kpi.get("name", "")),
                    str(kpi.get("value", "")),
                    str(kpi.get("unit", "")),
                ]
                for kpi in kpis
            ]

            table = Table(
                data,
                colWidths=[
                    3.5 * inch,
                    2.0 * inch,
                    2.0 * inch,
                ],
            )

            self._style_table(
                table,
                theme,
            )

            elements.append(table)

        elements.extend(
            self._source_block(
                slide.get("sources", []),
                theme,
            )
        )

        return elements

    def _build_overview_slide(
        self,
        slide: Dict[str, Any],
        theme: Dict[str, Any],
    ) -> List[Any]:

        elements = self._title_block(
            slide["title"],
            theme,
        )

        description = (
            slide.get(
                "content",
                {},
            ).get(
                "description",
                "",
            )
        )

        elements.append(
            Paragraph(
                str(description),
                self._body_style(theme),
            )
        )

        return elements

    def _build_kpi_slide(
        self,
        slide: Dict[str, Any],
        theme: Dict[str, Any],
    ) -> List[Any]:

        elements = self._title_block(
            slide["title"],
            theme,
        )

        content = slide.get(
            "content",
            {},
        )

        name = content.get(
            "name",
            "",
        )

        value = content.get(
            "value",
            "",
        )

        unit = content.get(
            "unit",
            "",
        )

        kpi_table = Table(
            [
                [
                    Paragraph(
                        str(name),
                        self._heading_style(
                            theme,
                            center=True,
                        ),
                    )
                ],
                [
                    Paragraph(
                        f"{value} {unit}".strip(),
                        self._kpi_style(theme),
                    )
                ],
            ],
            colWidths=[6.5 * inch],
        )

        kpi_table.setStyle(
            TableStyle(
                [
                    (
                        "BACKGROUND",
                        (0, 0),
                        (-1, -1),
                        self._color(
                            theme["surface"]
                        ),
                    ),
                    (
                        "BOX",
                        (0, 0),
                        (-1, -1),
                        1,
                        self._color(
                            theme["border"]
                        ),
                    ),
                    (
                        "VALIGN",
                        (0, 0),
                        (-1, -1),
                        "MIDDLE",
                    ),
                    (
                        "ALIGN",
                        (0, 0),
                        (-1, -1),
                        "CENTER",
                    ),
                    (
                        "TOPPADDING",
                        (0, 0),
                        (-1, -1),
                        20,
                    ),
                    (
                        "BOTTOMPADDING",
                        (0, 0),
                        (-1, -1),
                        20,
                    ),
                ]
            )
        )

        elements.append(kpi_table)

        elements.extend(
            self._source_block(
                slide.get("sources", []),
                theme,
            )
        )

        return elements

    def _build_chart_slide(
        self,
        slide: Dict[str, Any],
        theme: Dict[str, Any],
    ) -> List[Any]:

        elements = self._title_block(
            slide["title"],
            theme,
        )

        content = slide.get(
            "content",
            {},
        )

        chart_type = content.get(
            "chart_type",
            "unknown",
        )

        data = content.get(
            "data",
            [],
        )

        elements.append(
            Paragraph(
                f"Chart Type: {chart_type}",
                self._heading_style(theme),
            )
        )

        elements.append(
            Spacer(1, 0.15 * inch)
        )

        if data:

            table_data = [
                ["#", "Data"]
            ]

            for index, item in enumerate(
                data,
                start=1,
            ):

                table_data.append(
                    [
                        str(index),
                        str(item),
                    ]
                )

            table = Table(
                table_data,
                colWidths=[
                    0.5 * inch,
                    9.5 * inch,
                ],
            )

            self._style_table(
                table,
                theme,
            )

            elements.append(table)

        elements.extend(
            self._source_block(
                slide.get("sources", []),
                theme,
            )
        )

        return elements

    def _build_table_slide(
        self,
        slide: Dict[str, Any],
        theme: Dict[str, Any],
    ) -> List[Any]:

        elements = self._title_block(
            slide["title"],
            theme,
        )

        content = slide.get(
            "content",
            {},
        )

        columns = content.get(
            "columns",
            [],
        )

        rows = content.get(
            "rows",
            [],
        )

        table_data = [
            [str(column) for column in columns]
        ]

        table_data.extend(
            [
                [
                    str(value)
                    for value in row
                ]
                for row in rows
            ]
        )

        if table_data:

            column_count = len(
                table_data[0]
            )

            width = (
                10.2 * inch
                / max(column_count, 1)
            )

            table = Table(
                table_data,
                colWidths=[
                    width
                    for _ in range(
                        column_count
                    )
                ],
                repeatRows=1,
            )

            self._style_table(
                table,
                theme,
            )

            elements.append(table)

        elements.extend(
            self._source_block(
                slide.get("sources", []),
                theme,
            )
        )

        return elements

    def _build_map_slide(
        self,
        slide: Dict[str, Any],
        theme: Dict[str, Any],
    ) -> List[Any]:

        elements = self._title_block(
            slide["title"],
            theme,
        )

        content = slide.get(
            "content",
            {},
        )

        metric = content.get(
            "metric",
            "",
        )

        unit = content.get(
            "unit",
            "",
        )

        data = content.get(
            "data",
            [],
        )

        elements.append(
            Paragraph(
                f"Metric: {metric} ({unit})",
                self._heading_style(theme),
            )
        )

        elements.append(
            Spacer(1, 0.15 * inch)
        )

        table_data = [
            [
                "Location",
                "Value",
            ]
        ]

        for item in data:

            table_data.append(
                [
                    str(
                        item.get(
                            "location",
                            "Unknown",
                        )
                    ),
                    f'{item.get("value", "")} {unit}'.strip(),
                ]
            )

        table = Table(
            table_data,
            colWidths=[
                4.0 * inch,
                2.0 * inch,
            ],
            repeatRows=1,
        )

        self._style_table(
            table,
            theme,
        )

        elements.append(table)

        elements.extend(
            self._source_block(
                slide.get("sources", []),
                theme,
            )
        )

        return elements

    def _build_analysis_slide(
        self,
        slide: Dict[str, Any],
        theme: Dict[str, Any],
    ) -> List[Any]:

        elements = self._title_block(
            slide["title"],
            theme,
        )

        content = slide.get(
            "content",
            {},
        )

        data = [
            [
                "Component",
                "Count",
            ],
            [
                "KPIs",
                len(
                    content.get(
                        "kpis",
                        [],
                    )
                ),
            ],
            [
                "Charts",
                len(
                    content.get(
                        "charts",
                        [],
                    )
                ),
            ],
            [
                "Tables",
                len(
                    content.get(
                        "tables",
                        [],
                    )
                ),
            ],
            [
                "Maps",
                len(
                    content.get(
                        "maps",
                        [],
                    )
                ),
            ],
        ]

        table = Table(
            data,
            colWidths=[
                4.0 * inch,
                2.0 * inch,
            ],
            repeatRows=1,
        )

        self._style_table(
            table,
            theme,
        )

        elements.append(table)

        elements.extend(
            self._source_block(
                slide.get("sources", []),
                theme,
            )
        )

        return elements

    def _build_sources_slide(
        self,
        slide: Dict[str, Any],
        theme: Dict[str, Any],
    ) -> List[Any]:

        elements = self._title_block(
            slide["title"],
            theme,
        )

        sources = (
            slide.get(
                "content",
                {},
            ).get(
                "sources",
                [],
            )
        )

        for source in sources:

            name = source.get(
                "source",
                "Unknown Source",
            )

            url = source.get(
                "source_url",
                "",
            )

            text = str(name)

            if url:
                text += f" — {url}"

            elements.append(
                Paragraph(
                    text,
                    self._body_style(theme),
                )
            )

            elements.append(
                Spacer(
                    1,
                    0.08 * inch,
                )
            )

        return elements

    def _title_block(
        self,
        title: str,
        theme: Dict[str, Any],
    ) -> List[Any]:

        return [
            Paragraph(
                str(title),
                self._title_style(theme),
            ),
            Spacer(
                1,
                0.22 * inch,
            ),
        ]

    def _source_block(
        self,
        sources: List[Dict[str, Any]],
        theme: Dict[str, Any],
    ) -> List[Any]:

        if not sources:
            return []

        names = []

        for source in sources:

            name = source.get(
                "source",
                "Unknown Source",
            )

            url = source.get(
                "source_url",
                "",
            )

            if url:
                names.append(
                    f"{name} — {url}"
                )
            else:
                names.append(
                    str(name)
                )

        return [
            Spacer(
                1,
                0.25 * inch,
            ),
            Paragraph(
                "Sources: "
                + "; ".join(names),
                self._small_style(theme),
            ),
        ]

    def _style_table(
        self,
        table: Table,
        theme: Dict[str, Any],
    ) -> None:

        table.setStyle(
            TableStyle(
                [
                    (
                        "BACKGROUND",
                        (0, 0),
                        (-1, 0),
                        self._color(
                            theme["primary"]
                        ),
                    ),
                    (
                        "TEXTCOLOR",
                        (0, 0),
                        (-1, 0),
                        self._color(
                            theme["background"]
                        ),
                    ),
                    (
                        "BACKGROUND",
                        (0, 1),
                        (-1, -1),
                        self._color(
                            theme["surface"]
                        ),
                    ),
                    (
                        "TEXTCOLOR",
                        (0, 1),
                        (-1, -1),
                        self._color(
                            theme["text"]
                        ),
                    ),
                    (
                        "GRID",
                        (0, 0),
                        (-1, -1),
                        0.5,
                        self._color(
                            theme["border"]
                        ),
                    ),
                    (
                        "FONTNAME",
                        (0, 0),
                        (-1, -1),
                        theme["font_family"],
                    ),
                    (
                        "FONTSIZE",
                        (0, 0),
                        (-1, -1),
                        theme["body_size"],
                    ),
                    (
                        "VALIGN",
                        (0, 0),
                        (-1, -1),
                        "MIDDLE",
                    ),
                    (
                        "TOPPADDING",
                        (0, 0),
                        (-1, -1),
                        7,
                    ),
                    (
                        "BOTTOMPADDING",
                        (0, 0),
                        (-1, -1),
                        7,
                    ),
                ]
            )
        )

    def _draw_page_background(
        self,
        canvas,
        document,
        theme: Dict[str, Any],
    ) -> None:

        canvas.saveState()

        canvas.setFillColor(
            self._color(
                theme["background"]
            )
        )

        canvas.rect(
            0,
            0,
            self.PAGE_WIDTH,
            self.PAGE_HEIGHT,
            stroke=0,
            fill=1,
        )

        canvas.restoreState()

    def _title_style(
        self,
        theme: Dict[str, Any],
        center: bool = False,
        size: Optional[int] = None,
    ) -> ParagraphStyle:

        return ParagraphStyle(
            "CognexaTitle",
            fontName=theme["font_family"],
            fontSize=(
                size
                or theme["title_size"]
            ),
            leading=(
                (size or theme["title_size"])
                * 1.2
            ),
            textColor=self._color(
                theme["text"]
            ),
            alignment=(
                TA_CENTER
                if center
                else TA_LEFT
            ),
            spaceAfter=8,
        )

    def _heading_style(
        self,
        theme: Dict[str, Any],
        center: bool = False,
    ) -> ParagraphStyle:

        return ParagraphStyle(
            "CognexaHeading",
            fontName=theme["font_family"],
            fontSize=theme["heading_size"],
            leading=theme["heading_size"] * 1.2,
            textColor=self._color(
                theme["text"]
            ),
            alignment=(
                TA_CENTER
                if center
                else TA_LEFT
            ),
        )

    def _body_style(
        self,
        theme: Dict[str, Any],
        center: bool = False,
        size: Optional[int] = None,
    ) -> ParagraphStyle:

        return ParagraphStyle(
            "CognexaBody",
            fontName=theme["font_family"],
            fontSize=(
                size
                or theme["body_size"]
            ),
            leading=(
                (size or theme["body_size"])
                * 1.35
            ),
            textColor=self._color(
                theme["text"]
            ),
            alignment=(
                TA_CENTER
                if center
                else TA_LEFT
            ),
        )

    def _kpi_style(
        self,
        theme: Dict[str, Any],
    ) -> ParagraphStyle:

        return ParagraphStyle(
            "CognexaKPI",
            fontName=theme["font_family"],
            fontSize=32,
            leading=38,
            textColor=self._color(
                theme["accent"]
            ),
            alignment=TA_CENTER,
        )

    def _small_style(
        self,
        theme: Dict[str, Any],
    ) -> ParagraphStyle:

        return ParagraphStyle(
            "CognexaSmall",
            fontName=theme["font_family"],
            fontSize=theme["small_size"],
            leading=theme["small_size"] * 1.3,
            textColor=self._color(
                theme["muted_text"]
            ),
        )

    @staticmethod
    def _color(hex_color: str):

        value = hex_color.replace(
            "#",
            "",
        )

        if len(value) != 6:
            raise ValueError(
                f"Invalid hex color: {hex_color}"
            )

        return colors.HexColor(
            f"#{value}"
        )


