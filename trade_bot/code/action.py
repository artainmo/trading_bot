from utils.classes import *
import data.api.api_actions as api
from data.interpret.ema import *
from data.interpret.rsi import *
from data.interpret.sar import *
from data.interpret.protection_sell import *
import utils.global_variables as g

def set_buy_sell_dict(type, price=None):
    dict = {
    "type": type,
    "proposed_price": price
    }
    return dict

def find_signal(coin, account):
    coin.buy = set_buy_sell_dict(None, None)
    coin.sell = set_buy_sell_dict(None, None)
    coin = get_ema_signal(coin, account)
    coin = get_rsi_signal(coin, account)
    coin = get_sar_signal(coin, account)
    coin = protection_sell(coin, account)
    if coin.opp["rsi"]["proposed_buy_price"] != None:
        coin.buy = set_buy_sell_dict("limit", coin.opp["rsi"]["proposed_buy_price"])
    if coin.opp["protection_sell"]["proposed_price"] != None:
        coin.sell = set_buy_sell_dict("limit", coin.opp["protection_sell"]["proposed_price"])
    if coin.opp["ema"] == "BUY" and g.BUY_EMA_CROSSOVER["buy"] == "instant":
        coin.buy = set_buy_sell_dict("market")
    if coin.opp["ema"] == "SELL" and g.SELL_EMA_CROSSOVER["sell"] == "instant":
        coin.sell = set_buy_sell_dict("market")
    if coin.opp["sar"] == "SELL" and g.SELL_SAR["sell"] == "instant":
        coin.sell = set_buy_sell_dict("market")
    return coin


def buy_sell_signal(coins, account):
    i = 0
    while i < len(coins):
        coins[i] = find_signal(coins[i], account)
        i += 1
    return coins


def sell(coins, account):
    i = 0
    while i < len(coins):
        if coins[i].sell["type"] == "market":
                coins[i].delete_existing_limit_orders("sell", account)
                quantity = account.available(coins[i].market_name)["available"]
                if quantity != 0:
                    coins[i].market_sell(account, quantity)
        elif coins[i].sell["type"] == "limit":
                    coins[i].limit_sell(account)
        i += 1
    return coins


def buy(coins, account):
    i = 0
    ret = 0
    to_buy_indexes = []
    while i < len(coins):
        if coins[i].buy["type"] != None:
            to_buy_indexes.append(i)
        i += 1
    if to_buy_indexes != []:
        euro_split = account.euros["available"] / len(to_buy_indexes)
    for index in to_buy_indexes:
        if coins[index].buy["type"] == "market":
            ret = coins[index].market_buy(account, euro_split + ret)
        elif coins[index].buy["type"] == "limit":
            ret = coins[index].limit_buy(account, euro_split + ret)
    return coins


def buying_selling_opportunity(coins, account):
    coins = buy_sell_signal(coins, account)
    coins = sell(coins, account)
    coins = buy(coins, account)
