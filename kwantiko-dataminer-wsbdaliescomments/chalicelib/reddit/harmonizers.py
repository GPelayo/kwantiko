from praw.models import Comment

from chalicelib.common.harmonizers import Harmonizer
from chalicelib.common.models import Post


class RedditCommentHarmonizer(Harmonizer):
    def serialize(self, comment: Comment) -> Post:
        post = Post()
        post.id = comment.id
        post.date_submitted = int(comment.created_utc)
        post.user = comment.author.name if comment.author else '[deleted]'
        post.message = comment.body
        post.sentiment = comment.score
        return post
