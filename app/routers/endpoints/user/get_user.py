from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from app.services.crud.user_crud import get_user

router = APIRouter()

@router.get("/user/id/{user_id}")
async def get_user_(user_id: str):
    user_data = await get_user(user_id)
    if user_data is None:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": f"ID: {user_id} foydalanuvchi mavjud emas"}
        )
    return user_data