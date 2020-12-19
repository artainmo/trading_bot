import utils.global_variables as g
from utils.classes import *
from utils.file_handler import *
from utils.time_handler import *


def set_rsi_signal(coin, sell, buy, price=None):
    coin.opp["rsi"]["sell_signal_amplifier"] = sell
    coin.opp["rsi"]["buy_signal_amplifier"] = buy
    coin.opp["rsi"]["proposed_buy_price"] = price
    return coin

def rsi_sell_signal(coin, last_line):
    if float(last_line["rsi"]) > g.SELL_RSI["level1"]["value"]:
        if float(last_line["rsi"]) > g.SELL_RSI["level2"]["value"]:
            coin = set_rsi_signal(coin, g.SELL_RSI["level2"]["amplifier"], None)
        else:
            coin = set_rsi_signal(coin, g.SELL_RSI["level1"]["amplifier"], None)
    return coin

def rsi_buy_signal(coin, last_line):
    if float(last_line["rsi"]) < g.BUY_RSI["level1"]["value"]:
        if float(last_line["rsi"]) < g.BUY_RSI["level2"]["value"]:
            coin = set_rsi_signal(coin, 1/g.SELL_RSI["level2"]["amplifier"], g.BUY_RSI["level2"]["amplifier"])
        else:
            coin = set_rsi_signal(coin, 1/g.SELL_RSI["level1"]["amplifier"], g.BUY_RSI["level1"]["amplifier"])
    return coin

def get_rsi_signal(coin, account):
    last_line = coin.last_line(g.BUY_RSI["type"])
    coin = set_rsi_signal(coin, 1, None)
    if account.euros["balance"] > 10:
        coin = rsi_buy_signal(coin, last_line)
    if account.coins[coin.market_name]["balance"]:
        coin = rsi_sell_signal(coin, last_line)
    if coin.opp["rsi"]["buy_signal_amplifier"] != None and g.BUY_RSI["buy"] == "trailing":
        last_line = coin.last_line("_min")
        coin.opp["rsi"]["proposed_buy_price"] = float(last_line["low"]) + (float(last_line["low"]) * (g.BUY_RSI["trailing"] / float(coin.opp["rsi"]["buy_signal_amplifier"])))
    return coin
