import discord
from chalicelib.common.models import Post
from chalicelib.common.outflows import Outflow
from chalicelib.secrets import AWSSecretsManager
from chalicelib.config import DISCORD_WEBHOOK_ID_NAME, DISCORD_WEBHOOK_TOKEN_NAME


class Messenger(Outflow):
    def __init__(self, secret_manager: AWSSecretsManager):
        secrets = secret_manager.secrets
        webhook_id = secrets[DISCORD_WEBHOOK_ID_NAME]
        webhook_token = secrets[DISCORD_WEBHOOK_TOKEN_NAME]
        self.webhook = discord.Webhook.partial(webhook_id, webhook_token, adapter=discord.RequestsWebhookAdapter())

    def send(self, post: Post):
        self.webhook.send(post.message)
