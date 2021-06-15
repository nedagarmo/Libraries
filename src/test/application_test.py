from ..application import SearchBook, CreateBook
from ..domain.models import Book


def test_search_exist_book():
    results = SearchBook().do(name='term')
    assert len(results) > 0


def test_search_no_exist_book():
    results = SearchBook().do('anything')
    assert len(results) == 0


def test_create_new_book():
    book = CreateBook(name="Python 3")
    assert isinstance(book, Book)
