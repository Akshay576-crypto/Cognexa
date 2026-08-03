from typing import List, Optional
from pydantic import BaseModel, Field


class ConsultingFinding(BaseModel):
    title: str
    description: str
    evidence: str = ""
    importance: str = "medium"


class ConsultingKPI(BaseModel):
    name: str
    value: Optional[float] = None
    unit: str = ""
    period: str = ""
    change: Optional[float] = None
    trend: str = ""
    source: str = ""
    source_url: str = ""


class ConsultingTrend(BaseModel):
    metric: str
    direction: str
    description: str
    data: List[dict] = Field(default_factory=list)


class ConsultingComparison(BaseModel):
    metric: str
    entity_a: str
    value_a: Optional[float] = None
    entity_b: str
    value_b: Optional[float] = None
    unit: str = ""
    winner: str = ""


class ConsultingRecommendation(BaseModel):
    title: str
    description: str
    priority: str = "medium"
    timeframe: str = ""


class ConsultingRisk(BaseModel):
    title: str
    description: str
    severity: str = "medium"


class ConsultingOpportunity(BaseModel):
    title: str
    description: str
    importance: str = "medium"


class ConsultingResult(BaseModel):
    question: str

    executive_summary: str = ""

    problem_definition: str = ""

    findings: List[ConsultingFinding] = Field(
        default_factory=list
    )

    kpis: List[ConsultingKPI] = Field(
        default_factory=list
    )

    trends: List[ConsultingTrend] = Field(
        default_factory=list
    )

    comparisons: List[ConsultingComparison] = Field(
        default_factory=list
    )

    opportunities: List[ConsultingOpportunity] = Field(
        default_factory=list
    )

    risks: List[ConsultingRisk] = Field(
        default_factory=list
    )

    recommendations: List[ConsultingRecommendation] = Field(
        default_factory=list
    )

    data_limitations: List[str] = Field(
        default_factory=list
    )

    sources: List[dict] = Field(
        default_factory=list
    )