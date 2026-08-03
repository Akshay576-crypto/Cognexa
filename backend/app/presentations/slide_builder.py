from typing import Any, Dict, List, Optional


class SlideBuilder:
    """
    Deterministic slide specification builder.

    Responsibilities:
    - Convert a planned slide into a structured slide specification.
    - Build title, KPI, chart, table, map, analysis, and source slides.
    - Preserve source attribution.

    Does NOT:
    - Create a .pptx file.
    - Render PowerPoint shapes.
    - Perform LLM reasoning.
    """

    SUPPORTED_SLIDE_TYPES = {
        "title",
        "executive_summary",
        "overview",
        "kpi",
        "chart",
        "table",
        "map",
        "analysis",
        "sources",
    }

    def build_slide(
        self,
        slide_plan: Dict[str, Any],
    ) -> Dict[str, Any]:

        if not slide_plan:
            raise ValueError("Slide plan cannot be empty.")

        slide_type = slide_plan.get("slide_type")

        if not slide_type:
            raise ValueError("Slide type is required.")

        if slide_type not in self.SUPPORTED_SLIDE_TYPES:
            raise ValueError(
                f"Unsupported slide type: {slide_type}"
            )

        title = slide_plan.get("title")

        if not title:
            raise ValueError("Slide title cannot be empty.")

        builder = getattr(
            self,
            f"_build_{slide_type}_slide",
            None,
        )

        if builder is None:
            raise ValueError(
                f"No builder available for: {slide_type}"
            )

        return builder(slide_plan)

    def build_presentation(
        self,
        slide_plans: List[Dict[str, Any]],
    ) -> Dict[str, Any]:

        if not slide_plans:
            raise ValueError(
                "Slide plans cannot be empty."
            )

        slides = []

        for slide_plan in slide_plans:

            slides.append(
                self.build_slide(slide_plan)
            )

        return {
            "type": "presentation_specification",
            "slide_count": len(slides),
            "slides": slides,
        }

    def _base_slide(
        self,
        slide_plan: Dict[str, Any],
        slide_type: str,
    ) -> Dict[str, Any]:

        return {
            "slide_number": slide_plan.get(
                "slide_number"
            ),
            "slide_type": slide_type,
            "title": slide_plan.get("title"),
            "purpose": slide_plan.get("purpose"),
            "content": {},
            "sources": [],
        }

    def _build_title_slide(
        self,
        slide_plan: Dict[str, Any],
    ) -> Dict[str, Any]:

        slide = self._base_slide(
            slide_plan,
            "title",
        )

        slide["content"] = {
            "subtitle": slide_plan.get(
                "description"
            ),
        }

        return slide

    def _build_executive_summary_slide(
        self,
        slide_plan: Dict[str, Any],
    ) -> Dict[str, Any]:

        slide = self._base_slide(
            slide_plan,
            "executive_summary",
        )

        components = slide_plan.get(
            "components",
            {},
        )

        slide["content"] = {
            "kpis": components.get("kpis", []),
        }

        slide["sources"] = components.get(
            "sources",
            [],
        )

        return slide

    def _build_overview_slide(
        self,
        slide_plan: Dict[str, Any],
    ) -> Dict[str, Any]:

        slide = self._base_slide(
            slide_plan,
            "overview",
        )

        slide["content"] = {
            "description": slide_plan.get(
                "description"
            ),
        }

        return slide

    def _build_kpi_slide(
        self,
        slide_plan: Dict[str, Any],
    ) -> Dict[str, Any]:

        slide = self._base_slide(
            slide_plan,
            "kpi",
        )

        kpi = slide_plan.get(
            "component",
            {},
        )

        slide["content"] = {
            "name": kpi.get("name"),
            "value": kpi.get("value"),
            "unit": kpi.get("unit"),
        }

        slide["sources"] = self._extract_source(
            kpi
        )

        return slide

    def _build_chart_slide(
        self,
        slide_plan: Dict[str, Any],
    ) -> Dict[str, Any]:

        slide = self._base_slide(
            slide_plan,
            "chart",
        )

        chart = slide_plan.get(
            "component",
            {},
        )

        slide["content"] = {
            "chart_type": chart.get("type"),
            "data": chart.get("data", []),
        }

        slide["sources"] = self._extract_source(
            chart
        )

        return slide

    def _build_table_slide(
        self,
        slide_plan: Dict[str, Any],
    ) -> Dict[str, Any]:

        slide = self._base_slide(
            slide_plan,
            "table",
        )

        table = slide_plan.get(
            "component",
            {},
        )

        slide["content"] = {
            "columns": table.get(
                "columns",
                [],
            ),
            "rows": table.get(
                "rows",
                [],
            ),
        }

        slide["sources"] = self._extract_source(
            table
        )

        return slide

    def _build_map_slide(
        self,
        slide_plan: Dict[str, Any],
    ) -> Dict[str, Any]:

        slide = self._base_slide(
            slide_plan,
            "map",
        )

        map_spec = slide_plan.get(
            "component",
            {},
        )

        slide["content"] = {
            "location_type": map_spec.get(
                "location_type"
            ),
            "metric": map_spec.get(
                "metric"
            ),
            "unit": map_spec.get(
                "unit"
            ),
            "data": map_spec.get(
                "data",
                [],
            ),
        }

        slide["sources"] = self._extract_source(
            map_spec
        )

        return slide

    def _build_analysis_slide(
        self,
        slide_plan: Dict[str, Any],
    ) -> Dict[str, Any]:

        slide = self._base_slide(
            slide_plan,
            "analysis",
        )

        components = slide_plan.get(
            "components",
            {},
        )

        slide["content"] = {
            "kpis": components.get(
                "kpis",
                [],
            ),
            "charts": components.get(
                "charts",
                [],
            ),
            "tables": components.get(
                "tables",
                [],
            ),
            "maps": components.get(
                "maps",
                [],
            ),
        }

        slide["sources"] = self._collect_sources(
            components
        )

        return slide

    def _build_sources_slide(
        self,
        slide_plan: Dict[str, Any],
    ) -> Dict[str, Any]:

        slide = self._base_slide(
            slide_plan,
            "sources",
        )

        sources = slide_plan.get(
            "sources",
            [],
        )

        slide["content"] = {
            "sources": sources,
        }

        slide["sources"] = sources

        return slide

    def _extract_source(
        self,
        component: Dict[str, Any],
    ) -> List[Dict[str, Optional[str]]]:

        source = component.get("source")
        source_url = component.get("source_url")

        if not source and not source_url:
            return []

        return [
            {
                "source": source,
                "source_url": source_url,
            }
        ]

    def _collect_sources(
        self,
        components: Dict[str, Any],
    ) -> List[Dict[str, Optional[str]]]:

        sources = []

        for component_type in (
            "kpis",
            "charts",
            "tables",
            "maps",
        ):

            for component in components.get(
                component_type,
                [],
            ):

                extracted = self._extract_source(
                    component
                )

                for source in extracted:

                    if source not in sources:
                        sources.append(source)

        return sources

