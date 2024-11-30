from pydantic import BaseModel, Field

from src.app.micro_types import TemplateEnumType, TemplateFloatType, TemplateIntEnumType, TemplateIntType
from src.app.micro_types import TemplateLiteralType, TemplateStrEnumType, TemplateStringConstraintsType
from src.app.micro_types import TemplateStrType, TemplateUUID4Type


class TemplateModelBase(BaseModel):
    template_str: TemplateStrType = Field(
        examples=['str'],
    )
    template_int: TemplateIntType = Field(
        examples=[1],
    )
    template_UUID4: TemplateUUID4Type = Field(
        examples=['f310e0ab-e8ba-43a0-8c50-12c95827bc21'],
    )
    template_float: TemplateFloatType = Field(
        examples=[3.14],
    )
    template_str_enum: TemplateStrEnumType = Field(
        examples=[TemplateStrEnumType.ONE.value],
    )
    template_int_enum: TemplateIntEnumType = Field(
        examples=[TemplateIntEnumType.ONE.value],
    )
    template_enum: TemplateEnumType = Field(
        examples=[TemplateEnumType.FIRST.value],
    )
    template_literal: TemplateLiteralType = Field(
        examples=['a'],
    )
    template_string_constraints_type: TemplateStringConstraintsType = Field(
        examples=[' A '],
    )


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
