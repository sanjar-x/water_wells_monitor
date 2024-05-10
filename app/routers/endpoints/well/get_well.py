from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from app.services.crud.well_crud import get_well

router = APIRouter()

@router.get("/wells/{well_id}")
async def get_well_endpoint(well_id: str):
    well = await get_well(well_id)
    if well is None:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": f"ID: {well_id} quduq mavjud emas"}
        )
    return well


