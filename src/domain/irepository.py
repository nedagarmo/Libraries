from abc import ABC


class IRepository(ABC):

    async def get(self, payload):
        pass

    async def all(self):
        pass

    async def insert(self, instance):
        pass
