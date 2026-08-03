from typing import Any, Dict, List, Optional


class ComparisonEngine:
    """
    Deterministic comparison engine for Cognexa.

    Compares companies, products, markets, regions,
    periods, or any other entities containing numeric metrics.

    Does not use an LLM.
    """

    def calculate_difference(
        self,
        value_a: float,
        value_b: float,
    ) -> float:
        """Calculate absolute difference between two values."""

        return round(value_a - value_b, 2)

    def calculate_percentage_difference(
        self,
        value_a: float,
        value_b: float,
    ) -> Optional[float]:
        """
        Calculate percentage difference using value B
        as the comparison baseline.
        """

        if value_b == 0:
            return None

        return round(
            ((value_a - value_b) / value_b) * 100,
            2,
        )

    def determine_winner(
        self,
        value_a: float,
        value_b: float,
        higher_is_better: bool = True,
    ) -> str:
        """Determine which entity performs better."""

        if value_a == value_b:
            return "tie"

        if higher_is_better:
            return "A" if value_a > value_b else "B"

        return "A" if value_a < value_b else "B"

    def compare_values(
        self,
        entity_a: str,
        value_a: float,
        entity_b: str,
        value_b: float,
        metric: str,
        unit: str = "",
        higher_is_better: bool = True,
    ) -> Dict[str, Any]:
        """
        Compare two entities using a single metric.
        """

        difference = self.calculate_difference(
            value_a,
            value_b,
        )

        percentage_difference = self.calculate_percentage_difference(
            value_a,
            value_b,
        )

        winner_code = self.determine_winner(
            value_a,
            value_b,
            higher_is_better,
        )

        winner = {
            "A": entity_a,
            "B": entity_b,
            "tie": "tie",
        }[winner_code]

        return {
            "metric": metric,
            "unit": unit,
            "entity_a": {
                "name": entity_a,
                "value": value_a,
            },
            "entity_b": {
                "name": entity_b,
                "value": value_b,
            },
            "difference": difference,
            "percentage_difference": percentage_difference,
            "winner": winner,
            "higher_is_better": higher_is_better,
        }

    def compare_multiple_metrics(
        self,
        entity_a: str,
        entity_b: str,
        metrics: List[Dict[str, Any]],
    ) -> Dict[str, Any]:
        """
        Compare two entities across multiple metrics.

        Expected format:

        [
            {
                "metric": "Revenue",
                "value_a": 500,
                "value_b": 400,
                "unit": "USD Million",
                "higher_is_better": True
            }
        ]
        """

        comparisons = []

        for metric_data in metrics:
            comparison = self.compare_values(
                entity_a=entity_a,
                value_a=metric_data["value_a"],
                entity_b=entity_b,
                value_b=metric_data["value_b"],
                metric=metric_data["metric"],
                unit=metric_data.get("unit", ""),
                higher_is_better=metric_data.get(
                    "higher_is_better",
                    True,
                ),
            )

            comparisons.append(comparison)

        return {
            "entity_a": entity_a,
            "entity_b": entity_b,
            "metric_count": len(comparisons),
            "comparisons": comparisons,
        }

    def rank_entities(
        self,
        data: List[Dict[str, Any]],
        metric: str,
        descending: bool = True,
    ) -> List[Dict[str, Any]]:
        """
        Rank multiple entities based on a metric.

        Expected format:

        [
            {"name": "Company A", "value": 500},
            {"name": "Company B", "value": 400}
        ]
        """

        ranked = sorted(
            data,
            key=lambda item: item["value"],
            reverse=descending,
        )

        results = []

        for position, item in enumerate(ranked, start=1):
            results.append(
                {
                    "rank": position,
                    "name": item["name"],
                    "value": item["value"],
                }
            )

        return results

    def analyze(
        self,
        entity_a: str,
        entity_b: str,
        metrics: List[Dict[str, Any]],
    ) -> Dict[str, Any]:
        """
        Main comparison engine entry point.
        """

        return self.compare_multiple_metrics(
            entity_a=entity_a,
            entity_b=entity_b,
            metrics=metrics,
        )