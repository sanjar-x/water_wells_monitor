from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from app.schemas.wells_schemas import WellsSchema, WellsDevSchema
from app.services.crud.well_crud import create_well, get_well_by_number

router = APIRouter()


@router.post("/well")
async def create_well_dev_(well_data: WellsSchema):
    existing_well = await get_well_by_number(well_data.number)
    if existing_well:
        return JSONResponse(
            content={
                "message": f"{well_data.number} raqamiga {existing_well.name} qudug'i ro'yhatdan o'tkazilgan"
            },
            status_code=status.HTTP_400_BAD_REQUEST,
        )
    await create_well(well_data)
    return JSONResponse(
        content={"message": "Quduq ro'yhatdan o'tkazildi"},
        status_code=status.HTTP_201_CREATED,
    )


@router.post("/well/dev")
async def create_well_(well_data: WellsDevSchema):
    existing_well = await get_well_by_number(well_data.number)
    if existing_well:
        return JSONResponse(
            content={
                "message": f"{well_data.number} raqamiga {existing_well.name} qudug'i ro'yhatdan o'tkazilgan"
            },
            status_code=status.HTTP_400_BAD_REQUEST,
        )
    await create_well(well_data)
    return JSONResponse(
        content={"message": "Quduq ro'yhatdan o'tkazildi"},
        status_code=status.HTTP_201_CREATED,
    )
