import time
from HeisenV1.Signal.Bva import Bva
from HeisenV1.Exchange.KuCoin import KuCoin
from HeisenV1.Notification.Telegram import Telegram


class SqueezeMomentum:
    def __init__(self, bva_obj: Bva, kucoin_obj: KuCoin, telegram_obj: Telegram):
        self.__signal = bva_obj
        self.__connection = kucoin_obj
        self.__tel = telegram_obj

    def start(self, verbose=True):
        while True:
            new_num, open_position = self.__signal.get_trade_count()
            while not open_position:
                new_num, open_position = self.__signal.get_trade_count()
                time.sleep(200)

            current_price = self.__connection.get_current_mark_price()
            entry_price = current_price
            lots = int((1e5 * self.__size / current_price))
            self.__connection.place_market_order(clientOid='heisen_order', size=lots)
            msg = f'[+] Order executed!\n' \
                  f'\tCurrent_price = {current_price}$'
            if verbose:
                self.__tel.msg_channel(msg)
            print(msg)

            long, short = self.__signal.in_position()

            self.__connection.close_market_order(clientOid='heisen_order')
            status = False
            msg = f'UnrealisedPNL = {100 * (short - long) / long}%'
            if verbose:
                self.__tel.msg_channel(msg)
            print(msg)

            time.sleep(200)
