import asyncio
from contextlib import asynccontextmanager
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.routers.endpoints.auth.sign_in import router as sign_in_router
from app.routers.endpoints.user.create_user import router as create_user_router
from app.routers.endpoints.user.get_users import router as get_users_router
from app.routers.endpoints.user.get_user import router as get_user_router
from app.routers.endpoints.user.get_user_by_username import (
    router as get_user_by_username_route,
)
from app.routers.endpoints.user.update_user import router as update_user_router
from app.routers.endpoints.user.delete_user import router as delete_user_router
from app.routers.endpoints.user.set_user_status import router as set_user_status_route

from app.routers.endpoints.well.create_well import router as create_well_router
from app.routers.endpoints.well.delete_well import router as delete_well_router
from app.routers.endpoints.well.get_well import router as get_well_router
from app.routers.endpoints.well.get_wells import router as get_wells_router
from app.routers.endpoints.well.update_well import router as update_well_router

from app.routers.endpoints.statistics.get_messages import router as statistics_router
from app.routers.endpoints.statistics.get_well_messages import (
    router as well_statistics_router,
)

from app.routers.endpoints.message.create_message import router as create_message_router
from app.routers.endpoints.message.delete_messages import (
    router as delete_messages_router,
)

from app.routers.endpoints.settings import settings_router

HTTP_PORT = 8000


app = FastAPI(
    title="Wells Platform API",
    description="API-документация для веб-платформы колодец",
    version="0.0.1",
    openapi_url="/api/openapi.json",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# app.mount("/static", StaticFiles(directory="app/templates/static"), name="static")

# @app.get("/")
# async def root():
#     return FileResponse('app/templates/index.html')

app.include_router(router=sign_in_router, tags=["auth"], prefix="/api")

app.include_router(router=create_user_router, tags=["user"], prefix="/api")
app.include_router(router=get_users_router, tags=["user"], prefix="/api")
app.include_router(router=get_user_router, tags=["user"], prefix="/api")
app.include_router(router=get_user_by_username_route, tags=["user"], prefix="/api")
app.include_router(router=update_user_router, tags=["user"], prefix="/api")
app.include_router(router=delete_user_router, tags=["user"], prefix="/api")
app.include_router(router=set_user_status_route, tags=["user"], prefix="/api")

app.include_router(router=create_well_router, tags=["well"], prefix="/api")
app.include_router(router=get_well_router, tags=["well"], prefix="/api")
app.include_router(router=get_wells_router, tags=["well"], prefix="/api")
app.include_router(router=update_well_router, tags=["well"], prefix="/api")
app.include_router(router=delete_well_router, tags=["well"], prefix="/api")


app.include_router(router=statistics_router, tags=["statistics"], prefix="/api")
app.include_router(router=well_statistics_router, tags=["statistics"], prefix="/api")

app.include_router(router=create_message_router, tags=["message"], prefix="/api")
app.include_router(router=delete_messages_router, tags=["message"], prefix="/api")
app.include_router(router=settings_router, tags=["settings"], prefix="/api")

from app.core.database import engine


async def init_database():
    async with engine.begin() as conn:
        from app.models.models import (
            UserModel,
            WellsModel,
            MessageModel,
            StatementModel,
            Base,
        )

        await conn.run_sync(MessageModel.metadata.drop_all)
        await conn.run_sync(MessageModel.metadata.create_all)


if __name__ == "__main__":
    asyncio.run(init_database())
