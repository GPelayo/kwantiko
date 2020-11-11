from kog.common.models import Post


class DividerPost(Post):
    id = '??????'           # type: str
    date_submitted = '999'  # type: str
    user = None             # type: str
    message = ''*12         # type: str
    sentiment = None        # type: float
