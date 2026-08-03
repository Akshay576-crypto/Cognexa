from typing import Any, Dict, List, Optional


class AnalyticsEngine:
    """
    Deterministic analytics engine for Cognexa.

    Responsible for calculating business metrics from structured
    research data. It does not use an LLM.
    """

    def calculate_percentage_change(
        self,
        old_value: float,
        new_value: float
    ) -> Optional[float]:
        """
        Calculate percentage change between two values.
        """

        if old_value == 0:
            return None

        return round(
            ((new_value - old_value) / old_value) * 100,
            2
        )

    def calculate_growth_rate(
        self,
        initial_value: float,
        final_value: float,
        periods: int
    ) -> Optional[float]:
        """
        Calculate CAGR / compound growth rate.
        """

        if initial_value <= 0 or final_value <= 0 or periods <= 0:
            return None

        growth_rate = (
            (final_value / initial_value) ** (1 / periods) - 1
        ) * 100

        return round(growth_rate, 2)

    def calculate_total(
        self,
        values: List[float]
    ) -> float:
        """
        Calculate total of numeric values.
        """

        return round(sum(values), 2)

    def calculate_average(
        self,
        values: List[float]
    ) -> Optional[float]:
        """
        Calculate average of numeric values.
        """

        if not values:
            return None

        return round(sum(values) / len(values), 2)

    def calculate_market_share(
        self,
        company_value: float,
        total_market_value: float
    ) -> Optional[float]:
        """
        Calculate market share percentage.
        """

        if total_market_value == 0:
            return None

        return round(
            (company_value / total_market_value) * 100,
            2
        )

    def calculate_change(
        self,
        old_value: float,
        new_value: float
    ) -> float:
        """
        Calculate absolute change.
        """

        return round(new_value - old_value, 2)

    def calculate_kpis(
        self,
        data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Calculate common business KPIs from structured data.

        This method will become the main entry point for
        Cognexa's analytics layer.
        """

        kpis: Dict[str, Any] = {}

        if "previous_value" in data and "current_value" in data:

            previous = data["previous_value"]
            current = data["current_value"]

            kpis["current_value"] = current

            kpis["absolute_change"] = self.calculate_change(
                previous,
                current
            )

            kpis["percentage_change"] = self.calculate_percentage_change(
                previous,
                current
            )

        if "company_value" in data and "total_market_value" in data:

            kpis["market_share"] = self.calculate_market_share(
                data["company_value"],
                data["total_market_value"]
            )

        if (
            "initial_value" in data
            and "final_value" in data
            and "periods" in data
        ):

            kpis["growth_rate"] = self.calculate_growth_rate(
                data["initial_value"],
                data["final_value"],
                data["periods"]
            )

        if "values" in data:

            values = data["values"]

            if values:
                kpis["total"] = self.calculate_total(values)
                kpis["average"] = self.calculate_average(values)

        return kpis

    def analyze(
        self,
        data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Main analytics entry point.

        Receives structured data and returns deterministic
        analytical results that can later be consumed by:

        - Dashboard Engine
        - PPT Engine
        - PDF Engine
        """

        return {
            "input": data,
            "kpis": self.calculate_kpis(data),
        }