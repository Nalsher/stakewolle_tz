from fastapi import APIRouter
from fastapi import Cookie
from fastapi.params import Depends
from typing import Annotated
from src.dependencies.dependencies import UserServiceReturn
from src.schemas.schemas import CreateReferalRequestSchema
from src.services.user.user import UserService

referal_router = APIRouter(prefix="/referal")


@referal_router.post("/create",
                     summary="Create referal code"
                     )
async def create_code(code: CreateReferalRequestSchema,
                      service: UserService = Depends(UserServiceReturn),
                      token: Annotated[str, Cookie()] = None):
    create_code = await service.create_referal_code(code.code, token)
    return create_code


@referal_router.get("/delete",
                    summary="Delete referal code")
async def delete_code(service: UserService = Depends(UserServiceReturn),
                      token: Annotated[str, Cookie()] = None):
    delete_code = await service.delete_referal_code(token)
    return delete_code
