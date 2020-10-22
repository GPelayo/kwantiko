from chalicelib.config import AWS_REGION, USER_ID

GROUP_NAME = 'portfolio'
PROJECT_NAME = 'kwantiko'

THREAD_ID_FIELDNAME = 'thread_id'
DATE_RECORDED_FIELDNAME = 'date_recorded'


def build_reddit_threads_monitored_table_name() -> str:
    return f'{GROUP_NAME}-{PROJECT_NAME}-threadsmonitored-reddit'


def build_reddit_thread_queue_name() -> str:
    return f'{GROUP_NAME}-{PROJECT_NAME}-threads-reddit'


def build_reddit_thread_queue_arn() -> str:
    return f'https://sqs.{AWS_REGION}.amazonaws.com/{USER_ID}/{build_reddit_thread_queue_name()}'


POST_ID_FIELDNAME = 'post_id'


def build_reddit_posts_table_name(submission_id: str) -> str:
    return f'{GROUP_NAME}-{PROJECT_NAME}-posts-reddit-{submission_id}'


def build_reddit_posts_viewed_table_name(submission_id: str) -> str:
    return f'{GROUP_NAME}-{PROJECT_NAME}-postsviewed-reddit-{submission_id}'
