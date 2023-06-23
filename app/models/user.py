
from sqlalchemy import Column, String, Boolean
from sqlalchemy.orm import relationship
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable

from app.core.db import Base


# is_subscription - подписан ли я на этого пользоваля
# subscriptions - кто на меня подписан

# Реализовать
# Увидеть кто на меня подписался, и на кого я подписался
# Статьи которые пользователь создал, и статьи которые пользователь сохранил
class User(SQLAlchemyBaseUserTable[int], Base):
    first_name = Column(String(20), nullable=True)
    last_name = Column(String(20), nullable=True)
    is_subscription = Column(Boolean, default=False)

    articles = relationship('Article', cascade='delete', back_populates='author')

    # categories = relationship(Category)
    # subscriptions = relationship('Subscription', cascade='delete')
