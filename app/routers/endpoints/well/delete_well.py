from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.services.crud.well_crud import delete_well, get_well

router = APIRouter()


@router.delete("/wells/{well_id}")
async def delete_well_endpoint(well_id: str):
    existing_well = await get_well(well_id)
    if not existing_well:
        return JSONResponse(
            content={"message": f"ID: {well_id} Quduq topilmadi"}, status_code=404
        )

    deletion_success = await delete_well(well_id)
    if deletion_success:
        return JSONResponse(
            content={"message": f"ID: {well_id} Quduq o'chirib tashlandi"},
            status_code=200,
        )
    else:
        return JSONResponse(content={"message": f"Serverda hatolik"}, status_code=500)
