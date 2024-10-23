from typing import Optional
from uuid import UUID
from pydantic import BaseModel


class WelleSchema(BaseModel):
    name: Optional[str] = None
    number: str
    address: Optional[str] = None
    latitude: Optional[str] = None
    longitude: Optional[str] = None
    depth: Optional[str] = None


class WelleDevSchema(BaseModel):
    name: Optional[str] = None
    number: str
    address: Optional[str] = None
    latitude: Optional[str] = None
    longitude: Optional[str] = None
    salinity_start: Optional[str] = None
    salinity_end: Optional[str] = None
    temperature_start: Optional[str] = None
    temperature_end: Optional[str] = None
    water_level_start: Optional[str] = None
    water_level_end: Optional[str] = None
    depth: Optional[str] = None
    auto: Optional[bool] = False


class WelleUpdateSchema(BaseModel):
    name: Optional[str] = None
    number: Optional[str] = None
    address: Optional[str] = None
    latitude: Optional[str] = None
    longitude: Optional[str] = None
    depth: Optional[str] = None


class WelleUpdateDevSchema(BaseModel):
    name: Optional[str] = None
    number: Optional[str] = None
    address: Optional[str] = None
    latitude: Optional[str] = None
    longitude: Optional[str] = None
    depth: Optional[str] = None
    salinity_start: Optional[str] = None
    salinity_end: Optional[str] = None
    temperature_start: Optional[str] = None
    temperature_end: Optional[str] = None
    water_level_start: Optional[str] = None
    water_level_end: Optional[str] = None
    auto: Optional[bool] = False


from datetime import datetime


class WellSchema(BaseModel):
    well_id: UUID
    name: str
    number: str
    address: str
    latitude: str
    longitude: str
    depth: str
    status: bool
    created_time: datetime


class WellDevSchema(BaseModel):
    well_id: UUID
    name: str
    number: str
    address: str
    latitude: str
    longitude: str
    salinity_start: Optional[str] = None
    salinity_end: Optional[str] = None
    temperature_start: Optional[str] = None
    temperature_end: Optional[str] = None
    water_level_start: Optional[str] = None
    water_level_end: Optional[str] = None
    depth: str
    auto: Optional[bool] = False
    status: bool
    time: datetime
