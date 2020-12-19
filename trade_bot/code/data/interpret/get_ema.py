from utils.classes import *
from utils.file_handler import *
from utils.time_handler import *


def up_moves(new_candle, last_line):
    weighted_multiplier = 2.000000 / (14 + 1)
    change = float(new_candle[4]) - float(last_line["close"])
    if change < 0:
        change = 0
    ema_up = ((change - float(last_line["ema_up"])) * weighted_multiplier) + float(last_line["ema_up"])
    return ema_up


def down_moves(new_candle, last_line):
    weighted_multiplier = 2.000000 / (14 + 1)
    change = float(new_candle[4]) - float(last_line["close"])
    if change > 0:
        change = 0
    else:
        change *= -1
    ema_down = ((change - float(last_line["ema_down"])) * weighted_multiplier) + float(last_line["ema_down"])
    return ema_down


def get_ema(new_candle, old_ema12, old_ema26):
    weighted_multiplier = 2.000000 / (12 + 1)
    ema12 = ((new_candle[4] - old_ema12) * weighted_multiplier) + old_ema12
    weighted_multiplier = 2.000000 / (26 + 1)
    ema26 = ((new_candle[4] - old_ema26) * weighted_multiplier) + old_ema26
    return ema12, ema26


def emas_to_candle(candle, ema12, ema26, ema_up, ema_down):
    candle.append(ema12)
    candle.append(ema26)
    candle.append(ema_up)
    candle.append(ema_down)
    return candle


def set_ema(candle, last_line):
    if last_line == "":
        candle = emas_to_candle(candle, candle[4], candle[4], candle[4], candle[4])
    else:
        ema12, ema26 = get_ema(candle, float(last_line["ema12"]), float(last_line["ema26"]))
        ema_up = up_moves(candle, last_line)
        ema_down = down_moves(candle, last_line)
        candle = emas_to_candle(candle, ema12, ema26, ema_up, ema_down)
    return candle
