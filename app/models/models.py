import uuid
from datetime import datetime, timedelta, timezone

from sqlalchemy import BIGINT

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
)

from sqlalchemy.dialects.postgresql import (
    BOOLEAN,
    INTEGER,
    TEXT,
    UUID,
    VARCHAR,
    TIMESTAMP,
)

tz = timezone(timedelta(hours=5))


class Base(DeclarativeBase):
    pass


class UserModel(Base):
    __tablename__ = "users"

    user_id: Mapped[str] = mapped_column(
        VARCHAR,
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
        unique=True,
        nullable=False,
    )
    username: Mapped[str] = mapped_column(VARCHAR, unique=True)
    password_hash: Mapped[str] = mapped_column(TEXT)
    name: Mapped[str] = mapped_column(TEXT)
    surname: Mapped[str] = mapped_column(TEXT)
    is_superuser: Mapped[bool] = mapped_column(BOOLEAN, default=False)

    async def get_status(self):
        return self.is_superuser

    async def set_status(self, is_superuser: bool):
        self.is_superuser = is_superuser


class WellsModel(Base):
    __tablename__ = "wells"

    well_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    name: Mapped[str] = mapped_column(VARCHAR(255), nullable=True)
    number: Mapped[str] = mapped_column(VARCHAR(255), nullable=True)
    address: Mapped[str] = mapped_column(VARCHAR(255), nullable=True)
    latitude: Mapped[str] = mapped_column(VARCHAR(255), nullable=True)
    longitude: Mapped[str] = mapped_column(VARCHAR(255), nullable=True)
    depth: Mapped[str] = mapped_column(VARCHAR(255), nullable=True)
    imei: Mapped[int] = mapped_column(BIGINT, nullable=True)
    salinity_start: Mapped[str] = mapped_column(VARCHAR(255), nullable=True)
    salinity_end: Mapped[str] = mapped_column(VARCHAR(255), nullable=True)
    temperature_start: Mapped[str] = mapped_column(VARCHAR(255), nullable=True)
    temperature_end: Mapped[str] = mapped_column(VARCHAR(255), nullable=True)
    water_level_start: Mapped[str] = mapped_column(VARCHAR(255), nullable=True)
    water_level_end: Mapped[str] = mapped_column(VARCHAR(255), nullable=True)
    status: Mapped[bool] = mapped_column(BOOLEAN, default=True)
    auto: Mapped[bool] = mapped_column(BOOLEAN, default=False)
    time: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True), default=lambda: datetime.now(tz)
    )


class MessageModel(Base):
    __tablename__ = "messages"

    message_id: Mapped[str] = mapped_column(
        VARCHAR, primary_key=True, default=lambda: str(uuid.uuid4()), unique=True
    )
    temperature: Mapped[str] = mapped_column(TEXT, nullable=True)
    salinity: Mapped[str] = mapped_column(TEXT, nullable=True)
    water_level: Mapped[str] = mapped_column(TEXT, nullable=True)
    number: Mapped[str] = mapped_column(TEXT, nullable=True)
    received_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True), default=lambda: datetime.now(tz)
    )


class ErrorMessageModel(Base):
    __tablename__ = "error_messages"

    message_id: Mapped[str] = mapped_column(
        VARCHAR, primary_key=True, default=lambda: str(uuid.uuid4()), unique=True
    )
    temperature: Mapped[str] = mapped_column(TEXT, nullable=True)
    salinity: Mapped[str] = mapped_column(TEXT, nullable=True)
    water_level: Mapped[str] = mapped_column(TEXT, nullable=True)
    number: Mapped[str] = mapped_column(TEXT, nullable=True)
    received_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True), default=lambda: datetime.now(tz)
    )


class StatementModel(Base):
    __tablename__ = "statements"

    statement_id: Mapped[str] = mapped_column(
        VARCHAR,
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
        unique=True,
        nullable=False,
    )
    statement: Mapped[str] = mapped_column(TEXT, nullable=True)
    number: Mapped[str] = mapped_column(TEXT, nullable=True)
    time: Mapped[datetime] = mapped_column("time", TIMESTAMP, default=datetime.now(tz))
