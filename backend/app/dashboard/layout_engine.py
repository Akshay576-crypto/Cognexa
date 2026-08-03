from typing import Any, Dict, List


class LayoutEngine:
    """
    Deterministic dashboard layout specification engine.

    The Layout Engine decides how dashboard components should
    be organized. It does not render HTML, React, CSS, or images.
    """

    DEFAULT_GRID_COLUMNS = 12

    def create_layout(
        self,
        dashboard: Dict[str, Any],
        grid_columns: int = DEFAULT_GRID_COLUMNS,
    ) -> Dict[str, Any]:
        """
        Create a deterministic layout specification from a dashboard.
        """

        if not dashboard:
            raise ValueError("Dashboard cannot be empty.")

        if grid_columns <= 0:
            raise ValueError("Grid columns must be greater than zero.")

        layout = {
            "type": "dashboard_layout",
            "grid_columns": grid_columns,
            "rows": [],
        }

        # Header
        layout["rows"].append(
            {
                "row_type": "header",
                "components": [
                    {
                        "component_type": "header",
                        "title": dashboard.get("title"),
                        "description": dashboard.get("description"),
                        "width": grid_columns,
                    }
                ],
            }
        )

        # KPI row
        kpis = dashboard.get("kpis", [])

        if kpis:
            layout["rows"].append(
                {
                    "row_type": "kpi",
                    "components": self._create_kpi_layout(
                        kpis,
                        grid_columns,
                    ),
                }
            )

        # Charts
        charts = dashboard.get("charts", [])

        if charts:
            layout["rows"].extend(
                self._create_component_rows(
                    charts,
                    component_type="chart",
                    grid_columns=grid_columns,
                )
            )

        # Tables
        tables = dashboard.get("tables", [])

        if tables:
            layout["rows"].extend(
                self._create_component_rows(
                    tables,
                    component_type="table",
                    grid_columns=grid_columns,
                )
            )

        # Maps
        maps = dashboard.get("maps", [])

        if maps:
            layout["rows"].extend(
                self._create_component_rows(
                    maps,
                    component_type="map",
                    grid_columns=grid_columns,
                )
            )

        # Sources
        sources = dashboard.get("sources", [])

        if sources:
            layout["rows"].append(
                {
                    "row_type": "sources",
                    "components": [
                        {
                            "component_type": "sources",
                            "sources": sources,
                            "width": grid_columns,
                        }
                    ],
                }
            )

        return layout

    def _create_kpi_layout(
        self,
        kpis: List[Dict[str, Any]],
        grid_columns: int,
    ) -> List[Dict[str, Any]]:
        """
        Arrange KPIs evenly across the grid.
        """

        count = len(kpis)

        width = max(1, grid_columns // count)

        components = []

        for index, kpi in enumerate(kpis):
            components.append(
                {
                    "component_type": "kpi",
                    "component_id": f"kpi_{index + 1}",
                    "data": kpi,
                    "width": width,
                }
            )

        return components

    def _create_component_rows(
        self,
        components: List[Dict[str, Any]],
        component_type: str,
        grid_columns: int,
    ) -> List[Dict[str, Any]]:
        """
        Arrange generic components into rows.
        """

        rows = []

        for index, component in enumerate(components):

            rows.append(
                {
                    "row_type": component_type,
                    "components": [
                        {
                            "component_type": component_type,
                            "component_id": f"{component_type}_{index + 1}",
                            "data": component,
                            "width": grid_columns,
                        }
                    ],
                }
            )

        return rows