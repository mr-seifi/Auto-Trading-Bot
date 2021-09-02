import time
from CoreData.IEXCloud import IEXCloud
from CoreData.TAAPI import TAAPI
from Notification.Telegram import Telegram
from Strategy.CCI import CCI
from Exchange.KuCoin import KuCoin


class Heisen:
    def __init__(self,
                 KCConnection: KuCoin,
                 Telegram_obj: Telegram,
                 CCI_obj: CCI):
        self.__connection = KCConnection
        self.__Telegram_obj = Telegram_obj
        self.__CCI_obj = CCI_obj

    def exec(self):
        try:
            file = open('Assets/Emergency_Close.dat', 'w')
            file.close()
            self.__Telegram_obj.msg_channel('[+] Start working!')  # Send message as notice the user that I'm start
            while True:
                try:
                    self.__CCI_obj.cci_5m(symbol_iex='BTCUSDT',
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
