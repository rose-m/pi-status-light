import threading
from time import sleep

import requests

from rating_light import RatingLightInfo


class DataCollector:
    def __init__(self, endpoint_url):
        if not endpoint_url:
            raise ValueError('endpoint_url missing')
        self.endpoint_url = endpoint_url
        self._thread = None
        self._data = []

    def start(self):
        if self._thread:
            raise RuntimeError('already started')

        self._thread = threading.Thread(target=self.check)
        self._thread.daemon = True
        self._thread.start()

    def get_data(self):
        return self._data

    def check(self):
        while True:
            result = self._execute_request()
            if result:
                self._data = result
            else:
                print('Check failed...')
            sleep(5)

    def _execute_request(self):
        response = requests.get(self.endpoint_url)
        if not response.status_code == 200:
            return None

        data = response.json()
        if not data.values or not data.values.length:
            return None

        return [RatingLightInfo(name, value) for (name, value) in data.values if name]
