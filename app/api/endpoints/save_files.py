from fastapi import APIRouter, Depends
router = APIRouter()
from fastapi import APIRouter, UploadFile, File
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.user import current_user
from app.models.user import User

from app.core.db import get_async_session


session: AsyncSession = Depends(get_async_session)

@router.post('/',
            #  response_model=ArticleCreateResponse,
             summary='Сохранить файл')
async def create_new_article(file: list[UploadFile] = File(...),
                            #  user: User = Depends(current_user),
                             session=session):

    print(file)

    return 1
