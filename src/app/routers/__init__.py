from fastapi import APIRouter

from app.routers.template_routers import router as template_router
from app.settings import settings

router = APIRouter(prefix='/v1', include_in_schema=settings.DEVELOP)

router.include_router(template_router)
