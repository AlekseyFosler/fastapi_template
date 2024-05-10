from fastapi import APIRouter, Depends

from app.models import TemplateDeleteInput, TemplateDeleteOutput, TemplateGetOutput, TemplatePostInput
from app.models import TemplatePostOutput, TemplatePutInput, TemplatePutOutput
from app.services import TemplateService

router = APIRouter(prefix='/template', tags=['Templates'])


@router.get(
    path='/',
    response_model=TemplateGetOutput,
    response_description='Шаблон для получения исходящей модели',
    description='Шаблон для получения',
)
async def get_template(
    ticket_service: TemplateService = Depends(),
) -> TemplateGetOutput:
    return await ticket_service.get_template()


@router.post(
    path='/',
    response_model=TemplatePostOutput,
    response_description='Шаблон для получения исходящих моделей',
    description='Шаблон для получения исходящих моделей',
)
async def get_templates(
    template_model_input: TemplatePostInput,
    ticket_service: TemplateService = Depends(),
) -> TemplatePostOutput:
    return await ticket_service.get_templates(template_model_input)


@router.put(
    path='/',
    response_model=TemplatePutOutput,
    response_description='Шаблон для создания модели',
    description='Шаблон для создания',
)
async def put_template(
    template_model_input: TemplatePutInput,
    ticket_service: TemplateService = Depends(),
) -> TemplatePutOutput:
    return await ticket_service.put_template(template_model_input)


@router.delete(
    path='/',
    response_model=TemplatePutOutput,
    response_description='Шаблон для удаления модели',
    description='Шаблон для удаления',
)
async def delete_template(
    template_delete_input: TemplateDeleteInput,
    ticket_service: TemplateService = Depends(),
) -> TemplateDeleteOutput:
    return await ticket_service.delete_template(template_delete_input)
