from typing import Generator

from praw.models import MoreComments, Comment

from kog.common.extractors import Extractor
from kog.common.models import Post
from kog.reddit import create_reddit_object
from kog.reddit.harmonizers import RedditCommentHarmonizer


class RedditCommentExtractor(Extractor):
    def __init__(self,
                 post_id: str,
                 harmonizer: RedditCommentHarmonizer,
                 retrieval_limit: int = 10):
        self.post_id = post_id
        reddit = create_reddit_object()
        self.submission = reddit.submission(id=post_id)
        self.submission.comment_sort = 'new'
        self.date_submission_created = self.submission.created_utc
        self.harmonizer = harmonizer
        self.comments_read = 0
        self.retrieval_limit = retrieval_limit

    @property
    def posts(self) -> Generator[Post, None, None]:
        self.comments_read = 0
        for post in self._read_posts(self.submission.comments):
            yield post
            self.comments_read += 1
            if self.retrieval_limit < self.comments_read:
                break

    def _read_posts(self, comments) -> Generator[Post, None, None]:
        for comment_node in comments:
            if isinstance(comment_node, MoreComments):
                self._read_posts(comment_node.comments())
            elif isinstance(comment_node, Comment):
                serialized_comment = self.harmonizer.serialize(comment_node)
                yield serialized_comment
