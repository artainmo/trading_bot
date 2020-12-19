import sys

MARKET = None
START_DATE = None
END_DATE = None

VARIABLES = ["BUY_EMA_CROSSOVER_BUY", "BUY_EMA_CROSSOVER_TYPE", "BUY_RSI_BUY", "BUY_RSI_TYPE", "BUY_RSI_TRAILING", "BUY_RSI_L1_VALUE", "BUY_RSI_L1_AMPLIFIER", "BUY_RSI_L2_VALUE", "BUY_RSI_L2_AMPLIFIER", "PROTECTION_SAR_EMA_ACTIVE", "PROTECTION_SAR_EMA_TYPE", "SELL_EMA_CROSSOVER_SELL", "SELL_EMA_CROSSOVER_TYPE", "SELL_RSI_SELL", "SELL_RSI_TYPE", "SELL_RSI_L1_VALUE", "SELL_RSI_L1_AMPLIFIER", "SELL_RSI_L2_VALUE", "SELL_RSI_L2_AMPLIFIER", "SELL_SAR_SELL", "SELL_SAR_TYPE", "PROTECTION_SELL_EMA_SELL", "PROTECTION_SELL_EMA_TYPE", "PROTECTION_SELL_EMA_TRAILING", "PROTECTION_SELL_RSI_SELL", "PROTECTION_SELL_RSI_TYPE", "PROTECTION_SELL_RSI_TRAILING"]

BUY_EMA_CROSSOVER = {"buy": None, "type":None}
BUY_RSI = {
"buy":None,
"type":None,
"trailing":None,
"type":None,
"level1":{"value":None, "amplifier":None},
"level2":{"value":None, "amplifier":None}
}
PROTECTION_SAR_EMA = {"active":None, "type":None}
SELL_EMA_CROSSOVER = {"sell":None, "type":None}
SELL_RSI = {
"sell":None,
"type":None,
"level1":{"value":None, "amplifier":None},
"level2":{"value":None, "amplifier":None}
}
SELL_SAR = {"sell":None, "type":None}
PROTECTION_SELL_EMA = {"sell":None, "type":None, "trailing":None}
PROTECTION_SELL_RSI = {"sell":None, "type":None, "trailing":None}

# Trade bot on server 
# -Finish genetic program, see genetic.py
# -Launch genetic program
# Learn how to use google cloud or digitalocean

