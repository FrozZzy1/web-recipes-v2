from fastapi import APIRouter, Depends

from app.api.schemes.category import AddCategoryScheme
from app.services.category import CategoryService

router = APIRouter(
    prefix='/categories',
    tags=['Категории'],
)


@router.post('')
async def create(
    category: AddCategoryScheme = Depends(),
):
    category_id = await CategoryService.create(category)
    return {
        'status': 'ok',
        'id': category_id,
    }
