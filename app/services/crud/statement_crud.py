from typing import List
from sqlalchemy import delete
from sqlalchemy.future import select
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException

from app.core.database import get_session
from app.models.models import StatementModel
from app.schemas.statement_schemas import StatementSchema


async def create_statement(statement_data: StatementSchema) -> StatementModel:
    try:
        async with get_session() as session:
            created_statement = StatementModel(**statement_data.model_dump())
            session.add(created_statement)
            await session.commit()  # type: ignore
            return created_statement
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"Error creating statement: {e}")


async def get_statements() -> List[StatementModel]:
    try:
        async with get_session() as session:
            result = await session.execute(select(StatementModel))  # type: ignore
            statements = result.scalars().all()
            return list(statements)
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving statements: {e}")


async def delete_statements():
    try:
        async with get_session() as session:
            await session.execute(delete(StatementModel))  # type: ignore
            await session.commit()  # type: ignore
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail="Error deleting statement")


async def delete_statement(statement_id: str):
    try:
        async with get_session() as session:
            # Фильтрация заявления по ID и его удаление
            await session.execute(delete(StatementModel).where(StatementModel.statement_id == statement_id))  # type: ignore
            await session.commit()  # type: ignore
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error deleting statement with ID {statement_id}: {e}",
        )
