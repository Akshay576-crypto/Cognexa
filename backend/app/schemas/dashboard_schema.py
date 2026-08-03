from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class DashboardRequest(BaseModel):
    title: str = Field(
        ...,
        min_length=1,
        max_length=200,
    )

    description: Optional[str] = None

    kpis: List[Dict[str, Any]] = Field(
        default_factory=list
    )

    charts: List[Dict[str, Any]] = Field(
        default_factory=list
    )

    tables: List[Dict[str, Any]] = Field(
        default_factory=list
    )

    maps: List[Dict[str, Any]] = Field(
        default_factory=list
    )

    sources: List[Dict[str, Any]] = Field(
        default_factory=list
    )

    theme_name: str = "cognexa_aurora"

    grid_columns: int = Field(
        default=12,
        ge=1,
        le=24,
    )


class DashboardResponse(BaseModel):
    dashboard: Dict[str, Any]
    layout: Dict[str, Any]