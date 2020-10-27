import boto3

from chalicelib.common.models import Post
from chalicelib.constants import build_reddit_posts_table_name, POST_ID_FIELDNAME
from chalicelib.dynamodb import create_dynamodb_table


class Outflow:
    def send(self, item: Post):
        raise NotImplementedError()


class DynamoDBPostWriter(Outflow):
    def __init__(self, post_id: str):
        self.database = boto3.resource('dynamodb')
        self.table = create_dynamodb_table(build_reddit_posts_table_name(post_id), POST_ID_FIELDNAME)

    def send(self, post: Post):
        item = {POST_ID_FIELDNAME: post.id,
                'date_submitted': int(post.date_submitted),
                'user': post.user,
                'message': post.message,
                'score': post.sentiment}
        self.table.put_item(Item=item)
