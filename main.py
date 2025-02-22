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


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(
    title="Wells Platform API",
    description="API-документация для веб-платформы колодец",
    version="0.0.1",
    lifespan=lifespan,
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router=sign_in_router, tags=["auth"])

app.include_router(router=create_user_router, tags=["user"])
app.include_router(router=get_users_router, tags=["user"])
app.include_router(router=get_user_router, tags=["user"])
app.include_router(router=get_user_by_username_route, tags=["user"])
app.include_router(router=update_user_router, tags=["user"])
app.include_router(router=delete_user_router, tags=["user"])
app.include_router(router=set_user_status_route, tags=["user"])

app.include_router(router=create_well_router, tags=["well"])
app.include_router(router=get_well_router, tags=["well"])
app.include_router(router=get_wells_router, tags=["well"])
app.include_router(router=update_well_router, tags=["well"])
app.include_router(router=delete_well_router, tags=["well"])


app.include_router(router=statistics_router, tags=["statistics"])
app.include_router(router=well_statistics_router, tags=["statistics"])

app.include_router(router=create_message_router, tags=["message"])
app.include_router(router=delete_messages_router, tags=["message"])
app.include_router(router=settings_router, tags=["settings"])
