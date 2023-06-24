from typing import Optional
from fastapi import APIRouter, Depends
from fastapi import APIRouter, UploadFile, File
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.user import current_user
from app.models.user import User

from app.services.files import format_filename, save_file_to_uploads

from app.core.db import get_async_session


router = APIRouter()

session: AsyncSession = Depends(get_async_session)

@router.post('/',
            #  response_model=ArticleCreateResponse,
             summary='Сохранить файл')
async def create_file(name: Optional[str] = None,
                      file: list[UploadFile] = File(...),
                      #  user: User = Depends(current_user),
                      session=session):

    for item in file:
        full_name = format_filename(item, name)

    await save_file_to_uploads(file, full_name)

    # Сохранить в БД

    return item
