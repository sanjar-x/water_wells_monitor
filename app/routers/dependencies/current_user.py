from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.services.crud.user_crud import get_user
from app.core.security import verify

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/sign-in")


async def current_user(token: str = Depends(oauth2_scheme)):
    user_id = await verify(token)
    user_data = await get_user(user_id)
    if user_data:
        return user_data
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Avtorizatsiyadan qaydadan o'ting",
    )


async def current_user_status(token: str = Depends(oauth2_scheme)):
    user_id = await verify(token)
    user_data = await get_user(user_id)
    if user_data:
        return await user_data.get_status()
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Avtorizatsiyadan qaydadan o'ting",
    )
