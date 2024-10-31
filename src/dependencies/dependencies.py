from src.repositories.redis.redis import RedisRepository
from src.repositories.user.user import UserRepository
from src.services.user.user import UserService
from src.repositories.referals.referal import ReferalRepository

ReferalRepo = ReferalRepository()
UserRepo = UserRepository()
RedisRepo = RedisRepository()

Service = UserService(UserRepository=UserRepo,
                      ReferalRepository=ReferalRepo, RedisRepository=RedisRepo
                      )


async def UserServiceReturn():
    return Service
