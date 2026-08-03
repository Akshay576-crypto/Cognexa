from typing import Any, Dict, List

class SlidePlanner:
    """
    Deterministic presentation slide planner.

    Responsibilities:
    - Convert structured dashboard/research data into a slide plan.
    - Decide slide sequence and purpose.
    - Preserve source attribution.

    Does NOT:
    - Render PowerPoint slides.
    - Generate images.
    - Perform LLM reasoning.
    """

    def create_plan(
        self,
        title: str,
        dashboard: Dict[str, Any],
        minimum_slides: int = 20,
    ) -> Dict[str, Any]:

        if not title:
            raise ValueError("Presentation title cannot be empty.")

        if not dashboard:
            raise ValueError("Dashboard data cannot be empty.")

        if minimum_slides <= 0:
            raise ValueError("Minimum slides must be greater than zero.")

        slides = []

        self._add_title_slide(slides, title)
        self._add_executive_summary(slides, dashboard)
        self._add_market_overview(slides, dashboard)
        self._add_kpi_slides(slides, dashboard)
        self._add_chart_slides(slides, dashboard)
        self._add_table_slides(slides, dashboard)
        self._add_map_slides(slides, dashboard)
        self._add_sources_slide(slides, dashboard)

        self._ensure_minimum_slides(
            slides,
            minimum_slides,
            dashboard,
        )

        self._number_slides(slides)

        return {
            "type": "presentation_plan",
            "title": title,
            "slide_count": len(slides),
            "slides": slides,
        }

    def _add_title_slide(
        self,
        slides: List[Dict[str, Any]],
        title: str,
    ) -> None:

        slides.append(
            {
                "slide_type": "title",
                "title": title,
                "purpose": "Introduce the presentation topic.",
            }
        )

    def _add_executive_summary(
        self,
        slides: List[Dict[str, Any]],
        dashboard: Dict[str, Any],
    ) -> None:

        slides.append(
            {
                "slide_type": "executive_summary",
                "title": "Executive Summary",
                "purpose": "Present the most important findings.",
                "components": {
                    "kpis": dashboard.get("kpis", [])[:4],
                    "sources": dashboard.get("sources", []),
                },
            }
        )

    def _add_market_overview(
        self,
        slides: List[Dict[str, Any]],
        dashboard: Dict[str, Any],
    ) -> None:

        slides.append(
            {
                "slide_type": "overview",
                "title": "Market Overview",
                "purpose": "Provide high-level context for the analysis.",
                "description": dashboard.get("description"),
            }
        )

    def _add_kpi_slides(
        self,
        slides: List[Dict[str, Any]],
        dashboard: Dict[str, Any],
    ) -> None:

        for index, kpi in enumerate(
            dashboard.get("kpis", [])
        ):

            slides.append(
                {
                    "slide_type": "kpi",
                    "title": kpi.get(
                        "name",
                        f"KPI {index + 1}",
                    ),
                    "purpose": "Highlight a key business metric.",
                    "component": kpi,
                }
            )

    def _add_chart_slides(
        self,
        slides: List[Dict[str, Any]],
        dashboard: Dict[str, Any],
    ) -> None:

        for index, chart in enumerate(
            dashboard.get("charts", [])
        ):

            slides.append(
                {
                    "slide_type": "chart",
                    "title": chart.get(
                        "title",
                        f"Chart {index + 1}",
                    ),
                    "purpose": "Present quantitative analysis visually.",
                    "component": chart,
                }
            )

    def _add_table_slides(
        self,
        slides: List[Dict[str, Any]],
        dashboard: Dict[str, Any],
    ) -> None:

        for index, table in enumerate(
            dashboard.get("tables", [])
        ):

            slides.append(
                {
                    "slide_type": "table",
                    "title": table.get(
                        "title",
                        f"Table {index + 1}",
                    ),
                    "purpose": "Present structured comparison data.",
                    "component": table,
                }
            )

    def _add_map_slides(
        self,
        slides: List[Dict[str, Any]],
        dashboard: Dict[str, Any],
    ) -> None:

        for index, map_spec in enumerate(
            dashboard.get("maps", [])
        ):

            slides.append(
                {
                    "slide_type": "map",
                    "title": map_spec.get(
                        "title",
                        f"Map {index + 1}",
                    ),
                    "purpose": "Present geographic analysis.",
                    "component": map_spec,
                }
            )

    def _add_sources_slide(
        self,
        slides: List[Dict[str, Any]],
        dashboard: Dict[str, Any],
    ) -> None:

        slides.append(
            {
                "slide_type": "sources",
                "title": "Sources & References",
                "purpose": "Provide research source attribution.",
                "sources": dashboard.get("sources", []),
            }
        )

    def _ensure_minimum_slides(
        self,
        slides: List[Dict[str, Any]],
        minimum_slides: int,
        dashboard: Dict[str, Any],
    ) -> None:

        existing_count = len(slides)

        if existing_count >= minimum_slides:
            return

        required = minimum_slides - existing_count

        for index in range(required):

            slides.insert(
                -1,
                {
                    "slide_type": "analysis",
                    "title": f"Additional Analysis {index + 1}",
                    "purpose": (
                        "Provide additional analytical context "
                        "for the research findings."
                    ),
                    "components": {
                        "kpis": dashboard.get("kpis", []),
                        "charts": dashboard.get("charts", []),
                        "tables": dashboard.get("tables", []),
                        "maps": dashboard.get("maps", []),
                    },
                },
            )

    def _number_slides(
        self,
        slides: List[Dict[str, Any]],
    ) -> None:

        for index, slide in enumerate(slides):

            slide["slide_number"] = index + 1

