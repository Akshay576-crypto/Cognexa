from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class UserCreate(BaseModel):

    full_name : str = Field(..., min_length=3, max_length=100)
    email : EmailStr
    password : str = Field(...,min_length=8,max_length=128)

class UserLogin(BaseModel):

    email : EmailStr
    password : str

class UserResponse(BaseModel):
    user_id: int
    full_name: str
    email: EmailStr
    role: str
    account_status: str

    class Config:
        from_attributes = True
