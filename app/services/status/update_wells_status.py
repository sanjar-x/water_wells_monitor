from datetime import datetime, timedelta
from sqlalchemy.future import select
from app.core.database import get_session
from app.models.models import WellsModel, MessageModel


async def update_well_status():
    async with get_session() as session:
        result = await session.execute(select(WellsModel))
        wells = result.scalars().all()

        for well in wells:
            last_message_query = (
                select(MessageModel)
                .filter(MessageModel.number == well.number)
                .order_by(MessageModel.time.desc())
            )
            last_message = await session.execute(last_message_query)  # type: ignore
            last_message = last_message.scalars().first()

            if last_message and (
                datetime.utcnow() - last_message.time <= timedelta(days=1)
            ):
                well.status = True
            else:
                well.status = False

        await session.commit()
