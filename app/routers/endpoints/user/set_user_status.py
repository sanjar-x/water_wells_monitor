from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from app.services.status.set_user_status import set_status

router = APIRouter()

@router.put("/user/{user_id}", status_code=status.HTTP_200_OK)
async def set_user_status(user_id: str, is_superuser: bool):
        await set_status(user_id, is_superuser)
        return JSONResponse(status_code=status.HTTP_200_OK, content={"message": f"Foydalanuvchiga administrator lavozimi biriktirildi"})
   