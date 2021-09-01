from Exchange.KuCoin import KuCoin


class Heisen:
    def __init__(self, KCConnection: KuCoin):
        self.__connection = KCConnection

    def exec(self):
        self.__connection.get_accounts_overview()
        self.__connection.place_market_order(clientOid='123_ABC')
        self.__connection.get_orders_list()
