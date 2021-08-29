import pandas as pd
import requests


class IEXCloud:

    def __init__(self, token):
        self.__BASE_URL = 'https://cloud.iexapis.com/stable/crypto'
        self.__API_TOKEN = token

    def get_quote(self, symbol):
        url = f'{self.__BASE_URL}/{symbol}/quote?token={self.__API_TOKEN}'
        columns = ['symbol', 'price', 'low', 'high']
        result = requests.get(url)
        if result.status_code != 200:
            raise RuntimeError('IEXCloud: cannot connect to url (err code: %s)!' % result.status_code)

        return result.json()