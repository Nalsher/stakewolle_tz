from src.schemas.base import Base
from pydantic import EmailStr
from typing import Union


class CreateUserRequest(Base):
    username: str
    password: str
    email: str
    referals: Union[EmailStr, int , None] = None

class UpdateUserRequest(Base):
    username: str | None = None
    password: str | None = None
    email: str | None = None


class GetUserResponse:
    id: int
    username: str
    password: str
    email: str
    referals: list[int] | None = None


class GetUserResponses:
    user: list[GetUserResponse]
