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


def exec_heisen_bot():
    kucoin_obj = KuCoin(API_NAME=Heisen_API_NAME,
                        API_KEY=Heisen_API_KEY,
                        API_SECRETS=Heisen_API_SECRET,
                        API_PASSPHRASE=Heisen_API_PASSPHARSE)
    heisen_obj = Heisen(KCConnection=kucoin_obj,
                        IEX_CLOUD_API_TOKEN=IEX_CLOUD_API_TOKEN,
                        TAAPI_API_TOKEN=TAAPI_API_TOKEN,
                        TAAPI_API_TOKEN_2=TAAPI_API_TOKEN_2,
                        TELEGRAM_BOT_API_TOKEN=TELEGRAM_BOT_API_TOKEN,
                        TELEGRAM_CHANNEL_ID=TELEGRAM_CHANNEL_ID)
    heisen_obj.exec()


def emergency_close():
    telegram_obj = Telegram(token=TELEGRAM_BOT_API_TOKEN,
                            channel_id=TELEGRAM_CHANNEL_ID)
    telegram_obj.start_polling()


exec_heisen_bot()
