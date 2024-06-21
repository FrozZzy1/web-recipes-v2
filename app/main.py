from fastapi import FastAPI
from app.api.handlers.category import router as category_router

app = FastAPI(
    title='Рецепты',
)


@app.get('/api/v1/ping')
async def get_ping():
    return {'status': 'ok'}


app.include_router(category_router)
