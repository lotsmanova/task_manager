from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from src.auth.schemas import UserAdd
from src.auth.security import get_password_hash
from src.auth.models import Users


class UserCRUD:
    async def add_user(self, db: AsyncSession, user: UserAdd) -> Users:
        db_user = Users(
            username=user.username,
            email=user.email,
            hashed_password=get_password_hash(user.password),
        )
        db.add(db_user)
        try:
            await db.commit()
            return db_user
        except IntegrityError as e:
            await db.rollback()
            raise e

    async def get_user_by_username(self, db: AsyncSession, username: str) -> Users:
        user = await db.execute(select(Users).where(Users.username == username))
        user = user.scalar_one()
        return user

    async def get_user_by_id(self, db: AsyncSession, user_id: str) -> Users:
        user = await db.execute(select(Users).where(Users.id == user_id))
        user = user.scalar_one()
        return user


user_crud = UserCRUD()
