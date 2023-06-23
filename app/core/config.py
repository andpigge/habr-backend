from typing import Optional
from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'Фонд QRKot'
    app_description: str = 'API для фонда сбора пожертвования на различные целевые проекты нуждающихся хвостатым.'
    database_url: str = 'sqlite+aiosqlite:///./habr.db'
    secret: str = 'secret'

    class Config:
        env_file = '.env'


settings = Settings()
