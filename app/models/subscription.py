# from sqlalchemy import Column, ForeignKey, Integer

# from app.core.db import Base


# # При подписке отправляется специальный роут, тут заполняется кто на кого подписан,
# # и автоматически заполнить поле is_subscription=True пользователя, following_id
# class Subscription(Base):
#     user_id = Column(Integer, ForeignKey('user.id'))
#     following_id = Column(Integer, ForeignKey('user.id'))
