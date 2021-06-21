from .iservice import IService
from ..exceptions import WrongDataException
from ...domain.models import Book
from ...infrastructure.repositories import BookRepository


class DeleteBook(IService):

    async def do(self, key):
        """
        Elimina un libro en la base de datos
        :return: retorna un booleano según el estado de la ejeución del proceso
        """

        book = await self.exists('book_id', key)
        if not book:
            raise WrongDataException({"message": "Este identificador no existe en la base de datos de esta biblioteca!"})

        repository = BookRepository()
        return await repository.delete({
            "book_id": key,
            "book_name": book["book_name"]
        })

    async def exists(self, field, query):
        result = await BookRepository().get_by({"field": field, "query": query})
        if result["Count"] > 0:
            return result["Items"][0]
