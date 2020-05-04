from pandas import DataFrame 
from pandas import Series
import ccxt
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

portfolio = ["BTC/USDT","ETH/USDT","XRP/USDT","BNB/USDT","EOS/USDT"]
gap = 5

binance = ccxt.binance()
fee = 0.005

merge_df = {}
merge_outret = {}
for i in range(len(portfolio)):
    ohlcv = binance.fetch_ohlcv(portfolio[i],timeframe='1d')
    df = DataFrame(ohlcv)
    df.columns = ['time','open','high','low','close','volume']

    ac_1 = (df['close'].shift(1)-df['open'].shift(gap))/df['open'].shift(gap)
    ac_2 = (df['close']-df['open'])/df['open']

    df['ac_ratio'] = (ac_2/ac_1).shift(1)
    df['nag'] = ac_2 > 0
    df['ret'] = np.where(df['nag'] & (df['ac_ratio'] > 3), df['close']/df['open'] - fee, 1)
    df['hpr'] = df['ret'].cumprod()

    ret = DataFrame(df['hpr'])
    ret['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100
    merge_df[i] = ret

    df['outret'] = (df['close']/df['close'].shift(1)).cumprod()
    outret = DataFrame(df['outret'])
    outret['dd'] = (df['outret'].cummax() - df['outret']) / df['outret'].cummax() * 100
    merge_outret[i] = outret

ret1= merge_df[0]['hpr']
ret2= merge_df[1]['hpr']
ret3= merge_df[2]['hpr']
ret4= merge_df[3]['hpr']
ret5= merge_df[4]['hpr']

outret1 = merge_outret[0]['outret']
outret2 = merge_outret[1]['outret']
outret3 = merge_outret[2]['outret']
outret4 = merge_outret[3]['outret']
outret5 = merge_outret[4]['outret']

ret_mean = (ret1+ret2+ret3+ret4+ret5)/2
dd_mean = (ret_mean.cummax() - ret_mean) / ret_mean.cummax() * 100
hpr = list(ret_mean)

outret_mean = (outret1+outret2+outret3+outret4+outret5)/5
outdd_mean = (outret_mean.cummax() - outret_mean) / outret_mean.cummax() * 100
outhpr = list(outret_mean)

profit = ret_mean - ret_mean.shift(1)
p_trade = profit[profit>0]
l_trade = profit[profit<0]

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
print("OUT MDD: ", outdd_mean.max())
print("OUT HPR: ", (outhpr[-2]-1)*100)

plt.plot(ret_mean)
plt.show()

plt.plot(ret_mean)
plt.plot(outret_mean)
plt.show()
