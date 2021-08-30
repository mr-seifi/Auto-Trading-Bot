import requests

# What is TAAPI?
"""
    TAAPI.IO is a developer-friendly API that provides investors and traders easy and
        automated access to technical analysis data. With TAAPI.IO, you get easy access to
        most popular (MA, RSI, MACD etc.) and advanced indicators on crypto and other securities.
    TAAPI Main URL: https://taapi.io/
    TAAPI Indicators API Documentation URL: https://taapi.io/indicators/
"""


class TAAPI:

    def __init__(self, token):  # A simple constructor for TAAPI class
        self.__BASE_URL = 'https://api.taapi.io'
        self.__API_TOKEN = token

    def get_cci(self, symbol, interval, period='20', tp='close', exchange='binance'):  # This method return real-time
        # CCI value.
        # Arguments: interval is timeframe, period is length input, tp is source
        url = f'{self.__BASE_URL}/cci?' \
              f'symbol={symbol}&' \
              f'interval={interval}&' \
              f'period={period}&' \
              f'tp={tp}&' \
              f'exchange={exchange}&' \
              f'secret={self.__API_TOKEN}'  # Create an API URL

        result = requests.get(url)  # Send GET request to TAAPI servers
        if result.status_code != 200:  # Send GET request to IEX Cloud servers
            raise RuntimeError('TAAPI: cannot connect to url (err code %s)!' % result.status_code)

        return float(result.json()['value'])  # return the result as a floating point number

