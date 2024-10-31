from src.schemas.base import Base
from pydantic import EmailStr


class CreateUserRequestSchema(Base):
    username: str
    password: str
    email: EmailStr
    referals: str | None = None


class UpdateUserRequestSchema(Base):
    username: str | None = None
    password: str | None = None
    email: str | None = None


class GetCodeByEmailSchema(Base):
    email: EmailStr


class CreateReferalRequestSchema(Base):
    code: str


class AuthRequestSchema(Base):
    username: str
    password: str


class GetUserResponseSchema:
    id: int
    username: str
    password: str
    email: str
    referals: list[int] | None = None


class GetUserResponsesSchema:
    user: list[GetUserResponseSchema]
