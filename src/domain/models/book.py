import uuid


class Book:

    def __init__(self, book_id=None, book_name=None):
        self.id = book_id or uuid.uuid4()
        self.name = book_name

    def __repr__(self):
        return f'<Book {self.id}>'

    def as_dict(self):
        return {
            'id': str(self.id),
            'name': self.name
        }
