from collections.abc import AsyncGenerator

from app.db.base import AsyncSessionFactory
from sqlalchemy.ext.asyncio import AsyncSession


async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionFactory() as session:
        yield session
        await session.rollback()
