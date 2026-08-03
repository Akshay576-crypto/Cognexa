from fastapi import APIRouter, Depends

from app.auth.dependencies import get_current_user
from app.orchestration.intelligence_pipeline import IntelligencePipeline
from app.schemas.intelligence_schema import (
    IntelligenceRequest,
    IntelligenceResponse,
)


router = APIRouter(
    prefix="/api/v1/intelligence",
    tags=["Intelligence"],
)


pipeline = IntelligencePipeline()


@router.post(
    "/",
    response_model=IntelligenceResponse,
)
def intelligence(
    request: IntelligenceRequest,
    current_user=Depends(get_current_user),
):

    result = pipeline.run(
        question=request.question,
        document_id=request.document_id,
        top_k=request.top_k,
        sources=request.sources,
    )

    return result