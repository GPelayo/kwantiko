from datetime import datetime

import boto3

from chalicelib.reddit.lists import SubredditStickies
from chalicelib.secrets import AWSSecretsManager
from chalicelib.constants import build_reddit_threads_monitored_table_name, THREAD_ID_FIELDNAME, DATE_RECORDED_FIELDNAME
from chalicelib.config import REDDIT_SECRET_NAME


class StickyMonitor:
    def __init__(self, subreddit_name: str,  filter_substring: str = ''):
        self.subreddit_name = subreddit_name
        self.stickies = SubredditStickies(subreddit_name,
                                          AWSSecretsManager(REDDIT_SECRET_NAME),
                                          filter_substring)
        database = boto3.resource('dynamodb')
        self.table = database.Table(build_reddit_threads_monitored_table_name())

    def organize(self):
        date_string = datetime.today().strftime('%Y%m%d')
        response = self.table.scan()
        for item in response['Items']:
            if item[DATE_RECORDED_FIELDNAME] != date_string:
                self.table.delete_item(Key={THREAD_ID_FIELDNAME: item[THREAD_ID_FIELDNAME]})
        for sticky in self.stickies.sticky_ids:
            if 'Items' not in self.table.get_item(Key={THREAD_ID_FIELDNAME: sticky.id}).keys():
                self.table.put_item(Item={THREAD_ID_FIELDNAME: sticky.id, DATE_RECORDED_FIELDNAME: date_string})
