import logging
from telegram import Update
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import CallbackContext


class Telegram:

    def __init__(self, token, channel_id, kucoin_obj=None):
        self.__updater = Updater(token=token,
                                 use_context=True)
        self.__dispatcher = self.__updater.dispatcher
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                            level=logging.INFO)
        self.__channel_id = channel_id
        self.__kucoin_obj = kucoin_obj

    @staticmethod
    def authenticator(update: Update) -> bool:
        if update.effective_user.id == 100136658 or update.effective_user.id == 438963856:
            return True
        return False

    def hi(self, update: Update, context: CallbackContext):
        if self.authenticator(update=update):
            update.message.reply_text(text='Hello my friend!')

    def status(self, update: Update, context: CallbackContext):
        if self.authenticator(update=update):
            file = open('Assets/Status.dat', 'r')
            if file.read() == '1':
                update.message.reply_text(text='[+] I\'m on!')
            else:
                update.message.reply_text(text='[-] I\'m off!')

    def balance(self, update: Update, context: CallbackContext):
        if self.authenticator(update=update):
            update.message.reply_text(str(self.__kucoin_obj.get_available_balance()))

    def on(self, update: Update, context: CallbackContext):
        if self.authenticator(update=update):
            file = open('Assets/Power.dat', 'w')
            file.write('1')
            file.close()

    def off(self, update: Update, context: CallbackContext):
        if self.authenticator(update=update):
            file = open('Assets/Power.dat', 'w')
            file.write('0')
            file.close()

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
        hi_handler = CommandHandler('hi', self.hi)
        status_handler = CommandHandler('status', self.status)
        balance_handler = CommandHandler('balance', self.balance)
        on_handler = CommandHandler('on', self.on)
        off_handler = CommandHandler('off', self.off)
        close_handler = CommandHandler('close', self.close)
        self.__dispatcher.add_handler(hi_handler)
        self.__dispatcher.add_handler(status_handler)
        self.__dispatcher.add_handler(balance_handler)
        self.__dispatcher.add_handler(on_handler)
        self.__dispatcher.add_handler(off_handler)
        self.__dispatcher.add_handler(close_handler)
        self.__updater.start_polling()
