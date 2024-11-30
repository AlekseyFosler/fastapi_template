from datetime import datetime

from pydantic import UUID4, BaseModel, Field

from src.app.schemes.internal import InternalProduct


class RequestProduct(BaseModel):
    id: UUID4 = Field(
        description='Уникальный идентификатор продукта',
    )
    name: str = Field(
        description='Название продукта',
    )
    category: str = Field(
        description='Категория продукта',
    )
    brand: str = Field(
        description='Бренд продукта',
    )
    price: float = Field(
        description='Цена продукта',
    )
    discount: float = Field(
        description='Скидка на продукт (в процентах)',
    )
    stock_quantity: int = Field(
        description='Количество товара на складе',
    )
    is_available: bool = Field(
        description='Доступность продукта',
    )
    tags: list[str] = Field(
        description='Теги продукта',
    )
    rating: float = Field(
        description='Рейтинг продукта',
    )
    reviews_count: int = Field(
        description='Количество отзывов о продукте',
    )
    vendor_code: str = Field(
        description='Артикул продукта',
    )
    description: str = Field(
        description='Описание продукта',
    )
    created_at: datetime = Field(
        description='Дата создания',
    )
    updated_at: datetime = Field(
        description='Дата изменения',
    )
    is_delete: bool = Field(
        description='Объект удален',
    )

    def to_internal_model(self) -> InternalProduct:
        return InternalProduct(**self.model_dump())
