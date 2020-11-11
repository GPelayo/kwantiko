from kog.common.models import Post


class DividerPost(Post):
    id = 'DividerPost'         # type: str
    date_submitted = '999'     # type: str
    user = 'MadamDividerPost'  # type: str
    message = '='*12           # type: str
    sentiment = None           # type: float
