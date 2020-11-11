import discord
from kog.common.models import Post
from kog.common import Outflow
from kog.secrets import SecretsManager
import config


class Messenger(Outflow):
    def __init__(self, secret_manager: SecretsManager):
        secrets = secret_manager.secrets
        webhook_id = secrets[config.DISCORD_WEBHOOK_ID_NAME]
        webhook_token = secrets[config.DISCORD_WEBHOOK_TOKEN_NAME]
        self.webhook = discord.Webhook.partial(webhook_id, webhook_token, adapter=discord.RequestsWebhookAdapter())

    def send(self, post: Post):
        self.webhook.send(f'________\n{post.message}')
