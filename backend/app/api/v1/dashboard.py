from fastapi import APIRouter, Depends

from app.auth.dependencies import get_current_user
from app.dashboard.dashboard_engine import DashboardEngine
from app.schemas.dashboard_schema import (
    DashboardRequest,
    DashboardResponse,
)


router = APIRouter(
    prefix="/api/v1/dashboard",
    tags=["Dashboard"],
)


engine = DashboardEngine()


@router.post(
    "/",
    response_model=DashboardResponse,
)
def create_dashboard(
    request: DashboardRequest,
    current_user=Depends(get_current_user),
):

    result = engine.create_dashboard(
        title=request.title,
        description=request.description,
        kpis=request.kpis,
        charts=request.charts,
        tables=request.tables,
        maps=request.maps,
        sources=request.sources,
        theme_name=request.theme_name,
        grid_columns=request.grid_columns,
    )

    return DashboardResponse(
        dashboard=result["dashboard"],
        layout=result["layout"],
    )