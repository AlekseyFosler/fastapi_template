from uuid import UUID

from fastapi import APIRouter, Depends

from src.app.dependencies import get_user_service
from src.app.schemes import RequestUser, ResponseBriefUser, ResponseUser
from src.app.services import UserService

router = APIRouter(prefix='/user', tags=['Users'])


@router.post(
    path='/',
    response_model=ResponseUser,
    name='Создать одного пользователя',
    response_description='Создать одного пользователя',
    description='Создать одного пользователя',
)
async def add_user(
    item: RequestUser,
    user_service: UserService = Depends(get_user_service),
) -> ResponseUser:
    return await user_service.add(item)


@router.get(
    '/',
    response_model=ResponseUser,
    name='Получить одного пользователя',
    response_description='Получить одного пользователя',
    description='Получить одного пользователя',
)
async def get_user_by_id(
    user_id: UUID,
    user_service: UserService = Depends(get_user_service),
) -> ResponseUser:
    return await user_service.get_by_id(user_id)


@router.get(
    '/list/',
    response_model=list[ResponseBriefUser],
    name='Получить всех пользователей',
    response_description='Получить всех пользователей',
    description='Получить всех пользователей',
)
async def get_all_users(
    user_service: UserService = Depends(get_user_service),
) -> list[ResponseBriefUser]:
    return await user_service.get_all()
