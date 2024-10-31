from fastapi import APIRouter
from fastapi.params import Depends
from src.dependencies.dependencies import UserServiceReturn
from src.schemas.schemas import AuthRequestSchema
from src.services.user.user import UserService

auth_router = APIRouter(prefix="/auth")


@auth_router.post(path="/login",
                  summary="Login in account"
                  )
async def login(authmodel: AuthRequestSchema,
                service: UserService = Depends(UserServiceReturn)
                ):
    auth_reqeust = await service.login(authmodel)
    return auth_reqeust
