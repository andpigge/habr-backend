from fastapi import APIRouter, Depends
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
