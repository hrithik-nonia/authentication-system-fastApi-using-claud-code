from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, Field
from app.constants.roles import Role


class UserCreate(BaseModel):
    """Signup request ke liye — client se yeh data aayega."""
    name: str = Field(..., min_length=2, max_length=50)
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    """Login request ke liye."""
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    """API response ke liye """
    id: str
    name: str
    email: EmailStr
    role: Role
    is_active: bool
    is_verified: bool
    created_at: datetime

    model_config = {
        "from_attributes": True
    }