def get_variable(name):
    if name == "MARKET":
        return [6, 8,-1], ["BTC-EUR", "ETH-EUR", "LTC-EUR", "XRP-EUR"]
    elif name == "START_DATE":
        return [7,12,-1], ["NEUTRALTREND", "DOWNTREND", "UPTREND"]
    elif name == "BUY_EMA_CROSSOVER_BUY":
        return [8,16,-1], ["No", "instant"]
    elif name == "BUY_EMA_CROSSOVER_TYPE":
        return [9,0,-1], ["_min", "_quarter", "_hour", "_day"]
    elif name == "BUY_RSI_BUY":
        return [10,6,-1], ["No", "trailing"]
    elif name == "BUY_RSI_TYPE":
        return [11,0,-1], ["_min", "_quarter", "_hour", "_day"]
    elif name == "BUY_RSI_TRAILING":
        return [12,0,-1], ["_0.01", "_0.02", "_0.03", "_0.04", "_0.05", "_0.06", "_0.07", "_0.08", "_0.09", "_0.1"]
    elif name == "BUY_RSI_L1_VALUE":
        return [13,0,3], ["_35", "_34", "_33", "_32", "_31", "_30", "_29", "_28", "_27", "_26", "_25", "_24", "_23", "_22", "_21", "_20"]
    elif name == "BUY_RSI_L1_AMPLIFIER":
        return [13,6,-1], ["1", "1.1", "1.2", "1.3", "1.4", "1.5"]
    elif name == "BUY_RSI_L2_VALUE":
        return [14,0,3], ["_20", "_19", "_18", "_17", "_16", "_15", "_14", "_13", "_12", "_11", "_10"]
    elif name == "BUY_RSI_L2_AMPLIFIER":
        return [14,6,-1], ["1.5", "1.6", "1.7", "1.8", "1.8", "1.9", "2"]
    elif name == "PROTECTION_SAR_EMA_ACTIVE":
        return [15,21,-1], ["Yes", "No"]
    elif name == "PROTECTION_SAR_EMA_TYPE":
        return [16,0,-1], ["_min", "_quarter", "_hour", "_day"]
    elif name == "SELL_EMA_CROSSOVER_SELL":
        return [17,16,-1], ["No", "instant"]
    elif name == "SELL_EMA_CROSSOVER_TYPE":
        return [18,0,-1], ["_min", "_quarter", "_hour", "_day"]
    elif name == "SELL_RSI_SELL":
        return [19,6,-1], ["No", "trailing"]
    elif name == "SELL_RSI_TYPE":
        return [20,0,-1], ["_min", "_quarter", "_hour", "_day"]
    elif name == "SELL_RSI_L1_VALUE":
        return [21,0,3], ["_65", "_66", "_67", "_68", "_69", "_70", "_71", "_72", "_73", "_74", "_75", "_76", "_77", "_78", "_79", "_80"]
    elif name == "SELL_RSI_L1_AMPLIFIER":
        return [21,6,-1], ["1", "1.1", "1.2", "1.3", "1.4", "1.5"]
    elif name == "SELL_RSI_L2_VALUE":
        return [22,0,3], ["_80", "_81", "_82", "_83", "_84", "_85", "_86", "_87", "_88", "_89", "_90"]
    elif name == "SELL_RSI_L2_AMPLIFIER":
        return [22,6,-1], ["1.5", "1.6", "1.7", "1.8", "1.8", "1.9", "2"]
    elif name == "SELL_SAR_SELL":
        return [23,6,-1], ["instant", "No"]
    elif name == "SELL_SAR_TYPE":
        return [24,0,-1], ["_min", "_quarter", "_hour", "_day"]
    elif name == "PROTECTION_SELL_EMA_SELL":
        return [25,22,-1], ["No", "trailing"]
    elif name == "PROTECTION_SELL_EMA_TYPE":
        return [26,0,-1], ["_min", "_quarter", "_hour", "_day"]
    elif name == "PROTECTION_SELL_EMA_TRAILING":
        return [27,0,-1], ["_0.01", "_0.02", "_0.03", "_0.04", "_0.05", "_0.06", "_0.07", "_0.08", "_0.09", "_0.1"]
    elif name == "PROTECTION_SELL_RSI_SELL":
        return [28,22,-1], ["No", "trailing"]
    elif name == "PROTECTION_SELL_RSI_TYPE":
        return [29,0,-1], ["_min", "_quarter", "_hour", "_day"]
    elif name == "PROTECTION_SELL_RSI_TRAILING":
        return [30,0,-1], ["_0.01", "_0.02", "_0.03", "_0.04", "_0.05", "_0.06", "_0.07", "_0.08", "_0.09", "_0.1"]
    else:
        print("ERROR")

def new_file(coordinates, replace):
    i = 0
    new_text = ""
    with open("../users_data/user.txt", "r") as fd:
        lines = fd.readlines()
    while i <= coordinates[0]:
        new_text += lines[i]
        i += 1
    new_text += lines[i][0:coordinates[1]] + replace + lines[i][coordinates[2]:-1] + "\n"
    i += 1
    while i < len(lines):
        new_text += lines[i]
        i += 1
    with open("../users_data/user.txt", "w") as fd:
         fd.write(new_text)


if __name__ == "__main__":
    coordinates, trends = get_variable("START_DATE")
    copy_variable_neutral_file()
    for trend in trends
        new_file(coordinates, trend)
        for variable in VARIABLES:
            coordinates, vars = get_variable(variable)
            i = 0
            while i < len(vars):
                save_old_file()
                new_file(coordinates, vars[i])
                initial = get_current_result_total_eu()
                execute_program_for_each_coin_and_sum_results()
                new = get_current_result_total_eu()
                if new < initial:
                    set_back_old_file()
                    i == len(vars)
        print_result_trend_to_other_folder()
