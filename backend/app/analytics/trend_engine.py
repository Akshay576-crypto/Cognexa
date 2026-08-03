from typing import Any, Dict, List, Optional


class TrendEngine:
    """
    Deterministic trend analysis engine for Cognexa.

    Converts historical time-series data into structured
    trend intelligence for dashboards, PPTs, and PDFs.
    """

    def calculate_percentage_change(
        self,
        old_value: float,
        new_value: float,
    ) -> Optional[float]:
        """Calculate percentage change between two values."""

        if old_value == 0:
            return None

        return round(
            ((new_value - old_value) / old_value) * 100,
            2,
        )

    def analyze_period_changes(
        self,
        data: List[Dict[str, Any]],
    ) -> List[Dict[str, Any]]:
        """
        Calculate period-over-period changes.

        Expected format:

        [
            {"period": 2022, "value": 100},
            {"period": 2023, "value": 120},
        ]
        """

        if not data:
            return []

        results = []

        for index, current in enumerate(data):
            period = current["period"]
            value = current["value"]

            result = {
                "period": period,
                "value": value,
                "change": None,
                "percentage_change": None,
                "trend": "unknown",
            }

            if index > 0:
                previous = data[index - 1]
                previous_value = previous["value"]

                change = round(value - previous_value, 2)

                percentage_change = self.calculate_percentage_change(
                    previous_value,
                    value,
                )

                result["change"] = change
                result["percentage_change"] = percentage_change

                if percentage_change is None:
                    result["trend"] = "unknown"
                elif percentage_change > 0:
                    result["trend"] = "increasing"
                elif percentage_change < 0:
                    result["trend"] = "decreasing"
                else:
                    result["trend"] = "stable"

            results.append(result)

        return results

    def find_highest_period(
        self,
        data: List[Dict[str, Any]],
    ) -> Optional[Dict[str, Any]]:
        """Find the period with the highest value."""

        if not data:
            return None

        highest = max(
            data,
            key=lambda item: item["value"],
        )

        return {
            "period": highest["period"],
            "value": highest["value"],
        }

    def find_lowest_period(
        self,
        data: List[Dict[str, Any]],
    ) -> Optional[Dict[str, Any]]:
        """Find the period with the lowest value."""

        if not data:
            return None

        lowest = min(
            data,
            key=lambda item: item["value"],
        )

        return {
            "period": lowest["period"],
            "value": lowest["value"],
        }

    def determine_overall_direction(
        self,
        data: List[Dict[str, Any]],
    ) -> str:
        """Determine overall direction from first to last value."""

        if len(data) < 2:
            return "insufficient_data"

        first_value = data[0]["value"]
        last_value = data[-1]["value"]

        if last_value > first_value:
            return "increasing"

        if last_value < first_value:
            return "decreasing"

        return "stable"

    def calculate_overall_change(
        self,
        data: List[Dict[str, Any]],
    ) -> Optional[float]:
        """Calculate total percentage change across the period."""

        if len(data) < 2:
            return None

        first_value = data[0]["value"]
        last_value = data[-1]["value"]

        return self.calculate_percentage_change(
            first_value,
            last_value,
        )

    def analyze(
        self,
        data: List[Dict[str, Any]],
    ) -> Dict[str, Any]:
        """
        Main trend analysis entry point.
        """

        if not data:
            return {
                "period_count": 0,
                "trend_data": [],
                "overall_direction": "insufficient_data",
                "overall_change": None,
                "highest_period": None,
                "lowest_period": None,
            }

        trend_data = self.analyze_period_changes(data)

        return {
            "period_count": len(data),
            "trend_data": trend_data,
            "overall_direction": self.determine_overall_direction(data),
            "overall_change": self.calculate_overall_change(data),
            "highest_period": self.find_highest_period(data),
            "lowest_period": self.find_lowest_period(data),
        }