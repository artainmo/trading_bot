import json
import data.api.api_actions as api
import subprocess
from utils.file_handler import *

class times:
    def __init__(self, time):
        if time != None:
            self.all = time
            self.end = time[10:24]
            self.begin = time[0:10]
            self.year = time[0:4]
            self.month = time[5:7]
            self.day = time[8:10]
            self.hour = time[11:13]
            self.minute = time[14:16]
            self.seconds = time[17:19]
            self.finish = time[19:100]
            self.secondsend = time[16:100]


    def get_time(self, account):
        time = api.get("time", account)
        time = time["iso"]
        self.all = time
        self.end = time[10:24]
        self.begin = time[0:10]
        self.year = time[0:4]
        self.month = time[5:7]
        self.day = time[8:10]
        self.hour = time[11:13]
        self.minute = time[14:16]
        self.seconds = time[17:19]
        self.finish = time[19:100]
        self.secondsend = time[16:100]

    def earlier_than(self, time):
        if int(self.year) < int(time.year):
            return True
        if int(self.year) == int(time.year) and int(self.month) < int(time.month):
            return True
        if int(self.year) == int(time.year) and int(self.month) == int(time.month) and int(self.day) < int(time.day):
            return True
        if int(self.year) == int(time.year) and int(self.month) == int(time.month) and int(self.day) == int(time.day) and int(self.hour) < int(time.hour):
            return True
        if int(self.year) == int(time.year) and int(self.month) == int(time.month) and int(self.day) == int(time.day) and int(self.hour) == int(time.hour) and int(self.minute) <= int(time.minute):
            return True
        return False

    def get_absolute(self):
        self.all = self.year + "-" + self.month + "-" + self.day + "T" + self.hour
        + ':' + self.minute + ":" + self.seconds + self.finish
        self.end = self.all[10:24]
        self.begin = self.all[0:10]
        self.finish = self.all[19:100]
        self.secondsend = self.all[16:100]


    def set_frontzero(self, number):
            if len(str(number)) == 1:
                return "0" + number
            else:
                return number

    def substract(self, number, minus):
         return str(int(number) - minus)

    def addition(self, number, plus):
         return str(int(number) + plus)

    def get_month_lastday(self):
        months_dict = {
            '01': 31,
            '03': 31,
            '04': 30,
            '05': 31,
            '06': 30,
            '07': 31,
            '08': 31,
            '09': 30,
            '10': 31,
            '11': 30,
            '12': 31
        }
        if self.month != "02":
            return months_dict[self.month]
        else:
            if int(self.year) % 4 == 0:
                return 29
            return 28

    def get_prior_month_lastday(self):
        prior = int(self.month) - 1
        if prior == 0:
            prior = 12
        if len(str(prior)) == 1:
            prior = "0" + str(prior)
        return self.months_dict[str(prior)]


class coins_list:
        def __init__(self, market_name, start_date):
            self.market_name = market_name
            self.start_date = start_date
            self.current_value = 0
            self.buy = {"type": None, "amplifier": None, "proposed_price": None}
            self.sell = {"type": None, "amplifier": None}
            self.orders = []
            self.opp = {
                "market_name": market_name,
                "pattern": None,
                "ema": None,
                "rsi": {"proposed_buy_price": None, "buy_signal_amplifier": None, "sell_signal_amplifier": 1},
                "sar": None,
                "protection_sell": {"instant_sell": None, "sell_signal_amplifier": 1, "proposed_price": None},
                "price": None,
                "value": None,
                "status": None,
                "created_at" : None,
                "done_at" : None,
                "type" : None,
                "side" : None
            }

        def get_current_value(self, account):
            self.current_value = float(get("products/" + coin.market_name + "/ticker")["price"], account)
            return self.current_value

        def document_what_happened(self, price, value, order, account):
            if float(price) > 0:
                self.opp["price"] = str(price)
                self.opp["value"] = str(value)
                self.opp["status"] = str(order["status"])
                self.opp["created_at"] = times(str(order["created_at"])).all
                if order["type"] == "limit":
                    self.opp["done_at"] = self.last_update("_min")
                else:
                    self.opp["done_at"] = order["done_at"]
                self.opp["type"] = str(order["type"])
                self.opp["side"] = str(order["side"])
                account.write_to_transactions_file(self.opp)

        def delete_existing_limit_orders(self, side, account):
            for order in self.orders:
                if order["side"] == side:
                    api.cancel(order["id"], account)

        def get_side_order(self, side):
            orders = []
            for order in self.orders:
                if order != None and order["side"] == side:
                    orders.append(order)
            if orders == []:
                return None
            return orders

        def market_sell(self, account, size):
            while True:
                current_value = self.get_current_value(account)
                order = api.market_buy_sell(size, "sell", self.market_name, account)
                if isinstance(order, bool) and order == False:
                    return False
                order = api.get_order(order["id"])
                if order["size"] == order["filled_size"]:
                    self.document_what_happened(float(size) * float(current_value["ask"]), current_value["ask"], order, account)
                    return True
                size = float(size) - float(order["filled_size"])
                api.cancel(order["id"], account)


        def market_buy(self, account, eu_price):
            self.delete_existing_limit_orders("buy", account)
            eu_price += account.euros["available"] - account.available("EUR-")["available"] #Add new euros from deleted orders
            if eu_price < 10:
                return 0
            eu_price *= 0.9925
            while True:
                current_value = self.get_current_value(account)
                size = str(eu_price / float(current_value["bid"]))
                order = api.market_buy_sell(size, "buy", self.market_name, account)
                if isinstance(order, bool) and order == False:
                    return eu_price
                order = api.get_order(order["id"], account)
                if order["size"] == order["filled_size"]:
                    self.document_what_happened(eu_price, current_value["bid"], order, account)
                    return 0
                eu_price = float(eu_price) - (float(order["filled_size"]) * float(current_value["bid"]))
                api.cancel(order["id"], account)


        def limit_sell(self, account):
            order = self.get_side_order("sell")
            if order != None and float(self.sell["proposed_price"]) > float(order["value"]):
                api.cancel(order["id"], account)
                price = float(self.sell["proposed_price"])
            elif order == None:
                price = float(self.sell["proposed_price"])
            else:
                return False
            size = account.available(self.market_name)["available"]
            if size == 0:
                return False
            if price > self.get_current_value(account):
                return False
            order = api.limit_buy_sell(size, price, "sell", self.market_name, account)
            if order == False:
                return False
            return True

        def limit_buy(self, account, eu_price):
            order = self.get_side_order("buy")
            if order != None and float(self.buy["proposed_price"]) < float(order["value"]):
                api.cancel(order["id"], account)
                eu_price += account.euros["available"] - account.available("EUR-")["available"] #Add new euros from deleted orders
                price = float(self.buy["proposed_price"])
            elif order == None:
                price = float(self.buy["proposed_price"])
            else:
                eu_price
            if eu_price < 10:
                return eu_price
            if price < self.get_current_value(account):
                return eu_price
            eu_price *= 0.9925
            size = str(eu_price / price)
            order = api.limit_buy_sell(size, price, "buy", self.market_name, account)
            if isinstance(order, bool) and order == False:
                return eu_price
            return 0


        def last_update(self, file_extension):
            with open("../coins_data/" + self.market_name + file_extension + ".txt", "r") as fd:
                candle = get_last_line_in_dict(fd)
            return candle["iso_time"]

        def last_line(self, file_extension):
            with open("../coins_data/" + self.market_name + file_extension + ".txt", "r") as fd:
                candle = get_last_line_in_dict(fd)
            return candle

        def last_lines_in_dict(self, number, file_extension):
            ret = []
            with open("../coins_data/" + self.market_name + file_extension + ".txt", "r") as fd:
                ret = []
                try:
                    fd.seek(-1, 2) #goto byte before EOF
                except:
                    return ""
                if go_one_line_back(fd) == "ERROR":
                    return ""
                line = line_to_dict(fd.readline())
                ret.append(line)
                for i in range(0,number - 1):
                    go_one_line_back(fd)
                    if go_one_line_back(fd) == "ERROR":
                        return ""
                    line = line_to_dict(fd.readline())
                    ret.append(line)
                return ret


