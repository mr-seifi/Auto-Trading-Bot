import requests


class TAAPI:

    def __init__(self, token):
        self.__BASE_URL = 'https://api.taapi.io'
        self.__API_TOKEN = token

    def get_cci(self, symbol, interval, period='20', tp='close', exchange='binance'):
        url = f'{self.__BASE_URL}/cci?' \
              f'symbol={symbol}&' \
              f'interval={interval}&' \
              f'period={period}&' \
              f'tp={tp}&' \
              f'exchange={exchange}&' \
              f'secret={self.__API_TOKEN}'

        result = requests.get(url)

        if result.status_code != 200:
            raise RuntimeError('TAAPI: cannot connect to url (err code %s)!' % result.status_code)

        return float(result.json()['value'])
