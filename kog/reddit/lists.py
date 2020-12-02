from praw.models import Submission
from typing import Generator, Optional
from kog.reddit import create_reddit_object

MAX_STICKIES = 2


class SubredditStickies:
    def __init__(self, subreddit_name: str, filter_substring: Optional[str] = ''):
        self.reddit = create_reddit_object()
        self.subreddit_name = subreddit_name
        self.filter_substring = filter_substring

    @property
    def sticky_ids(self) -> Generator[Submission, None, None]:
        for i in range(1, MAX_STICKIES+1):
            sticky_id = self.reddit.subreddit(self.subreddit_name).sticky(i)
            if self.filter_substring in self.reddit.submission(id=sticky_id).title:
                yield sticky_id
