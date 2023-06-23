from pydantic import BaseModel, Field


class Сategory(BaseModel):
    name: str = Field(max_length=50, description='Требуемая сумма', example='frontend')

    class Config:
        title = 'Response категории'
        orm_mode = True
