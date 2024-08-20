from datetime import datetime, timedelta, timezone
from sqlalchemy.future import select
from app.core.database import get_session
from app.models.models import WellsModel, MessageModel


async def update_well_status():
    tz = timezone(timedelta(hours=5))
    async with get_session() as session:
        result = await session.execute(select(WellsModel))
        wells = list(result.scalars().all())

        for well in wells:
            last_message_query = (
                select(MessageModel)
                .where(MessageModel.number == well.number)
                .order_by(MessageModel.received_at.desc())
            )
            messages = await session.execute(last_message_query)
            last_message = messages.scalars().first()

            if last_message:
                received_at_with_tz = last_message.received_at.replace(tzinfo=tz)
                if timedelta(days=1) > datetime.now(tz) - received_at_with_tz:  # type: ignore
                    well.status = True  # type: ignore
                else:
                    well.status = False  # type: ignore

        await session.commit()
