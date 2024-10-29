from src.repositories.user.user import UserRepository
from src.schemas.schemas import CreateUserRequest

class UserService():
    def __init__(self, UserRepository:UserRepository):
        self.UserRepository = UserRepository

    async def create_user(self, model: CreateUserRequest) -> None:
        if model.referals.count("@"):
            await self.UserRepository.create_user(model)

