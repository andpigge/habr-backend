from fastapi import FastAPI

from app.api.routers import main_router
from app.core.config import settings
from fastapi_pagination import add_pagination

app = FastAPI(title=settings.app_title,
              description=settings.app_description)

app.include_router(main_router)

add_pagination(app)
