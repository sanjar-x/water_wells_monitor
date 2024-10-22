from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from app.services.crud.well_crud import update_well, get_well
from app.schemas.wells_schemas import WelleUpdateSchema, WelleUpdateDevSchema

router = APIRouter()


@router.patch("/wells/{well_id}")
async def update_well_endpoint(well_id: str, update_well_data: WelleUpdateDevSchema):
    existing_well = await get_well(well_id)
    if not existing_well:
        return JSONResponse(
            content={
                "message": f"Yangilash bekor qilindi! ID: {well_id} quduq ro'yhatdan o'tkazilmagani"
            },
            status_code=status.HTTP_404_NOT_FOUND,
        )
    await update_well(well_id, update_well_data)
    return JSONResponse(
        content={"message": f"Quduq ma'lumotlari yangilandi!"},
        status_code=status.HTTP_200_OK,
    )


@router.patch("/wells/{well_id}")
async def update_well_dev_endpoint(
    well_id: str, update_well_data: WelleUpdateDevSchema
):
    existing_well = await get_well(well_id)
    if not existing_well:
        return JSONResponse(
            content={
                "message": f"Yangilash bekor qilindi! ID: {well_id} quduq ro'yhatdan o'tkazilmagani"
            },
            status_code=status.HTTP_404_NOT_FOUND,
        )
    await update_well(well_id, update_well_data)
    return JSONResponse(
        content={"message": f"Quduq ma'lumotlari yangilandi!"},
        status_code=status.HTTP_200_OK,
    )
