from abc import ABC, abstractmethod


class AbstractReferalsRepository(ABC):

    @abstractmethod
    async def create_referal(self):
        ...

    @abstractmethod
    async def get_referals(self):
        ...
