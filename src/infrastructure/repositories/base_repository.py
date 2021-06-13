
class BaseRepository:

    def __init__(self, db_connection):
        self.db_connection = db_connection

    def insert(self, instance):
        pass
