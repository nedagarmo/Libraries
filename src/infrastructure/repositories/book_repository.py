from .base_repository import BaseRepository


class BookRepository(BaseRepository):
    def __init__(self):
        super(BookRepository, self).__init__()
        self.table_name = 'Book'
        self.key_schema = 'book_id'
