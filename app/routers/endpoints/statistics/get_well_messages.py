from fastapi import APIRouter, status
from app.services.statistics.get_statistics import get_well_messages

router = APIRouter()


@router.get("/statistics/{number}", status_code=status.HTTP_200_OK)
async def well_statistiks(number: str):
    messages_data = await get_well_messages(number)
    return messages_data
