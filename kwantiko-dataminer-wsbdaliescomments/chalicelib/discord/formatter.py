from chalicelib.common import Formatter


class DiscordFormatter(Formatter):
    @staticmethod
    def format_post(post):
        post['message'] = post['message'][:1000]
        return post
