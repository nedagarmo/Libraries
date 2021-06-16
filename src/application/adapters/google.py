import aiohttp
from .iadapter import IAdapter
from ...domain.models import Book


class GoogleAdapter(IAdapter):
    async def do(self, query: str):
        """
        Consulta al API los registros que coincidan con el criterio de búsqueda
        :param query: criterio de búsqueda
        :return: lista de resultados formateados
        """

        # TODO: Flexibilizar paginación
        async with aiohttp.ClientSession() as session:
            api_url = f'https://www.googleapis.com/books/v1/volumes?q={query.replace(" ", "+")}'
            async with session.get(api_url) as response:
                data = await response.json()
                results = []
                for i in range(len(data["items"])):
                    book = data["items"][i]
                    book_info = book["volumeInfo"]
                    results.append(Book(book_external_id=book["id"], book_name=book_info["title"],
                                        book_authors=book_info.get("authors", []),
                                        book_categories=book_info.get("categories", []),
                                        book_publication_date=book_info.get("publishedDate", None),
                                        book_editor=book_info.get("publisher", None),
                                        book_description=book_info.get("description", None),
                                        book_image=book_info.get("imageLinks", {"thumbnail": None})["thumbnail"],
                                        book_source="Google").to_dict())
                return results
