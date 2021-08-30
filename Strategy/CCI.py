from CoreData.IEXCloud import IEXCloud
from CoreData.TAAPI import TAAPI
from Notification.Telegram import Telegram
import time


class CCI:

    def __init__(self, IEXCloud_obj: IEXCloud, TAAPI_obj: TAAPI, Telegram_obj: Telegram):
        self.__iex = IEXCloud_obj
        self.__taapi = TAAPI_obj
        self.__tel = Telegram_obj

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
        else:
            while cci_value < -100:
                time.sleep(17)
                cci_value = self.__taapi.get_cci(symbol=symbol_ta,
                                                 interval='5m')
            current_price = self.__iex.get_price(symbol_iex)
            goal_price = goal_coefficient * current_price
            stop_price = stop_coefficient * current_price
            msg = f'[+] Order executed!\n' \
                  f'\tCurrent_price = {current_price}$\n' \
                  f'\tTarget_price = {goal_price}$ ({(goal_coefficient - 1) * 100}%)\n' \
                  f'\tStopLoss_price = {stop_price}$ ({(stop_coefficient - 1) * 100}%).'
            if verbose:
                self.__tel.msg_channel(msg)

            print(msg)
            while stop_price < current_price < goal_price:
                status = True
                current_price = self.__iex.get_price(symbol_iex)
                time.sleep(2)
            status = False
            if current_price >= goal_price:
                msg = f'[+] You earn {(goal_coefficient - 1) * 100}% of your account! nice job.'
                if verbose:
                    self.__tel.msg_channel(msg)
                print(msg)
            elif current_price <= stop_price:
                msg = f'[-] You loss {(stop_coefficient - 1) * 100}% of your account! see you soon.'
                if verbose:
                    self.__tel.msg_channel(msg)
                print(msg)
