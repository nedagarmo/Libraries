import graphene

from ...domain.models import Book


class BookListResponseField(graphene.ObjectType):
    list = graphene.List(Book)


class BookMutationResponseField(graphene.ObjectType):
    ok = graphene.Boolean()
    identifier = graphene.String()
