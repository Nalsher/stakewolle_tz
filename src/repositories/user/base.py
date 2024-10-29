from abc import abstractmethod, ABC


class AbstractUserRepository(ABC):

    @abstractmethod
    async def create_user(self):
        ...

    @abstractmethod
    async def get_user(self):
        ...

    @abstractmethod
    async def get_users(self):
        ...
