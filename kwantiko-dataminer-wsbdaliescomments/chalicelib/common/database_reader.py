import boto3

from chalicelib.dynamodb import create_dynamodb_table
from chalicelib.constants import build_reddit_posts_viewed_table_name, build_reddit_posts_table_name, POST_ID_FIELDNAME


class PostDatabaseReader:
    @property
    def post_items(self):
        raise NotImplementedError


class DynamoDBPostReader(PostDatabaseReader):
    def __init__(self, post_id: str):
        self.database = boto3.resource('dynamodb')
        self.posts_table = self.database.Table(build_reddit_posts_table_name(post_id))
        self.viewed_posts_table = create_dynamodb_table(build_reddit_posts_viewed_table_name(post_id),
                                                        POST_ID_FIELDNAME)

    @property
    def post_items(self):
        table_response = self.posts_table.scan()
        for item in table_response['Items']:
            if 'Item' not in self.viewed_posts_table.get_item(Key={POST_ID_FIELDNAME: item[POST_ID_FIELDNAME]}).keys():
                yield item
                self.viewed_posts_table.put_item(Item={POST_ID_FIELDNAME: item[POST_ID_FIELDNAME]})
