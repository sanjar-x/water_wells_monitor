from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.core.database import engine

settings_router = APIRouter()


@settings_router.get("/database/reset")
async def reset_database():
    async with engine.begin() as conn:
        from app.models.models import (
            UserModel,
            WellsModel,
            MessageModel,
            StatementModel,
            Base,
        )

        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
        return JSONResponse(content={"database": "reseted"})
