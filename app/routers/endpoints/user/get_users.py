from fastapi import APIRouter
from app.services.crud.user_crud import get_users

router = APIRouter()

@router.get("/users/")
async def get_users_():
    users_data = await get_users()
    return users_data