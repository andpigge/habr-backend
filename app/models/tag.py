from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.core.db import Base


class Tag(Base):
    name = Column(String(100), unique=True, nullable=False)

    article_id = Column(Integer, ForeignKey('article.id'))
    article = relationship('Article', back_populates='tags')
