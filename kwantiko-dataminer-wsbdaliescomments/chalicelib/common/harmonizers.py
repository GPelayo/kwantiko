
class Post:
    post_id = None         # type: str
    date_submitted = None  # type: str
    user = None            # type: str
    message = None         # type: str
    score = None           # type: float


class Harmonizer:
    fieldnames = [x for x in dir(Post) if not x.endswith('__') and not x.startswith('__')]
