import requests
import time
import base64
import hashlib
import hmac


class KuCoin:
    def __init__(self, API_NAME: str, API_KEY: str, API_SECRETS: str, API_PASSPHRASE: str):
        self.__BASE_URL = 'https://api.kucoin.com/'
        self.__API_NAME = API_NAME
        self.__API_KEY = API_KEY
        self.__API_SECRETS = API_SECRETS
        self.__API_PASSPHRASE = API_PASSPHRASE

    def authentication(self):
        now = int(time.time() * 1000)
        str_to_sign = str(now) + 'GET' + '/api/v1/accounts'
        signature = base64.b64encode(
            hmac.new(self.__API_SECRETS.encode('utf-8'), str_to_sign.encode('utf-8'), hashlib.sha256).digest())
        passphrase = base64.b64encode(
            hmac.new(self.__API_SECRETS.encode('utf-8'), self.__API_PASSPHRASE.encode('utf-8'),
                     hashlib.sha256).digest())
        headers = {
            "KC-API-SIGN": signature,
            "KC-API-TIMESTAMP": str(now),
            "KC-API-KEY": self.__API_KEY,
            "KC-API-PASSPHRASE": passphrase,
            "KC-API-KEY-VERSION": 2
        }
        return headers

    def get_accounts(self):
        url = 'https://openapi-sandbox.kucoin.com/api/v1/accounts'
        headers = self.authentication()
        response = requests.request('get', url, headers=headers)
        print(response.status_code)
        print(response.json())