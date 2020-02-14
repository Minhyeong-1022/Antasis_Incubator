import ccxt
import time
import numpy as np
import datetime


portfolio = ["ETH/USDT"] 
ideal = ["ETH/BTC"] 
exchange = ccxt.binance()
fee = 0.005

while True :
    try :
        now = datetime.datetime.utcnow()
        current = exchange.fetch_ticker(portfolio[0])['close']
        current_id = exchange.fetch_ticker(ideal[0])['close']
        current_st = exchange.fetch_ticker("BTC/USDT")['close']

        ideal_price = current_id*current_st
        ratio = round((current-ideal_price)/ideal_price,4)
        profit = ratio-fee

        file = open('data.txt', 'a')
        file.write(str(now))
        file.write(',')
        file.write(str(current))
        file.write(',')
        file.write(str(ideal_price))
        file.write(',')
        file.write(str(ratio))
        file.write(',')
        file.write(str(profit))
        file.write('\n')
        file.close()

        time.sleep(0.5)
    
    except :
        time.sleep(0.5)
