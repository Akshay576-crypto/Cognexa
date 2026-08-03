from typing import Any, Dict, List

class ChartEngine:
    """
    Deterministic chart specification engine for Cognexa.

    Converts structured analytical data into chart-ready
    specifications.

    Does not use an LLM.
    """

    def create_bar_chart(
        self,
        title: str,
        labels: List[str],
        values: List[float],
        x_axis: str = "",
        y_axis: str = "",
        unit: str = "",
        source: str = "",
        source_url: str = "",
    ) -> Dict[str, Any]:
        """
        Create a bar chart specification.
        """

        return {
            "type": "bar",
            "title": title,
            "data": {
                "labels": labels,
                "values": values,
            },
            "axes": {
                "x": x_axis,
                "y": y_axis,
            },
            "unit": unit,
            "source": source,
            "source_url": source_url,
        }

    def create_line_chart(
        self,
        title: str,
        periods: List[Any],
        values: List[float],
        x_axis: str = "",
        y_axis: str = "",
        unit: str = "",
        source: str = "",
        source_url: str = "",
    ) -> Dict[str, Any]:
        """
        Create a line chart specification.
        """

        return {
            "type": "line",
            "title": title,
            "data": {
                "periods": periods,
                "values": values,
            },
            "axes": {
                "x": x_axis,
                "y": y_axis,
            },
            "unit": unit,
            "source": source,
            "source_url": source_url,
        }

    def create_pie_chart(
        self,
        title: str,
        labels: List[str],
        values: List[float],
        unit: str = "%",
        source: str = "",
        source_url: str = "",
    ) -> Dict[str, Any]:
        """
        Create a pie chart specification.
        """

        return {
            "type": "pie",
            "title": title,
            "data": {
                "labels": labels,
                "values": values,
            },
            "unit": unit,
            "source": source,
            "source_url": source_url,
        }

    def create_donut_chart(
        self,
        title: str,
        labels: List[str],
        values: List[float],
        unit: str = "%",
        source: str = "",
        source_url: str = "",
    ) -> Dict[str, Any]:
        """
        Create a donut chart specification.
        """

        return {
            "type": "donut",
            "title": title,
            "data": {
                "labels": labels,
                "values": values,
            },
            "unit": unit,
            "source": source,
            "source_url": source_url,
        }

    def create_area_chart(
        self,
        title: str,
        periods: List[Any],
        values: List[float],
        x_axis: str = "",
        y_axis: str = "",
        unit: str = "",
        source: str = "",
        source_url: str = "",
    ) -> Dict[str, Any]:
        """
        Create an area chart specification.
        """

        return {
            "type": "area",
            "title": title,
            "data": {
                "periods": periods,
                "values": values,
            },
            "axes": {
                "x": x_axis,
                "y": y_axis,
            },
            "unit": unit,
            "source": source,
            "source_url": source_url,
        }

    def create_comparison_chart(
        self,
        title: str,
        entities: List[str],
        values: List[float],
        metric: str,
        unit: str = "",
        source: str = "",
        source_url: str = "",
    ) -> Dict[str, Any]:
        """
        Create a comparison chart specification.
        """

        return {
            "type": "comparison",
            "title": title,
            "metric": metric,
            "data": {
                "entities": entities,
                "values": values,
            },
            "unit": unit,
            "source": source,
            "source_url": source_url,
        }

    def create_chart_collection(
        self,
        charts: List[Dict[str, Any]],
    ) -> Dict[str, Any]:
        """
        Package multiple charts into a standardized collection.
        """

        return {
            "chart_count": len(charts),
            "charts": charts,
        }