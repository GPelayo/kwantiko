from praw import Reddit

import config


def create_reddit_object() -> Reddit:
    return Reddit(user_agent=config.REDDIT_USER_AGENT,
                  client_id=config.REDDIT_CLIENT_ID,
                  client_secret=config.REDDIT_CLIENT_SECRET,
                  username=config.REDDIT_USERNAME,
                  password=config.REDDIT_PASSWORD)
