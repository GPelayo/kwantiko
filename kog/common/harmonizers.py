from kog.common.models import Post


class Harmonizer:
    def serialize(self, post: any) -> Post:
        raise NotImplementedError
