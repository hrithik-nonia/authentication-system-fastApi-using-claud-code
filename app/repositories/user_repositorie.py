from typing import Optional
from app.database.mongodb import get_database
from app.models.user_model import UserModel


class UserRepository:
    def __init__(self):
        self.collection_name = "users"

    def _get_collection(self):
        db = get_database()
        return db[self.collection_name]

    async def find_by_email(self, email: str) -> Optional[dict]:
        collection = self._get_collection()
        user = await collection.find_one({"email": email})
        return user

    async def create(self, user: UserModel) -> dict:
        collection = self._get_collection()
        user_dict = user.model_dump(by_alias=True, exclude={"id"})
        result = await collection.insert_one(user_dict)
        created_user = await collection.find_one({"_id": result.inserted_id})
        return created_user


user_repository = UserRepository()