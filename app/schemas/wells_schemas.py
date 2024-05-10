
from typing import Optional
from pydantic import BaseModel

class WelleSchema(BaseModel):
    name: Optional[str] = None
    number: str
    address: Optional[str] = None
    latitude: Optional[str] = None
    longitude: Optional[str] = None

class WelleUpdateSchema(BaseModel):
    name: Optional[str] = None
    number: Optional[str] = None
    address: Optional[str] = None
    latitude: Optional[str] = None
    longitude: Optional[str] = None