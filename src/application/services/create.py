from iservice import IService
from ...domain.models import Book
from ...infrastructure.repositories import BookRepository


class CreateBook(IService):

    def do(self, **kwargs):
        """
        Crea un nuevo libro en la base de datos
        :param kwargs: argumentos proporcionados para la creación de un libro
        :return: retorna un objeto con los datos de la nueva instancia
        """
        book = Book(**kwargs)
        repository = BookRepository()
        return repository.insert(book)
