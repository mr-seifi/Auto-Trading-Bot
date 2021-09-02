import time
from CoreData.IEXCloud import IEXCloud
from CoreData.TAAPI import TAAPI
from Notification.Telegram import Telegram
from Strategy.CCI import CCI
from Exchange.KuCoin import KuCoin


class Heisen:
    def __init__(self, KCConnection: KuCoin,
                 IEX_CLOUD_API_TOKEN: str,
                 TAAPI_API_TOKEN: str,
                 TAAPI_API_TOKEN_2: str,
                 TELEGRAM_BOT_API_TOKEN: str,
                 TELEGRAM_CHANNEL_ID: str):
        self.__connection = KCConnection
        self.__IEX_CLOUD_API_TOKEN = IEX_CLOUD_API_TOKEN
        self.__TAAPI_API_TOKEN = TAAPI_API_TOKEN
        self.__TAAPI_API_TOKEN_2 = TAAPI_API_TOKEN_2
        self.__TELEGRAM_BOT_API_TOKEN = TELEGRAM_BOT_API_TOKEN
        self.__TELEGRAM_CHANNEL_ID = TELEGRAM_CHANNEL_ID

    def exec(self):
        try:
            iex_obj = IEXCloud(self.__IEX_CLOUD_API_TOKEN)  # Create IEXCloud object that gives the bot last crypto price
            taapi_obj = TAAPI(self.__TAAPI_API_TOKEN)  # Create TAAPI object that gives the bot indicators values
            taapi_obj2 = TAAPI(self.__TAAPI_API_TOKEN_2)
            telegram_obj = Telegram(token=self.__TELEGRAM_BOT_API_TOKEN,
                                    channel_id=self.__TELEGRAM_CHANNEL_ID)  # Create Telegram object that gives the bot the ability
            # of sending logs to telegram channel
            cci_obj = CCI(IEXCloud_obj=iex_obj,
                          TAAPI_obj=taapi_obj,
                          TAAPI_obj2=taapi_obj2,
                          Telegram_obj=telegram_obj,
                          KuCoin_connection=self.__connection)  # Create CCI object that gives the bot the ability of technical
            # analysis and get along with cci indicator
            telegram_obj.msg_channel('[+] Start working!')  # Send message as notice the user that I'm start
            while True:
                try:
                    cci_obj.cci_5m(symbol_iex='BTCUSDT',
                                   symbol_ta='BTC/USDT',
                                   verbose=True)  # Call 5m cci method that signal user when put an order or when not (5
                    # min)
                    time.sleep(17)  # Sleep for 17 second for 2 reason
                    # First. We use free version of TAAPI and for each api request we should wait for 15 sec
                    # Second. For Prevent more than 50% of the cci value noises and wait for gain more confident
                except Exception as ex:
                    print('main: %s' % ex)

        except Exception as ex:
            print('main: %s' % ex)
