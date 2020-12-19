import sys
from utils.file_handler import *
from utils.classes import *
import start_users

FD_BTCMIN = open("../../Real/coins_data/BTC-EUR_min.txt", "r")
FD_BTCQUARTER = open("../../Real/coins_data/BTC-EUR_quarter.txt", "r")
FD_BTCHOUR = open("../../Real/coins_data/BTC-EUR_hour.txt", "r")
FD_BTCDAY = open("../../Real/coins_data/BTC-EUR_day.txt", "r")

FD_ETHMIN = open("../../Real/coins_data/ETH-EUR_min.txt", "r")
FD_ETHQUARTER = open("../../Real/coins_data/ETH-EUR_quarter.txt", "r")
FD_ETHHOUR = open("../../Real/coins_data/ETH-EUR_hour.txt", "r")
FD_ETHDAY = open("../../Real/coins_data/ETH-EUR_day.txt", "r")

FD_LTCMIN = open("../../Real/coins_data/LTC-EUR_min.txt", "r")
FD_LTCQUARTER = open("../../Real/coins_data/LTC-EUR_quarter.txt", "r")
FD_LTCHOUR = open("../../Real/coins_data/LTC-EUR_hour.txt", "r")
FD_LTCDAY = open("../../Real/coins_data/LTC-EUR_day.txt", "r")

FD_XRPMIN = open("../../Real/coins_data/XRP-EUR_min.txt", "r")
FD_XRPQUARTER = open("../../Real/coins_data/XRP-EUR_quarter.txt", "r")
FD_XRPHOUR = open("../../Real/coins_data/XRP-EUR_hour.txt", "r")
FD_XRPDAY = open("../../Real/coins_data/XRP-EUR_day.txt", "r")

MARKET = None
START_DATE = None
END_DATE = None

BUY_EMA_CROSSOVER = {"buy": None, "type":None}
BUY_RSI = {
"buy":None,
"type":None,
"trailing":None,
"type":None,
"level1":{"value":None, "amplifier":None},
"level2":{"value":None, "amplifier":None}
}
PROTECTION_SAR_EMA = {"active":None, "type":None}
SELL_EMA_CROSSOVER = {"sell":None, "type":None}
SELL_RSI = {
"sell":None,
"type":None,
"level1":{"value":None, "amplifier":None},
"level2":{"value":None, "amplifier":None}
}
SELL_SAR = {"sell":None, "type":None}
PROTECTION_SELL_EMA = {"sell":None, "type":None, "trailing":None}
PROTECTION_SELL_RSI = {"sell":None, "type":None, "trailing":None}




