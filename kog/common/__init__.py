from typing import List

from kog.common.database_reader import PostDatabaseReader
from kog.common.extractors import Extractor
from kog.common.filters import Filter
from kog.common.formatter import Formatter
from kog.common.outflows import Outflow
from kog.common.cache import CacheManager


class PostMiner:
    def __init__(self, *args, **kwargs):
        self.extractor = []   # type: List[Extractor]
        self.outflows = []    # type: List[Outflow]
        self.filters = []     # type: List[Filter]
        self.formatter = []   # type: List[Formatter]
        self.cache_manager = None  # type: CacheManager

    def process(self):
        for post in self.extractor.posts:
            if not self.cache_manager.has_key(post.id):
                for m in self.formatter:
                    post = m.format_post(post)
                for outflow in self.outflows:
                    if not self.filters or all([f.validate(post) for f in self.filters]):
                        self.cache_manager.add_key(post.id)
                        outflow.send(post)


class Publisher:
    def __init__(self, *args, **kwargs):
        self.database_reader = PostDatabaseReader()  # type: PostDatabaseReader
        self.formatter = []                          # type: List[Formatter]
        self.messenger = Outflow()                   # type: Outflow

    def publish_messages(self):
        for post in self.database_reader.post_items:
            self.messenger.send(post)
