import signal
from time import *
from utils.classes import *
from data.get.get_data import *
from data.api.api_call import *
from data.api.api_actions import *
import sys


coins_str = [["BTC-EUR", "2015-04-22T21:00:00.000000Z"], ["ETH-EUR", "2017-05-23T18:00:00.000000Z"], ["LTC-EUR", "2017-05-22T22:00:00.000000Z"], ["XRP-EUR", "2019-02-26T17:00:00.000000Z"]] #["EOS-EUR", "2019-04-09T12:00:00.000000Z"] EOS can only do limit orders

account_name = "Ar*"
api_url = "https://api.pro.coinbase.com/"
api_key = "db*"
api_secret_key = "dk*"
api_passphrase = "un*"
api_authentification = CoinbaseExchangeAuth(api_key, api_secret_key, api_passphrase)


#See account_name and api_authentification variables inside api_actions
def init_account():
    account = accounts(account_name, api_authentification, api_url)
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
        if sys.argv[1] == "start":
            get_coin_history(list[i], account)
        i += 1
    return list


def update_coins(coins, account):
    i = 0
    while i < len(coins):
        coins[i] = update_coin_history(coins[i], account)
        i += 1
    return coins


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    account = init_account()
    init_error_file()
    coins = init_coins(account)
    while True:
        coins = update_coins(coins, account)
