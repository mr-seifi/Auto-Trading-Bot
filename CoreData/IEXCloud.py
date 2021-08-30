import pandas as pd
import requests

# What is IEX Cloud?
"""
    IEX Cloud is a platform that makes financial data and services accessible to everyone.
    IEXCloud Main URL: https://iexcloud.io/
    IEXCloud API Documentation URL: https://iexcloud.io/docs/api
"""


class IEXCloud:

    def __init__(self, token):  # A simple constructor from IEXCloud class
        self.__BASE_URL = 'https://cloud.iexapis.com/stable/crypto'
        self.__API_TOKEN = token

    def get_quote(self, symbol):  # This method return quote(info) of your crypto that identified by a symbol
        url = f'{self.__BASE_URL}/{symbol}/quote?token={self.__API_TOKEN}'  # Create API URL
        result = requests.get(url)  # Send GET request to IEX Cloud servers
        if result.status_code != 200:  # If the result of your request is not ok throw exception
            raise RuntimeError('IEXCloud (get_quote): cannot connect to url (err code: %s)!' % result.status_code)

        return result.json()  # return the json parsed result

    # Using this method for get price is more efficiency than get quote method
    def get_price(self, symbol):  # This method return price of your crypto that identified by a symbol
        url = f'{self.__BASE_URL}/{symbol}/price?token={self.__API_TOKEN}'  # Create API URL
        result = requests.get(url)  # Send GET request to IEX Cloud servers
        if result.status_code != 200:  # If the result of your request is not ok throw exception
            raise RuntimeError('IEXCloud (get_price): cannot connect to url (err code: %s)!' % result.status_code)

        return float(result.json()['price'])  # return the result as a floating point number


# Error Codes
"""
    IEX Cloud uses HTTP response codes to indicate the success or failure of an API request.

    General HTML status codes
    
    2xx Success.
    
    4xx Errors based on information provided in the request
    
    5xx Errors on IEX Cloud servers
    
    IEX Cloud HTTP Status Codes
    HTTP CODE	TYPE	DESCRIPTION
    400	Incorrect Values	Invalid values were supplied for the API request
    400	No Symbol	No symbol provided
    400	Type Required	Batch request types parameter requires a valid value
    401	Authorization Restricted	Hashed token authorization is restricted
    401	Authorization Required	Hashed token authorization is required
    401	Restricted	The requested data is marked restricted and the account does not have access.
    401	No Key	An API key is required to access the requested endpoint.
    401	Secret Key Required	The secret key is required to access to requested endpoint.
    401	Denied Referer	The referer in the request header is not allowed due to API token domain restrictions.
    402	Over Limit	You have exceeded your allotted credit quota (and pay-as-you-go is not enabled on legacy plans).
    402	Free Tier Not Allowed	The requested endpoint is not available to free accounts.
    402	Tier Not Allowed	The requested data is not available to your current tier.
    403	Authorization Invalid	Hashed token authorization is invalid.
    403	Disabled Key	The provided API token has been disabled
    403	Invalid Key	The provided API token is not valid.
    403	Test Token in Production	A test token was used for a production endpoint.
    403	Production Token in Sandbox	A production token was used for a sandbox endpoint.
    403	Circuit Breaker	Your pay-as-you-go circuit breaker has been engaged and further requests are not allowed.
    403	Inactive	Your account is currently inactive.
    404	Unknown Symbol	Unknown symbol provided
    404	Not Found	Resource not found
    413	Max Types	Maximum number of types values provided in a batch request.
    429	Too Many Requests	Too many requests hit the API too quickly. An exponential backoff of your requests is recommended.
    451	Enterprise Permission Required	The requested data requires additional permission to access.
    500	System Error	Something went wrong on an IEX Cloud server.
"""
