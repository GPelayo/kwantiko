from kog.common.formatter import Formatter
from kog.common.models import Post


class DiscordFormatter(Formatter):
    @staticmethod
    def format_post(post: Post) -> Post:
        post.message = post.message[:1000]
        return post
