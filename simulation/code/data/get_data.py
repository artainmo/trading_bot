from utils.time_handler import *
from utils.classes import *
from utils.file_handler2 import *
import utils.global_variables as g

def curr_value(product_id):
    with open("../coins_data/" + product_id + "_min.txt", "r") as fd:
        candle = get_last_line_in_dict(fd)
    return float(candle["close"])

def print_result(account, coins):
    for coin in coins:
        for order in coin.orders:
            if order["side"] == "buy":
                account.euros["available"] += order["price"]
                account.euros["balance"] += order["price"]
            else:
                account.coins[order["market_name"]]["available"] += order["size"]
    final_eu = account.euros["available"]
    for coin in account.coins:
        final_eu += account.coins[coin]["available"] * curr_value(coin)
    with open("../feedback/result.txt", "a") as fd:
        fd.write(g.START_DATE.all + "\n")
        if g.START_DATE != "DEFAULT" and g.START_DATE != "UPTREND" and g.START_DATE != "DOWNTREND" and g.START_DATE != "NEUTRALTREND":
            fd.write(g.END_DATE.all + "\n")
        fd.write("START EU: 1000\n")
        fd.write("FINAL TOTAL EU: " + str(final_eu) + "\n")
        fd.write("ACTUAL EU: " + str(account.euros["available"]) + "\n")
        for coin in account.coins:
            fd.write("ACTUAL " + coin + ": " + str(account.coins[coin]["available"]) + "\n")
        fd.write("\n")


def print_data(coin, file_extension, line):
    with open("../coins_data/" + coin.market_name + file_extension + ".txt", "a") as fda:
        fda.write(line)

def take_data(coin, file_extension):
    line = ""
    if coin.market_name == "BTC-EUR" and file_extension == "_min":
        line = g.FD_BTCMIN.readline()
    elif coin.market_name == "BTC-EUR" and file_extension == "_quarter":
        line = g.FD_BTCQUARTER.readline()
    elif coin.market_name == "BTC-EUR" and file_extension == "_hour":
        line = g.FD_BTCHOUR.readline()
    elif coin.market_name == "BTC-EUR" and file_extension == "_day":
        line = g.FD_BTCDAY.readline()
    elif coin.market_name == "ETH-EUR" and file_extension == "_min":
        line = g.FD_ETHMIN.readline()
    elif coin.market_name == "ETH-EUR" and file_extension == "_quarter":
        line = g.FD_ETHQUARTER.readline()
    elif coin.market_name == "ETH-EUR" and file_extension == "_hour":
        line = g.FD_ETHHOUR.readline()
    elif coin.market_name == "ETH-EUR" and file_extension == "_day":
        line = g.FD_ETHDAY.readline()
    elif coin.market_name == "LTC-EUR" and file_extension == "_min":
        line = g.FD_LTCMIN.readline()
    elif coin.market_name == "LTC-EUR" and file_extension == "_quarter":
        line = g.FD_LTCQUARTER.readline()
    elif coin.market_name == "LTC-EUR" and file_extension == "_hour":
        line = g.FD_LTCHOUR.readline()
    elif coin.market_name == "LTC-EUR" and file_extension == "_day":
        line = g.FD_LTCDAY.readline()
    elif coin.market_name == "XRP-EUR" and file_extension == "_min":
        line = g.FD_XRPMIN.readline()
    elif coin.market_name == "XRP-EUR" and file_extension == "_quarter":
        line = g.FD_XRPQUARTER.readline()
    elif coin.market_name == "XRP-EUR" and file_extension == "_hour":
        line = g.FD_XRPHOUR.readline()
    elif coin.market_name == "XRP-EUR" and file_extension == "_day":
        line = g.FD_XRPDAY.readline()
    if line == "":
        return True
    print_data(coin, file_extension, line)
    return False

def get_data(coin):
    ret = take_data(coin, "_min")
    time_m = times(coin.last_update("_min"))
    if g.END_DATE != None and g.END_DATE.earlier_than(time_m):
        ret = True
    time_q = coin.last_update("_quarter")
    time_h = coin.last_update("_hour")
    time_d = coin.last_update("_day")
    if time_q == None or increase_1quarter(times(time_q)).earlier_than(time_m):
        take_data(coin, "_quarter")
    if time_h == None or increase_1hour(times(time_h)).earlier_than(time_m):
        take_data(coin, "_hour")
    if time_d == None or increase_1day(times(time_d)).earlier_than(time_m):
        take_data(coin, "_day")
    return ret

def go_to_start_date(coin):
    if coin.market_name == "BTC-EUR":
        fd_m = g.FD_BTCMIN
        fd_q = g.FD_BTCQUARTER
        fd_h = g.FD_BTCHOUR
        fd_d = g.FD_BTCDAY
    elif coin.market_name == "ETH-EUR":
        fd_m = g.FD_ETHMIN
        fd_q = g.FD_ETHQUARTER
        fd_h = g.FD_ETHHOUR
        fd_d = g.FD_ETHDAY
    elif coin.market_name == "LTC-EUR":
        fd_m = g.FD_LTCMIN
        fd_q = g.FD_LTCQUARTER
        fd_h = g.FD_LTCHOUR
        fd_d = g.FD_LTCDAY
    elif coin.market_name == "XRP-EUR":
        fd_m = g.FD_XRPMIN
        fd_q = g.FD_XRPQUARTER
        fd_h = g.FD_XRPHOUR
        fd_d = g.FD_XRPDAY
    line = fd_m.readline()
    line = line_to_dict(line)
    while times(line["iso_time"]).earlier_than(g.START_DATE):
        line = fd_m.readline()
        line = line_to_dict(line)
        if line == "":
            break
    line = fd_q.readline()
    line = line_to_dict(line)
    while times(line["iso_time"]).earlier_than(g.START_DATE):
        line = fd_q.readline()
        line = line_to_dict(line)
        if line == "":
            break
    line = fd_h.readline()
    line = line_to_dict(line)
    while times(line["iso_time"]).earlier_than(g.START_DATE):
        line = fd_h.readline()
        line = line_to_dict(line)
        if line == "":
            break
    line = fd_d.readline()
    line = line_to_dict(line)
    while times(line["iso_time"]).earlier_than(g.START_DATE):
        line = fd_d.readline()
        line = line_to_dict(line)
        if line == "":
            break
