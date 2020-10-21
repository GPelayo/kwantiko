import logging

import boto3
from chalice import Chalice, Rate

from chalicelib.data_miners import RedditLinkMiner, RedditLinkPublisher
from chalicelib.constants import (build_reddit_thread_queue_arn,
                                  build_reddit_threads_monitored_table_name,
                                  build_reddit_thread_queue_name,
                                  THREAD_ID_FIELDNAME)

app = Chalice(app_name='kwantiko-dataminer-wsbdaliescomments')
app.log.setLevel(logging.DEBUG)


@app.on_sqs_message(queue=build_reddit_thread_queue_name(), batch_size=1)
def wsb_link_miner_publisher(event):
    for message in event:
        app.log.debug(message.body)
        data_miner = RedditLinkMiner(message.body)
        data_miner.process()
        publisher = RedditLinkPublisher(message.body)
        publisher.publish_messages()


@app.schedule(Rate(5, Rate.MINUTES))
def wsb_foreman(event):
    database = boto3.resource('dynamodb')
    table = database.Table(build_reddit_threads_monitored_table_name())
    response = table.scan()
    sqs = boto3.resource('sqs')
    queue = sqs.Queue(build_reddit_thread_queue_arn())
    for item in response['Items']:
        queue.send_message(MessageBody=item[THREAD_ID_FIELDNAME])
