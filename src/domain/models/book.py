import uuid


class Book:

    def __init__(self, book_id=None, book_external_id=None, book_name=None, book_subtitle=None, book_authors=None,
                 book_categories=None, book_publication_date=None, book_editor=None, book_description=None,
                 book_image=None, book_source=None, book_action='S'):
        self.id = book_id or str(uuid.uuid4())
        self.external_id = book_external_id
        self.name = book_name
        self.subtitle = book_subtitle
        self.authors = book_authors or []
        self.categories = book_categories or []
        self.publication_date = book_publication_date
        self.editor = book_editor
        self.description = book_description
        self.image = book_image
        self.source = book_source or "DB Interna" if book_action == 'S' else "DB Interna"

    def __repr__(self):
        return f'<Book {self.id}>'

    def to_dict(self):
        return {
            'book_id': self.id,
            'book_external_id': self.external_id,
            'book_name': self.name,
            'book_subtitle': self.subtitle,
            'book_authors': self.authors,
            'book_categories': self.categories,
            'book_publication_date': self.publication_date,
            'book_editor': self.editor,
            'book_description': self.description,
            'book_image': self.image,
            'book_source': self.source
        }
