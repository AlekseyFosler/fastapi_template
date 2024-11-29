from typing import Optional, Sequence
from uuid import UUID

from sqlalchemy import Result, and_, exists, select
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.orm import load_only

from app.engines.postgres import Transaction
from app.models import User
from app.schemes import RequestUser, ResponseBriefUser, ResponseUser


class UserRepository:
    def __init__(self, transaction: Transaction):
        self.transaction = transaction

    async def add(self, user: RequestUser) -> ResponseUser:
        stmt = insert(User).values(user.model_dump()).returning(User)
        cursor: Result = await self.transaction.execute(stmt)
        result: User = cursor.scalar_one()
        return ResponseUser.model_validate(result, from_attributes=True)

    async def get_by_id(self, user_id: UUID) -> Optional[ResponseUser]:
        stmt = select(User).where(and_(User.user_id == user_id))
        cursor: Result = await self.transaction.execute(stmt)
        result: Optional[User] = cursor.scalar_one_or_none()
        return ResponseUser.model_validate(result, from_attributes=True) if result else None

    async def get_all(self) -> list[ResponseBriefUser]:
        stmt = select(User).options(load_only(User.user_id, User.full_name))
        cursor: Result = await self.transaction.execute(stmt)
        result: Sequence[User] = cursor.scalars().all()
        return [ResponseBriefUser.model_validate(_, from_attributes=True) for _ in result] if result else []

    async def check_by_mobile_phone(self, mobile_phone: str) -> bool:
        stmt = select(exists(User.user_id).where(and_(User.mobile_phone == mobile_phone)))
        cursor: Result = await self.transaction.execute(stmt)
        return cursor.scalar()
