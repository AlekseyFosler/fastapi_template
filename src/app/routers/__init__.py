from fastapi import APIRouter

from src.app.settings import settings

from .products import router as product_router
from .template_root import router as root_router
from .template_routers import router as template_router
from .user import router as user_router

router = APIRouter(
    prefix='/v1',
    include_in_schema=settings.app.DEVELOP,
)

router.include_router(template_router)
router.include_router(user_router)
router.include_router(root_router)
router.include_router(product_router)
