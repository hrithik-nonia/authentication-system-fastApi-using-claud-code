from datetime import datetime, timezone
from typing import Optional
from pydantic import BaseModel, EmailStr, Field
from app.utils.py_object_id import PyObjectId
from app.constants.roles import Role


class UserModel(BaseModel):
    """
    Yeh represent karta hai User document MongoDB mein kaise store hota hai.
    """
    id: Optional[PyObjectId] = Field(default=None, alias="_id")
    name: str
    email: EmailStr
    hashed_password: str
    role: Role = Role.USER
    is_active: bool = True
    is_verified: bool = False
    refresh_token: Optional[str] = None
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    model_config = {
        "populate_by_name": True,
        "arbitrary_types_allowed": True,
        "json_encoders": {},
    }