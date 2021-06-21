import graphene
from flask_graphql_auth import AuthInfoField

from ..fields.book import BookListResponseField, BookMutationResponseField


class BookListProtected(graphene.Union):
    class Meta:
        types = (BookListResponseField, AuthInfoField)

    @classmethod
    def resolve_type(cls, instance, info):
        return type(instance)


class BookMutationProtected(graphene.Union):
    class Meta:
        types = (BookMutationResponseField, AuthInfoField)

    @classmethod
    def resolve_type(cls, instance, info):
        return type(instance)
