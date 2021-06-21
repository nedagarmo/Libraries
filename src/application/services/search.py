import asyncio
from .iservice import IService
from ..exceptions import WrongDataException
from ...infrastructure.repositories import BookRepository
from ..adapters import GoogleAdapter, EtnassoftAdapter


class SearchBook(IService):

    async def do(self, payload):
        """
        Busca un libro que coincida con los parámetros de búsqueda
        :param payload: valor por el que se filtrarán los datos aplicado a todos los campos de los libros.
        :return: lista de objetos que coincidan con el criterio de búsqueda
        """

        results = await BookRepository().get(payload)
        if len(results) <= 0:
            apis_result = await asyncio.gather(GoogleAdapter().do(payload), EtnassoftAdapter().do(payload))
            results = apis_result[0] + apis_result[1]

        return results
