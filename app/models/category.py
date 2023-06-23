from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from app.core.db import Base


class Category(Base):
    name = Column(String(50), unique=True, nullable=False)

    users = relationship('User', secondary='category_user', backref='categories')

    subcategories = relationship('Subcategory', cascade='delete', back_populates='category')

    articles = relationship('Article')

    class Config:
        validate_assignment = True
