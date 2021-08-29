from secrets import IEX_CLOUD_API_TOKEN
from CoreData.IEXCloud import IEXCloud

iex_obj = IEXCloud(IEX_CLOUD_API_TOKEN)
print(iex_obj.get_quote('BTCUSDT'))