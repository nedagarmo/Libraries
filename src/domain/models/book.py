import uuid
import graphene


class Book(graphene.ObjectType):
    book_id = graphene.String(default_value=str(uuid.uuid4()))
    book_external_id = graphene.String()
    book_name = graphene.NonNull(graphene.String)
    book_subtitle = graphene.String()
    book_authors = graphene.List(graphene.NonNull(graphene.String))
    book_categories = graphene.List(graphene.NonNull(graphene.String))
    book_publication_date = graphene.String(default_value="Desconocida")
    book_editor = graphene.String(default_value="Desconocido")
    book_description = graphene.String(default_value="Sin descripción")
    book_image = graphene.String()
    book_source = graphene.String(default_value="DB Interna")

    def __repr__(self):
        return f'<Book {self.book_id}>'

    def to_dict(self):
        return {
            'book_id': self.book_id,
            'book_external_id': self.book_external_id,
            'book_name': self.book_name,
            'book_subtitle': self.book_subtitle,
            'book_authors': self.book_authors,
            'book_categories': self.book_categories,
            'book_publication_date': self.book_publication_date,
            'book_editor': self.book_editor,
            'book_description': self.book_description,
            'book_image': self.book_image,
            'book_source': self.book_source
        }
