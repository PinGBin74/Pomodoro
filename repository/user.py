from typing import Optional

from sqlalchemy import insert, select
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from dataclasses import dataclass
from models import UserProfile
from schema import UserCreateSchema


@dataclass
class UserRepository:
    db_session: AsyncSession

    async def get_user_by_email(self, email: str) -> Optional[UserProfile]:
        query = select(UserProfile).where(UserProfile.email == email)
        async with self.db_session as session:
            return await session.execute(query).scalar_one_or_none()

    async def create_user(self, user: UserCreateSchema) -> UserProfile:
        query = (
            insert(UserProfile).values(**user.model_dump()).returning(UserProfile.id)
        )
        # model_dump превращает в словарь( с помощью ** распаковываем)
        async with self.db_session as session:
            user_id: int = (await session.execute(query)).scalar()
            await session.commit()
            await session.flush()
            return await self.get_user(user_id)

    async def get_user(self, user_id) -> Optional[UserProfile]:
        query = select(UserProfile).where(UserProfile.id == user_id)
        async with self.db_session as session:
            return await session.execute(query).scalars().first()

    async def get_user_by_username(self, username: str) -> Optional[UserProfile]:
        query = select(UserProfile).where(UserProfile.username == username)
        async with self.db_session as session:
            return await session.execute(query).scalars().first()
