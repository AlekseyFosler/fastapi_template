from pydantic import PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix='APP_')

    DEVELOP: bool = True
    SERVER_HOST: str = '127.0.0.1'
    SERVER_PORT: int = 8000
    TITLE: str = 'FastApi Template API'
    VERSION: str = 'v1.0'
    DOC_URL: str = '/docs'
    OPENAPI_URL: str = '/openapi.json'
    LOG_LEVEL: str = 'debug'
    WORKERS: int = 1
    TIME_OUT: int = 120


class PostgresSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix='POSTGRES_')

    STORAGE_URI: PostgresDsn = PostgresDsn('postgresql+asyncpg://admin:admin@localhost:5432/db')
    POOL_SIZE: int = 20
    MAX_OVERFLOW: int = 5
    MAX_TIME: int = 2
    MAX_TRIES: int = 3


class ClickHouseSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix='CLICKHOUSE_')

    HOST: str = 'localhost'
    USER: str = 'admin'
    PASSWORD: str = 'admin'
    PORT: int = 9000
    DB: str = 'db'
    MAX_TIME: int = 2
    MAX_TRIES: int = 3


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
    )

    app: AppSettings = AppSettings()
    postgres: PostgresSettings = PostgresSettings()
    clickhouse: ClickHouseSettings = ClickHouseSettings()


settings = Settings()
