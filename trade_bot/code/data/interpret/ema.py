from utils.classes import *
from utils.file_handler import *
from utils.time_handler import *
import utils.global_variables as g

def time_check(last_line, account):
    now = times(None)
    now.get_time(account)
    limit_time = addminutes(times(last_line["iso_time"]), 5)
    return now.earlier_than(limit_time) #Do not buy if you are later than ema cross


def buy_ema_signal(coin, file_extension, account):
    ret = 0
    lines = coin.last_lines_in_dict(3, file_extension)
    if lines == "":
        return 0
    last_line = lines[0]
    second_last_line = lines[1]
    third_last_line = lines[2]
    if time_check(last_line, account) == False:
        return 0
    if float(last_line["ema12"]) > float(last_line["ema26"]) and float(second_last_line["ema12"]) < float(second_last_line["ema26"]):
        ret += 1
        if float(last_line["ema12"]) > float(second_last_line["ema12"]):
            ret += 1
        if float(last_line["ema26"]) > float(second_last_line["ema26"]):
            ret += 1
    return ret

def sell_ema_signal(coin, file_extension, account):
    ret = 0
    lines = coin.last_lines_in_dict(3, file_extension)
    if lines == "":
        return 0
    last_line = lines[0]
    second_last_line = lines[1]
    third_last_line = lines[2]
    if time_check(last_line, account) == False:
        return 0
    if float(last_line["ema12"]) < float(last_line["ema26"]) and float(second_last_line["ema12"]) > float(second_last_line["ema26"]):
        ret -= 1
        if float(last_line["ema12"]) < float(second_last_line["ema12"]):
            ret -= 1
        if float(last_line["ema26"]) < float(second_last_line["ema26"]):
            ret -= 1
    return ret


def get_ema_signal(coin, account):
    ret_buy = 0
    ret_sell = 0
    if int(account.euros["balance"]) > 10:
        ret_buy = buy_ema_signal(coin, g.BUY_EMA_CROSSOVER["type"], account)
    if float(account.coins[coin.market_name]["balance"]) != 0:
        ret_sell = sell_ema_signal(coin, g.SELL_EMA_CROSSOVER["type"], account)
    if ret_buy == 3 and g.BUY_EMA_CROSSOVER["buy"] == "instant":
        coin.opp["ema"] = "BUY"
        return coin
    elif ret_sell == -3 and g.SELL_EMA_CROSSOVER["sell"] == "instant":
        coin.opp["ema"] = "SELL"
        return coin
    else:
        coin.opp["ema"] = None
        return coin
