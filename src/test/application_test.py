from ..application import SearchBook


def test_search_exist_book():
    results = SearchBook().do('term')
    assert len(results) > 0


def test_search_no_exist_book():
    results = SearchBook().do('anything')
    assert len(results) == 0
