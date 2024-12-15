import asyncio
from app.core.database import engine


async def init_database():
    from app.models.models import (
        UserModel,
        WellsModel,
        MessageModel,
        StatementModel,
        Base,
    )

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


if __name__ == "__main__":
    asyncio.run(init_database())
