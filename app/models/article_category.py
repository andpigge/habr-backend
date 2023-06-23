from sqlalchemy import Column, ForeignKey, Integer, Table

from app.core.db import Base


article_category = Table('article_category',
                         Base.metadata,
                         Column('article_id', Integer, ForeignKey('article.id')),
                         Column('category_id', Integer, ForeignKey('category.id')))
