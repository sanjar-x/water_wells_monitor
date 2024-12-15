from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, EmailStr
from typing import Optional, Dict, List, Any


class Message(BaseModel):
    temperature: str
    salinity: str
    water_level: str
    number: str


class MessageSchema(BaseModel):
    message_id: UUID
    water_level: str
    received_at: datetime
    number: str
    temperature: str
    salinity: str
