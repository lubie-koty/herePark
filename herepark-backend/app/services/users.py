import logging

from app.db.models.users import User
from app.interfaces.users import IUserService
from app.schemas.users import UserRegistrationData
from app.utils.security import get_password_hash, verify_password
from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

log = logging.getLogger(__name__)


class UserService(IUserService):
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def get_user(self, username: str) -> User | None:
        q = select(User).where(User.username == username)
        return await self.db_session.scalar(q)

    async def add_user(self, register_data: UserRegistrationData) -> None:
        try:
            async with self.db_session.begin():
                existing_user = await self.get_user(register_data.username)
                if existing_user:
                    raise HTTPException(
                        status_code=status.HTTP_400_BAD_REQUEST,
                        detail='User already exists',
                        headers={'WWW-Authenticate': 'Bearer'}
                    )
                new_user = User(
                    username=register_data.username,
                    password_hash=get_password_hash(register_data.password),
                    first_name=register_data.first_name,
                    last_name=register_data.last_name
                )
                self.db_session.add(new_user)
        except Exception:
            log.error('Error while creating a new user', exc_info=True)
            raise
        return new_user

    async def authenticate_user(self, username: str, password: str) -> User | None:
        user = await self.get_user(username)
        if not user or not verify_password(password, user.password_hash):
            return None
        return user
