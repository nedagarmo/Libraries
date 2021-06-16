from .iservice import IService
from ..exceptions import WrongDataException
from ...domain.models import Book
from ...infrastructure.repositories import BookRepository


class CreateBook(IService):

    async def do(self, **kwargs):
        """
        Crea un nuevo libro en la base de datos
        :param kwargs: argumentos proporcionados para la creación de un libro
        :return: retorna un objeto con los datos de la nueva instancia
        """
        book = Book(**kwargs, book_action='C')

        if book.external_id and await self.exists('book_external_id', book.external_id):
            raise WrongDataException({"message": "Este libro ya existe en la base de datos de esta biblioteca!"})

        repository = BookRepository()
        return await repository.insert(book)

    async def exists(self, field, query):
        result = await BookRepository().get_by({"field": field, "query": query})
        print(result)
        return result["Count"] > 0
