from contextlib import suppress
from sqlalchemy.exc import IntegrityError

from app.api.schemes.category import AddCategoryScheme
from app.database.models.category import CategoryOrm
from app.api.dependencies.session import async_session


class CategoryRepository:
    @classmethod
    async def create(
        cls,
        data: AddCategoryScheme
    ) -> dict:
        with suppress(IntegrityError):
            async with async_session() as session:
                category = CategoryOrm(
                    title=data.title,
                )
                session.add(category)
                await session.commit()

                return {
                    'data': category.id,
                }
