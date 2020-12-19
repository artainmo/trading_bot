import signal
from utils.classes import *
from action import *
from data.orders import *
from data.get.get_data import *
import sys


coins_str = [["BTC-EUR", "2015-04-22T21:00:00.000000Z"], ["ETH-EUR", "2017-05-23T18:00:00.000000Z"], ["LTC-EUR", "2017-05-22T22:00:00.000000Z"], ["XRP-EUR", "2019-02-26T17:00:00.000000Z"]] #["EOS-EUR", "2019-04-09T12:00:00.000000Z"] EOS can only do limit orders

account_name = sys.argv[1]
api_url = sys.argv[2]
api_key = sys.argv[3]
api_secret_key = sys.argv[4]
api_passphrase = sys.argv[5]
api_authentification = CoinbaseExchangeAuth(api_key, api_secret_key, api_passphrase)


def init_account():
    account = accounts(account_name, api_authentification, api_url)
    account.euros = {"available":0, "balance":0}
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


def init_coins(account):
    list = []
    i = 0
    for product_id in coins_str:
        list.append(coins_list(product_id[0], product_id[1]))
    return list


def update_account(account):
    account.euros = account.available("EUR-")
    for product_id in coins_str:
        account.coins[product_id[0]] = account.available(product_id[0])
    return account


def update_coins(coins, account):
    i = 0
    while i < len(coins):
        coins[i] = get_orders(coins[i], account)
        i += 1
    return coins


def data_up_to_date_check(account):
    now = times(None)
    now.get_time(account)
    for product_id in coins_str:
        with open("../coins_data/" + product_id[0] + "_hour.txt", "r") as fd:
            line = get_last_line_in_dict(fd)
        data_time = addminutes(times(line["iso_time"]), 120)
        if data_time.earlier_than(now) == True:
            return False
    return True


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    account = init_account()
    init_error_file()
    coins = init_coins(account)
    while True:
        update_account(account)
        update_coins(coins, account)
        if data_up_to_date_check(account) == True:
            buying_selling_opportunity(coins, account)
