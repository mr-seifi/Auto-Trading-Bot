from CoreData.IEXCloud import IEXCloud
from CoreData.TAAPI import TAAPI
import time


class CCI:

    def __init__(self, IEXCloud_obj: IEXCloud, TAAPI_obj: TAAPI):
        self.__iex = IEXCloud_obj
        self.__taapi = TAAPI_obj

    def cci_5m(self, symbol_iex, symbol_ta):
        goal_coefficient = 1.00350
        stop_coefficient = 0.99280
        current_price = None
        goal_price = None
        stop_price = None
        status = False
        cci_value = self.__taapi.get_cci(symbol=symbol_ta,
                                         interval='5m')

        if -100 < cci_value:
            print(f'[-] Not found good entry point (cci = {cci_value})')
        else:
            while cci_value < -100:
                cci_value = self.__taapi.get_cci(symbol=symbol_ta,
                                                 interval='5m')
                time.sleep(15)
            current_price = float(self.__iex.get_quote(symbol_iex)['latestPrice'])
            goal_price = goal_coefficient * current_price
            stop_price = stop_coefficient * current_price
            print(f'[+] Order executed!\n'
                  f'\tCurrent_price = {current_price}$\n'
                  f'\tTarget_price = {goal_price}$ ({(goal_coefficient - 1) * 100}%)\n'
                  f'\tStopLoss_price = {stop_price}$ ({(stop_coefficient - 1) * 100}%).')
            while stop_price < current_price < goal_price:
                status = True
                current_price = float(self.__iex.get_quote(symbol_iex)['latestPrice'])
                goal_price = goal_coefficient * current_price
                stop_price = stop_coefficient * current_price
                time.sleep(15)
            status = False
            if current_price >= goal_price:
                print(f'[+] You earn {(goal_coefficient - 1) * 100}% of your account! nice job.')
            elif current_price <= stop_price:
                print(f'[-] You loss {(stop_coefficient - 1) * 100}% of your account! see you soon.')