line = ""
with open("../users_data/algo.txt", "r") as fd:
    start_users.find_user(line, fd)
    while line[0:8] != "MARKET: ":
        line = fd.readline()
    MARKET = line[8:-1]
    while line[0:12] != "START DATE: ":
        line = fd.readline()
    START_DATE = line[12:-1]
    line = fd.readline()
    END_DATE = line[10:-1]
    if MARKET == "BTC-EUR":
        if START_DATE == "DEFAULT":
            START_DATE = "2015-04-22T21:00:00.000000Z"
            END_DATE = None
        elif START_DATE == "NEUTRALTREND":
            START_DATE = "2018-09-01T00:00:00.000000Z"
            END_DATE = "2018-11-04T01:00:00.000000Z"
        elif START_DATE == "UPTREND":
            START_DATE = "2019-03-04T21:00:00.000000Z"
            END_DATE = "2019-07-10T21:00:00.000000Z"
        elif START_DATE == "DOWNTREND":
            START_DATE = "2019-07-10T21:00:00.000000Z"
            END_DATE = "2019-12-17T21:00:00.000000Z"
        elif START_DATE == "RSI-BUY":
            START_DATE = "2020-05-09T02:00:00.000000Z"
            END_DATE = "2020-05-10T21:00:00.000000Z"
        elif START_DATE == "EMA":
            START_DATE = "2020-05-04T10:00:00.000000Z"
            END_DATE = "2020-05-09T10:00:00.000000Z"
        START_DATE = times(START_DATE)
        END_DATE = times(END_DATE)
    elif MARKET == "ETH-EUR":
        if START_DATE == "DEFAULT":
            START_DATE = "2017-05-23T18:00:00.000000Z"
            END_DATE = None
        elif START_DATE == "NEUTRALTREND":
            START_DATE = "2019-03-01T00:00:00.000000Z"
            END_DATE = "2019-03-31T01:00:00.000000Z"
        elif START_DATE == "UPTREND":
            START_DATE = "2018-04-04T00:00:00.000000Z"
            END_DATE = "2018-05-06T00:00:00.000000Z"
        elif START_DATE == "DOWNTREND":
            START_DATE = "2018-05-06T00:00:00.000000Z"
            END_DATE = "2018-12-16T00:00:00.000000Z"
        START_DATE = times(START_DATE)
        END_DATE = times(END_DATE)
    elif MARKET == "LTC-EUR":
        if START_DATE == "DEFAULT":
            START_DATE = "2017-05-22T22:00:00.000000Z"
            END_DATE = None
        elif START_DATE == "NEUTRALTREND":
            START_DATE = "2018-08-16T00:00:00.000000Z"
            END_DATE = "2018-11-12T01:00:00.000000Z"
        elif START_DATE == "UPTREND":
            START_DATE = "2018-12-14T00:00:00.000000Z"
            END_DATE = "2019-06-16T00:00:00.000000Z"
        elif START_DATE == "DOWNTREND":
            START_DATE = "2019-06-16T00:00:00.000000Z"
            END_DATE = "2019-12-17T00:00:00.000000Z"
        START_DATE = times(START_DATE)
        END_DATE = times(END_DATE)
    else:
        print("Market not found")
        exit()
    while line.strip('\n') != "BUY:":
        line = fd.readline()
    while line.strip('\n') != "SELL:":
        line = fd.readline()
        if line[0:14] == "ema crossover ":
            BUY_EMA_CROSSOVER["buy"] = line[16:-1]
            line = fd.readline()
            if line.find("_") != -1:
                BUY_EMA_CROSSOVER["type"] = line[0:-1]
        if line[0:6] == "rsi = ":
            BUY_RSI["buy"] = line[6:-1]
            line = fd.readline()
            if line.find("_") != -1:
                BUY_RSI["type"] = line[0:-1]
                line = fd.readline()
                if line.find("_") != -1:
                    BUY_RSI["trailing"] = float(line[1:-1])
                    line = fd.readline()
                    if line.find("_") != -1:
                        BUY_RSI["level1"]["value"] = float(line[1:line.find(" ")])
                        BUY_RSI["level1"]["amplifier"] = float(line[line.find("=") + 1:-1])
                        line = fd.readline()
                        if line.find("_") != -1:
                            BUY_RSI["level2"]["value"] = float(line[1:line.find(" ")])
                            BUY_RSI["level2"]["amplifier"] = float(line[line.find("=") + 1:-1])
        if line[0:21] == "protection sar ema = ":
            PROTECTION_SAR_EMA["active"] = line[21:-1]
            line = fd.readline()
            if line.find("_") != -1:
                PROTECTION_SAR_EMA["type"] = line[0:-1]
    while line.strip('\n') != "":
        line = fd.readline()
        if line[0:14] == "ema crossover ":
            SELL_EMA_CROSSOVER["sell"] = line[16:-1]
            line = fd.readline()
            if line.find("_") != -1:
                SELL_EMA_CROSSOVER["type"] = line[0:-1]
        line = fd.readline()
        if line[0:6] == "rsi = ":
            SELL_RSI["sell"] = line[6:-1]
            line = fd.readline()
            if line.find("_") != -1:
                SELL_RSI["type"] = line[0:-1]
                line = fd.readline()
                if line.find("_") != -1:
                    SELL_RSI["level1"]["value"] = float(line[1:line.find(" ")])
                    SELL_RSI["level1"]["amplifier"] = float(line[line.find("=") + 1:-1])
                    line = fd.readline()
                    if line.find("_") != -1:
                        SELL_RSI["level2"]["value"] = float(line[1:line.find(" ")])
                        SELL_RSI["level2"]["amplifier"] = float(line[line.find("=") + 1:-1])
        line = fd.readline()
        if line[0:6] == "sar = ":
            SELL_SAR["sell"] = line[6:-1]
            line = fd.readline()
            if line.find("_") != -1:
                SELL_SAR["type"] = line[0:-1]
        line = fd.readline()
        if line[0:22] == "protection sell ema = ":
            PROTECTION_SELL_EMA["sell"] = line[22:-1]
            line = fd.readline()
            if line.find("_") != -1:
                PROTECTION_SELL_EMA["type"] = line[0:-1]
            line = fd.readline()
            if line.find("_") != -1:
                PROTECTION_SELL_EMA["trailing"] = float(line[1:-1])
        line = fd.readline()
        if line[0:22] == "protection sell rsi = ":
            PROTECTION_SELL_RSI["sell"] = line[22:-1]
            line = fd.readline()
            if line.find("_") != -1:
                PROTECTION_SELL_RSI["type"] = line[0:-1]
            line = fd.readline()
            if line.find("_") != -1:
                PROTECTION_SELL_RSI["trailing"] = float(line[1:-1])
