from rodi import Container

from src.app.engines.clickhouse import ClickHouseEngine
from src.app.engines.postgres import Engine, Transaction
from src.app.repositories import ProductRepository, UserRepository
from src.app.services import ProductService, TemplateService, UserService

container = Container()


def init_dependencies() -> None:
    container.add_singleton(Engine)
    container.add_singleton(ClickHouseEngine)

    container.add_scoped(Transaction)

    container.add_scoped(UserRepository)
    container.add_scoped(ProductRepository)

    container.add_transient(TemplateService)
    container.add_transient(UserService)
    container.add_transient(ProductService)


def get_template_service() -> TemplateService:
    return container.resolve(TemplateService)


def get_user_service() -> UserService:
    return container.resolve(UserService)


def get_product_service() -> ProductService:
    return container.resolve(ProductService)
