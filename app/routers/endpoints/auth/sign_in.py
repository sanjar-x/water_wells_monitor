from fastapi import APIRouter, status, Depends
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from app.schemas.token_schemas import ResponseTokenSchema
from app.services.crud.user_crud import get_user_by_username
from app.core.security import verify_password, create_token
from app.routers.dependencies.current_user import current_user

router = APIRouter()


@router.post("/sign-in", response_model=ResponseTokenSchema)
async def admin_sign_in(data: OAuth2PasswordRequestForm = Depends()):
    user_data = await get_user_by_username(data.username)
    if user_data is None:
        return JSONResponse(content={"error": "Login hato"}, status_code=400)

    password_hash = user_data.password_hash
    await verify_password(str(password_hash), data.password)
    token = await create_token(str(user_data.user_id))

    return {"access_token": token, "token_type": "bearer"}


@router.get("/me")
async def read_users_me(current_user=Depends(current_user)):
    return current_user
