import asyncio
import graphene
from flask_graphql_auth import query_header_jwt_required

from ..fields.book import BookListResponseField
from ..responses.book import BookListProtected
from ...application import SearchBook


class BookQuery(graphene.ObjectType):
    result = graphene.Field(type=BookListProtected)

    @classmethod
    @query_header_jwt_required
    def resolve_list(cls, _, info, payload):
        results = asyncio.run(SearchBook().do(payload))
        return BookListResponseField(list=results)
