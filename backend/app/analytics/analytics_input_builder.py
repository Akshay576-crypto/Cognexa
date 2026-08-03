from typing import Any, Dict, List

from app.schemas.consulting_result_schema import ConsultingResult


class AnalyticsInputBuilder:
    """
    Converts structured ConsultingResult data into
    deterministic analytics-ready inputs.

    This class does not calculate metrics and does not
    use an LLM.

    Responsibilities:
    - Extract KPI data
    - Extract trend time-series
    - Extract comparison metrics
    - Preserve evidence and source metadata
    - Produce a standardized analytics input structure
    """

    def build(
        self,
        consulting_result: ConsultingResult,
    ) -> Dict[str, Any]:
        """
        Build a complete analytics input package.
        """

        if not isinstance(
            consulting_result,
            ConsultingResult,
        ):
            raise TypeError(
                "consulting_result must be a ConsultingResult."
            )

        return {
            "question": consulting_result.question,
            "kpis": self.build_kpis(
                consulting_result
            ),
            "trends": self.build_trends(
                consulting_result
            ),
            "comparisons": self.build_comparisons(
                consulting_result
            ),
            "sources": list(
                consulting_result.sources
            ),
            "data_limitations": list(
                consulting_result.data_limitations
            ),
        }

    def build_kpis(
        self,
        consulting_result: ConsultingResult,
    ) -> List[Dict[str, Any]]:
        """
        Convert ConsultingResult KPIs into
        analytics-ready dictionaries.
        """

        return [
            {
                "name": kpi.name,
                "value": kpi.value,
                "unit": kpi.unit,
                "period": kpi.period,
                "change": kpi.change,
                "trend": kpi.trend,
                "source": kpi.source,
                "source_url": kpi.source_url,
            }
            for kpi in consulting_result.kpis
        ]

    def build_trends(
        self,
        consulting_result: ConsultingResult,
    ) -> List[Dict[str, Any]]:
        """
        Convert consulting trends into
        analytics-ready time-series structures.
        """

        trends = []

        for trend in consulting_result.trends:
            trends.append(
                {
                    "metric": trend.metric,
                    "direction": trend.direction,
                    "description": trend.description,
                    "data": list(trend.data),
                }
            )

        return trends

    def build_comparisons(
        self,
        consulting_result: ConsultingResult,
    ) -> List[Dict[str, Any]]:
        """
        Convert consulting comparisons into
        analytics-ready comparison structures.
        """

        comparisons = []

        for comparison in consulting_result.comparisons:
            comparisons.append(
                {
                    "metric": comparison.metric,
                    "entity_a": comparison.entity_a,
                    "value_a": comparison.value_a,
                    "entity_b": comparison.entity_b,
                    "value_b": comparison.value_b,
                    "unit": comparison.unit,
                    "winner": comparison.winner,
                }
            )

        return comparisons