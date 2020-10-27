from chalicelib.common.models import Post


class Formatter:
    @staticmethod
    def format_post(post: Post):
        raise NotImplementedError()
