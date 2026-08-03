from typing import Any, Dict, List


class TableEngine:
    """
    Deterministic table specification engine for Cognexa.

    Converts structured analytical data into reusable tables
    for dashboards, PPTs, and PDFs.

    Does not use an LLM.
    """

    def create_table(
        self,
        title: str,
        columns: List[str],
        rows: List[Dict[str, Any]],
        source: str = "",
        source_url: str = "",
    ) -> Dict[str, Any]:
        """
        Create a standardized table specification.
        """

        return {
            "type": "table",
            "title": title,
            "columns": columns,
            "rows": rows,
            "row_count": len(rows),
            "source": source,
            "source_url": source_url,
        }

    def create_comparison_table(
        self,
        title: str,
        entities: List[str],
        metrics: List[Dict[str, Any]],
        source: str = "",
        source_url: str = "",
    ) -> Dict[str, Any]:
        """
        Create a comparison table.

        Expected metrics format:

        [
            {
                "metric": "Revenue",
                "values": {
                    "Company A": 500,
                    "Company B": 400
                },
                "unit": "USD Million"
            }
        ]
        """

        columns = ["Metric", "Unit"] + entities

        rows = []

        for metric in metrics:
            row = {
                "Metric": metric["metric"],
                "Unit": metric.get("unit", ""),
            }

            values = metric.get("values", {})

            for entity in entities:
                row[entity] = values.get(entity)

            rows.append(row)

        return self.create_table(
            title=title,
            columns=columns,
            rows=rows,
            source=source,
            source_url=source_url,
        )

    def create_kpi_table(
        self,
        title: str,
        kpis: List[Dict[str, Any]],
        source: str = "",
        source_url: str = "",
    ) -> Dict[str, Any]:
        """
        Convert Cognexa KPI objects into a table.
        """

        columns = [
            "KPI",
            "Value",
            "Unit",
            "Period",
            "Change",
            "Trend",
        ]

        rows = []

        for kpi in kpis:
            rows.append(
                {
                    "KPI": kpi.get("name"),
                    "Value": kpi.get("value"),
                    "Unit": kpi.get("unit", ""),
                    "Period": kpi.get("period", ""),
                    "Change": kpi.get("change"),
                    "Trend": kpi.get("trend", ""),
                }
            )

        return self.create_table(
            title=title,
            columns=columns,
            rows=rows,
            source=source,
            source_url=source_url,
        )

    def create_table_collection(
        self,
        tables: List[Dict[str, Any]],
    ) -> Dict[str, Any]:
        """
        Package multiple tables into a standardized collection.
        """

        return {
            "table_count": len(tables),
            "tables": tables,
        }