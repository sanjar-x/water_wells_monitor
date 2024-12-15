from fastapi import APIRouter
from app.services.status.update_wells_status import (
    update_well_status,
    generate_well_message,
)
from app.services.crud.well_crud import get_wells

router = APIRouter()


@router.get("/wells/")
async def get_wells_endpoint():
    await generate_well_message()
    await update_well_status()
    return await get_wells()
