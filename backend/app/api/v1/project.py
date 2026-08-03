from fastapi import APIRouter, Depends
from app.schemas.project_schema import ProjectCreate, ProjectUpdate
from app.services.project_service import ProjectService
from app.auth.dependencies import get_current_user


router = APIRouter(
    prefix="/api/v1/projects",
    tags=["Projects"]
)

service = ProjectService()


# ----------------------------
# Create Project
# ----------------------------
@router.post("/")
def create_project(
    project: ProjectCreate,
    current_user=Depends(get_current_user)
):

    return service.create_project(
        user_id=current_user["user_id"],
        project_name=project.project_name,
        description=project.description,
        project_type=project.project_type
    )


# ----------------------------
# Get All Projects
# ----------------------------
@router.get("/")
def get_all_projects(
    current_user=Depends(get_current_user)
):

    return service.get_all_projects(
        user_id=current_user["user_id"]
    )


# ----------------------------
# Get Project By ID
# ----------------------------
@router.get("/{project_id}")
def get_project(
    project_id: int,
    current_user=Depends(get_current_user)
):

    return service.get_project_by_id(
        project_id=project_id,
        user_id=current_user["user_id"]
    )


# ----------------------------
# Update Project
# ----------------------------
@router.put("/{project_id}")
def update_project(
    project_id: int,
    project: ProjectUpdate,
    current_user=Depends(get_current_user)
):

    return service.update_project(
        project_id=project_id,
        user_id=current_user["user_id"],
        project_name=project.project_name,
        description=project.description,
        project_type=project.project_type
    )

# ----------------------------
# Delete Project
# ----------------------------
@router.delete("/{project_id}")
def delete_project(
    project_id: int,
    current_user=Depends(get_current_user)
):

    return service.delete_project(
        project_id=project_id,
        user_id=current_user["user_id"]
    )