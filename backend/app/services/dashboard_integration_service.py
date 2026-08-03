from typing import Any, Dict, Optional

from app.dashboard.dashboard_engine import DashboardEngine
from app.schemas.intelligence_result_schema import IntelligenceResult


class DashboardIntegrationService:
    """
    Converts a canonical IntelligenceResult into
    a dashboard specification using DashboardEngine.

    Responsibilities:
    - Extract dashboard-ready data from IntelligenceResult
    - Preserve KPI, chart, table, and source data
    - Delegate dashboard construction to DashboardEngine

    It does NOT:
    - Perform research
    - Perform LLM reasoning
    - Calculate analytics
    - Render dashboards
    """

    def __init__(
        self,
        dashboard_engine: Optional[DashboardEngine] = None,
    ):
        self.dashboard_engine = (
            dashboard_engine or DashboardEngine()
        )

    def build_dashboard(
        self,
        intelligence_result: IntelligenceResult,
        title: str,
        description: Optional[str] = None,
        theme_name: str = "cognexa_aurora",
        grid_columns: int = 12,
    ) -> Dict[str, Any]:
        """
        Build a dashboard from a canonical IntelligenceResult.
        """

        if not title or not title.strip():
            raise ValueError(
                "Dashboard title cannot be empty."
            )

        consulting = intelligence_result.consulting

        kpis = [
            kpi.model_dump()
            for kpi in consulting.kpis
        ]

        sources = consulting.sources

        charts = intelligence_result.charts
        tables = intelligence_result.tables

        return self.dashboard_engine.create_dashboard(
            title=title.strip(),
            description=description,
            kpis=kpis,
            charts=charts,
            tables=tables,
            maps=[],
            sources=sources,
            theme_name=theme_name,
            grid_columns=grid_columns,
        )