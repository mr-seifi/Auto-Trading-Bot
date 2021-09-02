import time
from CoreData.TAAPI import TAAPI
from CoreData.IEXCloud import IEXCloud
from Strategy.CCI import CCI
from Notification.Telegram import Telegram
from secrets import TAAPI_API_TOKEN
from secrets import TAAPI_API_TOKEN_2
from secrets import IEX_CLOUD_API_TOKEN
from secrets import TELEGRAM_CHANNEL_ID
from secrets import TELEGRAM_BOT_API_TOKEN
from Exchange.KuCoin import KuCoin
from Release.Heisen import Heisen
from secrets import Heisen_API_NAME
from secrets import Heisen_API_KEY
from secrets import Heisen_API_SECRET
from secrets import Heisen_API_PASSPHARSE


def exec_bot():
    kucoin_obj = KuCoin(API_NAME=Heisen_API_NAME,
                        API_KEY=Heisen_API_KEY,
                        API_SECRETS=Heisen_API_SECRET,
                        API_PASSPHRASE=Heisen_API_PASSPHARSE)
    heisen_obj = Heisen(KCConnection=kucoin_obj)
    heisen_obj.exec()


def exec_strategy():
    try:
        iex_obj = IEXCloud(IEX_CLOUD_API_TOKEN)  # Create IEXCloud object that gives the bot last crypto price
        taapi_obj = TAAPI(TAAPI_API_TOKEN)  # Create TAAPI object that gives the bot indicators values
        taapi_obj2 = TAAPI(TAAPI_API_TOKEN_2)
        telegram_obj = Telegram(token=TELEGRAM_BOT_API_TOKEN,
                                channel_id=TELEGRAM_CHANNEL_ID)  # Create Telegram object that gives the bot the ability
        # of sending logs to telegram channel
        cci_obj = CCI(IEXCloud_obj=iex_obj,
                      TAAPI_obj=taapi_obj,
                      TAAPI_obj2=taapi_obj2,
                      Telegram_obj=telegram_obj)  # Create CCI object that gives the bot the ability of technical
        # analysis and get along with cci indicator
        telegram_obj.msg_channel('[+] Start working!')  # Send message as notice the user that I'm start
        while True:
            try:
                cci_obj.cci_5m(symbol_iex='BTCUSDT',
                               symbol_ta='BTC/USDT',
                               verbose=True)  # Call 5m cci method that signal user when put an order or when not (5
                # min)
                time.sleep(17)  # Sleep for 17 second for 2 reason
                # First. We use free version of TAAPI and for each api request we should wait for 15 sec
                # Second. For Prevent more than 50% of the cci value noises and wait for gain more confident
            except Exception as ex:
                print('main: %s' % ex)

    except Exception as ex:
        print('main: %s' % ex)


def emergency_close():
    telegram_obj = Telegram(token=TELEGRAM_BOT_API_TOKEN,
                            channel_id=TELEGRAM_CHANNEL_ID)
    telegram_obj.start_polling()


exec_bot()
