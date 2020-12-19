from data.interpret.get_ema import *
from data.interpret.get_rsi import *
from data.interpret.get_sar import *
from utils.file_handler import *
from utils.time_handler import *


def set_iso_time(data, start):
    i = 0
    minutes = 0
    while i < len(data):
        data[i].append(start.all)
        if i > 0:
            minutes = (data[i - 1][0] - data[i][0]) / 60
        for min in range(0,minutes):
            start = add_1min(start)
        i += 1
    return data

def write_complete_candles(coin, file_extension, data, time):
    i = 0
    data = set_iso_time(data, time)
    while i < len(data):
        with open("../coins_data/" + coin.market_name + file_extension + ".txt", "a+") as fd_a, open("../coins_data/" + coin.market_name + file_extension + ".txt", "r") as fd_r:
            last_line = get_last_line_in_dict(fd_r)
            if last_line == "" or data[i][6] != last_line["iso_time"]:
                data[i] = set_ema(data[i], last_line)
                data[i] = set_rsi(data[i])
                data[i] = set_parabolic_sar(data[i], last_line)
                data[i] = ','.join(map(str, data[i]))
                fd_a.write(data[i] + "\n")
        i += 1
