from typing import Any, Dict, List

from pydantic import BaseModel, Field

from app.schemas.consulting_result_schema import ConsultingResult


class ResearchEvidence(BaseModel):
    """
    Canonical research output used by Cognexa intelligence flow.
    """

    evidence: str = ""


class IntelligenceResult(BaseModel):
    """
    Canonical intelligence object for Cognexa.

    This is the bridge between:

        Research
            ↓
        Consulting
            ↓
        Analytics
            ↓
        Visualization
            ↓
        Dashboard / PDF / PPT
    """

    question: str

    research: ResearchEvidence = Field(
        default_factory=ResearchEvidence
    )

    consulting: ConsultingResult

    analytics: Dict[str, Any] = Field(
        default_factory=dict
    )

    charts: List[Dict[str, Any]] = Field(
        default_factory=list
    )

    tables: List[Dict[str, Any]] = Field(
        default_factory=list
    )