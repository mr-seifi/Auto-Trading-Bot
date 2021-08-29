import logging
from telegram.ext import Updater


class Telegram:

    def __init__(self, token, channel_id):
        self.__updater = Updater(token=token,
                                 use_context=True)
        self.__dispatcher = self.__updater.dispatcher
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                            level=logging.INFO)
        self.__channel_id = channel_id

    def msg_channel(self, msg):
        self.__updater.bot.send_message(text=msg,
                                        chat_id=self.__channel_id)
