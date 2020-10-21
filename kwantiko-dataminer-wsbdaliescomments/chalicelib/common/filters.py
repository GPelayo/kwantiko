class Filter:
    @staticmethod
    def validate(post) -> bool:
        raise NotImplementedError


class LinkFilter:
    @staticmethod
    def validate(post) -> bool:
        return 'http' in post['message']
