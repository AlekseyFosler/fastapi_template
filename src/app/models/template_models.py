from pydantic import BaseModel, Field

from app.types import TemplateFloat, TemplateInt, TemplateStr, TemplateUUID4


class TemplateModelBase(BaseModel):
    template_str: TemplateStr = Field(examples=['str'])
    template_int: TemplateInt = Field(examples=[1])
    template_UUID4: TemplateUUID4 = Field(examples=['f310e0ab-e8ba-43a0-8c50-12c95827bc21'])
    template_float: TemplateFloat = Field(examples=[3.14])


class TemplateGetInput(TemplateModelBase):
    pass


class TemplateGetOutput(TemplateModelBase):
    pass


class TemplatePostInput(TemplateModelBase):
    pass


class TemplatePostOutput(TemplateModelBase):
    pass


class TemplatePutInput(TemplateModelBase):
    pass


class TemplatePutOutput(TemplateModelBase):
    pass


class TemplateDeleteInput(TemplateModelBase):
    pass


class TemplateDeleteOutput(TemplateModelBase):
    pass
