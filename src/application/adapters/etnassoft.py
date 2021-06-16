import aiohttp
from .iadapter import IAdapter
from ...domain.models import Book


class EtnassoftAdapter(IAdapter):

    async def do(self, query: str):
        """
        Consulta al API los registros que coincidan con el criterio de búsqueda
        :param query: criterio de búsqueda
        :return: lista de resultados formateados
        """

        # TODO: Flexibilizar paginación
        async with aiohttp.ClientSession() as session:
            api_url = f'https://www.etnassoft.com/api/v1/get/?keyword={query}'
            async with session.get(api_url) as response:
                results = await response.json(content_type='text/html')
                for i in range(len(results)):
                    book = results[i]
                    results[i] = Book(book_external_id=book["ID"], book_name=book["title"],
                                      book_authors=[book["author"]], book_categories=book["categories"],
                                      book_publication_date=book["publisher_date"], book_editor=book["publisher"],
                                      book_description=book["content"], book_image=book["thumbnail"],
                                      book_source="Etnassoft").to_dict()
                return results
