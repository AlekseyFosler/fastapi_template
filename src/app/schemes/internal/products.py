from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass(frozen=True)
class InternalProduct:
    id: UUID
    name: str
    category: str
    brand: str
    price: float
    discount: float
    stock_quantity: int
    is_available: bool
    tags: list[str]
    rating: float
    reviews_count: int
    vendor_code: str
    description: str
    created_at: datetime
    updated_at: datetime
    is_delete: bool
