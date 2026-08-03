from fastapi import APIRouter, Depends

from app.auth.dependencies import get_current_user
from app.agents.consulting_agent import ConsultingAgent
from app.schemas.consulting_schema import (
    ConsultingRequest,
    ConsultingResponse,
)


router = APIRouter(
    prefix="/api/v1/consulting",
    tags=["Consulting"],
)


agent = ConsultingAgent()


@router.post(
    "/",
    response_model=ConsultingResponse,
)
def consulting(
    request: ConsultingRequest,
    current_user=Depends(get_current_user),
):

    analysis = agent.analyze(
        question=request.question,
        context=request.context,
        sources=request.sources,
    )

    return ConsultingResponse(
        question=request.question,
        analysis=analysis,
    )