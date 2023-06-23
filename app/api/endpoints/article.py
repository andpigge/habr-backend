from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.article import ArticleCreate, ArticleDB, ArticleUpdate, ArticleUpdateRating
from app.crud.article import article_crud
from app.api.validators import check_category_exists, check_subcategories_exists, check_title_duplicate, check_article_exists, check_user_is_author_article
from app.core.user import current_user
from app.models.user import User
from fastapi.encoders import jsonable_encoder

from fastapi_pagination import Page, paginate

from app.core.db import get_async_session

router = APIRouter()


session: AsyncSession = Depends(get_async_session)

# "total": 2,
# "page": 1,
# "size": 50,
# "pages": 1
# [ArticleAllDB]
@router.get('/',
            response_model=Page[ArticleDB],
            summary='Получить все статьи')
async def get_all_article(session=session):
    article = await article_crud.get_all_articles(session)

    return paginate(article)


@router.get('/{article_id}',
            response_model=ArticleDB,
            summary='Получить статью')
async def get_article(article_id: int,
                      session=session):
    article = await article_crud.get_article_by_id(article_id, session)
    article = await article_crud.generate_article(article)

    return article


@router.post('/',
             response_model=ArticleDB,
             summary='Создать статью')
async def create_new_article(article: ArticleCreate,
                             user: User = Depends(current_user),
                             session=session):

    await check_title_duplicate(article.title, session)

    subcategories = await check_subcategories_exists([x.lower() for x in article.subcategories], session)

    category = await check_category_exists(article.category.lower(), session)

    new_article = await article_crud.save_article_category(article, category, subcategories, user, session)

    return new_article


@router.patch('/{article_id}',
              response_model_exclude_none=True,
              response_model=ArticleDB,
              summary='Обновить статью')
async def update_article(article_id: int,
                         obj_in: ArticleUpdate,
                         user: User = Depends(current_user),
                         session=session):

    article = await check_article_exists(article_id, session)

    await check_user_is_author_article(article.author.id, user.id)

    if obj_in.title is not None:
        await check_title_duplicate(obj_in.title, session)

    category = None
    if obj_in.category is not None:
        category = await check_category_exists(obj_in.category.lower(), session)

    subcategories = None
    if obj_in.subcategories is not None:
        subcategories = await check_subcategories_exists([x.lower() for x in obj_in.subcategories], session)

    new_article = await article_crud.update_article_category(article, category, obj_in, subcategories, session)

    return new_article


@router.put('/{article_id}/rating',
              response_model=ArticleDB,
              summary='Обновить рейтинг статьи')
async def update_rating_in_article(article_id: int,
                             obj_in: ArticleUpdateRating,
                             user: User = Depends(current_user),
                             session=session):

    article = await check_article_exists(article_id, session)

    await check_user_is_author_article(article.author.id, user.id)

    new_article = await article_crud.update_rating_in_article(article, obj_in, session)

    return new_article


@router.delete('/{article_id}',
              response_model=ArticleDB,
              dependencies=[Depends(current_user)],
              summary='Удалить статью')
async def update_reservation(article_id: int,
                             user: User = Depends(current_user),
                             session=session):

    article = await check_article_exists(article_id, session)

    await check_user_is_author_article(article.author.id, user.id)

    article = await article_crud.generate_article(article)

    return article
