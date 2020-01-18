from pandas import DataFrame 
from pandas import Series
import ccxt
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime


portfolio = ["BTC/USDT","ETH/USDT","XRP/USDT","EOS/USDT","LTC/USDT"] 
p = [10,5,5,5,5]

binance = ccxt.binance()
fee = 0.005

#df1
df1 = ohlcv = binance.fetch_ohlcv(portfolio[0],timeframe='1m')
df = DataFrame(df1)
df.columns = ['time','open','high','low','close','volume']

df['nr4'] = (df['high']-df['low']).rolling(window=4).min() >= (df['high']-df['low'])
df['inside_day'] = (df['high'].shift(1) > df['high']) & (df['low'].shift(1) < df['low'])
df['signal'] = df['nr4'].shift(1) & df['inside_day'].shift(1)

df['ret'] = np.where(df['signal'], df['open']/df['close'].shift(-p[0]),1)
df['hpr'] = df['ret'].cumprod()
pro1 = df


#df2
df2 = ohlcv = binance.fetch_ohlcv(portfolio[1],timeframe='1m')
df = DataFrame(df2)
df.columns = ['time','open','high','low','close','volume']

df['nr4'] = (df['high']-df['low']).rolling(window=4).min() >= (df['high']-df['low'])
df['inside_day'] = (df['high'].shift(1) > df['high']) & (df['low'].shift(1) < df['low'])
df['signal'] = df['nr4'].shift(1) & df['inside_day'].shift(1)

df['ret'] = np.where(df['signal'], df['open']/df['close'].shift(-p[1]),1)
df['hpr'] = df['ret'].cumprod()
pro2 = df


#df3
df3 = ohlcv = binance.fetch_ohlcv(portfolio[2],timeframe='1m')
df = DataFrame(df3)
df.columns = ['time','open','high','low','close','volume']

df['nr4'] = (df['high']-df['low']).rolling(window=4).min() >= (df['high']-df['low'])
df['inside_day'] = (df['high'].shift(1) > df['high']) & (df['low'].shift(1) < df['low'])
df['signal'] = df['nr4'].shift(1) & df['inside_day'].shift(1)

df['ret'] = np.where(df['signal'], df['open']/df['close'].shift(-p[2]),1)
df['hpr'] = df['ret'].cumprod()
pro3 = df


#df4
df4 = ohlcv = binance.fetch_ohlcv(portfolio[3],timeframe='1m')
df = DataFrame(df4)
df.columns = ['time','open','high','low','close','volume']

df['nr4'] = (df['high']-df['low']).rolling(window=4).min() >= (df['high']-df['low'])
df['inside_day'] = (df['high'].shift(1) > df['high']) & (df['low'].shift(1) < df['low'])
df['signal'] = df['nr4'].shift(1) & df['inside_day'].shift(1)

df['ret'] = np.where(df['signal'], df['open']/df['close'].shift(-p[3]),1)
df['hpr'] = df['ret'].cumprod()
pro4 = df


#df5
df5 = ohlcv = binance.fetch_ohlcv(portfolio[4],timeframe='1m')
df = DataFrame(df5)
df.columns = ['time','open','high','low','close','volume']

df['nr4'] = (df['high']-df['low']).rolling(window=4).min() >= (df['high']-df['low'])
df['inside_day'] = (df['high'].shift(1) > df['high']) & (df['low'].shift(1) < df['low'])
df['signal'] = df['nr4'].shift(1) & df['inside_day'].shift(1)

df['ret'] = np.where(df['signal'], df['open']/df['close'].shift(-p[4]),1)
df['hpr'] = df['ret'].cumprod()
pro5 = df





ret_mean = (pro1['hpr']+pro2['hpr']+pro3['hpr']+pro4['hpr']+pro5['hpr'])/5
#ret_mean = (pro1['hpr']+pro3['hpr']+pro4['hpr']+pro5['hpr'])/4
hpr = list(ret_mean)

dd_mean = (ret_mean.cummax() - ret_mean) / ret_mean.cummax() * 100

profit = ret_mean - ret_mean.shift(1)
p_trade = profit[profit>0]
l_trade = profit[profit<0]

plt.plot(ret_mean)
plt.show()

ind = DataFrame(pro1['hpr'])
ind['2'] = pro2['hpr']
ind['3'] = pro3['hpr']
ind['4'] = pro4['hpr']
ind['5'] = pro5['hpr']
ind.columns = portfolio
ind.plot()
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

