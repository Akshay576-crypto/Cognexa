from pydantic import BaseModel, Field


class ConsultingRequest(BaseModel):
    question: str = Field(
        ...,
        min_length=3,
        max_length=5000,
    )

    context: str = Field(
        ...,
        min_length=1,
    )

    sources: str = ""


class ConsultingResponse(BaseModel):
    question: str
    analysis: str