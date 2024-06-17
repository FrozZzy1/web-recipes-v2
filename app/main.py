from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.database.db import delete_tables
from app.database.db import create_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    await create_tables()
    yield


app = FastAPI(
    title='Рецепты',
    lifespan=lifespan,
)


@app.get('/api/v1/ping')
async def get_ping():
    return {'status': 'ok'}
