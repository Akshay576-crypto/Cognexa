from fastapi import Depends,UploadFile,APIRouter,File

from app.auth.dependencies import get_current_user
from app.services.document_service import DocumentService

router = APIRouter(
    prefix="/api/v1/documents",
    tags=["documents"]
)

service = DocumentService()

@router.post("/uploads/{project_id}")
def upload_document(project_id:int,file:UploadFile = File(...) ,current_user=Depends(get_current_user)):

    return service.upload_document(project_id=project_id,user_id=current_user["user_id"],file=file)

@router.get("/{project_id}")
def get_all_documents(project_id:int,current_user=Depends(get_current_user)):

    return service.get_all_documents(
        project_id=project_id,
        user_id=current_user["user_id"]
    )

@router.delete("/{documnet_id}")
def delete_documnet(document_id:int,current_user=Depends(get_current_user)):

    return service.delete_document(
        document_id=document_id,
        user_id=current_user["user_id"]
    )

