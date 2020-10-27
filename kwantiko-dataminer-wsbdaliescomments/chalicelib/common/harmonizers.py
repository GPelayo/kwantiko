from chalicelib.common.models import Post
from chalicelib.constants import POST_ID_FIELDNAME


class Harmonizer:
    def serialize(self, post: any) -> Post:
        raise NotImplementedError


class DynamoDBPostHarmonizer(Harmonizer):
    def serialize(self, post_db_item: dict):
        output_post = Post()
        output_post.id = post_db_item[POST_ID_FIELDNAME]
        output_post.date_submitted = post_db_item['date_submitted']
        output_post.user = post_db_item['user']
        output_post.message = post_db_item['message']
        output_post.sentiment = post_db_item['score']
        return output_post
