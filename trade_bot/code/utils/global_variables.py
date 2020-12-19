import time
import sys
from utils.file_handler import *
import start_users


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
with open("../users_data/users.txt", "r") as fd:
    start_users.find_user(line, fd)
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
