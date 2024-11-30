from typing import Iterable

from src.app.repositories import ProductRepository
from src.app.schemes.internal import InternalProduct


class ProductService:
    def __init__(self, product_repository: ProductRepository):
        self.product_repository: ProductRepository = product_repository

    async def add(
        self,
        *,
        items: Iterable[InternalProduct],
    ) -> None:
        print(items)
        return None
