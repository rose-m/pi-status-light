import threading
from time import sleep

import requests

from rating_light import RatingLightInfo


class DataCollector:
    def __init__(self, endpoint_url,
                 authenticator=None):
        if not endpoint_url:
            raise ValueError('endpoint_url missing')
        self.endpoint_url = endpoint_url
        self.authenticator = authenticator
        self._thread = None
        self._data = []

    def start(self):
        if self._thread:
            raise RuntimeError('already started')

        self._thread = threading.Thread(target=self.check)
        self._thread.daemon = True
        self._thread.start()

    def get_data(self):
        """

        :return:
        :type: list of RatingLightInfo
        """
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
        response = requests.get(self.endpoint_url, auth=self.authenticator)
        if not response.status_code == 200:
            return None

        data = response.json()
        if not data['values'] or not len(data['values']):
            return None

        result = []
        for v in data['values']:
            name = v['name']
            if name:
                value = v['value'] if 'value' in v else None
                result.append(RatingLightInfo(name, value))

        return result
