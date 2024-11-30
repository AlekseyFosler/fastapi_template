from typing import Annotated, Literal

from pydantic import UUID4, Field, StringConstraints

from src.app.enums import TemplateEnum, TemplateIntEnum, TemplateStrEnum

__template_fields = Field(
    title='title',
    description='description',
)

TemplateStrType = Annotated[
    str,
    __template_fields,
]
TemplateStringConstraintsType = Annotated[
    str,
    StringConstraints(strip_whitespace=True, to_upper=True, pattern=r'^[A-Z]+$'),
    __template_fields,
]
TemplateIntType = Annotated[
    int,
    __template_fields,
]
TemplateUUID4Type = Annotated[
    UUID4,
    __template_fields,
]
TemplateFloatType = Annotated[
    float,
    __template_fields,
]
TemplateEnumType = Annotated[
    TemplateEnum,
    __template_fields,
]
TemplateIntEnumType = Annotated[
    TemplateIntEnum,
    __template_fields,
]
TemplateStrEnumType = Annotated[
    TemplateStrEnum,
    __template_fields,
]
TemplateLiteralType = Annotated[
    Literal['a', 'b', 'c'],
    __template_fields,
]
