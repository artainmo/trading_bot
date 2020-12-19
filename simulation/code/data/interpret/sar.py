from utils.classes import *
from utils.file_handler import *
from utils.time_handler import *
import utils.global_variables as g

def get_sar_signal(coin, account):
    coin.opp["sar"] = None
    last_line = coin.last_line(g.PROTECTION_SAR_EMA["type"])
    if coin.opp["ema"] == "BUY" and float(last_line["sar"]) > float(last_line["close"]) and g.PROTECTION_SAR_EMA["active"] == "Yes":
        coin.opp["ema"] = None
    last_line = coin.last_line(g.SELL_SAR["type"])
    if float(account.coins[coin.market_name]["balance"]) != 0 and account.bought_coin_signal(coin.market_name) == "ema" and float(last_line["sar"]) > float(last_line["close"]):
        coin.opp["sar"] = "SELL"
    return coin
