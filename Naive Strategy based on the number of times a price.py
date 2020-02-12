# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 07:25:40 2020

@author: Dell
"""


'''
beeyi aiki dakiyaw ba
a naive strategy based on the number of times a price
increases or decreases. This strategy is based on the historical price momentum
'''
import pandas as pd
import matplotlib.pyplot as plt


goil=pd.read_excel(r'C:\Users\Dell\Desktop\data\goil 1st2019-1st2020.xlsx') 

def naiveMomentumTradingStrategy(data,numberConsecutiveDays):
    
    #create dataframe for signals
    signals=pd.DataFrame(index=data.Date)
    signals['Orders']=0
    
    #declare variables
    consecutiveDays=0
    priorPrice=0
    init=True
    
    #create signals
    for _ in range(len(data['Closing Price VWAP (GHS)'])):
        price=data['Closing Price VWAP (GHS)'][_]
        if init:
            priorPrice=price
            init=False
        elif price>priorPrice:
            if consecutiveDays<0:
                consecutiveDays=0
            consecutiveDays+=1
        elif priorPrice<price:
            if consecutiveDays>0:
               consecutiveDays=0
            consecutiveDays-=1
        if consecutiveDays==-numberConsecutiveDays:
           signals['Orders'][_]=1
        elif consecutiveDays == -numberConsecutiveDays:
           signals['Orders'][_]=-1
    
    return signals

strategy=naiveMomentumTradingStrategy(goil,5)
print(strategy)

figure=plt.figure()
ax1=figure.add_subplot(111,ylabel='GOIL VWAP CLOSING PRICES')

goil['Closing Price VWAP (GHS)'].plot(ax=ax1,color='g',lw=.5)

ax1.plot(strategy.loc[strategy.Orders== 1.0].index.values,\
         goil["Closing Price VWAP (GHS)"][strategy.Orders == 1].values,\
         '^', markersize=7, color='k')
ax1.plot(strategy.loc[strategy.Orders== -1.0].index.values\
         ,goil["Closing Price VWAP (GHS)"][strategy.Orders == -1].values\
         ,'v', markersize=7, color='k')           
           
plt.legend(["Price","Buy","Sell"])
plt.title("Turtle Trading Strategy")
plt.show()           
            
        
    
    
    
    
    