import discord
from kog.common.models import Post
from kog.common import Outflow
import config


class Messenger(Outflow):
    def __init__(self):
        webhook_id = config.DISCORD_WEBHOOK_ID
        webhook_token = config.DISCORD_WEBHOOK_TOKEN
        self.webhook = discord.Webhook.partial(webhook_id, webhook_token, adapter=discord.RequestsWebhookAdapter())

    def send(self, post: Post):
        self.webhook.send(f'________\n{post.message}')
