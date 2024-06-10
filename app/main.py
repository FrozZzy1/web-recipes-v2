from fastapi import FastAPI

app = FastAPI(
    title='Рецепты',
)


@app.get('/api/v1/ping')
async def get_ping():
    return {'status': 'ok'}
