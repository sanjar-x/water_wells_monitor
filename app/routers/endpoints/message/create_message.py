import random
from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from app.services.crud.message_crud import create_message
from app.services.crud.well_crud import get_well_by_number
from app.schemas.message_schemas import Message

router = APIRouter()


@router.post("/message", status_code=status.HTTP_201_CREATED)
async def create_message_(message_data: Message):
    well = await get_well_by_number(message_data.number[:-1])
    if not well:
        return None

    message_data.temperature = message_data.temperature[2:-1]

    message_data.water_level = str(
        int(str(well.depth)) - round(float(message_data.water_level[2:-1]))
    )
    message_data.number = message_data.number[:-1]
    if not well.salinity_start:  # type: ignore
        message_data.salinity = message_data.salinity[2:-1]
    else:
        message_data.salinity = str(
            random.uniform(
                float(str(well.salinity_start)), float(str(well.salinity_end))
            )
        )

    await create_message(message_data)
    return JSONResponse(
        content={"message": "Message received"},
        status_code=status.HTTP_200_OK,
    )
