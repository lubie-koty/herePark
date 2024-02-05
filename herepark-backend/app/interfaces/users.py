from abc import ABC, abstractmethod

from app.db.models.users import User
from app.schemas.users import UserRegistrationData


class IUserService(ABC):
    @abstractmethod
    async def get_user(username: str) -> User | None:
        ...

    @abstractmethod
    async def add_user(register_data: UserRegistrationData) -> User:
        ...

    @abstractmethod
    async def authenticate_user(username: str, password: str) -> User | None:
        ...
