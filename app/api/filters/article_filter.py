from datetime import datetime
from typing import Optional
from unicodedata import category
from fastapi_filter.contrib.sqlalchemy import Filter
from app.models import Article, Category, Subcategory
from pydantic import Field
from fastapi_filter import FilterDepends, with_prefix


class CategoryFilter(Filter):
    name: Optional[str]

    class Constants(Filter.Constants):
        model = Category
        search_model_fields = ['name']


class ArticleSubcategoryFilter(Filter):
    name: Optional[str]

    class Constants(Filter.Constants):
        model = Subcategory
        search_model_fields = ['name']


class ArticleFilter(Filter):
    # address__street: Optional[str]
    title__like: Optional[str] = Field(alias='title')
    category: Optional[CategoryFilter] = FilterDepends(with_prefix(prefix='category', Filter=CategoryFilter))
    article_subcategory: Optional[ArticleSubcategoryFilter] = Field(FilterDepends(with_prefix(prefix='article_subcategory', Filter=ArticleSubcategoryFilter)))
    # category_id: Optional[str]
    rating: Optional[int]
    id: Optional[int]
    create_date__gte: Optional[datetime] = Field(alias='create_date_from')

    class Constants(Filter.Constants):
        model = Article
        search_model_fields = ['title']

    class Config:
        allow_population_by_field_name = True
