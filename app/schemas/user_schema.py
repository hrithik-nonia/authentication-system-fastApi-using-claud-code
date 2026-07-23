from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, Field , field_validator
from app.constants.roles import Role
import re


class UserCreate(BaseModel):
    """Signup request ke liye — client se yeh data aayega."""
    name: str = Field(..., min_length=2, max_length=50)
    email: EmailStr
    password: str


    @field_validator("email")
    @classmethod
    def validate_gmail_only(cls, value: str) -> str:
        if not value.lower().endswith("@gmail.com"):
            raise ValueError("Only Gmail addresses are allowed (e.g. example@gmail.com)")
        return value.lower()

    @field_validator("password")
    @classmethod
    def validate_password_strength(cls, value: str) -> str:
        if len(value) < 8:
            raise ValueError("Password must be at least 8 characters long")
        if not re.search(r"[A-Z]", value):
            raise ValueError("Password must contain at least one uppercase letter")
        if not re.search(r"[a-z]", value):
            raise ValueError("Password must contain at least one lowercase letter")
        if not re.search(r"\d", value):
            raise ValueError("Password must contain at least one number")
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", value):
            raise ValueError("Password must contain at least one special character")
        return value
    

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