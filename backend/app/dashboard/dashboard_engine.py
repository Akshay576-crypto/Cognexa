from typing import Any, Dict, List, Optional

from app.dashboard.dashboard_schema import DashboardSchema
from app.dashboard.layout_engine import LayoutEngine
from app.visualization.theme_engine import ThemeEngine


class DashboardEngine:
    """
    Deterministic Dashboard Engine.

    Responsibilities:
    - Assemble dashboard components
    - Apply themes
    - Preserve source attribution
    - Generate dashboard layout
    - Produce a reusable dashboard specification

    It does NOT:
    - Perform LLM reasoning
    - Calculate business metrics
    - Render charts
    - Render maps
    - Render frontend UI
    """

    def __init__(
        self,
        theme_engine: Optional[ThemeEngine] = None,
        layout_engine: Optional[LayoutEngine] = None,
    ):
        self.theme_engine = theme_engine or ThemeEngine()
        self.layout_engine = layout_engine or LayoutEngine()

    def create_dashboard(
        self,
        title: str,
        description: Optional[str] = None,
        kpis: Optional[List[Dict[str, Any]]] = None,
        charts: Optional[List[Dict[str, Any]]] = None,
        tables: Optional[List[Dict[str, Any]]] = None,
        maps: Optional[List[Dict[str, Any]]] = None,
        sources: Optional[List[Dict[str, Any]]] = None,
        theme_name: str = "cognexa_aurora",
        grid_columns: int = 12,
    ) -> Dict[str, Any]:
        """
        Assemble a complete dashboard specification.
        """

        theme = self.theme_engine.get_theme(theme_name)

        dashboard = DashboardSchema(
            title=title,
            description=description,
            theme=theme,
        )

        self._add_kpis(dashboard, kpis or [])
        self._add_charts(dashboard, charts or [])
        self._add_tables(dashboard, tables or [])
        self._add_maps(dashboard, maps or [])
        self._add_sources(dashboard, sources or [])

        dashboard_spec = dashboard.to_dict()

        layout = self.layout_engine.create_layout(
            dashboard_spec,
            grid_columns=grid_columns,
        )

        return {
            "dashboard": dashboard_spec,
            "layout": layout,
        }

    def _add_kpis(
        self,
        dashboard: DashboardSchema,
        kpis: List[Dict[str, Any]],
    ) -> None:
        """Add KPI specifications to the dashboard."""

        for kpi in kpis:
            dashboard.add_kpi(kpi)

    def _add_charts(
        self,
        dashboard: DashboardSchema,
        charts: List[Dict[str, Any]],
    ) -> None:
        """Add chart specifications to the dashboard."""

        for chart in charts:
            dashboard.add_chart(chart)

    def _add_tables(
        self,
        dashboard: DashboardSchema,
        tables: List[Dict[str, Any]],
    ) -> None:
        """Add table specifications to the dashboard."""

        for table in tables:
            dashboard.add_table(table)

    def _add_maps(
        self,
        dashboard: DashboardSchema,
        maps: List[Dict[str, Any]],
    ) -> None:
        """Add map specifications to the dashboard."""

        for map_spec in maps:
            dashboard.add_map(map_spec)

    def _add_sources(
        self,
        dashboard: DashboardSchema,
        sources: List[Dict[str, Any]],
    ) -> None:
        """Add source attribution to the dashboard."""

        for source in sources:
            dashboard.add_source(
                source=source.get("source", "Unknown Source"),
                source_url=source.get("source_url"),
            )