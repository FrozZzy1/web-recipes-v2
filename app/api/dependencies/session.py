from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from app.core.config import DATABASE_URL

database_url = DATABASE_URL
async_engine = create_async_engine(database_url)

async_session = async_sessionmaker(async_engine)
