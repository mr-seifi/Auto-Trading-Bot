from CoreData.TAAPI import TAAPI
from CoreData.IEXCloud import IEXCloud
from secrets import TAAPI_API_TOKEN
from secrets import IEX_CLOUD_API_TOKEN

try:
    # iex_obj = IEXCloud(IEX_CLOUD_API_TOKEN)
    # print(iex_obj.get_quote('BTCUSDT'))

    taapi_obj = TAAPI(TAAPI_API_TOKEN)
    print(taapi_obj.get_cci(symbol='BTC/USDT',
                            interval='1h'))
except Exception as ex:
    print('main: %s' % ex)
