import json

import requests
import time
import base64
import hashlib
import hmac


class KuCoin:
    def __init__(self, API_NAME: str, API_KEY: str, API_SECRETS: str, API_PASSPHRASE: str):
        self.__BASE_URL = 'https://api-futures.kucoin.com'
        self.__API_NAME = API_NAME
        self.__API_KEY = API_KEY
        self.__API_SECRETS = API_SECRETS
        self.__API_PASSPHRASE = API_PASSPHRASE

    def authentication(self, request_type: str, endpoint: str, data_json=''):
        now = int(time.time() * 1000)
        str_to_sign = str(now) + request_type.upper() + endpoint + data_json
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
            "KC-API-KEY-VERSION": '2',
            "Content-Type": 'application/json'
        }
        return headers

    def get_accounts_overview(self, currency='USDT'):
        req_type = 'GET'
        endpoint = f'/api/v1/account-overview?currency={currency}'
        url = f'{self.__BASE_URL}{endpoint}'
        headers = self.authentication(request_type=req_type,
                                      endpoint=endpoint)
        response = requests.request(req_type.lower(), url, headers=headers)
        print(response.status_code)
        print(response.json())

    def get_transaction_history(self):
        req_type = 'GET'
        endpoint = '/api/v1/transaction-history?type=RealisedPNL'
        url = f'{self.__BASE_URL}{endpoint}'
        headers = self.authentication(request_type=req_type,
                                      endpoint=endpoint)
        response = requests.request(req_type.lower(), url, headers=headers)
        print(response.status_code)
        print(response.json())

    def place_market_order(self, clientOid, side='buy', symbol='XBTUSDTM', type='market', leverage='100', size=5):
        req_type = 'POST'
        endpoint = '/api/v1/orders'
        url = f'{self.__BASE_URL}{endpoint}'
        data = {'clientOid': clientOid,
                'side': side,
                'symbol': symbol,
                'type': type,
                'leverage': leverage,
                'size': size}
        data_json = json.dumps(data)
        headers = self.authentication(request_type=req_type,
                                      endpoint=endpoint,
                                      data_json=data_json)
        response = requests.request(req_type.lower(), url, headers=headers, data=data_json)
        print(response.status_code)
        print(response.json())

    def close_market_order(self, clientOid: str, symbol='XBTUSDTM'):
        req_type = 'POST'
        endpoint = '/api/v1/orders'
        url = f'{self.__BASE_URL}{endpoint}'
        data = {'clientOid': clientOid,
                'symbol': symbol,
                'type': 'market',                'closeOrder': True}
        data_json = json.dumps(data)
        headers = self.authentication(request_type=req_type,
                                      endpoint=endpoint,
                                      data_json=data_json)
        response = requests.request(req_type.lower(), url, headers=headers, data=data_json)
        print(response.status_code)
        print(response.json())

    def get_orders_list(self):
        req_type = 'GET'
        endpoint = '/api/v1/orders'
        url = f'{self.__BASE_URL}{endpoint}'
        headers = self.authentication(request_type=req_type,
                                      endpoint=endpoint)
        response = requests.request(req_type.lower(), url, headers=headers)
        print(response.status_code)
        print(response.json())

    def get_positions_list(self):
        req_type = 'GET'
        endpoint = f'/api/v1/positions'
        url = f'{self.__BASE_URL}{endpoint}'
        headers = self.authentication(request_type=req_type,
                                      endpoint=endpoint)
        response = requests.request(req_type.lower(), url, headers=headers)
        print(response.status_code)
        print(response.json())


# Error Codes
"""
    Errors When errors occur, the HTTP error code or system error code will be returned. The body will also contain a 
    message parameter indicating the cause. 
    
    Code	Meaning 400	Bad Request -- Invalid request format 401	Unauthorized -- Invalid API Key 403	Forbidden -- 
    The request is forbidden 404	Not Found -- The specified resource could not be found 405	Method Not Allowed -- 
    You tried to access the resource with an invalid method. 415	Content-Type -- application/json 429	Too Many 
    Requests -- Access limit breached 500	Internal Server Error -- We had a problem with our server. Please try 
    again later. 503	Service Unavailable -- We're temporarily offline for maintenance. Please try again later. 
    System Error Code Code	Meaning 400001	Any of KC-API-KEY, KC-API-SIGN, KC-API-TIMESTAMP, KC-API-PASSPHRASE is 
    missing in your request header. 400002	KC-API-TIMESTAMP Invalid -- Time differs from server time by more than 5 
    seconds 400003	KC-API-KEY not exists 400004	KC-API-PASSPHRASE error 400005	Signature error -- Please check 
    your signature 400006	The IP address is not in the API whitelist 400007	Access Denied -- Your API key does not 
    have sufficient permissions to access the URI 404000	URL Not Found -- The requested resource could not be found 
    400100	Parameter Error -- You tried to access the resource with invalid parameters 411100	User is frozen -- 
    Please contact us via support center 500000	Internal Server Error -- We had a problem with our server. Try again 
    later. If the returned HTTP status code is not 200, the error code will be included in the returned results. If 
    the interface call is successful, the system will return the code and data fields. If not, the system will return 
    the code and msg fields. You can check the error code for details. 
    
    Success A successful response is indicated by an HTTP status code 200 and system code 200000. The success 
    response is as follows 
"""
