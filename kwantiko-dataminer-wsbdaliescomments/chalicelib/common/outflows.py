import boto3

from chalicelib.constants import build_reddit_posts_table_name, POST_ID_FIELDNAME
from chalicelib.dynamodb import create_dynamodb_table


class Outflow:
    def send(self, item: dict):
        raise NotImplementedError()


class DynamoDBPostWriter(Outflow):
    def __init__(self, post_id: str):
        self.database = boto3.resource('dynamodb')
        self.table = create_dynamodb_table(build_reddit_posts_table_name(post_id), POST_ID_FIELDNAME)

    def send(self, item: dict):
        self.table.put_item(Item=item)
