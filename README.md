# Auto-Trading-Bot

### Motivation
> My motivation for this project is to make a bot that trades for you. 
> Therefore, you don't need to check the chart yourself and spend your time every day.

### How can I start the bot?
> Same as the other trading systems, this bot also needs a good strategy to get a good profit at the end of the month or week.
> I wrote two strategies by myself for the default option but if you are a trader, absolutely your strategy works better than mine.

### How can I write a strategy?
> If you know Python programming language, write your strategy by getting real-time market data from IEXCloud and access indicators by TAAPI service.
> If you know Pine script, write your strategy and connect it with BVA to let this script access alerts that come from TradingView. 

## Requirements
1. [Beautiful soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
2. [Python Telegram bot](https://python-telegram-bot.readthedocs.io/en/stable/)
3. [Requests](https://docs.python-requests.org/en/latest/)
4. [Requests-HTML](https://docs.python-requests.org/projects/requests-html/en/latest/)
5. [Pyppeteer](https://miyakogi.github.io/pyppeteer/)

## Core Data
This package is for getting data from web.
- ### IEXCloud
    > Stocks, forex, crypto, and more. A core set of financial data all in one place, so you can focus on building.
    
    IEX Cloud is a platform that makes financial data and services accessible to everyone. <br/>
    IEXCloud Main URL: https://iexcloud.io/ <br/>
    IEXCloud API Documentation URL: https://iexcloud.io/docs/api
- ### TAAPI
    > TAAPI.IO is a straightforward REST API and price data provider for fetching popular Technical Analysis (TA) Indicator Data.
  
    TAAPI.IO is a developer-friendly API that provides investors and traders easy and
    automated access to technical analysis data. With TAAPI.IO, you get easy access to
    the most popular (MA, RSI, MACD, etc.) and advanced indicators on crypto and other securities. <br/>
    TAAPI Main URL: https://taapi.io/ <br/>
    TAAPI Indicators API Documentation URL: https://taapi.io/indicators/

## Exchange
This package is for place a new limit/market order and open positions which your strategy let that.
- ### KuCoin
    > KuCoin is a global cryptocurrency exchange for numerous digital assets and cryptocurrencies. Launched in September 2017, KuCoin has grown to become one of the most popular crypto exchanges and already has 8 million registered users across 207 countries and regions around the world.
  
    KuCoin URL: https://kucoin.com