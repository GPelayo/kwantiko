from chalicelib.common.models import Post


class Filter:
    @staticmethod
    def validate(post: Post) -> bool:
        raise NotImplementedError


class LinkFilter:
    @staticmethod
    def validate(post: Post) -> bool:
        return 'http' in post.message
