import random
from app.services.centre import send_data
from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from app.services.crud.message_crud import create_message, create_error_messages
from app.services.crud.well_crud import get_well_by_number
from app.services.status.update_wells_status import generate_well_message
from app.schemas.message_schemas import Message

router = APIRouter()


@router.post("/message", status_code=status.HTTP_201_CREATED)
async def create_message_(message_data: Message):
    well = await get_well_by_number(message_data.number[:-1])
    message_data.number = message_data.number[:-1]
    if well:
        if well.salinity_start:  # type: ignore
            message_data.salinity = str(
                random.uniform(
                    float(str(well.salinity_start)), float(str(well.salinity_end))
                )
            )
        else:
            message_data.salinity = message_data.salinity[2:-1]
        if well.temperature_start is not None:
            message_data.temperature = str(
                random.uniform(
                    float(str(well.temperature_start)), float(str(well.temperature_end))
                )
            )
        else:
            message_data.temperature = message_data.temperature[2:-1]
        if well.water_level_start is not None:
            message_data.water_level = str(
                random.randint(
                    int(str(well.water_level_start)), int(str(well.water_level_end))
                )
            )
        else:
            if message_data.water_level[2:-1]:
                message_data.water_level = str(
                    int(str(well.depth)) - round(float(message_data.water_level[2:-1]))
                )
        await send_data(
            code=well.imei,
            level=float(message_data.water_level),
            meneral=float(message_data.salinity),
            temperature=float(message_data.temperature),
        )
    else:
        message_data.salinity = message_data.salinity[2:-1]
        message_data.temperature = message_data.temperature[2:-1]
        message_data.water_level = message_data.water_level[2:-1]

    await create_message(message_data)

    await generate_well_message()
    return JSONResponse(
        content={"message": "Message received"},
        status_code=status.HTTP_200_OK,
    )
