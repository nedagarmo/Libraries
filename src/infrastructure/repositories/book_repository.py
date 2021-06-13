from ...domain import IRepository
from ..database import reports_table
from base_repository import BaseRepository


class BookRepository(BaseRepository, IRepository):

    def insert(self, book):
        with self.db_connection.begin():
            self.db_connection.execute(
                reports_table.insert(),
                book.as_dict()
            )
