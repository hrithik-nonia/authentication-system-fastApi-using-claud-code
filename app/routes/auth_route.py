from fastapi import APIRouter, status, Depends
from app.schemas.user_schema import UserCreate, UserResponse , UserLogin
from app.services.auth_service import auth_service
from app.dependencies.auth_dependency import get_current_user

router = APIRouter(prefix="/auth", tags=["Authentication"])


# signup route
@router.post("/signup", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def signup(user_data: UserCreate):
    return await auth_service.signup(user_data)


# login route
@router.post("/login")
async def login(credentials: UserLogin):
    return await auth_service.login(credentials)


# protected route 
@router.get("/me", response_model=UserResponse)
async def get_me(current_user: dict = Depends(get_current_user)):
    return UserResponse(
        id=str(current_user["_id"]),
        name=current_user["name"],
        email=current_user["email"],
        role=current_user["role"],
        is_active=current_user["is_active"],
        is_verified=current_user["is_verified"],
        created_at=current_user["created_at"],
    )