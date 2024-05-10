import logging
from typing import List, Optional
from sqlalchemy import delete
from sqlalchemy.future import select
from sqlalchemy.exc import NoResultFound, SQLAlchemyError

from app.core.database import get_session
from app.models.models import WellsModel
from app.schemas.wells_schemas import WelleSchema, WelleUpdateSchema

logger = logging.getLogger(__name__)


async def create_well(well_data: WelleSchema) -> WellsModel:
    async with get_session() as session:
        new_well = WellsModel(**well_data.model_dump())
        session.add(new_well)
        await session.commit()  # type: ignore
        return new_well


async def get_wells() -> List[WellsModel]:
    async with get_session() as session:
        try:
            result = await session.execute(select(WellsModel))  # type: ignore
            wells = result.scalars().all()
            return wells
        except SQLAlchemyError as e:
            logger.error(f"Error fetching all wells: {e}")
            return []


async def get_well(well_id: str) -> Optional[WellsModel]:
    async with get_session() as session:
        try:
            result = await session.execute(
                select(WellsModel).filter(WellsModel.well_id == well_id)
            )  # type: ignore
            return result.scalar_one()
        except NoResultFound:
            return None
        except SQLAlchemyError as e:
            logger.error(f"Error fetching well with ID {well_id}: {e}")
            return None


async def get_well_by_number(number: str) -> Optional[WellsModel]:
    async with get_session() as session:
        try:
            result = await session.execute(
                select(WellsModel).filter(WellsModel.number == number)
            )  # type: ignore
            return result.scalar_one()
        except NoResultFound:
            return None
        except SQLAlchemyError as e:
            logger.error(f"Error fetching well with number {number}: {e}")
            return None


async def update_well(
    well_id: str, update_well_data: WelleUpdateSchema
) -> Optional[WellsModel]:
    update_data_dict = update_well_data.dict()  # Convert Pydantic model to dictionary
    async with get_session() as session:
        try:
            result = await session.execute(
                select(WellsModel).filter(WellsModel.well_id == well_id)
            )  # type: ignore
            well_to_update = result.scalar_one()
            for (
                key,
                value,
            ) in update_data_dict.items():  # Now iterate over the dictionary
                if value is not None:
                    setattr(well_to_update, key, value)
            await session.commit()  # type: ignore
            await session.refresh(well_to_update)  # type: ignore
            return well_to_update
        except NoResultFound:
            return None
        except SQLAlchemyError as e:
            logger.error(f"Error updating well with ID {well_id}: {e}")
            return None


async def delete_well(well_id: str) -> bool:
    async with get_session() as session:
        try:
            await session.execute(
                delete(WellsModel).where(WellsModel.well_id == well_id)
            )  # type: ignore
            await session.commit()  # type: ignore
            return True
        except NoResultFound:
            return False
