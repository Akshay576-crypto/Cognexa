from typing import Any, Dict, List, Optional


class MapEngine:
    """
    Deterministic geographic visualization specification engine.

    The Map Engine does not render maps.
    It converts structured geographic data into a reusable
    map specification that can later be consumed by:

    - Dashboard Engine
    - PPT Engine
    - PDF Engine
    """

    def create_map_spec(
        self,
        title: str,
        data: List[Dict[str, Any]],
        location_type: str = "region",
        metric: Optional[str] = None,
        unit: Optional[str] = None,
        source: Optional[str] = None,
        source_url: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Create a deterministic map specification.

        Expected data format:

        [
            {
                "location": "Maharashtra",
                "value": 32,
                "latitude": 19.7515,
                "longitude": 75.7139
            }
        ]
        """

        if not title:
            raise ValueError("Map title cannot be empty.")

        if not data:
            raise ValueError("Map data cannot be empty.")

        normalized_data = []

        for item in data:
            if "location" not in item:
                raise ValueError("Each map data item must contain 'location'.")

            if "value" not in item:
                raise ValueError(
                    "Each map data item must contain 'value'."
                )

            normalized_item = {
                "location": item["location"],
                "value": item["value"],
                "latitude": item.get("latitude"),
                "longitude": item.get("longitude"),
            }

            normalized_data.append(normalized_item)

        return {
            "type": "map",
            "title": title,
            "location_type": location_type,
            "metric": metric,
            "unit": unit,
            "data": normalized_data,
            "source": source,
            "source_url": source_url,
        }

    def create_region_map(
        self,
        title: str,
        data: List[Dict[str, Any]],
        metric: str,
        unit: Optional[str] = None,
        source: Optional[str] = None,
        source_url: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Create a region-level map specification.
        """

        return self.create_map_spec(
            title=title,
            data=data,
            location_type="region",
            metric=metric,
            unit=unit,
            source=source,
            source_url=source_url,
        )

    def create_country_map(
        self,
        title: str,
        data: List[Dict[str, Any]],
        metric: str,
        unit: Optional[str] = None,
        source: Optional[str] = None,
        source_url: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Create a country-level map specification.
        """

        return self.create_map_spec(
            title=title,
            data=data,
            location_type="country",
            metric=metric,
            unit=unit,
            source=source,
            source_url=source_url,
        )