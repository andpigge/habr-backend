from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Article, Category, Subcategory
from fastapi.encoders import jsonable_encoder

from app.crud.article import article_crud


async def check_category_exists(category: str,
                                session: AsyncSession) -> Category:

    category = await article_crud.get_category_by_name(category, session)

    if category is None:
        raise HTTPException(
            status_code=400,
            detail='Категория с таким именем не существует!',
        )

    return category


async def check_subcategories_exists(subcategories: list[str],
                                     session: AsyncSession) -> Subcategory:

    subcategories_string = ', '.join(subcategories)

    subcategories = await article_crud.get_subcategory_by_name(subcategories, session)

    if subcategories is None:
        raise HTTPException(
            status_code=400,
            detail=f'Подкатегории: {subcategories_string} с таким именами не существуют!',
        )

    return subcategories


async def check_article_exists(article_id: str,
                               session: AsyncSession) -> Article:

    article = await article_crud.get_article_by_id(article_id, session)

    if article is None:
        raise HTTPException(
            status_code=400,
            detail=f'Статья с id: "{article_id}" не существует или статью пытается изменить или удалить не автор!',
        )

    return article


async def check_user_is_author_article(article_author_id: int,
                                       user_id: int) -> None:

    if not article_author_id == user_id:
        raise HTTPException(
            status_code=400,
            detail=f'Изменить или удалить статью может только автор!',
        )


async def check_title_duplicate(title: str,
                                session: AsyncSession) -> None:

    article = await article_crud.get_article_by_title(title, session)

    if article is not None:
        raise HTTPException(
            status_code=400,
            detail=f'Такой заголовок: "{title}" в других статьях уже существует!',
        )
