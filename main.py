import time
from CoreData.TAAPI import TAAPI
from CoreData.IEXCloud import IEXCloud
from Strategy.CCI import CCI
from secrets import TAAPI_API_TOKEN
from secrets import IEX_CLOUD_API_TOKEN

try:
    iex_obj = IEXCloud(IEX_CLOUD_API_TOKEN)
    taapi_obj = TAAPI(TAAPI_API_TOKEN)
    cci_obj = CCI(IEXCloud_obj=iex_obj,
                  TAAPI_obj=taapi_obj)
    while True:
        cci_obj.cci_5m(symbol_iex='BTCUSDT',
                       symbol_ta='BTC/USDT')
        time.sleep(15)

except Exception as ex:
    print('main: %s' % ex)
