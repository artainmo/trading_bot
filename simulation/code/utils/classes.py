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
            return orders[0]

        def market_sell(self, account, size):
            current_value = self.last_price()
            order, account = self.new_order(current_value * size, current_value, "Done", self.last_update("_min"), self.last_update("_min"), size, "market", "sell", account)
            self.document_what_happened(size * current_value, current_value, order, account)
            return account


        def market_buy(self, account, eu_price):
            self.orders, account = self.cancel_orders("buy", account)
            if account.euros["available"] < 10:
                return account
            eu_price = account.euros["available"] * 0.9925
            current_value = self.last_price()
            size = eu_price / float(current_value)
            order, account = self.new_order(current_value * size, current_value, "Done", self.last_update("_min"), self.last_update("_min"), size, "market", "buy", account)
            self.document_what_happened(eu_price, current_value, order, account)
            return account


        def limit_sell(self, account):
            order = self.get_side_order("sell")
            if order != None and float(self.sell["proposed_price"]) > float(order["value"]):
                self.orders, account = self.cancel_orders("sell", account)
                price = float(self.sell["proposed_price"])
            elif order == None:
                price = float(self.sell["proposed_price"])
            else:
                return account
            size = float(account.coins[self.market_name]["available"])
            if size == 0:
                return False
            if price > self.last_price():
                return False
            self.orders, account = self.new_order(price * size, price, "open", None, self.last_update("_min"), size, "limit", "sell", account)
            return account

        def limit_buy(self, account, eu_price):
            order = self.get_side_order("buy")
            if order != None and float(self.buy["proposed_price"]) < float(order["value"]):
                self.orders, account = self.cancel_orders("buy", account)
                price = float(self.buy["proposed_price"])
            elif order == None:
                price = float(self.buy["proposed_price"])
            else:
                return account
            eu_price = account.euros["available"] * 0.9925
            if eu_price < 10:
                return account
            if price < self.last_price():
                return account
            size = eu_price / price
            self.orders, account = self.new_order(price * size, price, "open", None, self.last_update("_min"), size, "limit", "buy", account)
            return account

        def new_order(self, price, value, status, done_at, created_at, size, type, side, account):
            order = {
            "market_name": self.market_name,
            "price": price,
            "value": value,
            "status": status,
            "done_at": done_at,
            "created_at": created_at,
            "size": size,
            "type": type,
            "side": side
            }
            if order["type"] == "limit" and order["done_at"] == None:
                self.orders.append(order)
            if order["side"] == "sell" and order["type"] == "market":
                account.euros["available"] += (order["price"] * 0.995)
                account.euros["balance"] += (order["price"] * 0.995)
                account.coins[self.market_name]["available"] -= order["size"]
                account.coins[self.market_name]["balance"] -= order["size"]
                return order, account
            if order["side"] == "sell" and order["type"] == "limit":
                account.coins[self.market_name]["available"] -= order["size"]
            if order["side"] == "buy" and order["type"] == "market":
                account.euros["available"] -= order["price"]
                account.euros["balance"] -= order["price"]
                account.coins[self.market_name]["available"] += (order["size"] * 0.995)
                account.coins[self.market_name]["balance"] += (order["size"] * 0.995)
                return order, account
            if order["side"] == "buy" and order["type"] == "limit":
                account.euros["available"] -= order["price"]
            return self.orders, account

        def finished_limit_order(self, order, account):
            if order["side"] == "buy":
                account.euros["balance"] -= order["price"]
                account.coins[self.market_name]["available"] += (float(order["size"]) * 0.995)
                account.coins[self.market_name]["balance"] += (float(order["size"]) * 0.995)
                self.document_what_happened(order["price"], order["value"], order, account)
                self.orders = self.cancel_finished_limit_order("buy")
            else:
                account.euros["available"] += (order["price"] * 0.995)
                account.euros["balance"] += (order["price"] * 0.995)
                account.coins[self.market_name]["balance"] -= float(order["size"])
                self.document_what_happened(order["price"], order["value"], order, account)
                self.orders = self.cancel_finished_limit_order("sell")
            return self.orders, account

        def cancel_finished_limit_order(self, side):
            orders = []
            for order in self.orders:
                if order != None and order["side"] != side:
                    orders.append(order)
            self.orders = orders
            return self.orders

        def cancel_orders(self, side, account):
            orders = []
            eu = 0
            size = 0
            for order in self.orders:
                if order != None and order["side"] != side:
                    orders.append(order)
                else:
                    eu += order["price"]
                    size += order["size"]
            self.orders = orders
            if side == "buy":
                account.euros["available"] += eu
                account.euros["balance"] += eu
            if side == "sell":
                account.coins[self.market_name]["available"] += size
            return self.orders, account


        def last_update(self, file_extension):
            with open("../coins_data/" + self.market_name + file_extension + ".txt", "a+") as fd:
                candle = get_last_line_in_dict(fd)
            try:
                return candle["iso_time"]
            except:
                return None

        def last_price(self):
            with open("../coins_data/" + self.market_name + "_min.txt", "r") as fd:
                candle = get_last_line_in_dict(fd)
            return float(candle["close"])

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
    def __init__(self):
        self.euros = 0
        self.coins = {}


    def write_to_transactions_file(self, data):
        if data["ema"] == "BUY" or data["ema"] == "SELL":
            signal = "ema"
        elif data["sar"] == "SELL":
            signal = "sar"
        else:
            signal = "limit_order"
        with open("../feedback/transactions.txt", "a+") as fd:
            fd.write(data["side"] + " " + str(data["market_name"]) + ":\n")
            fd.write("Signal: " + signal + "\n")
            fd.write("Price in eu: " + str(data["price"])+ "\n")
            fd.write("Value coin: " + str(data["value"])+ "\n")
            fd.write("Status: " + str(data["status"])+ "\n")
            fd.write("Created at (server time): " + str(data["created_at"])+ "\n")
            fd.write("Done at (server time): " + str(data["done_at"])+ "\n")
            fd.write("Type: " + str(data["type"])+ "\n")

    def bought_coin_value(self, product_id):
        with open("../feedback/transactions.txt", "r") as fd:
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
        with open("../feedback/transactions.txt", "r") as fd:
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
        with open("../feedback/transactions.txt", "r") as fd:
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
