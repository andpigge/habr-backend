from sqlalchemy import Column, ForeignKey, Integer, Table

from app.core.db import Base


article_subcategory = Table('article_subcategory',
                             Base.metadata,
                             Column('article_id', Integer, ForeignKey('article.id')),
                             Column('subcategory_id', Integer, ForeignKey('subcategory.id')))
