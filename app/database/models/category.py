from sqlalchemy.orm import Mapped, mapped_column

from app.database.models.base import Base


class CategoryOrm(Base):
    __tablename__ = 'categories'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
