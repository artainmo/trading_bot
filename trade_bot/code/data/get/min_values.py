from data.api.api_actions import *
from data.interpret.complete_candle import *
from data.get.timeframe_values import *
from utils.classes import *
from utils.time_handler import *
from time import sleep

def get_historic_data(coin, start, end, account):
    data = []
    data = historic_data(coin.market_name, start.all, end.all, 60, account) #TODO
    if data != []:
        write_complete_candles(coin, "_min", data, start)

def get_raisig_5hours_min(start, now, coin, account):
    end = increase_5_hours(start)
    if end.earlier_than(now):
        get_historic_data(coin, start, end, account)
    return end

def get_raising_min(start, now, coin, account):
    end = add_1min(start)
    if end.earlier_than(now):
        get_historic_data(coin, start, end, account)
    return end

def get_historical_values_in_min(start_date, now, coin, account):
    minute_values = []
    ret = []
    remember = start_date
    while start_date.earlier_than(now):
        remember = start_date
        start_date = get_raisig_5hours_min(start_date, now, coin, account)
    start_date = remember
    while start_date.earlier_than(now):
        start_date = get_raising_min(start_date, now, coin, account)
