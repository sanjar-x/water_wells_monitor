from pydantic import BaseModel
from typing import Optional

class UserCreateSchema(BaseModel):
    username: str
    password_hash: str
    name: str
    surname: str

class UserCreateRequestSchema(BaseModel):
    username: str
    password: str
    name: str
    surname: str

class UserUpdateSchema(BaseModel):
    username: Optional[str] = None
    name: Optional[str] = None
    surname: Optional[str] = None