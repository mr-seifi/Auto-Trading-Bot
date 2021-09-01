from Exchange.KuCoin import KuCoin


class Heisen:
    def __init__(self, KCConnection: KuCoin):
        self.__connection = KCConnection

    def exec(self):
        self.__connection.get_sub_user()
