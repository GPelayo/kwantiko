from praw.models import Comment

from chalicelib.common.harmonizers import Harmonizer
from chalicelib.constants import POST_ID_FIELDNAME


class RedditCommentHarmonizer(Harmonizer):
    def serialize(self, comment: Comment):
        raise NotImplementedError()


class SimpleRedditCommentHarmonizer(RedditCommentHarmonizer):
    def serialize(self, comment: Comment):
        translated_comment = {POST_ID_FIELDNAME: comment.id,
                              'date_submitted': int(comment.created_utc),
                              'user': comment.author.name if comment.author else '[deleted]',
                              'message': comment.body,
                              'score': comment.score}
        return translated_comment
