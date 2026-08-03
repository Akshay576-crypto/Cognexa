from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from enum import Enum

class ProjectCreate(BaseModel):
    project_name: str = Field(..., min_length=3, max_length=200)
    description: Optional[str] = None
    project_type: Optional[str] = None

class ProjectUpdate(BaseModel):
    project_name: Optional[str] = Field(None, min_length=3, max_length=200)
    description: Optional[str] = None
    project_type: Optional[str] = None
    status: Optional[str] = None

class ProjectResponse(BaseModel):
    project_id: int
    user_id: int
    project_name: str
    description: Optional[str]
    project_type: Optional[str]
    status: str
    created_at : datetime
    updated_at : datetime

class ProjectStatus(str,Enum):
    ACTIVE = "ACTIVE"
    ARCHIVED = "ARCHIVED"
    DELETE = "DELETE"
