from fastapi import APIRouter, Depends

from app.schemes import TemplateDeleteInput, TemplateDeleteOutput, TemplateGetOutput, TemplatePostInput
from app.schemes import TemplatePostOutput, TemplatePutInput, TemplatePutOutput
from app.services import TemplateService

router = APIRouter(prefix='/template', tags=['Templates'])


@router.get(
    path='/',
    name='Получить один шаблон',
    response_model=TemplateGetOutput,
    response_description='Шаблон для получения исходящей модели',
    description='Шаблон для получения',
)
async def get_template(
    template_service: TemplateService = Depends(),
) -> TemplateGetOutput:
    return await template_service.get_template()


@router.post(
    path='/',
    name='Получить шаблоны',
    response_model=TemplatePostOutput,
    response_description='Шаблон для получения исходящих моделей',
    description='Шаблон для получения исходящих моделей',
)
async def get_templates(
    template_model_input: TemplatePostInput,
    template_service: TemplateService = Depends(),
) -> TemplatePostOutput:
    return await template_service.get_templates(template_model_input)


@router.put(
    path='/',
    name='Создать шаблон',
    response_model=TemplatePutOutput,
    response_description='Шаблон для создания модели',
    description='Шаблон для создания',
)
async def put_template(
    template_model_input: TemplatePutInput,
    template_service: TemplateService = Depends(),
) -> TemplatePutOutput:
    return await template_service.put_template(template_model_input)


@router.delete(
    path='/',
    name='Удалить шаблон',
    response_model=TemplatePutOutput,
    response_description='Шаблон для удаления модели',
    description='Шаблон для удаления',
)
async def delete_template(
    template_delete_input: TemplateDeleteInput,
    template_service: TemplateService = Depends(),
) -> TemplateDeleteOutput:
    return await template_service.delete_template(template_delete_input)
