import logging
import secrets
import string
from datetime import datetime, timedelta, timezone

from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError, InvalidHashError, VerificationError
from dotenv import load_dotenv
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, ExpiredSignatureError, JWTError
from .settings import settings
from app.schemas.token_schemas import TokenSchema


logging.basicConfig(level=logging.INFO)


SECRET = settings.secret.get_secret_value()
VERIFY_SECRET = settings.verify_secret.get_secret_value()
ALGORITHM = settings.algorithm.get_secret_value()
KID = settings.kid.get_secret_value()
TOKEN_EXP = 3600.0


load_dotenv()


hasher = PasswordHasher()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/sign-in")


async def password_generator(length=8, uppercase=True, digits=True, characters=False):
    alphabet = string.ascii_lowercase
    if uppercase:
        alphabet += string.ascii_uppercase
    if digits:
        alphabet += string.digits
    if characters:
        alphabet += string.punctuation

    password = "".join(secrets.choice(alphabet) for _ in range(length))

    return password


async def hash_password(password: str) -> str:
    password = password + VERIFY_SECRET
    return hasher.hash(password)


async def verify_password(hashed_password: str, password: str) -> bool:
    password_with_secret = password + VERIFY_SECRET
    try:
        hasher.verify(hash=hashed_password, password=password_with_secret)
        return True
    except VerifyMismatchError:
        logging.warning("Пароль не совпадает с хэшем.")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Parol xato! Qaytadan urinib ko'ring",
        )
    except InvalidHashError:
        logging.error("Пароль был неправильно сохранён в базе.")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Внутренняя ошибка сервера.",
        )
    except VerificationError as ve:
        logging.error(f"Ошибка проверки пароля: {ve}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Внутренняя ошибка сервера.",
        )


async def create_token(user_id: str) -> str:
    payload = {
        "sub": user_id,
        "exp": datetime.now(timezone.utc) + timedelta(minutes=TOKEN_EXP),
        "iss": "algoritm",
    }
    headers = {"kid": KID}
    try:
        token = jwt.encode(payload, SECRET, algorithm=ALGORITHM, headers=headers)  # type: ignore
        return token
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Keyinroq urinib ko'ring"
        )


async def verify(token: str = Depends(oauth2_scheme)) -> str:
    try:
        payload = jwt.decode(token, key=SECRET, algorithms=[ALGORITHM])  # type: ignore
        token_data = TokenSchema(**payload)
        return token_data.sub
    except ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Token muddati tugagan"
        )
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Token aniqlanmadi"
        )
