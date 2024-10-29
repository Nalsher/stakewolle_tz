from src.repositories.user.user import UserRepository as _UserRepository
from src.services.user.user import UserService as _UserService


UserRepository = _UserRepository()

UserService = _UserService(UserRepository=UserRepository)

async def UserServiceReturn():
    return UserService