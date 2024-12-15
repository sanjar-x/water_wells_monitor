from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.services.crud.user_crud import delete_user , get_user

router = APIRouter()

@router.delete("/user/{user_id}")
async def delete_user_(user_id: str):
    existing_user = await get_user(user_id)
    if not existing_user:
        return JSONResponse(
            content={"message": f"ID: {user_id} fodalanuvchi topilmadi"},
            status_code=404
        )

    deletion_success = await delete_user(user_id)
    if deletion_success:
        return JSONResponse(
            content={"message": f"ID: {user_id} fodalanuvchi o'chirib tashlandi"},
            status_code=200
        )
    else:
        return JSONResponse(
            content={"message": f"Serverda hatolik"},
            status_code=500
        )
