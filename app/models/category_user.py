from sqlalchemy import Column, ForeignKey, Integer, Table

from app.core.db import Base


category_user = Table('category_user',
                      Base.metadata,
                      Column('category_id', Integer, ForeignKey('category.id')),
                      Column('user_id', Integer, ForeignKey('user.id')))
