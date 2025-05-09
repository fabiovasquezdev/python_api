from passlib.context import CryptContext
from app.repository.user import UserRepository
from app.schemas.user import UserCreate, UserUpdate, User
from typing import List, Optional

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def _hash_password(self, password: str) -> str:
        return pwd_context.hash(password)

    def create_user(self, user: UserCreate) -> User:
        hashed_password = self._hash_password(user.password)
        user_data = user.dict()
        user_data["password"] = hashed_password
        return self.user_repository.create(UserCreate(**user_data))

    def get_user(self, user_id: int) -> Optional[User]:
        return self.user_repository.get_by_id(user_id)

    def get_user_by_email(self, email: str) -> Optional[User]:
        return self.user_repository.get_by_email(email)

    def get_users(self) -> List[User]:
        return self.user_repository.get_all()

    def update_user(self, user_id: int, user: UserUpdate) -> Optional[User]:
        if user.password:
            user.password = self._hash_password(user.password)
        return self.user_repository.update(user_id, user)

    def delete_user(self, user_id: int) -> bool:
        return self.user_repository.delete(user_id)

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return pwd_context.verify(plain_password, hashed_password) 