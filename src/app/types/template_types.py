from typing import Annotated

from pydantic import UUID4, Field

__template_fields = Field(title='title', description='description')

TemplateStr = Annotated[str, __template_fields]
TemplateInt = Annotated[int, __template_fields]
TemplateUUID4 = Annotated[UUID4, __template_fields]
TemplateFloat = Annotated[float, __template_fields]
