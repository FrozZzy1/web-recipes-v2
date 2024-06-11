from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker

from app.database.models.base import Base

engine = create_async_engine(
    'sqlite+aiosqlite:///recipes.db'
)
session = async_sessionmaker(engine, expire_on_commit=False)


async def create_tables():
    async with engine.begin() as connect:
        await connect.run_sync(Base.metadata.create_all)


async def delete_tables():
    async with engine.begin() as connect:
        await connect.run_sync(Base.metadata.drop_all)
