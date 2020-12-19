# bucket time, low, high, open, close, volume, iso time, ema12, ema26, sar, rsi
def line_to_dict(line):
    dict = {
        "bucket_time" : 0,
        "low" : 0,
        "high" : 0,
        "open" : 0,
        "close" : 0,
        "volume" : 0,
        "iso_time" : 0,
        "ema12" : 0,
        "ema26" : 0,
    }
    if line == "":
        return ""
    line = line.strip("\n").split(',')
    dict["bucket_time"] = line[0]
    dict["low"] = line[1]
    dict["high"] = line[2]
    dict["open"] = line[3]
    dict["close"] = line[4]
    dict["volume"] = line[5]
    dict["iso_time"] = line[6]
    dict["ema12"] = line[7]
    dict["ema26"] = line[8]
    dict["ema_up"] = line[9]
    dict["ema_down"] = line[10]
    dict["rsi"] = line[11]
    dict["sar"] = line[12]
    dict["AF_sar"] = line[13]
    dict["EP"] = line[14]
    return dict

def readlastline(fd):
    try:
        fd.seek(-2, 2)              # Jump to the second last byte.
        while fd.read(1) != "\n":  # Until EOL is found...
            fd.seek(-2, 1)
        return fd.readlines(1)[0]
    except:
        return fd.readline()

def get_last_line_in_dict(fd):
    last_line = readlastline(fd)
    if last_line == "":
        return ""
    return line_to_dict(last_line)

def go_one_line_back(fd):
    try:
        fd.seek(-2, 1)
        while fd.read(1) != "\n":
            fd.seek(-2, 1)
    except:
        return "ERROR"
