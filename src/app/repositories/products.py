from typing import Optional, Sequence
from uuid import UUID

from src.app.engines.clickhouse import ClickHouseEngine


class ProductRepository:
    def __init__(self, click_house_engine: ClickHouseEngine):
        self.click_house_engine: ClickHouseEngine = click_house_engine

    async def add(
        self,
    ):
        pass
