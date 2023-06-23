from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional


class Tags(BaseModel):
    id: int
    name: str

class Author(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str

    class Config:
        orm_mode = True

class Subcategory(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class Category(BaseModel):
    id: int
    name: str
    subcategories: list[Subcategory]

    class Config:
        orm_mode = True

class ArticleDB(BaseModel):
    id: int
    create_date: datetime
    title: str
    description: str
    rating: int
    category: Category
    author: Author
    tags: list[Tags]

    class Config:
        orm_mode = True


class ArticleCreate(BaseModel):
    title: str = Field(max_length=100,
                       example='Каскадные таблицы стилей',
                       description='Можно вводить в любом регистре')
    description: str = Field(example='Каскадные таблицы стилей (Cascading Style Sheets, CSS) — это стандарт, определяющий представление данных в браузере...')
    category: str = Field(max_length=50,
                    example='Frontend',
                    description='Категория статьи')
    subcategories: list[str] = Field(example=['Css', 'Стили', 'Браузер'],
                                     description='Подкатегории статьи. Передается списком.')


class ArticleUpdate(BaseModel):
    title: Optional[str] = Field(max_length=100,
                                 example='Каскадные таблицы стилей',
                                 description='Можно вводить в любом регистре')
    description: Optional[str] = Field(example='Каскадные таблицы стилей (Cascading Style Sheets, CSS) — это стандарт, определяющий представление данных в браузере...')
    category: Optional[str] = Field(max_length=50,
                                    example='Frontend',
                                    description='Категория статьи')
    subcategories: Optional[list[str]] = Field(example=['Css', 'Стили', 'Браузер'],
                                               description='Подкатегории статьи. Передается списком.')


class ArticleUpdateRating(BaseModel):
    rating: int = Field(example=10, gt=9, lt=11)
