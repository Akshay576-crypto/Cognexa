from typing import Any, Dict, List
from pydantic import BaseModel, Field


class PDFRequest(BaseModel):
    presentation_spec: Dict[str, Any] = Field(
        ...,
        description="Cognexa presentation specification."
    )

    output_filename: str = Field(
        default="cognexa_report.pdf",
        min_length=1,
        max_length=255,
    )

    theme_id: str = Field(
        default="cognexa_aurora",
        min_length=1,
        max_length=100,
    )


class PDFResponse(BaseModel):
    type: str
    title: str
    slide_count: int
    output_path: str
    theme_id: str