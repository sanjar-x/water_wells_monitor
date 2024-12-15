from typing import Optional
from sqlalchemy.future import select
from sqlalchemy.exc import NoResultFound, SQLAlchemyError

from app.core.database import get_session
from app.models.models import UserModel
from app.schemas.user_schemas import UserCreateSchema, UserUpdateSchema


async def create_user(user_data: UserCreateSchema):
    async with get_session() as session:
        new_user = UserModel(**user_data.model_dump())
        session.add(new_user)
        await session.commit()
        return new_user


async def get_users():
    async with get_session() as session:
        result = await session.execute(select(UserModel))
        users = result.scalars().all()
        return users


async def get_user(user_id: str) -> Optional[UserModel]:
    async with get_session() as session:
        query = select(UserModel).where(UserModel.user_id == user_id)
        result = await session.execute(query)
        user = result.scalars().first()
        return user


async def get_user_by_username(username: str) -> Optional[UserModel]:
    async with get_session() as session:
        result = await session.execute(
            select(UserModel).where(UserModel.username == username)
        )
        user_data = result.scalars().first()
        return user_data


async def update_user(
    user_id: str, update_user_data: UserUpdateSchema
) -> Optional[UserModel]:
    update_data_dict = update_user_data.model_dump()
    async with get_session() as session:
        try:
            query = select(UserModel).filter(UserModel.user_id == user_id)
            result = await session.execute(query)
            user_data = result.scalar_one()
            for key, value in update_data_dict.items():
                if value is not None:
                    setattr(user_data, key, value)
            await session.commit()
            await session.refresh(user_data)
            return user_data
        except NoResultFound:
            return None
        except SQLAlchemyError as e:
            # logger.error(f"Error updating user with ID {user_id}: {e}")
            return None


async def delete_user(user_id: str):
    async with get_session() as session:
        user = await session.get(UserModel, user_id)
        if user:
            await session.delete(user)
            await session.commit()
            return True
        return False
