from chalicelib.common import PostMiner, Publisher
from chalicelib.common.database_reader import DynamoDBPostReader
from chalicelib.common.filters import LinkFilter
from chalicelib.common.outflows import DynamoDBPostWriter
from chalicelib.discord.formatter import DiscordFormatter
from chalicelib.discord.outflows import Messenger as DiscordMessager
from chalicelib.reddit.extractors import RedditCommentExtractor
from chalicelib.reddit.harmonizers import SimpleRedditCommentHarmonizer
from chalicelib.secrets import AWSSecretsManager
from chalicelib.config import DISCORD_SECRET_NAME, REDDIT_SECRET_NAME


class RedditLinkMiner(PostMiner):
    def __init__(self, post_id: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.extractor = RedditCommentExtractor(AWSSecretsManager(REDDIT_SECRET_NAME),
                                                post_id,
                                                SimpleRedditCommentHarmonizer(),
                                                retrieval_limit=250)
        self.filters = [LinkFilter()]
        self.formatter = [DiscordFormatter()]
        self.outflows = [DynamoDBPostWriter(post_id)]


class RedditLinkPublisher(Publisher):
    def __init__(self, post_id: str, *args, **kwargs):
        super().__init__(post_id, args, kwargs)
        self.database_reader = DynamoDBPostReader(post_id)
        self.formatter = [DiscordFormatter()]
        self.messenger = DiscordMessager(AWSSecretsManager(DISCORD_SECRET_NAME))
