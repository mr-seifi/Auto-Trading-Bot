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

# --------------------------------------------- Create Objects ---------------------------------------------
iex_obj = IEXCloud(IEX_CLOUD_API_TOKEN)  # Create IEXCloud object that gives the bot last crypto price
taapi_obj = TAAPI(TAAPI_API_TOKEN)  # Create TAAPI object that gives the bot indicators values
taapi_obj2 = TAAPI(TAAPI_API_TOKEN_2)
telegram_obj = Telegram(token=TELEGRAM_BOT_API_TOKEN,
                        channel_id=TELEGRAM_CHANNEL_ID)  # Create Telegram object that gives the bot the ability
kucoin_obj = KuCoin(API_NAME=Heisen_API_NAME,
                    API_KEY=Heisen_API_KEY,
                    API_SECRETS=Heisen_API_SECRET,
                    API_PASSPHRASE=Heisen_API_PASSPHARSE)
# of sending logs to telegram channel
cci_obj = CCI(IEXCloud_obj=iex_obj,
              TAAPI_obj=taapi_obj,
              TAAPI_obj2=taapi_obj2,
              Telegram_obj=telegram_obj,
              KuCoin_connection=kucoin_obj,
              size=45)  # Create CCI object that gives the bot the ability of technical
# analysis and get along with cci indicator


# --------------------------------------------- Define Bot Functions ---------------------------------------------
def exec_heisen_bot():
    heisen_obj = Heisen(KCConnection=kucoin_obj,
                        Telegram_obj=telegram_obj,
                        CCI_obj=cci_obj)
    heisen_obj.exec()


# --------------------------------------------- Define Emergencies ---------------------------------------------
def emergency_close():
    telegram_obj.start_polling()


# --------------------------------------------- Execute ---------------------------------------------
exec_heisen_bot()