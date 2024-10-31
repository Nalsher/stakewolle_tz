from sqlalchemy import select
from src.repositories.user.base import AbstractUserRepository
from src.schemas.schemas import CreateUserRequestSchema
from src.database.postgresql.tables.tables import User as _User
from src.database.postgresql.base.base import async_session, engine


class UserRepository(AbstractUserRepository):
    session = async_session
    engine = engine

    async def create_user(self, model: CreateUserRequestSchema) -> int:
        async with self.session() as session:
            User = _User(username=model.username,
                         password=model.password, email=model.email
                         )
            session.add(User)
            await session.commit()
            await session.refresh(User)
            return User.id

    async def get_user(self, id: int) -> _User | None:
        async with self.session() as session:
            query = select(_User).where(_User.id == id)
            execute = await session.execute(query)
            try:
                User = execute.scalar_one()
                return User
            finally:
                return None

    async def get_user_id_by_email(self, email: str) -> int | None:
        async with self.session() as session:
            query = select(_User).where(_User.email == email)
            execute = await session.execute(query)
            try:
                User = execute.scalar_one()
                return User.id
            finally:
                return None

    async def get_user_by_username(self, username: str) -> _User | None:
        async with self.session() as session:
            query = select(_User).where(_User.username == username)
            execute = await session.execute(query)
            try:
                User = execute.scalar_one()
                return User
            finally:
                return None

    async def get_users(self, id: list[int]) -> list | None:
        users_list = []
        try:
            for i in id:
                users_list.append(await self.get_user(i))
            return users_list
        finally:
            return None
