from typing import Optional

from pydantic import BaseModel, Field

from app.schemas.intelligence_result_schema import IntelligenceResult


class IntelligenceRequest(BaseModel):
    question: str = Field(
        ...,
        min_length=3,
        max_length=5000,
    )

    document_id: Optional[int] = None

    top_k: int = Field(
        default=5,
        ge=1,
        le=20,
    )

    sources: str = ""


class IntelligenceResponse(IntelligenceResult):
    pass