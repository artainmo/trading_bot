from utils.classes import *

def add_1min(time):
    ret = []
    difference = 0
    if int(time.minute) < 59:
        ret = times(time.begin + "T" + time.hour
        + ':' + time.set_frontzero(time.addition(time.minute, 1)) + time.secondsend)
    elif int(time.hour) < 23:
        ret = times(time.begin + "T" + time.set_frontzero(time.addition(time.hour, 1))
        + ':' + "00" + time.secondsend)
    elif int(time.day) < int(time.get_month_lastday()):
        ret = times(time.year + "-" + time.month + "-" + time.set_frontzero(time.addition(time.day, 1))
         + "T" + "00" + ':' + "00" + time.secondsend)
    elif int(time.month) < 12:
        ret = times(time.year + "-" + time.set_frontzero(time.addition(time.month, 1))
        + "-" + "01" + "T" + "00" + ':' + "00" + time.secondsend)
    elif int(time.month) == 12:
        ret = times(time.addition(time.year, 1) + "-" + "01"
        + "-" + "01" + "T" + "00"
        + ':' + "00" + time.secondsend)
    return ret

def increase_1quarter(time):
    ret = []
    difference = str((int(time.minute) + 15 - 60))
    if int(time.minute) < 45:
        ret = times(time.begin + "T" + time.hour
        + ':' + time.set_frontzero(time.addition(time.minute, 15)) + time.secondsend)
    elif int(time.hour) < 23:
        ret = times(time.begin + "T" + time.set_frontzero(time.addition(time.hour, 1))
        + ':' + time.set_frontzero(difference) + time.secondsend)
    elif int(time.day) < int(time.get_month_lastday()):
        ret = times(time.year + "-" + time.month + "-" + time.set_frontzero(time.addition(time.day, 1))
         + "T" + "00" + ':' + time.set_frontzero(difference) + time.secondsend)
    elif int(time.month) < 12:
        ret = times(time.year + "-" + time.set_frontzero(time.addition(time.month, 1))
        + "-" + "01" + "T" + "00" + ':' + time.set_frontzero(difference) + time.secondsend)
    elif int(time.month) == 12:
        ret = times(time.addition(time.year, 1) + "-" + "01"
        + "-" + "01" + "T" + "00"
        + ':' + time.set_frontzero(difference) + time.secondsend)
    return ret

def increase_1hour(time):
    ret = []
    if int(time.hour) < 23:
        ret = times(time.begin + "T" + time.set_frontzero(time.addition(time.hour, 1))
        + ':' + time.minute + time.secondsend)
    elif int(time.day) < int(time.get_month_lastday()):
        ret = times(time.year + "-" + time.month + "-" + time.set_frontzero(time.addition(time.day, 1))
         + "T" + "00" + ':' + time.minute + time.secondsend)
    elif int(time.month) < 12:
        ret = times(time.year + "-" + time.set_frontzero(time.addition(time.month, 1))
        + "-" + "01" + "T" + "00" + ':' + time.minute + time.secondsend)
    elif int(time.month) == 12:
        ret = times(time.addition(time.year, 1) + "-" + "01"
        + "-" + "01" + "T" + "00"
        + ':' + time.minute + time.secondsend)
    return ret


def increase_1day(time):
    ret = []
    if int(time.day) < int(time.get_month_lastday()):
        ret = times(time.year + "-" + time.month + "-" + time.set_frontzero(time.addition(time.day, 1))
         + "T" + time.hour + ':' + time.minute + time.secondsend)
    elif int(time.month) < 12:
        ret = times(time.year + "-" + time.set_frontzero(time.addition(time.month, 1))
        + "-" + "01" + "T" + time.hour + ':' + time.minute + time.secondsend)
    elif int(time.month) == 12:
        ret = times(time.addition(time.year, 1) + "-" + "01"
        + "-" + "01" + "T" + time.hour
        + ':' + time.minute + time.secondsend)
    return ret


def addminutes(time, minutes):
    i = 0
    while i != minutes:
        time = add_1min(time)
        i += 1
    return time


def increase_5_hours(time):
    return addminutes(time, 60 * 5)
