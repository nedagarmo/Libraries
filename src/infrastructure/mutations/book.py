import graphene
import asyncio
from flask_graphql_auth import mutation_header_jwt_required

from ..fields.book import BookMutationResponseField
from ..responses.book import BookMutationProtected
from ...application import CreateBook, DeleteBook


class BookCreateMutation(graphene.Mutation):
    class Arguments:
        book_external_id = graphene.String()
        book_name = graphene.NonNull(graphene.String)
        book_subtitle = graphene.String()
        book_authors = graphene.List(graphene.NonNull(graphene.String))
        book_categories = graphene.List(graphene.NonNull(graphene.String))
        book_publication_date = graphene.NonNull(graphene.String)
        book_editor = graphene.NonNull(graphene.String)
        book_description = graphene.NonNull(graphene.String)
        book_image = graphene.String()

    result = graphene.Field(type=BookMutationProtected)

    @classmethod
    @mutation_header_jwt_required
    def mutate(cls, _, info, book_name,
               book_publication_date, book_editor, book_description, book_image=None, book_external_id=None,
               book_subtitle=None, book_authors=None, book_categories=None):
        data = {
            "book_external_id": book_external_id,
            "book_name": book_name,
            "book_subtitle": book_subtitle or "",
            "book_authors": book_authors if book_authors else ["Desconocido"],
            "book_categories": book_categories if book_categories else ["Desconocida"],
            "book_publication_date": book_publication_date,
            "book_editor": book_editor,
            "book_description": book_description or "Sin descripción",
            "book_image": book_image or ""
        }
        result, book = asyncio.run(CreateBook().do(**data))
        return BookCreateMutation(result=BookMutationResponseField(ok=result, identifier=book.book_id))


class BookDeleteMutation(graphene.Mutation):
    class Arguments:
        book_id = graphene.NonNull(graphene.String)

    result = graphene.Field(type=BookMutationProtected)

    @classmethod
    @mutation_header_jwt_required
    def mutate(cls, _, info, book_id):
        result = asyncio.run(DeleteBook().do(book_id))
        return BookCreateMutation(result=BookMutationResponseField(ok=result, identifier=None))
