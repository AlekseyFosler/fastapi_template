from fastapi import APIRouter

from src.app.schemes import TemplateTest, TemplateUsers

router = APIRouter(prefix='/template_root', tags=['Template Root'])


@router.get(
    path='/',
    name='Получить один шаблон',
    response_model=TemplateUsers,
    response_description='Шаблон для получения исходящей модели',
    description='Шаблон для получения',
)
async def get_template() -> TemplateUsers:
    return TemplateUsers.model_validate(
        {
            '36c6c25a-d776-4084-845b-168e02995448': [
                {
                    '36c6c25a-d776-4084-845b-168e02995440': [
                        'базовая информация1',
                        'базовая информация2 и тд',
                    ]
                }
            ],
            '36c6c25a-d776-4084-845b-168e02995449': [
                {
                    '36c6c25a-d776-4084-845b-168e02995440': [
                        'базовая информация1',
                        'базовая информация2 и тд',
                    ]
                }
            ],
        }
    )


@router.post(
    path='/',
    name='Получить шаблоны',
    response_model=TemplateUsers,
    response_description='Шаблон для получения исходящих моделей',
    description='Шаблон для получения исходящих моделей',
)
async def get_templates(
    template_model_input: TemplateUsers,
) -> TemplateUsers:
    return TemplateUsers.model_validate(template_model_input)


@router.get(
    path='/tmp/',
    name='Получить один шаблон',
    response_model=TemplateTest,
    response_description='Шаблон для получения исходящей модели',
    description='Шаблон для получения',
)
async def get_template1() -> TemplateTest:
    return TemplateTest.model_validate({'36c6c25a-d776-4084-845b-168e02995448': '123'})
