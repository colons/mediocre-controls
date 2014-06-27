import requests

from django.conf import settings


class GiantBombAPIError(Exception):
    def __init__(self, code, message):
        self.code = code
        self.message = message

    def __str__(self):
        return '{message} (error {code})'.format(
            message=self.message,
            code=self.code,
        )


class GiantBombAPI(object):
    def get(self, method, **kwargs):
        params = {
            'format': 'json',
            'api_key': settings.GIANT_BOMB_API_KEY,
        }

        params.update(kwargs)

        resp = requests.get(
            'http://www.giantbomb.com/api/{0}/'.format(method),
            params=params,
        ).json()

        if resp['status_code'] != 1:
            raise GiantBombAPIError(resp['status_code'], resp['error'])

        return resp
