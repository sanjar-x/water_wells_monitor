from fastapi import APIRouter, status, Depends
from fastapi.responses import JSONResponse
from app.schemas.user_schemas import UserCreateRequestSchema, UserCreateSchema
from app.core.security import hash_password
from app.services.crud.user_crud import create_user, get_user_by_username
from app.routers.dependencies.current_user import current_user_status

router = APIRouter()


@router.post("/user", status_code=status.HTTP_201_CREATED)
async def create_user_(user_data: UserCreateRequestSchema):
    existing_user = await get_user_by_username(user_data.username)
    if existing_user:
        return JSONResponse(
            content={
                "message": f"'{user_data.username}' foydalanuvchi nomi oldin ro'yhatdan o'tkazilgan "
            },
            status_code=status.HTTP_400_BAD_REQUEST,
        )
    hashed_password = await hash_password(user_data.password)
    user_data = UserCreateSchema(
        username=user_data.username,
        password_hash=hashed_password,
        name=user_data.name,
        surname=user_data.surname,
    )  # type: ignore
    await create_user(user_data)  # type: ignore
    return JSONResponse(
        content={
            "message": f"'{user_data.username}' foydalanuvchi ro'yhatdan o'tkazildi "
        },
        status_code=status.HTTP_201_CREATED,
    )


# @router.post("/user", status_code=status.HTTP_201_CREATED)
# async def create_user_(user_data: UserCreateRequestSchema, user_status: bool = Depends(current_user_status)):
#     if user_status:
#         existing_user = await get_user_by_username(user_data.username)
#         if existing_user:
#             return JSONResponse(
#                 content={
#                     "message": f"'{user_data.username}' foydalanuvchi nomi oldin ro'yhatdan o'tkazilgan "
#                 },
#                 status_code=status.HTTP_400_BAD_REQUEST,
#             )
#         hashed_password = await hash_password(user_data.password)
#         user_data = UserCreateSchema(
#             username=user_data.username,
#             password_hash=hashed_password,
#             name=user_data.name,
#             surname=user_data.surname,
#         ) # type: ignore
#         await create_user(user_data) # type: ignore
#         return JSONResponse(
#             content={
#                 "message": f"'{user_data.username}' foydalanuvchi ro'yhatdan o'tkazildi "
#             },
#             status_code=status.HTTP_201_CREATED,
#         )
#     return JSONResponse(
#         content={
#             "message": f"Sizning vakolatingiz yetari emas! Administrator bilan boglaning"
#         },
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         )
