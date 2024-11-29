from fastapi import APIRouter

from app.routers.template_root import router as root_router
from app.routers.template_routers import router as template_router
from app.routers.user import router as user_router
from app.settings import settings

router = APIRouter(prefix='/v1', include_in_schema=settings.app.DEVELOP)

router.include_router(template_router)
router.include_router(user_router)
router.include_router(root_router)
