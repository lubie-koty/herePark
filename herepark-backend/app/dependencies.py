from collections.abc import AsyncGenerator

from app.db.base import AsyncSessionFactory
from app.db.models.users import User
from app.interfaces.users import IUserService
from app.services.parking import ParkingService
from app.services.users import UserService
from app.utils.security import JWTBearer
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


async def get_current_user(
    user_service: Annotated[IUserService, Depends(get_user_service)],
    token: Annotated[dict, Depends(JWTBearer())]
) -> User:
    username = token['sub']
    user = await user_service.get_user(username)
    return user


async def get_parking_service(db_session: Annotated[AsyncSession, Depends(get_db_session)]) -> ParkingService:
    return ParkingService(db_session)


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')
