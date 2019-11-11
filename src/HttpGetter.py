from dic.user_agent import user_agent_list

import requests
import time
import random


class HttpGetter:
    def __init__(self, url):
        self.url = url
        self._get_response()

    def _get_response(self):
        trial = 0
        status = False
        while (not status) and (trial != 5):
            headers = {'User-Agent': random.choice(user_agent_list)}
            self.response = requests.get(self.url, headers=headers)
            trial += 1
            status = self._check_status(60)

    def _check_status(self, n):
        if self.response.status_code != requests.codes.ok:
            print('<Warning> Got 404 response, will stop requests for {} seconds.'.format(n))
            time.sleep(n)
            return False
        else:
            print('Succesfully get {}'.format(self.url))
            return True
