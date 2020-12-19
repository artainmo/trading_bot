import data.api.api_actions as api
from utils.classes import *


def manage_partially_filled_orders(coin, order):
    price = order["filled_size"] * order["price"]
    value = order["price"]
    coin.document_what_happened(price, value, order)
    order["size"] = float(order["size"]) - float(order["filled_size"])
    order["filled_size"] = 0
    return order


def filled_limit_order(coin, filled_order_id, account):
    filled_order = api.fills(filled_order_id, None, account)
    if filled_order != False:
        coin.document_what_happened(float(order["size"]) * float(order["price"]), order["price"], filled_order)


def check_filled_orders(coin, orders, account):
    still = False
    for ancient_order in coin.orders:
        for order in orders:
            if ancient_order["id"] == order["id"]:
                still = True
        if still == False and ancient_order != None:
            filled_limit_order(coin, ancient_order["id"], account)
        still = False

def orders_to_one(coin, orders, side, account):
    if orders == None or len(orders) == 1:
        return orders
    final = float(orders[0]["price"])
    if side == "buy":
        for order in orders:
            if float(order["price"]) < final:
                final = float(order["price"])
    if side == "sell":
        for order in orders:
            if float(order["price"]) > final:
                final = float(order["price"])
    coin.delete_existing_limit_orders(side)
    if side == "buy":
        eu = account.available("EUR-")["available"] - float(account.euros)["available"] #Euros from canceled orders
        order = api.limit_buy_sell(eu/final, final, "buy", self.market_name, account)
    if side == "sell":
        size = account.available(self.market_name)["available"]
        order = api.limit_buy_sell(size, final, "sell", self.market_name, account)
    return order



def get_orders(coin, account):
    orders = api.orders(coin.market_name, "open", account)
    check_filled_orders(coin, orders, account)
    for order in orders:
        if order["filled_size"] != 0:
            order = manage_partially_filled_orders(coin, order)
        coin.orders.append(order)
    buy_order = orders_to_one(coin, coin.get_side_order("buy"), "buy", account)
    sell_order = orders_to_one(coin, coin.get_side_order("sell"), "sell", account)
    coin.orders = []
    coin.orders.append(buy_order)
    coin.orders.append(sell_order)
    return coin
