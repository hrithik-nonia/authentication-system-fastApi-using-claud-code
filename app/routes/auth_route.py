from fastapi import APIRouter, status
from app.schemas.user_schema import UserCreate, UserResponse
from app.services.auth_service import auth_service

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/signup", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def signup(user_data: UserCreate):
    return await auth_service.signup(user_data)