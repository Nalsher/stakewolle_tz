from datetime import datetime, timedelta
from typing import Any
from src.repositories.redis.base import AbstractRedisRepository
from src.database.redis.config.config import redis


class RedisRepository(AbstractRedisRepository):

    async def create_code(self, code: str, user_id: int) -> None:
        redis.set(user_id, code)

    async def expire_set(self, code: str) -> None:
        date = datetime.datetime.now() + timedelta(hours=1)
        string_date = date.strftime("%m:%d:%H:%M")
        redis.set(code, string_date)

    async def check_if_expires(self, code: str) -> Any:
        code = str(redis.get(code))
        return datetime.strptime(code, "%m:%d:%H:%M")

    async def delete_code(self, user_id: int) -> None:
        redis.delete(user_id)

    async def get_code(self, user_id: int) -> str | None:
        try:
            code = redis.get(user_id)
            return code
        finally:
            return None

    async def get_id_by_code(self, code: str) -> int | None:
        try:
            for key in redis.scan_iter():
                if redis.get(key).decode("utf-8") == code:
                    key = int(key)
                    return key
        finally:
            return False

    async def check_if_user_have_code(self, user_id: int) -> bool:
        try:
            user_code_get = redis.get(user_id)
            if user_code_get:
                return True
            else:
                return False
        finally:
            return False
