
from pathlib import Path
from typing import Any, Dict, List, Optional

from pptx import Presentation
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches, Pt

from app.presentations.theme_engine import (
    PresentationThemeEngine,
)


class PPTEngine:
    """
    Deterministic PowerPoint generation engine.

    Converts a presentation specification into a .pptx file.

    Responsibilities:
    - Create PowerPoint presentation
    - Apply presentation theme
    - Build supported slide types
    - Preserve source attribution

    Does NOT:
    - Perform research
    - Perform LLM reasoning
    - Plan slides
    """

    def __init__(
        self,
        theme_engine: Optional[
            PresentationThemeEngine
        ] = None,
    ):
        self.theme_engine = (
            theme_engine
            or PresentationThemeEngine()
        )

    def generate(
        self,
        presentation_spec: Dict[str, Any],
        output_path: str,
        theme_id: str = "cognexa_aurora",
    ) -> Dict[str, Any]:

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

        theme = self.theme_engine.get_theme(
            theme_id
        )

        output = Path(output_path)

        output.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        prs = Presentation()

        # Remove the default blank slide.
        if len(prs.slides) > 0:
            slide_id = prs.slides._sldIdLst[0]
            prs.part.drop_rel(
                slide_id.rId
            )
            del prs.slides._sldIdLst[0]

        for slide_spec in slides:

            self._add_slide(
                prs,
                slide_spec,
                theme,
            )

        prs.save(output)

        return {
            "type": "pptx",
            "title": presentation_spec.get(
                "title"
            ),
            "slide_count": len(prs.slides),
            "output_path": str(output),
            "theme_id": theme["theme_id"],
        }

    def _add_slide(
        self,
        prs: Presentation,
        slide_spec: Dict[str, Any],
        theme: Dict[str, Any],
    ) -> None:

        slide_type = slide_spec.get(
            "slide_type"
        )

        layout = prs.slide_layouts[6]

        slide = prs.slides.add_slide(layout)

        self._apply_background(
            slide,
            theme,
        )

        if slide_type == "title":
            self._build_title_slide(
                slide,
                slide_spec,
                theme,
            )

        elif slide_type == "executive_summary":
            self._build_executive_summary_slide(
                slide,
                slide_spec,
                theme,
            )

        elif slide_type == "overview":
            self._build_overview_slide(
                slide,
                slide_spec,
                theme,
            )

        elif slide_type == "kpi":
            self._build_kpi_slide(
                slide,
                slide_spec,
                theme,
            )

        elif slide_type == "chart":
            self._build_chart_slide(
                slide,
                slide_spec,
                theme,
            )

        elif slide_type == "table":
            self._build_table_slide(
                slide,
                slide_spec,
                theme,
            )

        elif slide_type == "map":
            self._build_map_slide(
                slide,
                slide_spec,
                theme,
            )

        elif slide_type == "analysis":
            self._build_analysis_slide(
                slide,
                slide_spec,
                theme,
            )

        elif slide_type == "sources":
            self._build_sources_slide(
                slide,
                slide_spec,
                theme,
            )

        else:
            raise ValueError(
                f"Unsupported slide type: {slide_type}"
            )

    def _apply_background(
        self,
        slide,
        theme: Dict[str, Any],
    ) -> None:

        fill = slide.background.fill

        fill.solid()

        fill.fore_color.rgb = self._hex_to_rgb(
            theme["background"]
        )

    def _add_title(
        self,
        slide,
        title: str,
        theme: Dict[str, Any],
        top: float = 0.45,
        height: float = 0.7,
    ) -> None:

        shape = slide.shapes.add_textbox(
            Inches(0.6),
            Inches(top),
            Inches(12.1),
            Inches(height),
        )

        text_frame = shape.text_frame

        text_frame.clear()

        paragraph = text_frame.paragraphs[0]

        paragraph.text = title

        paragraph.alignment = PP_ALIGN.LEFT

        run = paragraph.runs[0]

        run.font.name = theme[
            "heading_font"
        ]

        run.font.size = Pt(
            theme["title_size"]
        )

        run.font.bold = True

        run.font.color.rgb = (
            self._hex_to_rgb(
                theme["text"]
            )
        )

    def _add_body_text(
        self,
        slide,
        text: str,
        theme: Dict[str, Any],
        left: float = 0.8,
        top: float = 1.5,
        width: float = 11.5,
        height: float = 4.5,
        font_size: Optional[int] = None,
    ) -> None:

        shape = slide.shapes.add_textbox(
            Inches(left),
            Inches(top),
            Inches(width),
            Inches(height),
        )

        frame = shape.text_frame

        frame.clear()

        paragraph = frame.paragraphs[0]

        paragraph.text = str(text)

        run = paragraph.runs[0]

        run.font.name = theme[
            "font_family"
        ]

        run.font.size = Pt(
            font_size
            or theme["body_size"]
        )

        run.font.color.rgb = (
            self._hex_to_rgb(
                theme["text"]
            )
        )

    def _build_title_slide(
        self,
        slide,
        spec: Dict[str, Any],
        theme: Dict[str, Any],
    ) -> None:

        self._add_title(
            slide,
            spec["title"],
            theme,
            top=2.3,
            height=1.0,
        )

        subtitle = (
            spec.get("content", {})
            .get("subtitle")
        )

        if subtitle:

            self._add_body_text(
                slide,
                subtitle,
                theme,
                left=0.8,
                top=3.4,
                width=11.5,
                height=1.0,
            )

    def _build_executive_summary_slide(
        self,
        slide,
        spec: Dict[str, Any],
        theme: Dict[str, Any],
    ) -> None:

        self._add_title(
            slide,
            spec["title"],
            theme,
        )

        kpis = (
            spec.get("content", {})
            .get("kpis", [])
        )

        lines = []

        for kpi in kpis:

            lines.append(
                f'{kpi.get("name", "KPI")}: '
                f'{kpi.get("value", "")} '
                f'{kpi.get("unit", "")}'
            )

        self._add_body_text(
            slide,
            "\n".join(lines),
            theme,
        )

        self._add_sources(
            slide,
            spec.get("sources", []),
            theme,
        )

    def _build_overview_slide(
        self,
        slide,
        spec: Dict[str, Any],
        theme: Dict[str, Any],
    ) -> None:

        self._add_title(
            slide,
            spec["title"],
            theme,
        )

        description = (
            spec.get("content", {})
            .get("description")
            or ""
        )

        self._add_body_text(
            slide,
            description,
            theme,
        )

    def _build_kpi_slide(
        self,
        slide,
        spec: Dict[str, Any],
        theme: Dict[str, Any],
    ) -> None:

        self._add_title(
            slide,
            spec["title"],
            theme,
        )

        content = spec.get(
            "content",
            {},
        )

        value = content.get(
            "value",
            "",
        )

        unit = content.get(
            "unit",
            "",
        )

        text = f"{value} {unit}".strip()

        self._add_body_text(
            slide,
            text,
            theme,
            top=2.2,
            height=1.5,
            font_size=32,
        )

        self._add_sources(
            slide,
            spec.get("sources", []),
            theme,
        )

    def _build_chart_slide(
        self,
        slide,
        spec: Dict[str, Any],
        theme: Dict[str, Any],
    ) -> None:

        self._add_title(
            slide,
            spec["title"],
            theme,
        )

        content = spec.get(
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

        text = (
            f"Chart Type: {chart_type}\n\n"
            f"Data Points: {len(data)}"
        )

        self._add_body_text(
            slide,
            text,
            theme,
        )

        self._add_sources(
            slide,
            spec.get("sources", []),
            theme,
        )

    def _build_table_slide(
        self,
        slide,
        spec: Dict[str, Any],
        theme: Dict[str, Any],
    ) -> None:

        self._add_title(
            slide,
            spec["title"],
            theme,
        )

        content = spec.get(
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

        text_lines = [
            " | ".join(
                str(column)
                for column in columns
            )
        ]

        for row in rows:

            text_lines.append(
                " | ".join(
                    str(value)
                    for value in row
                )
            )

        self._add_body_text(
            slide,
            "\n".join(text_lines),
            theme,
            font_size=14,
        )

        self._add_sources(
            slide,
            spec.get("sources", []),
            theme,
        )

    def _build_map_slide(
        self,
        slide,
        spec: Dict[str, Any],
        theme: Dict[str, Any],
    ) -> None:

        self._add_title(
            slide,
            spec["title"],
            theme,
        )

        content = spec.get(
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

        lines = [
            f"Metric: {metric} ({unit})",
            "",
        ]

        for item in data:

            location = item.get(
                "location",
                "Unknown",
            )

            value = item.get(
                "value",
                "",
            )

            lines.append(
                f"{location}: {value} {unit}"
            )

        self._add_body_text(
            slide,
            "\n".join(lines),
            theme,
        )

        self._add_sources(
            slide,
            spec.get("sources", []),
            theme,
        )

    def _build_analysis_slide(
        self,
        slide,
        spec: Dict[str, Any],
        theme: Dict[str, Any],
    ) -> None:

        self._add_title(
            slide,
            spec["title"],
            theme,
        )

        content = spec.get(
            "content",
            {},
        )

        summary = (
            f"KPIs: "
            f"{len(content.get('kpis', []))}\n"
            f"Charts: "
            f"{len(content.get('charts', []))}\n"
            f"Tables: "
            f"{len(content.get('tables', []))}\n"
            f"Maps: "
            f"{len(content.get('maps', []))}"
        )

        self._add_body_text(
            slide,
            summary,
            theme,
        )

        self._add_sources(
            slide,
            spec.get("sources", []),
            theme,
        )

    def _build_sources_slide(
        self,
        slide,
        spec: Dict[str, Any],
        theme: Dict[str, Any],
    ) -> None:

        self._add_title(
            slide,
            spec["title"],
            theme,
        )

        sources = spec.get(
            "content",
            {},
        ).get(
            "sources",
            [],
        )

        lines = []

        for source in sources:

            name = source.get(
                "source",
                "Unknown Source",
            )

            url = source.get(
                "source_url",
                "",
            )

            lines.append(
                f"{name} - {url}"
            )

        self._add_body_text(
            slide,
            "\n".join(lines),
            theme,
            font_size=12,
        )

    def _add_sources(
        self,
        slide,
        sources: List[Dict[str, Any]],
        theme: Dict[str, Any],
    ) -> None:

        if not sources:
            return

        names = []

        for source in sources:

            name = source.get(
                "source",
                "Unknown Source",
            )

            names.append(
                str(name)
            )

        self._add_body_text(
            slide,
            "Sources: " + ", ".join(names),
            theme,
            left=0.8,
            top=6.7,
            width=11.5,
            height=0.35,
            font_size=9,
        )

    @staticmethod
    def _hex_to_rgb(hex_color: str):

        from pptx.dml.color import RGBColor

        value = hex_color.replace(
            "#",
            "",
        )

        if len(value) != 6:
            raise ValueError(
                f"Invalid hex color: {hex_color}"
            )

        return RGBColor(
            int(value[0:2], 16),
            int(value[2:4], 16),
            int(value[4:6], 16),
        )

