from typing import Any

from src.dependencies.dependencies import UserService
from src.repositories.user.base import AbstractUserRepository
from src.schemas.schemas import CreateUserRequest, GetUserResponse
from src.database.postgresql.tables.tables import User as _User
from src.database.postgresql.base.base import async_session, engine



class UserRepository(AbstractUserRepository):
    session = async_session
    engine = engine

    async def create_user(self, model: CreateUserRequest) -> None:
        async with self.session() as session:
            User = _User(username=model.username, password=model.password, email=model.email)
            session.add(User)
            await session.commit()

    async def get_user(self, id: int) -> GetUserResponse:
        async with self.session() as session:
            User = await session.get(_User, id)
            UserToDTO = GetUserResponse(GetUserResponse.username==User.username,GetUserResponse.email==User.email,\
                                        GetUserResponse.password==User.password,GetUserResponse.id==id)
            return UserToDTO

    async def get_users(self, id: list[int]) -> list:
        users_list = []
        for i in id:
            users_list.append(await self.get_user(i))









