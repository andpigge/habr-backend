from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Text, DateTime, Integer, ForeignKey

from app.core.db import Base


class Article(Base):
    title = Column(String(100), nullable=False)
    description = Column(Text, nullable=False)
    create_date = Column(DateTime, default=datetime.now, nullable=True)
    rating = Column(Integer, default=10)

    tags = relationship('Tag', cascade='delete', back_populates='article')

    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship('Category', back_populates='articles')

    author_id = Column(Integer, ForeignKey('user.id'))
    author = relationship('User', back_populates='articles')

    article_subcategory = relationship('Subcategory', secondary='article_subcategory', backref='articles')

    class Config:
        validate_assignment = True
