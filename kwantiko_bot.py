from datetime import datetime
import time

from kog.data_miners import WSBLinkMiner

import config


class Task:
    def __init__(self):
        self.cache = dict()  # type: dict

    def run(self):
        raise NotImplementedError


class WSBDailiesTask(Task):
    def __init__(self):
        super().__init__()
        self.cache['last_num_comments'] = 0
        self.cache['post_id'] = None

    def run(self):
        miner = WSBLinkMiner()
        num_new_comments = miner.extractor.submission.num_comments - self.cache['last_num_comments']
        miner.extractor.retrieval_limit = num_new_comments
        if self.cache['post_id'] != miner.extractor.post_id:
            print(f'The first sticky submission was changed. Clearing cache for {self.cache["post_id"]} '
                  f'and extracting from {miner.extractor.post_id}')
            miner.cache_manager.clear_cache()
        self.cache['post_id'] = miner.extractor.post_id
        self.cache['last_num_comments'] = miner.extractor.submission.num_comments
        miner.process()
        print(f'Checked {min(num_new_comments, miner.extractor.retrieval_limit)} '
              f'comments and sent dump at {datetime.now()} ')


tasks = [WSBDailiesTask()]

if __name__ == '__main__':
    while True:
        for task in tasks:
            task.run()
        time.sleep(int(config.DELAY_IN_SECONDS))
