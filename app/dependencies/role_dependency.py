from fastapi import Depends, HTTPException, status
from app.dependencies.auth_dependency import get_current_user
from app.constants.roles import Role


def require_role(*allowed_roles: Role):
    async def role_checker(current_user: dict = Depends(get_current_user)) -> dict:
        user_role = current_user["role"]

        if user_role not in [role.value for role in allowed_roles]:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"You don't have permission to access this resource. Required role: {[r.value for r in allowed_roles]}"
            )

        return current_user

    return role_checker