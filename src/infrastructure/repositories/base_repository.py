import aioboto3
from boto3.dynamodb.conditions import Key

from ...config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY
from ...domain import IRepository


class BaseRepository(IRepository):

    def __init__(self):
        self.table_name = None
        self.service = 'dynamodb'
        self.region = 'us-east-2'

    async def get(self, payload):
        async with aioboto3.resource(self.service, region_name=self.region, aws_access_key_id=AWS_ACCESS_KEY_ID,
                                     aws_secret_access_key=AWS_SECRET_ACCESS_KEY) as client:
            table = await client.Table(self.table_name)
            result = await table.query(
                KeyConditionExpression=Key('name').eq('test1')
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
            return await table.put_item(Item={'pk': instance.id, 'name': instance.name})
