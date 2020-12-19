#Constant base trailing stop loss sell
from utils.classes import *
from utils.time_handler import *
import utils.global_variables as g

def set_protection_sell(coin, instant_sell, amplifier, price=None):
    coin.opp["protection_sell"]["instant_sell"] = instant_sell
    coin.opp["protection_sell"]["sell_signal_amplifier"] = amplifier
    coin.opp["protection_sell"]["proposed_price"] = price
    return coin

def protection_sell(coin, account):
    coin = set_protection_sell(coin, None, None, None)
    if float(account.coins[coin.market_name]["balance"]) == 0:
        return coin
    coin = set_protection_sell(coin, None, 1, None)
    if coin.opp["rsi"]["sell_signal_amplifier"] != 1 and g.SELL_RSI["sell"] == "trailing":
        coin = set_protection_sell(coin, None, coin.opp["rsi"]["sell_signal_amplifier"])
    if account.bought_coin_signal(coin.market_name) == "ema" and g.PROTECTION_SELL_EMA["sell"] == "trailing":
        last_line = coin.last_line(g.PROTECTION_SELL_EMA["type"])
        coin.opp["protection_sell"]["proposed_price"] = float(last_line["high"]) - (float(last_line["high"]) * (g.PROTECTION_SELL_EMA["trailing"] / float(coin.opp["protection_sell"]["sell_signal_amplifier"])))
    elif account.bought_coin_signal(coin.market_name) == "limit_order" and g.PROTECTION_SELL_RSI["sell"] == "trailing":
        last_line = coin.last_line(g.PROTECTION_SELL_RSI["type"])
        coin.opp["protection_sell"]["proposed_price"] = float(last_line["high"]) - (float(last_line["high"]) * (g.PROTECTION_SELL_RSI["trailing"] / float(coin.opp["protection_sell"]["sell_signal_amplifier"])))
    return coin
