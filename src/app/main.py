import uvicorn
from fastapi import FastAPI
from fastapi.openapi.docs import get_redoc_html, get_swagger_ui_html
from fastapi.responses import HTMLResponse, ORJSONResponse
from settings import settings
from starlette.staticfiles import StaticFiles

from app.routers import router

app = FastAPI(
    title=settings.TITLE,
    version=settings.VERSION,
    docs_url=None,
    redoc_url=None,
    openapi_url=settings.OPENAPI_URL,
    default_response_class=ORJSONResponse,
)


@app.get('/docs', include_in_schema=False)
async def custom_swagger_ui_html() -> HTMLResponse:
    return get_swagger_ui_html(
        openapi_url=settings.OPENAPI_URL,
        title=settings.TITLE,
        swagger_js_url='/static/swagger-ui-bundle.js',
        swagger_css_url='/static/swagger-ui.css',
    )


@app.get('/redoc', include_in_schema=False)
async def redoc_html() -> HTMLResponse:
    return get_redoc_html(
        openapi_url=settings.OPENAPI_URL,
        title=settings.TITLE,
        redoc_js_url='/static/redoc.standalone.js',
    )


app.mount('/static', StaticFiles(directory='static'), name='static')

app.include_router(router)

if __name__ == '__main__':
    uvicorn.run(
        app='main:app',
        host=settings.SERVER_HOST,
        port=settings.SERVER_PORT,
        log_level=settings.LOG_LEVEL,
        reload=settings.DEVELOP,
        use_colors=settings.DEVELOP,
    )
