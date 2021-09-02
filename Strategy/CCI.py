import time
from CoreData.IEXCloud import IEXCloud
from CoreData.TAAPI import TAAPI
from Notification.Telegram import Telegram
from Exchange.KuCoin import KuCoin


class CCI:

    def __init__(self, IEXCloud_obj: IEXCloud, TAAPI_obj: TAAPI, TAAPI_obj2: TAAPI, Telegram_obj: Telegram, KuCoin_connection: KuCoin, size: float):
        self.__iex = IEXCloud_obj
        self.__taapi = TAAPI_obj
        self.__taapi2 = TAAPI_obj2
        self.__tel = Telegram_obj
        self.__connection = KuCoin_connection
        self.__size = size

    def cci_5m(self, symbol_iex, symbol_ta, verbose=True):
        goal_coefficient = 1.00000 + 0.00310
        stop_coefficient = 1.00000 - 0.00620
        current_price = None
        goal_price = None
        stop_price = None
        status = False
        cci_value = self.__taapi.get_cci(symbol=symbol_ta,
                                         interval='5m')

        if -100 < cci_value:
            msg = f'[-] Not found good entry point (cci = {cci_value})'
            print(msg)

            return -1

        while cci_value < -100:
            time.sleep(17)
            cci_value = self.__taapi.get_cci(symbol=symbol_ta,
                                             interval='5m')
            msg = f'[+] Waiting for a good point! (cci = {cci_value})'
            print(msg)

        # cci_1h_value = self.__taapi2.get_cci(symbol=symbol_ta,
        #                                      interval='1h')
        # if cci_1h_value > -50:
        #     msg = f'[-] Not found good entry point (cci 1h = {cci_1h_value})'
        #     print(msg)
        #
        #     return -1

        current_price = self.__connection.get_current_mark_price()
        entry_price = current_price
        lots = int((1e5 * self.__size / current_price) - 10)
        goal_price = goal_coefficient * current_price
        stop_price = stop_coefficient * current_price
        self.__connection.place_market_order(clientOid='heisen_order', size=lots)
        msg = f'[+] Order executed!\n' \
              f'\tCurrent_price = {current_price}$\n' \
              f'\tTarget_price = {goal_price}$ ({(goal_coefficient - 1) * 100}%)\n' \
              f'\tStopLoss_price = {stop_price}$ ({(stop_coefficient - 1) * 100}%).'
        if verbose:
            self.__tel.msg_channel(msg)

        print(msg)
        while stop_price < current_price < goal_price:
            status = True
            current_price = self.__connection.get_current_mark_price()
            print(f'[+] In position, {100 * (current_price - entry_price) / (goal_price - entry_price)}%'
                  f' to achieve your goal!')
            file = open('Assets/Emergency_Close.dat', 'r')
            if file.read() == '-1':
                self.__connection.close_market_order(clientOid='heisen_order')
                file.close()
                file = open('Assets/Emergency_Close.dat', 'w')
                file.close()
                break
            file.close()
            time.sleep(2)
        self.__connection.close_market_order(clientOid='heisen_order')
        status = False
        msg = f'UnrealisedPNL = {100 * (current_price - entry_price) / (goal_price - entry_price)}%'
        if verbose:
            self.__tel.msg_channel(msg)
        print(msg)

        # --------------------------------- Notifier -----------------------------------------
        # if current_price >= goal_price:
        #     self.__connection.close_market_order(clientOid='heisen_order')
        #     msg = f'[+] You earn {(goal_coefficient - 1) * 100}% of your account! nice job.'
        #     if verbose:
        #         self.__tel.msg_channel(msg)
        #     print(msg)
        # elif current_price <= stop_price:
        #     self.__connection.close_market_order(clientOid='heisen_order')
        #     msg = f'[-] You loss {(stop_coefficient - 1) * 100}% of your account! see you soon.'
        #     if verbose:
        #         self.__tel.msg_channel(msg)
        #     print(msg)
        # else:

