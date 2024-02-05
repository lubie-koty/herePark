from collections.abc import AsyncGenerator

from app.db.base import AsyncSessionFactory
from app.services.users import UserService
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession
from typing_extensions import Annotated


async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionFactory() as session:
        yield session
        await session.rollback()


async def get_user_service(db_session: Annotated[AsyncSession, Depends(get_db_session)]) -> UserService:
    return UserService(db_session)


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')
