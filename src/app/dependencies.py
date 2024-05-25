from rodi import Container

from app.database import Engine, Transaction
from app.repositories import UserRepository
from app.services import TemplateService, UserService

container = Container()


def init_dependencies() -> None:
    container.add_singleton(Engine)

    container.add_scoped(Transaction)

    container.add_scoped(UserRepository)

    container.add_transient(TemplateService)
    container.add_transient(UserService)


def get_template_service() -> TemplateService:
    return container.resolve(TemplateService)


def get_user_service() -> UserService:
    return container.resolve(UserService)
