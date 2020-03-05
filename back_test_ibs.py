from pandas import DataFrame 
from pandas import Series
import ccxt
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime


portfolio = ["BTC/USDT","ETH/USDT","XRP/USDT","BNB/USDT","BCH/USDT"] 
th_long = 0.5
th_short = 0.5

binance = ccxt.binance()
fee = 0.00
time = '30m'

#df1
df1 = ohlcv = binance.fetch_ohlcv(portfolio[0],timeframe=time)
df = DataFrame(df1)
df.columns = ['time','open','high','low','close','volume']

df['ibs'] = (df['close']-df['low'])/(df['high']-df['low'])

df['ret_long'] = np.where((df['ibs'].shift(1) < th_long) ,df['close']/df['open'] - fee, 1)
df['ret_short'] = np.where((df['ibs'].shift(1) > th_short) ,df['open']/df['close'] - fee, 1)

df['ret'] = df['ret_long']*df['ret_short']

df['hpr'] = df['ret'].cumprod()
df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100
pro1 = df

#df2
df2 = ohlcv = binance.fetch_ohlcv(portfolio[1],timeframe=time)
df = DataFrame(df2)
df.columns = ['time','open','high','low','close','volume']

df['ibs'] = (df['close']-df['low'])/(df['high']-df['low'])

df['ret_long'] = np.where((df['ibs'].shift(1) < th_long) ,df['close']/df['open'] - fee, 1)
df['ret_short'] = np.where((df['ibs'].shift(1) > th_short) ,df['open']/df['close'] - fee, 1)

df['ret'] = df['ret_long']*df['ret_short']

df['hpr'] = df['ret'].cumprod()
df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100
pro2 = df

#df3
df3 = ohlcv = binance.fetch_ohlcv(portfolio[2],timeframe=time)
df = DataFrame(df3)
df.columns = ['time','open','high','low','close','volume']

df['ibs'] = (df['close']-df['low'])/(df['high']-df['low'])

df['ret_long'] = np.where((df['ibs'].shift(1) < th_long) ,df['close']/df['open'] - fee, 1)
df['ret_short'] = np.where((df['ibs'].shift(1) > th_short) ,df['open']/df['close'] - fee, 1)

df['ret'] = df['ret_long']*df['ret_short']

df['hpr'] = df['ret'].cumprod()
df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100
pro3 = df

#df4
df1 = ohlcv = binance.fetch_ohlcv(portfolio[3],timeframe=time)
df = DataFrame(df4)
df.columns = ['time','open','high','low','close','volume']

df['ibs'] = (df['close']-df['low'])/(df['high']-df['low'])

df['ret_long'] = np.where((df['ibs'].shift(1) < th_long) ,df['close']/df['open'] - fee, 1)
df['ret_short'] = np.where((df['ibs'].shift(1) > th_short) ,df['open']/df['close'] - fee, 1)

df['ret'] = df['ret_long']*df['ret_short']

df['hpr'] = df['ret'].cumprod()
df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100
pro4 = df

#df5
df5 = ohlcv = binance.fetch_ohlcv(portfolio[4],timeframe=time)
df = DataFrame(df5)
df.columns = ['time','open','high','low','close','volume']

df['ibs'] = (df['close']-df['low'])/(df['high']-df['low'])

df['ret_long'] = np.where((df['ibs'].shift(1) < th_long) ,df['close']/df['open'] - fee, 1)
df['ret_short'] = np.where((df['ibs'].shift(1) > th_short) ,df['open']/df['close'] - fee, 1)

df['ret'] = df['ret_long']*df['ret_short']

df['hpr'] = df['ret'].cumprod()
df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100
pro5 = df


ret1 = np.cumprod(pro1['ret'])
ret2 = np.cumprod(pro2['ret'])
ret3 = np.cumprod(pro3['ret'])
ret4 = np.cumprod(pro4['ret'])
ret5 = np.cumprod(pro5['ret'])

ret_mean = (ret1+ret2+ret3+ret4+ret5)/5 

hpr = list(ret_mean)

dd_mean = (ret_mean.cummax() - ret_mean) / ret_mean.cummax() * 100

profit = ret_mean - ret_mean.shift(1)
p_trade = profit[profit>0]
l_trade = profit[profit<0]

plt.plot(ret_mean)
plt.show()


print("MDD: ", dd_mean.max())
print("HPR: ", (hpr[-2]-1)*100)
print("Trading Days", len(ret_mean))
print("Trades", len(p_trade)+len(l_trade))
print("Trades/Days", (len(p_trade)+len(l_trade))/len(ret_mean))
print("Profit Trades", len(p_trade))
print("Loss Trades", len(l_trade))
print("Winning Rate", len(p_trade)/(len(p_trade)+len(l_trade)))
print("Average profit per trade", p_trade.mean())
print("Average loss per trade", l_trade.mean())
print("P/L Rate", p_trade.mean()/l_trade.mean())

ind = DataFrame(pro1['hpr'])
ind['2'] = pro2['hpr']
ind['3'] = pro3['hpr']
ind['4'] = pro4['hpr']
ind['5'] = pro5['hpr']
ind.columns = portfolio
ind.plot()
plt.show()
