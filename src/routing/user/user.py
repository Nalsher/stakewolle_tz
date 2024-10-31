from fastapi import APIRouter
from fastapi.params import Depends
from src.dependencies.dependencies import UserServiceReturn
from src.schemas.schemas import CreateUserRequestSchema, GetCodeByEmailSchema
from src.services.user.user import UserService

users_router = APIRouter(prefix="/users")


@users_router.post(path='/create',
                   summary='Create new user')
async def create_user(user: CreateUserRequestSchema,
                      service: UserService = Depends(UserServiceReturn)):
    user_id = await service.create_user(model=user)
    return user_id


@users_router.post(path="/getcode",
                   summary="Get Referal code by user email")
async def get_code_by_mail(email: GetCodeByEmailSchema,
                           service: UserService = Depends(UserServiceReturn)):
    get_code = await service.get_code_by_mail(email.email)
    return get_code


@users_router.get(path="/getrefs/{id}",
                  summary="Get all referals by id")
async def get_all_refs(id: int,
                       service: UserService = Depends(UserServiceReturn)):
    referals = await service.get_all_refers(id)
    return referals
