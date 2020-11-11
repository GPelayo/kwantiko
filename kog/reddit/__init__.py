from praw import Reddit

from kog.config import (REDDIT_USER_AGENT,
                        REDDIT_CLIENT_ID,
                        REDDIT_CLIENT_SECRET,
                        REDDIT_USERNAME,
                        REDDIT_PASSWORD)


def create_reddit_object(secrets: dict) -> Reddit:
    return Reddit(user_agent=secrets[REDDIT_USER_AGENT],
                  client_id=secrets[REDDIT_CLIENT_ID],
                  client_secret=secrets[REDDIT_CLIENT_SECRET],
                  username=secrets[REDDIT_USERNAME],
                  password=secrets[REDDIT_PASSWORD])
