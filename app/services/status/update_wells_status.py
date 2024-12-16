from datetime import datetime, timedelta, timezone
import random
from sqlalchemy.future import select
from app.core.database import get_session
from app.models.models import WellsModel, MessageModel


async def update_well_status():
    tz = timezone(timedelta(hours=5))
    async with get_session() as session:
        result = await session.execute(select(WellsModel))
        wells = result.scalars().all()

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
                if timedelta(days=2) > datetime.now(tz) - received_at_with_tz:  # type: ignore
                    well.status = True  # type: ignore
                else:
                    well.status = False  # type: ignore

        await session.commit()


async def generate_well_message():
    tz = timezone(timedelta(hours=5))
    async with get_session() as session:  # Assuming get_session is defined elsewhere
        result = await session.execute(select(WellsModel))
        wells = result.scalars().all()

        for well in wells:
            if not well.auto:  # Skip wells that are not marked as auto
                continue

            # Fetch the last message for the current well
            last_message_query = (
                select(MessageModel)
                .where(MessageModel.number == well.number)
                .order_by(MessageModel.received_at.desc())
            )
            messages = await session.execute(last_message_query)
            last_message = messages.scalars().first()

            # Create the new message
            gen_message = MessageModel(
                temperature=str(
                    random.uniform(
                        float(str(well.temperature_start)),
                        float(str(well.temperature_end)),
                    )
                ),
                salinity=str(
                    random.uniform(
                        float(str(well.salinity_start)),
                        float(str(well.salinity_end)),
                    )
                ),
                water_level=str(
                    random.randint(
                        int(str(well.water_level_start)),
                        int(str(well.water_level_end)),
                    )
                ),
                number=well.number,
            )

            if last_message:
                received_at_with_tz = last_message.received_at.astimezone(tz)
                print(f"before {last_message.message_id}", received_at_with_tz)

                if timedelta(hours=5) < datetime.now(tz) - received_at_with_tz:
                    gen_message.received_at = received_at_with_tz + timedelta(hours=5)
                    print("after", received_at_with_tz + timedelta(hours=5))
                    session.add(gen_message)
                else:
                    print(
                        f"Skipping well {well.number}: last message received less than 5 hours ago."
                    )
                    continue

            else:
                gen_message.received_at = datetime.now(tz)
                session.add(gen_message)

        await session.commit()
