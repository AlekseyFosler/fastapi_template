from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DEVELOP: bool = True

    SERVER_HOST: str = '127.0.0.1'
    SERVER_PORT: int = 8000

    TITLE: str = 'FastApi Template API'
    VERSION: str = 'v1.0'

    DOC_URL: str = '/docs'
    OPENAPI_URL: str = '/openapi.json'

    LOG_LEVEL: str = 'debug'


settings = Settings()
