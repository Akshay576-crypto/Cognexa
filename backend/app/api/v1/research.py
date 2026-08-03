from fastapi import APIRouter, Depends

from app.auth.dependencies import get_current_user
from app.agents.research_agent import ResearchAgent
from app.schemas.research_schema import (
    ResearchRequest,
    ResearchResponse,
)


router = APIRouter(
    prefix="/api/v1/research",
    tags=["Research"],
)


agent = ResearchAgent()


@router.post(
    "/",
    response_model=ResearchResponse,
)
def research(
    request: ResearchRequest,
    current_user=Depends(get_current_user),
):

    answer = agent.answer(
        question=request.question,
        document_id=request.document_id,
        top_k=request.top_k,
    )

    return ResearchResponse(
        question=request.question,
        answer=answer,
        document_id=request.document_id,
    )