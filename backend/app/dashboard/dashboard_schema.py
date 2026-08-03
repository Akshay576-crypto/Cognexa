from typing import Any, Dict, List, Optional


class DashboardSchema:
    """
    Deterministic dashboard specification.

    This schema defines WHAT a dashboard contains.
    It does not render the dashboard.

    Consumers can later use this specification for:
    - React frontend
    - PPT generation
    - PDF generation
    """

    def __init__(
        self,
        title: str,
        description: Optional[str] = None,
        theme: Optional[Dict[str, Any]] = None,
    ):
        if not title:
            raise ValueError("Dashboard title cannot be empty.")

        self.title = title
        self.description = description
        self.theme = theme

        self.kpis: List[Dict[str, Any]] = []
        self.charts: List[Dict[str, Any]] = []
        self.tables: List[Dict[str, Any]] = []
        self.maps: List[Dict[str, Any]] = []
        self.sections: List[Dict[str, Any]] = []
        self.sources: List[Dict[str, Any]] = []

    def add_kpi(self, kpi: Dict[str, Any]) -> None:
        """Add a KPI specification."""
        self.kpis.append(kpi)

    def add_chart(self, chart: Dict[str, Any]) -> None:
        """Add a chart specification."""
        self.charts.append(chart)

    def add_table(self, table: Dict[str, Any]) -> None:
        """Add a table specification."""
        self.tables.append(table)

    def add_map(self, map_spec: Dict[str, Any]) -> None:
        """Add a map specification."""
        self.maps.append(map_spec)

    def add_section(
        self,
        title: str,
        component_type: str,
        component_ids: Optional[List[str]] = None,
    ) -> None:
        """Add a dashboard section."""

        self.sections.append(
            {
                "title": title,
                "component_type": component_type,
                "component_ids": component_ids or [],
            }
        )

    def add_source(
        self,
        source: str,
        source_url: Optional[str] = None,
    ) -> None:
        """Add source attribution."""

        self.sources.append(
            {
                "source": source,
                "source_url": source_url,
            }
        )

    def to_dict(self) -> Dict[str, Any]:
        """Convert dashboard specification into a dictionary."""

        return {
            "type": "dashboard",
            "title": self.title,
            "description": self.description,
            "theme": self.theme,
            "kpis": self.kpis,
            "charts": self.charts,
            "tables": self.tables,
            "maps": self.maps,
            "sections": self.sections,
            "sources": self.sources,
        }