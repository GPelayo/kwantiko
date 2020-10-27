from typing import List

from chalicelib.common.database_reader import PostDatabaseReader
from chalicelib.common.extractors import Extractor
from chalicelib.common.formatter import Formatter
from chalicelib.common.filters import Filter
from chalicelib.common.formatter import Formatter
from chalicelib.common.outflows import Outflow


class PostMiner:
    def __init__(self, *args, **kwargs):
        self.extractor = []   # type: List[Extractor]
        self.outflows = []    # type: List[Outflow]
        self.filters = []     # type: List[Filter]
        self.formatter = []   # type: List[Formatter]

    def process(self):
        for post in self.extractor.posts:
            for m in self.formatter:
                post = m.format_post(post)
            for outflow in self.outflows:
                if not self.filters or all([f.validate(post) for f in self.filters]):
                    outflow.send(post)


class Publisher:
    def __init__(self, *args, **kwargs):
        self.database_reader = PostDatabaseReader()  # type: PostDatabaseReader
        self.formatter = []                          # type: List[Formatter]
        self.messenger = Outflow()                   # type: Outflow

    def publish_messages(self):
        for post in self.database_reader.post_items:
            self.messenger.send(post)
