from praw import Reddit

import config


def create_reddit_object(secrets: dict) -> Reddit:
    return Reddit(user_agent=secrets[config.REDDIT_USER_AGENT],
                  client_id=secrets[config.REDDIT_CLIENT_ID],
                  client_secret=secrets[config.REDDIT_CLIENT_SECRET],
                  username=secrets[config.REDDIT_USERNAME],
                  password=secrets[config.REDDIT_PASSWORD])
