import asyncio
import os

from sqlalchemy import Column, Float, Integer, MetaData, Table
from sqlalchemy.ext.asyncio import create_async_engine

meta = MetaData()
spaces = Table(
    'spaces', meta,
    Column('space_id', Integer, primary_key=True),
    Column('latitude', Float),
    Column('longitude', Float),
    Column('reservation_limit', Integer)
)


async def insert_data():
    engine = create_async_engine(os.getenv('HP_DB_URI'))

    async with engine.begin() as conn:
        await conn.execute(
            spaces.insert(),
            [
                {'latitude': 51.25148, 'longitude': 22.559841, 'reservation_limit': 5},
                {'latitude': 51.248364, 'longitude': 22.565764, 'reservation_limit': 5},
                {'latitude': 51.246967, 'longitude': 22.545851, 'reservation_limit': 15},
                {'latitude': 51.241389, 'longitude': 22.522354, 'reservation_limit': 10},
                {'latitude': 51.234296, 'longitude': 22.544241, 'reservation_limit': 10},
                {'latitude': 51.240557, 'longitude': 22.558618, 'reservation_limit': 5}
            ]
        )

    await engine.dispose()

if __name__ == '__main__':
    asyncio.run(insert_data())
