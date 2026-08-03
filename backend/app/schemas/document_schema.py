from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from enum import Enum


class UploadStatus(str, Enum):
    UPLOADED = "uploaded"
    PROCESSING = "processing"
    INDEXED = "indexed"
    FAILED = "failed"


class DocumentResponse(BaseModel):
    document_id: int
    project_id: int
    user_id: int

    original_filename: str
    stored_filename: str

    file_extension: Optional[str]
    mime_type: Optional[str]
    file_size: Optional[int]

    upload_path: str

    upload_status: UploadStatus

    created_at: datetime
    updated_at: datetime