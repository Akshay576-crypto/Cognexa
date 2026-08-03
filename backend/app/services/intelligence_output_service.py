from typing import Any, Dict, List, Optional
from app.analytics.analytics_engine import AnalyticsEngine
from app.analytics.kpi_engine import KPIEngine
from app.analytics.trend_engine import TrendEngine
from app.analytics.comparison_engine import ComparisonEngine
from app.visualization.chart_engine import ChartEngine
from app.visualization.table_engine import TableEngine
from app.schemas.consulting_result_schema import ConsultingResult

class IntelligenceOutputService:
    """
    Converts Cognexa IntelligenceResult data into a unified
    analytics and visualization package.

    This service does not perform research or LLM reasoning.

    It acts as the bridge between:

        Intelligence Pipeline
                ↓
        Analytics / Visualization
                ↓
        Dashboard / PDF / PPT
    """

    def __init__(
        self,
        analytics_engine: Optional[AnalyticsEngine] = None,
        kpi_engine: Optional[KPIEngine] = None,
        trend_engine: Optional[TrendEngine] = None,
        comparison_engine: Optional[ComparisonEngine] = None,
        chart_engine: Optional[ChartEngine] = None,
        table_engine: Optional[TableEngine] = None,
    ):
        self.analytics_engine = (
            analytics_engine or AnalyticsEngine()
        )

        self.kpi_engine = (
            kpi_engine or KPIEngine()
        )

        self.trend_engine = (
            trend_engine or TrendEngine()
        )

        self.comparison_engine = (
            comparison_engine or ComparisonEngine()
        )

        self.chart_engine = (
            chart_engine or ChartEngine()
        )

        self.table_engine = (
            table_engine or TableEngine()
        )

    def analyze_metrics(
        self,
        data: Dict[str, Any],
    ) -> Dict[str, Any]:
        """
        Run deterministic analytics against structured data.
        """

        return self.analytics_engine.analyze(data)

    def create_kpis(
        self,
        kpis: List[Dict[str, Any]],
    ) -> Dict[str, Any]:
        """
        Package KPI objects into a standardized KPI set.
        """

        return self.kpi_engine.create_kpi_set(kpis)

    def analyze_trends(
        self,
        data: List[Dict[str, Any]],
    ) -> Dict[str, Any]:
        """
        Analyze historical time-series data.
        """

        return self.trend_engine.analyze(data)

    def compare(
        self,
        entity_a: str,
        entity_b: str,
        metrics: List[Dict[str, Any]],
    ) -> Dict[str, Any]:
        """
        Compare two entities across multiple metrics.
        """

        return self.comparison_engine.analyze(
            entity_a=entity_a,
            entity_b=entity_b,
            metrics=metrics,
        )

    def create_charts(
        self,
        charts: List[Dict[str, Any]],
    ) -> Dict[str, Any]:
        """
        Package chart specifications.
        """

        return self.chart_engine.create_chart_collection(
            charts
        )

    def create_tables(
        self,
        tables: List[Dict[str, Any]],
    ) -> Dict[str, Any]:
        """
        Package table specifications.
        """

        return self.table_engine.create_table_collection(
            tables
        )

    def build_output(
        self,
        analytics_data: Optional[Dict[str, Any]] = None,
        kpis: Optional[List[Dict[str, Any]]] = None,
        trend_data: Optional[List[Dict[str, Any]]] = None,
        comparison: Optional[Dict[str, Any]] = None,
        charts: Optional[List[Dict[str, Any]]] = None,
        tables: Optional[List[Dict[str, Any]]] = None,
    ) -> Dict[str, Any]:
        """
        Build the unified Cognexa intelligence output package.

        Only supplied components are processed.
        """

        output: Dict[str, Any] = {
            "analytics": None,
            "kpis": None,
            "trends": None,
            "comparison": comparison,
            "charts": None,
            "tables": None,
        }

        if analytics_data is not None:
            output["analytics"] = self.analyze_metrics(
                analytics_data
            )

        if kpis is not None:
            output["kpis"] = self.create_kpis(kpis)

        if trend_data is not None:
            output["trends"] = self.analyze_trends(
                trend_data
            )

        if charts is not None:
            output["charts"] = self.create_charts(
                charts
            )

        if tables is not None:
            output["tables"] = self.create_tables(
                tables
            )

        return output

    def build_from_consulting_result(
    self,
    result: ConsultingResult,
    ) -> Dict[str, Any]:
        """
        Convert a validated ConsultingResult into the
        deterministic analytics and visualization layer.

        The ConsultingAgent remains responsible for LLM reasoning.
        This method only transforms already-validated structured data.
        """

        analytics: Dict[str, Any] = {}
        kpis: List[Dict[str, Any]] = []
        trends: List[Dict[str, Any]] = []
        comparisons: List[Dict[str, Any]] = []

        # ---------------------------------------------------------
        # KPIs
        # ---------------------------------------------------------

        for kpi in result.kpis:
            kpis.append(
                kpi.model_dump()
            )

        # ---------------------------------------------------------
        # TRENDS
        # ---------------------------------------------------------

        for trend in result.trends:
            trend_data = trend.data or []

            if trend_data:
                analyzed_trend = self.analyze_trends(
                    trend_data
                )

                trends.append(
                    {
                        "metric": trend.metric,
                        "direction": trend.direction,
                        "description": trend.description,
                        "analysis": analyzed_trend,
                    }
                )
            else:
                trends.append(
                    {
                        "metric": trend.metric,
                        "direction": trend.direction,
                        "description": trend.description,
                        "analysis": None,
                    }
                )

        # ---------------------------------------------------------
        # COMPARISONS
        # ---------------------------------------------------------

        for comparison in result.comparisons:

            if (
                comparison.value_a is not None
                and comparison.value_b is not None
            ):
                comparison_result = self.compare(
                    entity_a=comparison.entity_a,
                    entity_b=comparison.entity_b,
                    metrics=[
                        {
                            "metric": comparison.metric,
                            "value_a": comparison.value_a,
                            "value_b": comparison.value_b,
                            "unit": comparison.unit,
                            "higher_is_better": True,
                        }
                    ],
                )

                comparisons.append(
                    comparison_result
                )
            else:
                comparisons.append(
                    comparison.model_dump()
                )

        # ---------------------------------------------------------
        # KPI TABLE
        # ---------------------------------------------------------

        kpi_table = None

        if kpis:
            kpi_table = self.table_engine.create_kpi_table(
                title="Key Performance Indicators",
                kpis=kpis,
                source="Cognexa Consulting Intelligence",
            )

        # ---------------------------------------------------------
        # TREND CHARTS
        # ---------------------------------------------------------

        charts: List[Dict[str, Any]] = []

        for trend in result.trends:
            if not trend.data:
                continue

            periods = [
                item["period"]
                for item in trend.data
                if "period" in item
            ]

            values = [
                item["value"]
                for item in trend.data
                if "value" in item
            ]

            if len(periods) != len(values):
                continue

            charts.append(
                self.chart_engine.create_line_chart(
                    title=f"{trend.metric} Trend",
                    periods=periods,
                    values=values,
                    x_axis="Period",
                    y_axis=trend.metric,
                    source="Cognexa Consulting Intelligence",
                )
            )

        # ---------------------------------------------------------
        # OUTPUT PACKAGE
        # ---------------------------------------------------------

        output: Dict[str, Any] = {
            "question": result.question,
            "executive_summary": result.executive_summary,
            "problem_definition": result.problem_definition,
            "findings": [
                finding.model_dump()
                for finding in result.findings
            ],
            "kpis": kpis,
            "trends": trends,
            "comparisons": comparisons,
            "opportunities": [
                opportunity.model_dump()
                for opportunity in result.opportunities
            ],
            "risks": [
                risk.model_dump()
                for risk in result.risks
            ],
            "recommendations": [
                recommendation.model_dump()
                for recommendation in result.recommendations
            ],
            "data_limitations": result.data_limitations,
            "sources": result.sources,
            "analytics": analytics,
            "charts": self.create_charts(charts),
            "tables": self.create_tables(
                [kpi_table] if kpi_table else []
            ),
        }

        return output