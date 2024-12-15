from typing import List
from datetime import datetime, timedelta
from app.models.models import MessageModel
from sqlalchemy import and_
from sqlalchemy.future import select
from app.core.database import get_session


async def get_well_messages(number: str) -> List[MessageModel]:
    async with get_session() as session:
        result = await session.execute(
            select(MessageModel).where(MessageModel.number == number)
        )  # type: ignore
        messages = result.scalars().all()
        return list(messages)


async def get_well_messages_within_days(number: str, days: int) -> List[MessageModel]:
    async with get_session() as session:
        date_limit = datetime.now() - timedelta(days=days)
        result = await session.execute(
            select(MessageModel)
            .where(MessageModel.number == number)
            .where(MessageModel.received_at >= date_limit.isoformat())
        )  # type: ignore
        return list(result.scalars().all())


async def get_well_messages_last_week(number: str) -> List[MessageModel]:
    return await get_well_messages_within_days(number, 7)


async def get_well_messages_last_month(number: str) -> List[MessageModel]:
    return await get_well_messages_within_days(number, 30)


async def get_well_messages_last_year(number: str) -> List[MessageModel]:
    return await get_well_messages_within_days(number, 365)
