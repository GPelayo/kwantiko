from kog.common import PostMiner
from kog.common.cache import LocalTestCacheManager
from kog.common.filters import LinkFilter
from kog.common.models import Post
from kog.discord.formatter import DiscordFormatter
from kog.discord.outflows import Messenger as DiscordMessager
from kog.reddit.extractors import RedditCommentExtractor
from kog.reddit.harmonizers import RedditCommentHarmonizer
from kog.reddit.lists import SubredditStickies
from kog.secrets import SecretsManager


class WSBLinkMiner(PostMiner):
    def __init__(self,
                 discord_secrets_manager: SecretsManager,
                 reddit_secrets_manager: SecretsManager,
                 retrieval_limit: int = 10000,
                 *args,
                 **kwargs):

        super().__init__(*args, **kwargs)

        sticky_id = next(SubredditStickies('wallstreetbets', reddit_secrets_manager).sticky_ids)
        self.extractor = RedditCommentExtractor(reddit_secrets_manager,
                                                sticky_id,
                                                RedditCommentHarmonizer(),
                                                retrieval_limit=retrieval_limit)
        self.cache_manager = LocalTestCacheManager()
        self.filters = [LinkFilter()]
        self.formatter = [DiscordFormatter()]
        self.outflows = [DiscordMessager(discord_secrets_manager)]
        self.outflows = [DiscordMessager(discord_secrets_manager)]
