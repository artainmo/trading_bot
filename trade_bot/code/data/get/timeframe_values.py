from utils.classes import *
from data.interpret.complete_candle import *
from data.get.min_values import *
from utils.time_handler import *
from utils.file_handler2 import *

def get_candle(values, start, file_extension, coin):
    ret = [int(values[0]["bucket_time"]), float("inf"), 0.0, float(values[0]["open"]), float(values[len(values) - 1]["close"]), 0.0]
    for value in values:
        if float(value["low"]) < ret[1]:
            ret[1] = float(value["low"])
        if float(value["high"]) > ret[2]:
            ret[2] = float(value["high"])
        ret[5] += float(value["volume"])
    write_complete_candles(coin, file_extension, [ret], start)

def min_to_timeframe(start, end, coin, get_lines_func, file_extension, fd):
    i = 0
    ret = []
    timeframe_in_min = get_lines_func(start, end, fd)
    if timeframe_in_min != []:
        return get_candle(timeframe_in_min, start, file_extension, coin)

def get_raising_timeframe(start, now, coin, increase_time_func, get_lines_func, file_extension, fd):
    end = increase_time_func(start)
    if end.earlier_than(now):
        min_to_timeframe(start, end, coin, get_lines_func, file_extension, fd)
    return end

def get_timeframe(start_date, now, coin, increase_time_func, get_lines_func, file_extension):
    minute_values = []
    ret = []
    with open("../coins_data/" + coin.market_name + "_min" + ".txt", "r") as fd:
        while start_date.earlier_than(now):
            start_date = get_raising_timeframe(start_date, now, coin, increase_time_func, get_lines_func, file_extension, fd)
