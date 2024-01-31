import logging
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from app.db.base import setup_db
from fastapi import FastAPI

log = logging.getLogger(__name__)


async def startup(app: FastAPI) -> None:
    app.state.db_engine = await setup_db()


async def shutdown(app: FastAPI) -> None:
    await app.state.db_engine.dispose()


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    await startup(app)
    yield
    await shutdown(app)
