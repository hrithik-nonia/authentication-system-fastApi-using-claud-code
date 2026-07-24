from app.repositories.user_repositorie import user_repository
from app.models.user_model import UserModel
from app.schemas.user_schema import UserCreate, UserResponse , UserLogin
from app.security.password_handler import hash_password , verify_password
from app.exceptions.custom_exception import UserAlreadyExistsException , InvalidCredentialsException
from app.security.jwt_handler import create_access_token , create_refresh_token


class AuthService:
    def __init__(self):
        self.user_repository = user_repository

    async def signup(self, user_data: UserCreate) -> UserResponse:
        # Step 1: Check karo email already exist toh nahi karta
        existing_user = await self.user_repository.find_by_email(user_data.email)
        if existing_user:
            raise UserAlreadyExistsException(user_data.email)

        # Step 2: Password hash karo
        hashed_pw = hash_password(user_data.password)

        # Step 3: UserModel banao (DB-ready format)
        new_user = UserModel(
            name=user_data.name,
            email=user_data.email,
            hashed_password=hashed_pw,
        )

        # Step 4: Repository ko bolo save karne ke liye
        created_user = await self.user_repository.create(new_user)

        # Step 5: Response schema mein convert karke return karo
        return UserResponse(
            id=str(created_user["_id"]),
            name=created_user["name"],
            email=created_user["email"],
            role=created_user["role"],
            is_active=created_user["is_active"],
            is_verified=created_user["is_verified"],
            created_at=created_user["created_at"],
        )


    # login handler
    async def login(self, credentials: UserLogin) -> dict:
        # Step 1: User dhoondo email se
        user = await self.user_repository.find_by_email(credentials.email)
        if not user:
            raise InvalidCredentialsException()

        # Step 2: Password verify karo
        if not verify_password(credentials.password, user["hashed_password"]):
            raise InvalidCredentialsException()

        # Step 3: Check karo account active hai ya nahi
        if not user["is_active"]:
            raise InvalidCredentialsException()

        # Step 4: Tokens banao
        user_id = str(user["_id"])
        token_payload = {"sub": user_id, "role": user["role"]}

        access_token = create_access_token(token_payload)
        refresh_token = create_refresh_token(token_payload)

        # Step 5: Refresh token DB mein save karo
        await self.user_repository.update_refresh_token(user_id, refresh_token)

        # Step 6: Response return karo
        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer",
        }




auth_service = AuthService()


auth_service = AuthService()