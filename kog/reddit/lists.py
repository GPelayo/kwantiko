from praw.models import Submission
from typing import Generator
from kog.reddit import create_reddit_object
from kog.aws.secrets import AWSSecretsManager

MAX_STICKIES = 2


class SubredditStickies:
    def __init__(self, subreddit_name: str, secrets_manager: AWSSecretsManager, filter_substring: str = ''):
        self.reddit = create_reddit_object(secrets_manager.secrets)
        self.subreddit_name = subreddit_name
        self.filter_substring = filter_substring

    @property
    def sticky_ids(self) -> Generator[Submission, None, None]:
        for i in range(1, MAX_STICKIES+1):
            sticky_id = self.reddit.subreddit(self.subreddit_name).sticky(i)
            if self.filter_substring in self.reddit.submission(id=sticky_id).title:
                yield sticky_id
