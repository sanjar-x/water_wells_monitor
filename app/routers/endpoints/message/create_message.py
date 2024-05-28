from fastapi import APIRouter, Form, status
from fastapi.responses import JSONResponse
from app.services.crud.message_crud import create_message
from app.schemas.message_schemas import Message

router = APIRouter()


@router.post("/message", status_code=status.HTTP_201_CREATED)
async def create_message_(message_data: Message):

    await create_message(message_data)
    return JSONResponse(
        content={"message": "Message received"},
        status_code=status.HTTP_200_OK,
    )
