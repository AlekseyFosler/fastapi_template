import logging

import backoff
from clickhouse_driver import Client
from clickhouse_driver.errors import NetworkError, ServerException

from src.app.settings import settings

logger = logging.getLogger(__name__)


class ClickHouseEngine:
    def __init__(self):
        self.connection = Client(
            host=settings.clickhouse.HOST,
            user=settings.clickhouse.USER,
            password=settings.clickhouse.PASSWORD,
            port=settings.clickhouse.PORT,
            database=settings.clickhouse.DB,
        )

    @backoff.on_exception(
        backoff.expo,
        ServerException,
        max_time=settings.clickhouse.MAX_TIME,
        max_tries=settings.clickhouse.MAX_TRIES,
    )
    async def execute(
        self,
        stmt: str,
        params: dict,
        with_column_types: bool = True,
        *args,
        **kwargs,
    ) -> tuple[dict, ...]:
        result = self.connection.execute(stmt, params, *args, **kwargs, with_column_types=with_column_types)
        keys = [key[0] for key in result[1]]
        return tuple(dict(zip(keys, row)) for row in result[0])