class accounts:
    def __init__(self, name, authentification, api_url):
        self.name = name
        self.api_authentification = authentification
        self.api_url = api_url
        self.euros = 0
        self.coins = {}

    def available(self, market_name):
        i = 0
        l = 0
        if market_name == None:
            return None
        accounts = api.get("accounts", self)
        while i < len(market_name) and market_name[i] != '-':
            i += 1
        while accounts[l]["currency"] != market_name[0:i]:
            l += 1
        account_id = accounts[l]["id"]
        quantity = api.get("accounts/" + account_id, self)
        dict ={
        "available": float(quantity["available"]),
        "balance": float(quantity["balance"])
        }
        return dict

    def write_to_transactions_file(self, data):
        if data["ema"] == "BUY" or data["ema"] == "SELL":
            signal = "ema"
        elif data["sar"] == "SELL":
            signal = "sar"
        else:
            signal = "limit_order"
        with open("../feedback/transactions_" + self.name + ".txt", "a+") as fd:
            fd.write(data["side"] + " " + str(data["market_name"]) + ":\n")
            fd.write("Signal: " + signal + "\n")
            fd.write("Price in eu: " + str(data["price"])+ "\n")
            fd.write("Value coin: " + str(data["value"])+ "\n")
            fd.write("Status: " + str(data["status"])+ "\n")
            fd.write("Created at (server time): " + str(data["created_at"])+ "\n")
            fd.write("Done at (server time): " + str(data["done_at"])+ "\n")
            fd.write("Type: " + str(data["type"])+ "\n")

    def bought_coin_value(self, product_id):
        with open("../feedback/transactions_" + self.name + ".txt", "r") as fd:
            try:
                fd.seek(-1, 2) #goto byte before EOF
            except:
                return None
            go_one_line_back(fd)
            line = fd.readline()
            while line.find(product_id) == -1:
                go_one_line_back(fd)
                go_one_line_back(fd)
                line = fd.readline()
            while line.find("Value coin:") == -1:
                line = fd.readline()
            return line[12:-1]

    def bought_coin_timing(self, product_id):
        with open("../feedback/transactions_" + self.name + ".txt", "r") as fd:
            fd.seek(-1, 2) #goto byte before EOF
            go_one_line_back(fd)
            line = fd.readline()
            while line.find(product_id) == -1:
                go_one_line_back(fd)
                go_one_line_back(fd)
                line = fd.readline()
            while line.find("Done at") == -1:
                line = fd.readline()
            return line[23:-1]

    def bought_coin_signal(self, product_id):
        with open("../feedback/transactions_" + self.name + ".txt", "r") as fd:
            fd.seek(-1, 2) #goto byte before EOF
            go_one_line_back(fd)
            line = fd.readline()
            while line.find(product_id) == -1:
                go_one_line_back(fd)
                go_one_line_back(fd)
                line = fd.readline()
            while line.find("Signal: ") == -1:
                line = fd.readline()
            return line[8:-1]
