from base_repository import BaseRepository


class BookRepository(BaseRepository):
    def __init__(self):
        super(BookRepository, self).__init__()
        self.table_name = 'Books'
