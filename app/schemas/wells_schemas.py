from typing import Optional
from uuid import UUID
from pydantic import BaseModel


class WellsSchema(BaseModel):
    name: Optional[str] = None
    number: str
    address: Optional[str] = None
    latitude: Optional[str] = None
    longitude: Optional[str] = None
    depth: Optional[str] = None


class WellsDevSchema(BaseModel):
    well_id: UUID
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
