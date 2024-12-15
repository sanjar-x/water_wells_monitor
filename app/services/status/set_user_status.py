from sqlalchemy.future import select
from app.core.database import get_session
from app.models.models import UserModel


async def set_status(user_id: str, is_superuser: bool):
    async with get_session() as session:
        data = await session.execute(
            select(UserModel).where(UserModel.user_id == user_id)
        ) # type: ignore
        user_data = data.scalars().first()
        await user_data.set_status(is_superuser)        
        await session.commit() # type: ignore