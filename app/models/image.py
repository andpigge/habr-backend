from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.core.db import Base


class ArticleImage(Base):
    name = Column(String(100), unique=True, nullable=False)
    size = Column(Integer, nullable=False)
    path: Column(String(100), unique=True, nullable=False)
    # type
