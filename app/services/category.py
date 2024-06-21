from app.api.schemes.category import AddCategoryScheme
from app.database.repositories.category import CategoryRepository


class CategoryService:
    @classmethod
    async def create(cls, data: AddCategoryScheme):
        result = await CategoryRepository.create(data)
        return result
