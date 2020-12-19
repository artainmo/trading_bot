#RSI under 30 and above 70 can be a buy signal with trailing stop loss to buy and sell / sell stop loss 2 times closer than constant sell stop loss
#RSI under 15 or above 85 can be signal with two times even more stop loss than the 30, 70
#Use the quarter based rsi

def get_rsi(candle):
    avgup = candle[9]
    avgdown = candle[10]
    RS = avgup/avgdown
    RSI = 100 - (100.00000 / (1 + RS))
    return RSI


def set_rsi(candle):
    candle.append(get_rsi(candle))
    return candle
