import signal
from utils.classes import *
import utils.global_variables as g
from action import *
from data.orders import *
import sys
import os
from data.api.api_call import *
from data.get_data import *

coins_str = [[g.MARKET, "2015-04-22T21:00:00.000000Z"]]#, ["ETH-EUR", "2017-05-23T18:00:00.000000Z"], ["LTC-EUR", "2017-05-22T22:00:00.000000Z"], ["XRP-EUR", "2019-02-26T17:00:00.000000Z"]] BTC only will go way faster


def init_account():
    account = accounts()
    account.euros = {"available":1000, "balance":1000}
    for product_id in coins_str:
        account.coins[product_id[0]] = {"available":0, "balance":0}
        account.coins[product_id[0]] = {"available":0, "balance":0}
    return account

def init_error_file():
    fd = os.open("../feedback/errors.txt", os.O_WRONLY | os.O_APPEND | os.O_CREAT)
    os.dup2(fd, 1)
    os.dup2(fd, 2)


def signal_handler(a, b):
    print("")
    exit()


def init_coins():
    list = []
    i = 0
    for product_id in coins_str:
        list.append(coins_list(product_id[0], product_id[1]))
    for coin in list:
        go_to_start_date(coin)
    return list


def update_coins(coins, account):
    i = 0
    while i < len(coins):
        coins[i] = get_orders(coins[i], account)
        EOF = get_data(coins[i])
        i += 1
    if EOF == True:
        print_result(account, coins)
        exit()
    return coins


if __name__ == "__main__":
    account = init_account()
    os.system("rm ../coins_data/*.txt ../feedback/transactions_" + account.name + ".txt")
    signal.signal(signal.SIGINT, signal_handler)
    # init_error_file()
    coins = init_coins()
    while True:
        update_coins(coins, account)
        buying_selling_opportunity(coins, account)
