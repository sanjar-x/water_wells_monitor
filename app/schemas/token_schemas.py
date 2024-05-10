from pydantic import BaseModel

class TokenSchema(BaseModel):
    sub: str
    exp: int
    iss: str

class ResponseTokenSchema(BaseModel):
    access_token: str
    token_type: str = "bearer"