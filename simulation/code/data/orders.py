from utils.classes import *


def orders_to_one(coin, orders, side, account):
    initial_eu = account.euros["available"]
    if orders == None or len(orders) == 1:
        return coin, account
    final = orders[0]["value"]
    if side == "buy":
        for order in orders:
            if order["value"] < final:
                final = order
    if side == "sell":
        for order in orders:
            if order["value"] > final:
                final = order
    coin.orders, account = coin.cancel_orders(side, account)
    if side == "buy":
        eu = account.euros["available"] - initial_eu #Euros from canceled orders
        size = eu/order["value"]
        self.orders, account = self.new_order(final["value"] * size, final["value"], "open", None, self.last_update("_min"), size, "limit", "buy", account)
        order = api.limit_buy_sell(eu/price, price, "buy", self.market_name, account)
    if side == "sell":
        size = account.coins[coin.market_name]["available"]
        self.orders, account = self.new_order(final["value"] * size, final["value"], "open", None, self.last_update("_min"), size, "limit", "sell", account)
        order = api.limit_buy_sell(size, price, "sell", self.market_name, account)
    return coin, account


def check_filled_orders(coin, account):
    for order in coin.orders:
        if order["side"] == "buy":
            if order["value"] < coin.last_price():
                coin.orders, account = coin.finished_limit_order(order, account)
        if order["side"] == "sell":
            if order["value"] > coin.last_price():
                coin.orders, account = coin.finished_limit_order(order, account)
    return coin, account

def get_orders(coin, account):
    # coin, account = orders_to_one(coin, coin.get_side_order("buy"), "buy", account)
    # coin, account = orders_to_one(coin, coin.get_side_order("sell"), "sell", account)
    coin, account = check_filled_orders(coin, account)
    return coin
