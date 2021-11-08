import os
import re
import time
from bs4 import BeautifulSoup
from requests_html import HTMLSession


class Bva:
    def __init__(self, strategy_number: int):
        self.__NUMBER = strategy_number
        self.__BASE_URL = 'https://bitcoinvsalts.com/strat/%i' % self.__NUMBER
        if not os.path.isfile('Assets/%i.dat' % self.__NUMBER):
            f = open(f'Assets/{self.__NUMBER}.dat', 'w')
            f.write('0')
            f.close()

    def get_file(self, mode: str):
        return open(f'Assets/{self.__NUMBER}.dat', mode)

    def render(self):
        print("[+] Try to connect BVA!")
        try:
            session = HTMLSession()
            r = session.get(self.__BASE_URL)
            r.html.render(sleep=2, timeout=20)
            print("[+] Success!")
        except Exception as ex:
            print(ex)
            return self.render()
        return r.html

    def get_trade_count(self):
        try:
            r = self.render()
            clean_page = BeautifulSoup(r.text, 'html.parser')
            new_num = int(re.findall(r'Trades Count\n(\d+)', clean_page.text)[0])

            f = self.get_file('r')
            old_num = int(f.read(5))
            f.close()

            f = self.get_file('w')
            f.write(str(new_num))
            f.close()
        except Exception as ex:
            print(ex)
            return self.get_trade_count()

        if new_num > old_num > 0:
            return new_num, old_num, True
        return new_num, old_num, False

    def in_position(self):
        try:
            print("[+] In Position")
            r = self.render()
            clean_page = BeautifulSoup(r.text, 'html.parser')
            last = re.findall(r'LONG\n((.+)\n(.+))', clean_page.text)[0]

            while last[2] == '---':
                r = self.render()
                clean_page = BeautifulSoup(r.text, 'html.parser')
                last = re.findall(r'LONG\n((.+)\n(.+))', clean_page.text)[0]
                time.sleep(10)

            return float(last[1]), float(last[2])
        except Exception as ex:
            print(ex)
            return self.in_position()
