from abc import ABC, abstractmethod


class AbstractRedisRepository(ABC):

    @abstractmethod
    async def create_code(self):
        ...

    @abstractmethod
    async def delete_code(self):
        ...

    @abstractmethod
    async def get_code(self):
        ...

    @abstractmethod
    async def get_id_by_code(self):
        ...

    @abstractmethod
    async def check_if_user_have_code(self):
        ...
