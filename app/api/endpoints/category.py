import re
from fastapi import APIRouter, Depends, UploadFile, File, Response
from sqlalchemy.ext.asyncio import AsyncSession
from app.crud.category import category_crud

from fastapi_pagination import Page, paginate
# from fastapi_pagination.ext.sqlalchemy import paginate

from app.core.db import get_async_session

router = APIRouter()


session: AsyncSession = Depends(get_async_session)

@router.get('/',
            response_model=Page,
            response_model_exclude_none=True,
            summary='Получить все категории')
async def get_all_category(session=session):
    category = await category_crud.get_multi(session)
    return paginate(category)


@router.post('/file')
def upload_file_bytes(file: UploadFile = File(...), session=session):

    return file

    # print(dir(file.file))

    # file_location = f"app/uploaded_files/{file.filename}"
    # with open(file_location, "wb+") as file_object:
    #     file_object.write(file.file.read())
    # return {"info": f"file '{file.filename}' saved at '{file_location}'"}


@router.get('/file')
def upload_file_bytes(session=session):

    pass
