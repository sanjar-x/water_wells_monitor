from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from app.services.crud.user_crud import get_user_by_username

router = APIRouter()

@router.get("/user/username/{username}")
async def get_user_by_username_(username: str):
    user_data = await get_user_by_username(username)
    if user_data is None:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": f"'{username}' foydalanuvchi mavjud emas"}
        )
    return user_data
