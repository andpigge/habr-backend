from fastapi import APIRouter

# from app.api.endpoints import (charity_project_router, donation_router,
#                                user_router)

from app.api.endpoints import user_router, article_router, category_router, save_files_router

main_router = APIRouter()

# main_router.include_router(charity_project_router,
#                            prefix='/charity_project',
#                            tags=['Charity Project'])

# main_router.include_router(donation_router,
#                            prefix='/donation',
#                            tags=['Donation'])

main_router.include_router(article_router,
                           prefix='/article',
                           tags=['Статьи'])

main_router.include_router(category_router,
                           prefix='/category',
                           tags=['Категории'])

main_router.include_router(save_files_router,
                           prefix='/file',
                           tags=['Файлы'])

main_router.include_router(user_router)
