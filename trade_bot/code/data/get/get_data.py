from data.api.api_actions import *
from utils.classes import *
from data.get.min_values import *
from data.get.timeframe_values import *
from utils.file_handler2 import *


def get_coin_history(coin, account):
    if coin.market_name == None:
        return None
    time = times(None)
    time.get_time(account)
    get_historical_values_in_min(times(coin.start_date), time, coin, account)
    get_timeframe(times(coin.start_date), time, coin, increase_1quarter, get_lines_as_dict, "_quarter")
    get_timeframe(times(coin.start_date), time, coin, increase_1hour, get_lines_as_dict, "_hour")
    get_timeframe(times(coin.start_date), time, coin, increase_1day, get_lines_as_dict, "_day")


def update_coin_history(coin, account):
    if coin == None:
        return coin
    now = times(None)
    now.get_time(account)
    get_historical_values_in_min(times(coin.last_update("_min")), now, coin, account)
    get_timeframe(times(coin.last_update("_quarter")), now, coin, increase_1quarter, get_lines_as_dict_backwards, "_quarter")
    get_timeframe(times(coin.last_update("_hour")), now, coin, increase_1hour, get_lines_as_dict_backwards, "_hour")
    get_timeframe(times(coin.last_update("_day")), now, coin, increase_1day, get_lines_as_dict_backwards, "_day")
    return coin
