import aioboto3
from boto3.dynamodb.conditions import Key, Attr

from ...config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY
from ...domain import IRepository
from ...domain.models import Book


class BaseRepository(IRepository):

    def __init__(self):
        self.table_name = None
        self.service = 'dynamodb'
        self.region = 'us-east-2'
        self.key_schema = None

    async def get(self, query):
        async with aioboto3.resource(self.service, region_name=self.region, aws_access_key_id=AWS_ACCESS_KEY_ID,
                                     aws_secret_access_key=AWS_SECRET_ACCESS_KEY) as client:
            table = await client.Table(self.table_name)
            result = await table.scan(
                FilterExpression=Attr('book_name').contains(query) | Attr('book_subtitle').contains(query)
                                                                   | Attr('book_authors').contains(query)
                                                                   | Attr('book_categories').contains(query)
                                                                   | Attr('book_description').contains(query)
                                                                   | Attr('book_editor').contains(query)
                                                                   | Attr('book_external_id').contains(query)
                                                                   | Attr('book_publication_date').contains(query)
            )

            items = [Book(**item) for item in result["Items"]]
            return items

    async def get_by_pk(self, query):
        async with aioboto3.resource(self.service, region_name=self.region, aws_access_key_id=AWS_ACCESS_KEY_ID,
                                     aws_secret_access_key=AWS_SECRET_ACCESS_KEY) as client:
            table = await client.Table(self.table_name)
            result = await table.query(
                FilterExpression=Key(self.key_schema).eq(query)
            )
            return result

    async def get_by(self, payload):
        async with aioboto3.resource(self.service, region_name=self.region, aws_access_key_id=AWS_ACCESS_KEY_ID,
                                     aws_secret_access_key=AWS_SECRET_ACCESS_KEY) as client:
            table = await client.Table(self.table_name)
            result = await table.scan(
                FilterExpression=Key(payload["field"]).eq(payload["query"])
            )
            return result

    async def all(self):
        async with aioboto3.resource(self.service, region_name=self.region, aws_access_key_id=AWS_ACCESS_KEY_ID,
                                     aws_secret_access_key=AWS_SECRET_ACCESS_KEY) as client:
            table = await client.Table(self.table_name)
            return await table.scan()

    async def insert(self, instance):
        async with aioboto3.resource(self.service, region_name=self.region, aws_access_key_id=AWS_ACCESS_KEY_ID,
                                     aws_secret_access_key=AWS_SECRET_ACCESS_KEY) as client:
            table = await client.Table(self.table_name)
            result = await table.put_item(Item=instance.to_dict())
            return result["ResponseMetadata"]["HTTPStatusCode"] == 200

    async def delete(self, payload: dict):
        async with aioboto3.resource(self.service, region_name=self.region, aws_access_key_id=AWS_ACCESS_KEY_ID,
                                     aws_secret_access_key=AWS_SECRET_ACCESS_KEY) as client:
            table = await client.Table(self.table_name)
            result = await table.delete_item(
                Key=payload
            )

            return result["ResponseMetadata"]["HTTPStatusCode"] == 200
