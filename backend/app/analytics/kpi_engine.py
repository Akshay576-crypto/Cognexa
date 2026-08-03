from typing import Any, Dict, List, Optional


class KPIEngine:
    """
    Creates structured business KPIs for Cognexa.

    This engine is deterministic.
    It does not use an LLM.
    """

    def create_kpi(
        self,
        name: str,
        value: Any,
        unit: str = "",
        period: str = "",
        source: str = "",
        source_url: str = "",
        change: Optional[float] = None,
        trend: str = "",
        importance: str = "medium",
    ) -> Dict[str, Any]:
        """
        Create a standardized KPI object.
        """

        return {
            "name": name,
            "value": value,
            "unit": unit,
            "period": period,
            "change": change,
            "trend": trend,
            "importance": importance,
            "source": source,
            "source_url": source_url,
        }

    def determine_trend(
        self,
        change: Optional[float],
        threshold: float = 0.01,
    ) -> str:
        """
        Determine KPI trend from percentage change.
        """

        if change is None:
            return "unknown"

        if change > threshold:
            return "increasing"

        if change < -threshold:
            return "decreasing"

        return "stable"

    def create_change_kpi(
        self,
        name: str,
        current_value: float,
        previous_value: float,
        unit: str = "",
        period: str = "",
        source: str = "",
        source_url: str = "",
        importance: str = "medium",
    ) -> Dict[str, Any]:
        """
        Create a KPI containing current value and percentage change.
        """

        if previous_value == 0:
            percentage_change = None
        else:
            percentage_change = round(
                ((current_value - previous_value) / previous_value) * 100,
                2,
            )

        trend = self.determine_trend(percentage_change)

        return self.create_kpi(
            name=name,
            value=current_value,
            unit=unit,
            period=period,
            source=source,
            source_url=source_url,
            change=percentage_change,
            trend=trend,
            importance=importance,
        )

    def create_market_share_kpi(
        self,
        name: str,
        company_value: float,
        total_market_value: float,
        unit: str = "%",
        period: str = "",
        source: str = "",
        source_url: str = "",
        importance: str = "high",
    ) -> Dict[str, Any]:
        """
        Create a market-share KPI.
        """

        if total_market_value == 0:
            market_share = None
        else:
            market_share = round(
                (company_value / total_market_value) * 100,
                2,
            )

        return self.create_kpi(
            name=name,
            value=market_share,
            unit=unit,
            period=period,
            source=source,
            source_url=source_url,
            trend="",
            importance=importance,
        )

    def create_kpi_set(
        self,
        kpis: List[Dict[str, Any]],
    ) -> Dict[str, Any]:
        """
        Package multiple KPIs into a standardized structure.
        """

        return {
            "kpi_count": len(kpis),
            "kpis": kpis,
        }