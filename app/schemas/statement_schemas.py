from pydantic import BaseModel, EmailStr
from typing import Optional, Dict, List, Any


class StatementSchema(BaseModel):
    number: str
    statement: str
