import time
from Signal.Bva import Bva
from Exchange.KuCoin import KuCoin
from Notification.Telegram import Telegram


class SqueezeMomentum:
    def __init__(self, bva_obj: Bva, kucoin_obj: KuCoin, telegram_obj: Telegram):
        self.__signal = bva_obj
        self.__connection = kucoin_obj
        self.__tel = telegram_obj

    def long_pos(self, verbose: bool):
        try:
            current_price = self.__connection.get_current_mark_price()
            leverage = '4'
            lots = int((1e3 * int(leverage) * self.__connection.get_available_balance() / current_price))
            self.__connection.place_market_order(clientOid='heisen_order', leverage=leverage, size=lots)
            msg = f'[+] Order executed!\n' \
                  f'\tCurrent_price = {current_price}$\nlots = {lots}'
            if verbose:
                self.__tel.msg_channel(msg)
            print(msg)
        except Exception as ex:
            print(ex)
            return self.long_pos(verbose)

    def flat_pos(self, verbose: bool, long: float, short: float):
        try:
            self.__connection.close_market_order(clientOid='heisen_order')
            msg = f'UnrealisedPNL = {100 * (short - long) / long}%'
            if verbose:
                self.__tel.msg_channel(msg)
            print(msg)
        except Exception as ex:
            print(ex)
            return self.flat_pos(verbose, long, short)

    def start(self, verbose=True):
        while True:
            new_num, old_num, open_position = self.__signal.get_trade_count()
            while not open_position:
                time.sleep(10)
                new_num, old_num, open_position = self.__signal.get_trade_count()

            self.long_pos(verbose)
            long, short = self.__signal.in_position()
            self.flat_pos(verbose, long, short)

            time.sleep(10)
