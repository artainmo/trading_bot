import requests
import json
from data.api.api_call import *
import subprocess
import os
import time


def request_failed(action):
    print("Request Failed " + action)
    subprocess.Popen("date")
    time.sleep(1)

def error_check(r, action):
    time.sleep(0.35)
    print(r.status_code, "-", action, r.json()['message'])
    subprocess.Popen("date")
    time.sleep(0.1)

def ret(r):
    time.sleep(0.35)#Max 3 requests per minue
    return r.json()

#action is buy or sell
#default action type is limit order with good till canceled as time of force
def market_buy_sell(size, action, product_id, account):
    order = {
        'size' : str(size),
        'type' : "market",
        'side': action,
        'product_id' : product_id
    }
    try:
        r = requests.post(account.api_url + 'orders', json.dumps(order), auth=account.api_authentification)
        if r.status_code != 200 and r.json()["message"][0:21] == 'Limit only mode':
            print("No market order allowed on " + product_id)
            return False
        if r.status_code != 200 and r.json()["message"][0:21] == 'size is too accurate.':
            return buy_sell(size[0:len(size) - 1], action, product_id)
        if r.status_code != 200 and r.json()["message"][0:18] == 'size is too small.':
            return False
        if r.status_code != 200 and r.json()["message"] == 'Insufficient funds':
            return False
        return ret(r)
    except:
        error_check(r, action)
        request_failed(action)

def limit_buy_sell(size, price, action, product_id, account):
    order = {
        'size' : str(size),
        'type' : "limit",
        'price': price,
        'side': action,
        'product_id' : product_id
    }
    try:
        r = requests.post(account.api_url + 'orders', json.dumps(order), auth=account.api_authentification)
        if r.status_code != 200 and r.json()["message"][0:21] == 'size is too accurate.':
            return limit_buy_sell(size[0:len(size) - 1], price, action, product_id)
        if r.status_code != 200 and r.json()["message"][0:22] == 'price is too accurate.':
            return limit_buy_sell(size, price[0:len(size) - 1], action, product_id)
        if r.status_code != 200 and r.json()["message"][0:18] == 'size is too small.':
            return False
        if r.status_code != 200 and r.json()["message"] == 'Insufficient funds':
            return False
        return ret(r)
    except:
        error_check(r, action)
        request_failed(action)

#if order-id == none all orders will be canceled
def cancel(order_id, account):
        r = requests.delete(account.api_url + 'orders/' + order_id, auth=account.api_authentification)
        if r.status_code != 200:
            error_check(r, "cancel")
            request_failed("cancel")
        return r.status_code

def get_order(id, account): #action is the rest of the url like accounts/id_number, this function is for the actions tha do not need query parameters
    r = None
    try:
        r = requests.get(account.api_url + "orders/" + id, auth=account.api_authentification)
        return ret(r)
    except:
        error_check(r, "get_order")
        request_failed("get_order")

def get(action, account): #action is the rest of the url like accounts/id_number, this function is for the actions tha do not need query parameters
    if action == None:
        return None
    r = None
    while True:
        try:
            r = requests.get(account.api_url + action, auth=account.api_authentification)
            if r.status_code == 200:
                break ;
            error_check(r, action)
        except:
            request_failed(action)
    return ret(r)

def orders(product_id, status, account):
    query = {
        'status': status,
        'product_id': product_id
    }
    while True:
        try:
            r = requests.get(account.api_url + 'orders', query, auth=account.api_authentification)
            if r.status_code == 200:
                break ;
            error_check(r, "orders")
        except:
            request_failed("orders")
    return ret(r)

#Either specify the order_is or the product_id, use None for the parameter you doon't want to specify
def fills(order_id, product_id, account):
    query = {
        'order_id' : order_id,
        'product_id': product_id
    }
    while True:
        try:
            r = requests.get(account.api_url + 'fills', query, auth=account.api_authentification)
            if r.status_code == 200:
                break ;
            if r.json()["message"][0:20] == 'not a valid order_id':
                return False
            error_check(r, "fills")
        except:
            request_failed("fills")
    return ret(r)

def historic_data(product_id, start, end, granularity, account):
    if product_id == None:
        return None
    query = {
        "start": start,
        "end" : end,
        "granularity": granularity
    }
    r = None
    while True:
        try:
            r = requests.get(account.api_url + 'products/' + product_id + '/candles', query, auth=account.api_authentification)
            if r.status_code == 200:
                break ;
            error_check(r, "historic_data")
        except:
            request_failed("historic_data")
    return ret(r)
