from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from app.services.crud.message_crud import delete_messages

router = APIRouter()

@router.delete("/messages", status_code=status.HTTP_200_OK)
async def delete_messages_():
    await delete_messages()
    return JSONResponse(content={"message": "Messages deleted"}, status_code=status.HTTP_200_OK)