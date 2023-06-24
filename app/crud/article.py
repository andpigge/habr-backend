from app.models import Article, Category, Subcategory
from app.crud.base import CRUDBase
from sqlalchemy.ext.asyncio import AsyncSession

from sqlalchemy import select, and_
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import joinedload, selectinload, subqueryload, lazyload

from app.core.db import AsyncSessionLocal
from app.crud.base import CRUDBase


# Метод subqueryload() больше подходит для загрузки связанных коллекций, а метод joinedload() лучше подходит для отношений «многие к одному».
""" and_(
        self.model.author_id == user.id
    ) """


class CRUDArticle(CRUDBase):

    """  Затипизировать все! """
    async def get_article_by_title(self,
                                   title: str,
                                   session: AsyncSession) -> Article:

        """ Вернуть любую статью по заголовку статьи. """
        article = await session.execute(select(self.model).where(
            self.model.title == title
        ))

        return article.scalars().first()


    async def get_article_by_id(self,
                                article_id: int,
                                session: AsyncSession) -> Article:

        """ Вернуть статью автора по id статьи. """
        article = await session.execute(select(self.model).where(
            self.model.id == article_id,
        ).options(
            subqueryload(self.model.article_subcategory),
            subqueryload(self.model.category),
            subqueryload(self.model.author),
            subqueryload(self.model.tags)
        ))

        return article.scalars().first()

    async def get_all_articles(self, session: AsyncSessionLocal):
        db_objs = await session.execute(select(self.model).options(
            subqueryload(self.model.article_subcategory),
            subqueryload(self.model.category),
            subqueryload(self.model.author),
            subqueryload(self.model.tags)
        ))
        db_objs = db_objs.scalars().all()

        new_arr = []
        for db_obj in db_objs:
            db_obj = jsonable_encoder(db_obj)

            db_obj['category']['subcategories'] = db_obj['article_subcategory']
            db_obj.pop('article_subcategory', None)

            new_arr.append(db_obj)

        return new_arr

    async def get_category_by_name(self, category, session):
        category = await session.execute(select(Category).where(Category.name == category))
        return category.scalars().first()

    async def get_subcategory_by_name(self, subcategories, session):
        subcategories = await session.execute(select(Subcategory).where(Subcategory.name.in_(subcategories)))
        return subcategories.scalars().all()

    async def save_article_category(self, article, category, subcategories, user, session: AsyncSessionLocal):
        article = article.dict()

        article.pop('subcategories', None)

        article.pop('category', None)
        article['author_id'] = user.id
        article['category_id'] = category.id

        article['title'] = article['title'].capitalize()
        db_obj = Article(**article)

        print(subcategories)
        for subcategory in subcategories:
            db_obj.article_subcategory.append(subcategory)

        session.add(db_obj)

        await session.commit()
        await session.refresh(db_obj)

        db_obj = await self.get_article_by_id(db_obj.id, session)
        db_obj = jsonable_encoder(db_obj)
        db_obj['category']['subcategories'] = db_obj['article_subcategory']
        return db_obj

    async def update_article_category(self, article, category, obj_in, subcategories, session: AsyncSessionLocal):
        obj_data = jsonable_encoder(article)

        update_data = obj_in.dict(exclude_unset=True)

        if category is not None:
            update_data.pop('category', None)
            article.category_id = category.id

        if subcategories is not None:
            update_data.pop('subcategories', None)
            article.article_subcategory = []

            for subcategory in subcategories:
                article.article_subcategory.append(subcategory)

        if 'title' in update_data:
            update_data['title'] = update_data['title'].capitalize()

        for field in obj_data:
            if field in update_data:
                setattr(article, field, update_data[field])

        session.add(article)

        await session.commit()

        await session.refresh(article)

        article = jsonable_encoder(article)
        article['category']['subcategories'] = article['article_subcategory']
        return article

    async def update_rating_in_article(self, article, obj_in, session: AsyncSessionLocal):
        article.rating += obj_in.rating

        session.add(article)

        await session.commit()
        await session.refresh(article)

        article = jsonable_encoder(article)
        article['category']['subcategories'] = article['article_subcategory']
        return article

    async def generate_article(self, article):
        article = jsonable_encoder(article)
        article['category']['subcategories'] = article['article_subcategory']
        return article


article_crud = CRUDArticle(Article)
