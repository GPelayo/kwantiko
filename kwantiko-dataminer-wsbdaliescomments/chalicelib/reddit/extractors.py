from praw.models import MoreComments
from praw import Reddit

from chalicelib.common.extractors import Extractor
from chalicelib.reddit.harmonizers import RedditCommentHarmonizer
from chalicelib.secrets import SecretsManager
from chalicelib.config import (REDDIT_USER_AGENT,
                               REDDIT_CLIENT_ID,
                               REDDIT_CLIENT_SECRET,
                               REDDIT_USERNAME,
                               REDDIT_PASSWORD)


class RedditCommentExtractor(Extractor):
    def __init__(self,
                 secrets_manager: SecretsManager,
                 post_id: str,
                 harmonizer: RedditCommentHarmonizer,
                 retrieval_limit: int = 0):
        self.secrets = secrets_manager.secrets
        reddit = Reddit(user_agent=self.secrets[REDDIT_USER_AGENT],
                        client_id=self.secrets[REDDIT_CLIENT_ID],
                        client_secret=self.secrets[REDDIT_CLIENT_SECRET],
                        username=self.secrets[REDDIT_USERNAME],
                        password=self.secrets[REDDIT_PASSWORD])
        self.post_id = post_id
        self.submission = reddit.submission(id=post_id)
        self.submission.comment_sort = 'new'
        self.date_submission_created = self.submission.created_utc
        self.harmonizer = harmonizer
        self.comments_read = 0
        self.retrieval_limit = retrieval_limit

    @property
    def posts(self):
        yield from self._read_posts(self.submission.comments)

    def _read_posts(self, comments):
        for comment_node in comments:
            if isinstance(comment_node, MoreComments):
                self._read_posts(comment_node.comments())
            else:
                serialized_comment = self.harmonizer.serialize(comment_node)
                yield serialized_comment
                self.comments_read += 1
                if self.retrieval_limit < self.comments_read:
                    break
