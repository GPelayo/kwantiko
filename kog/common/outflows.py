from kog.common.models import Post


class Outflow:
    def send(self, item: Post):
        raise NotImplementedError()
