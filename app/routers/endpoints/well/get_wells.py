from fastapi import APIRouter
from app.services.status.update_wells_status import update_well_status
from app.services.crud.well_crud import get_wells

router = APIRouter()


@router.get("/wells/")
async def get_wells_endpoint():
    # await update_well_status()
    return await get_wells()
