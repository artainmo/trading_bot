#If ema crossover buying signal but sar shows descend don't buy
#Descend sar is selling signal, for ema-crossover bought only
#Use the hour based sar
from utils.classes import *
from utils.file_handler import *
from utils.time_handler import *

def get_new_AF(AF_lasttrend, AF, current):
    if AF_lasttrend == "n" or AF_lasttrend == current:
        AF += 0.02
        if AF > 0.2:
            AF = 0.2
    else:
        AF = 0
    AF = current + str(AF)
    return AF

def get_EP(last_EP, potential_EP, trend):
    if trend == "u":
        EP = max(last_EP, potential_EP)
    else:
        EP = min(last_EP, potential_EP)
    return EP

def sar_to_candle(candle, sar, AF, EP):
    candle.append(sar)
    candle.append(AF)
    candle.append(EP)
    return candle


def set_parabolic_sar(candle, last_line):
    if last_line == "":
        return sar_to_candle(candle, candle[4], "n0", candle[4])
    AF = float(last_line["AF_sar"][1:len(last_line["AF_sar"])])
    AF_lasttrend = last_line["AF_sar"][0:1]
    if AF_lasttrend == "u":
        PSAR = float(last_line["sar"]) + (AF * (float(last_line["EP"]) - float(last_line["sar"])))
    else:
        PSAR = float(last_line["sar"]) - (AF * (float(last_line["sar"]) - float(last_line["EP"])))
    if PSAR < float(candle[4]):
        AF = get_new_AF(AF_lasttrend, AF, "u")
        EP = get_EP(float(last_line["EP"]), float(candle[4]), "u")
        return sar_to_candle(candle, PSAR, AF, EP)
    else:
        AF = get_new_AF(AF_lasttrend, AF, "d")
        EP = get_EP(float(last_line["EP"]), float(candle[4]), "d")
        return sar_to_candle(candle, PSAR, AF, EP)
