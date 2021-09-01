import requests
import time
import base64
import hashlib
import hmac


class KuCoin:
    def __init__(self, API_NAME: str, API_KEY: str, API_SECRETS: str, API_PASSPHRASE: str):
        self.__BASE_URL = 'https://api.kucoin.com'
        self.__API_NAME = API_NAME
        self.__API_KEY = API_KEY
        self.__API_SECRETS = API_SECRETS
        self.__API_PASSPHRASE = API_PASSPHRASE

    def authentication(self, request_type: str, endpoint: str):
        now = int(time.time() * 1000)
        str_to_sign = str(now) + request_type.upper() + endpoint
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
            "KC-API-KEY-VERSION": '2'
        }
        return headers

    def get_sub_user(self):
        req_type = 'GET'
        endpoint = '/api/v1/sub/user'
        url = f'{self.__BASE_URL}{endpoint}'
        headers = self.authentication(req_type, endpoint)
        response = requests.request(req_type.lower(), url, headers=headers)
        print(response.status_code)
        print(response.json())

    def get_accounts(self):
        req_type = 'GET'
        endpoint = '/api/v1/accounts'
        url = f'{self.__BASE_URL}{endpoint}'
        headers = self.authentication(req_type, endpoint)
        response = requests.request(req_type.lower(), url, headers=headers)
        print(response.status_code)
        print(response.json())


"""
    Request
    All requests and responses are application/json content type.
    
    Unless otherwise stated, all timestamp parameters should in milliseconds. e.g. 1544657947759
    
    Parameters For the GET, DELETE request, all query parameters need to be included in the request url. (e.g. 
    /api/v1/accounts?currency=BTC) 
    
    For the POST, PUT request, all query parameters need to be included in the request body with JSON. (e.g. {
    "currency":"BTC"}). Do not include extra spaces in JSON strings. 
    
    Errors When errors occur, the HTTP error code or system error code will be returned. The body will also contain a 
    message parameter indicating the cause. 
    
    HTTP error status codes
    {
      "code": "400100",
      "msg": "Invalid Parameter."
    }
    
    Code	Meaning 400	Bad Request -- Invalid request format. 401	Unauthorized -- Invalid API Key. 403	Forbidden 
    or Too Many Requests -- The request is forbidden or Access limit breached. 404	Not Found -- The specified 
    resource could not be found. 405	Method Not Allowed -- You tried to access the resource with an invalid method. 
    415	Unsupported Media Type. You need to use: application/json. 500	Internal Server Error -- We had a problem with 
    our server. Try again later. 503	Service Unavailable -- We're temporarily offline for maintenance. Please try 
    again later. System error codes Code	Meaning 200001	Order creation for this pair suspended 200002	Order 
    cancel for this pair suspended 200003	Number of orders breached the limit 200009	Please complete the KYC 
    verification before you trade XX 200004	Balance insufficient 400001	Any of KC-API-KEY, KC-API-SIGN, 
    KC-API-TIMESTAMP, KC-API-PASSPHRASE is missing in your request header 400002	KC-API-TIMESTAMP Invalid 400003	
    KC-API-KEY not exists 400004	KC-API-PASSPHRASE error 400005	Signature error 400006	The requested ip address 
    is not in the api whitelist 400007	Access Denied 404000	Url Not Found 400100	Parameter Error 400200	
    Forbidden to place an order 400500	Your located country/region is currently not supported for the trading of this 
    token 400700	Transaction restricted, there's a risk problem in your account 400800	Leverage order failed 
    411100	User are frozen 500000	Internal Server Error 900001	symbol not exists If the returned HTTP status code 
    is 200, whereas the operation failed, an error will occur. You can check the above error code for details. 
    
    Success A successful response is indicated by an HTTP status code 200 and system code 200000. The success 
    response is as follows: """
