import asyncio
from .iservice import IService
from ..exceptions import WrongDataException
from ...infrastructure.repositories import BookRepository
from ..adapters import GoogleAdapter, EtnassoftAdapter


class SearchBook(IService):

    async def do(self, **kwargs):
        """
        Busca un libro que coincida con los parámetros de búsqueda
        :param kwargs: campos por el que se filtrarán los datos, para esta
                       versión solo será válido el parámetro query que servirá para
                       filtrar por todos los campos de los libros.
        :return: lista de objetos que coincidan con el criterio de búsqueda
        """

        query = kwargs.pop('query', None)

        if query is None:
            raise WrongDataException({"message": "Para buscar un libro, debe proporcionar una palabra clave que "
                                                 "permita filtrar los resultados"})

        results = await BookRepository().get(query)
        if len(results['Items']) <= 0:
            apis_result = await asyncio.gather(GoogleAdapter().do(query), EtnassoftAdapter().do(query))
            results['Items'] = apis_result[0] + apis_result[1]
            results['Count'] = len(results['Items'])

        return results
