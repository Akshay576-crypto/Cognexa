from pydantic import BaseModel, Field
from typing import Optional


class ResearchRequest(BaseModel):
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


class ResearchResponse(BaseModel):
    question: str
    answer: str
    document_id: Optional[int] = None