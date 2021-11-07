import os
import re
import time
from bs4 import BeautifulSoup
from requests_html import HTMLSession


class Bva:
    def __init__(self, strategy_number: int):
        self.__NUMBER = strategy_number
        self.__BASE_URL = 'https://bitcoinvsalts.com/strat/%i' % self.__NUMBER
        if not os.path.isfile('../Assets/%i' % self.__NUMBER):
            f = open(f'{self.__NUMBER}.dat', 'w')
            f.write('0')
            f.close()

    def get_file(self, mode: str):
        return open(f'{self.__NUMBER}.dat', mode)

    def render(self):
        session = HTMLSession()
        r = session.get(self.__BASE_URL)
        r.html.render(sleep=2, timeout=20)
        return r.html

    def get_trade_count(self):
        r = self.render()
        clean_page = BeautifulSoup(r.text, 'html.parser')
        new_num = int(re.findall(r'Trades Count\n(\d+)', clean_page.text)[0])

        f = self.get_file('r')
        old_num = int(f.read(5))
        f.close()

        f = self.get_file('w')
        f.write(str(new_num))
        f.close()

        if new_num > old_num:
            return new_num, True
        return new_num, False

    def in_position(self):
        r = self.render()
        clean_page = BeautifulSoup(r.text, 'html.parser')
        last = re.findall(r'LONG\n((.+)\n(.+))', clean_page.text)[0]

        while last[1] == '---':
            r = self.render()
            clean_page = BeautifulSoup(r.text, 'html.parser')
            last = re.findall(r'LONG\n((.+)\n(.+))', clean_page.text)[0]
            time.sleep(200)
