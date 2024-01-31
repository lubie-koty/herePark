import logging

from app.core.config import settings
from sqlalchemy.ext.asyncio import (AsyncAttrs, AsyncEngine,
                                    async_sessionmaker, create_async_engine)
from sqlalchemy.orm import DeclarativeBase

log = logging.getLogger(__name__)

AsyncSessionFactory = async_sessionmaker(
    autoflush=False,
    expire_on_commit=False
)


class Base(AsyncAttrs, DeclarativeBase):
    pass


async def setup_db() -> AsyncEngine:
    db_engine = create_async_engine(settings.DB_URI.unicode_string())
    try:
        test_connection = await db_engine.connect()
        await test_connection.close()
        log.info('Successfully connected to the database')
    except Exception:
        log.error('Error while connecting to the database', exc_info=True)
        raise
    AsyncSessionFactory.configure(bind=db_engine)
    return db_engine
