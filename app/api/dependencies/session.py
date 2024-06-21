from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from app.core.config import DATABASE_URL

database_url = DATABASE_URL
engine = create_async_engine(database_url)


def get_session():
    async_session = async_sessionmaker(
        engine,
        expire_on_commit=False,
    )
    with async_session() as session:
        yield session
