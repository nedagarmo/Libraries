import graphene
from .book import BookCreateMutation, BookDeleteMutation
from .auth import AuthMutation, RefreshMutation


class MainMutation(graphene.ObjectType):
    book = BookCreateMutation.Field()
    delete = BookDeleteMutation.Field()
    auth = AuthMutation.Field()
    refresh = RefreshMutation.Field()
