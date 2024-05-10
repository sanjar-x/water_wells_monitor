from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from app.services.crud.user_crud import update_user, get_user
from app.schemas.user_schemas import UserUpdateSchema

router = APIRouter()

@router.patch("/user/{user_id}")
async def update_user_(user_id: str, update_user_data: UserUpdateSchema):
    existing_user = await get_user(user_id)
    if not existing_user:
            return JSONResponse(
        content={"message": f"Yangilash bekor qilindi! ID: {user_id} foydalanuvchi ro'yhatdan o'tkazilmagan"},
        status_code=status.HTTP_404_NOT_FOUND,
    )
    await update_user(user_id, update_user_data)
    return JSONResponse(
        content={"message": f"Foydalanuvchi ma'lumotlari yangilandi!"},
        status_code=status.HTTP_200_OK,
    )
