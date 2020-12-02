import os
import sys

DISCORD_WEBHOOK_ID = ""
DISCORD_WEBHOOK_ID_NAME = ""
DISCORD_WEBHOOK_TOKEN = ""
DISCORD_WEBHOOK_TOKEN_NAME = ""
REDDIT_CLIENT_ID = ""
REDDIT_CLIENT_SECRET = ""
REDDIT_PASSWORD = ""
REDDIT_USER_AGENT = ""
REDDIT_USERNAME = ""

try:
    import local_config
except ImportError:
    for key, value in os.environ.items():
        setattr(sys.modules[__name__], key, value)
else:
    for attribute in dir(local_config):
        if attribute[:2] != '__' and attribute[-2:] != '__':
            setattr(sys.modules[__name__], attribute, getattr(local_config, attribute))

