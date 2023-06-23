from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.core.db import Base


class Subcategory(Base):
    name = Column(String(50), unique=True, nullable=False)

    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship('Category', back_populates='subcategories')
