import graphene

from ...domain.models import Book


class BookListResponseField(graphene.ObjectType):
    list = graphene.List(Book, payload=graphene.NonNull(graphene.String))


class BookMutationResponseField(graphene.ObjectType):
    ok = graphene.Boolean()
    identifier = graphene.String()
