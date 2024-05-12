import logging

from app.enums import TemplateEnum, TemplateIntEnum, TemplateStrEnum
from app.models import TemplateDeleteOutput, TemplateGetOutput, TemplatePostInput, TemplatePostOutput, TemplatePutInput
from app.models import TemplatePutOutput

logger = logging.getLogger('default')


class TemplateService:
    @staticmethod
    async def get_template() -> TemplateGetOutput:
        return TemplateGetOutput(
            template_str='str',
            template_int=1,
            template_UUID4='f310e0ab-e8ba-43a0-8c50-12c95827bc21',
            template_float=3.14,
            template_str_enum=TemplateStrEnum.THREE,
            template_int_enum=TemplateIntEnum.ONE,
            template_enum=TemplateEnum.THIRD,
            template_literal='a',
            template_string_constraints_type='AZ',
        )

    @staticmethod
    async def get_templates(template_post_input: TemplatePostInput) -> TemplatePostOutput:
        logger.warning(f'{template_post_input=}')
        return TemplatePostOutput.model_validate(template_post_input, from_attributes=True)

    @staticmethod
    async def put_template(template_put_input: TemplatePutInput) -> TemplatePutOutput:
        logger.warning(f'{template_put_input=}')
        return TemplatePutOutput.model_validate(template_put_input, from_attributes=True)

    @staticmethod
    async def delete_template(template_delete_input):
        logger.warning(f'{template_delete_input=}')
        return TemplateDeleteOutput.model_validate(template_delete_input, from_attributes=True)
