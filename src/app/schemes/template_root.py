from pydantic import UUID4, Field, RootModel

from app.micro_types import ATemplateStates, ATemplateUsers


class TemplateStates(RootModel):
    root: ATemplateStates


class TemplateUsers(RootModel):
    root: ATemplateUsers


class TemplateTest(RootModel):
    root: dict[UUID4, str] = Field(
        default=...,
        description='Словарь, где ключом является UUID, а значением - строка, представляющая состояние шаблона.',
    )
