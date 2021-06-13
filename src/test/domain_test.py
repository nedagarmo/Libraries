from ..domain.models import Book


def test_create_new_book():
    book = Book('Libro 1')
    assert book.id is not None
