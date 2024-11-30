from fastapi import APIRouter, Depends

from src.app.dependencies import get_product_service
from src.app.schemes.external import RequestProduct
from src.app.services import ProductService

router = APIRouter(prefix='/products', tags=['Products', 'ClickHouse'])


@router.post(
    path='/',
    # response_model=,
    name='Создать',
    response_description='Создать',
    description='Создать',
)
async def add_user(
    items: list[RequestProduct],
    product_service: ProductService = Depends(get_product_service),
):
    # ) -> ResponseUser:
    return await product_service.add(
        items=(_.to_internal_model() for _ in items),
    )
