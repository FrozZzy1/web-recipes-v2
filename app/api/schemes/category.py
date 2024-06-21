from pydantic import BaseModel


class AddCategoryScheme(BaseModel):
    title: str
