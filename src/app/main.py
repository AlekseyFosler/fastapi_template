from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.docs import get_redoc_html, get_swagger_ui_html
from fastapi.responses import ORJSONResponse
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles

from app.dependencies import init_dependencies
from app.routers import router
from app.settings import settings


@asynccontextmanager
async def lifespan(app: FastAPI):  # noqa
    init_dependencies()
    yield


app = FastAPI(
    title=settings.app.TITLE,
    version=settings.app.VERSION,
    docs_url=None,
    redoc_url=None,
    openapi_url=settings.app.OPENAPI_URL,
    default_response_class=ORJSONResponse,
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.get('/docs', include_in_schema=False)
async def custom_swagger_ui_html() -> HTMLResponse:
    return get_swagger_ui_html(
        openapi_url=settings.app.OPENAPI_URL,
        title=settings.app.TITLE,
        swagger_js_url='/static/swagger-ui-bundle.js',
        swagger_css_url='/static/swagger-ui.css',
    )


@app.get('/redoc', include_in_schema=False)
async def redoc_html() -> HTMLResponse:
    return get_redoc_html(
        openapi_url=settings.app.OPENAPI_URL,
        title=settings.app.TITLE,
        redoc_js_url='/static/redoc.standalone.js',
    )


app.mount('/static', StaticFiles(directory='app/static'), name='static')

app.include_router(router)

if __name__ == '__main__':
    uvicorn.run(
        app='main:app',
        host=settings.app.SERVER_HOST,
        port=settings.app.SERVER_PORT,
        log_level=settings.app.LOG_LEVEL,
        reload=settings.app.DEVELOP,
        use_colors=settings.app.DEVELOP,
    )
