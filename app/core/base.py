""" Импорты класса Base и всех моделей для Alembic. """
from app.core.db import Base  # noqa
from app.models import User, Article, Category, Tag, Subcategory, category_user, article_subcategory  # noqa
# , SavedArticle, Subcategory, Subscription, Tag
