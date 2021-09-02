import logging
from telegram import Update
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import CallbackContext


class Telegram:

    def __init__(self, token, channel_id):
        self.__updater = Updater(token=token,
                                 use_context=True)
        self.__dispatcher = self.__updater.dispatcher
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                            level=logging.INFO)
        self.__channel_id = channel_id

    @staticmethod
    def authenticator(update: Update) -> bool:
        if update.effective_user.id == 100136658:
            return True
        return False

    def close(self, update: Update, context: CallbackContext):
        if self.authenticator(update=update):
            update.message.reply_text(text='[+] Your request is being process!')
            file = open('Assets/Emergency_Close.dat', 'w')
            file.write('-1')
            file.close()

    def msg_channel(self, msg):
        self.__updater.bot.send_message(text=msg,
                                        chat_id=self.__channel_id)

    def start_polling(self):
        close_handler = CommandHandler('close', self.close)
        self.__dispatcher.add_handler(close_handler)
        self.__updater.start_polling()
