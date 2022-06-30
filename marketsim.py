""""""  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
"""MC2-P1: Market simulator.  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
Copyright 2018, Georgia Institute of Technology (Georgia Tech)  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
Atlanta, Georgia 30332  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
All Rights Reserved  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
Template code for CS 4646/7646  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
Georgia Tech asserts copyright ownership of this template and all derivative  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
works, including solutions to the projects assigned in this course. Students  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
and other users of this template code are advised not to share it with others  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
or to make it available on publicly viewable websites including repositories  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
such as github and gitlab.  This copyright statement should not be removed  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
or edited.  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
We do grant permission to share solutions privately with non-students such  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
as potential employers. However, sharing with other current or future  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
students of CS 7646 is prohibited and subject to being investigated as a  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
GT honor code violation.  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
-----do not edit anything above this line---  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
Student Name: Mithulesh Kurale  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
GT User ID: mkurale3   		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
GT ID: 903081123   		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
"""  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
import datetime as dt  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
import os  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
import numpy as np  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
import pandas as pd  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
from util import get_data, plot_data  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
def author():
    return 'mkurale3'
 		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
def compute_portvals(  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    orders_file="./orders/orders.csv",  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    start_val=1000000,  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    commission=9.95,  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    impact=0.005,  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
):  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    """  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    Computes the portfolio values.  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    :param orders_file: Path of the order file or the file object  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    :type orders_file: str or file object  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    :param start_val: The starting value of the portfolio  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    :type start_val: int  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    :param commission: The fixed amount in dollars charged for each transaction (both entry and exit)  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    :type commission: float  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    :param impact: The amount the price moves against the trader compared to the historical data at each transaction  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    :type impact: float  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    :return: the result (portvals) as a single-column dataframe, containing the value of the portfolio for each trading day in the first column from start_date to end_date, inclusive.  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    :rtype: pandas.DataFrame  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    """  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    #Step 1: Read in orders file using pandas
    orders= pd.read_csv(orders_file, index_col='Date', parse_dates=True, na_values=[‘nan’]) 
    
    #Step 2: Fetch the start/ end date and symbols
    startDate = orders.index[0]
    endDate = orders.index[-1]
    symbols = sorted(list((set(orders.Symbol.tolist()))))
    
    #Step 3: Generate prices df, trades df, holdings df
    pricesDF = get_data(symbols,pd.date_range(startDate, endDate))
    pricesDF["Cash"] = 1
    
    #Step 4: Populate the trades data frame
    tradesDF = self.populateTradesDataFrame(orders, pricesDF, commission, impact)
    
    #Step 5: Populate the holdings data 
    holdingsDF = self.populateHoldingsDataFrame(tradesDF, start_val)
    
    portVals= (pricesDF * holdingsDF).sum(axis=1)
    
    return portVals
	  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
def populateTradesDataFrame(self, orders, pricesDF, commission, impact):
    tradesDataFrame = orders
    
    tradesDataFrame.loc[:, "Symbol"] = 0
    tradesDataFrame["Cash"] = 0
    
    for i in range(len(tradesDataFrame)):
        #for each row in orders fetch the column data
        date = orders.loc[i, "Date"]
        symbol = orders.loc[i, "Symbol"]
        order = orders.loc[i, "Orders"]
        shares = orders.loc[i, "Shares"]
        
        #if buy order than for specific date add to existing shares of certain stock
        currStockSharesOwned = tradesDataFrame.loc[date,symbol]
        currCashEarnings = tradesDataFrame.loc[date,"Cash"]
        stockPrice = pricesDF.loc[date,symbol]
        
        if order == "BUY":
            currStockSharesOwned = currStockSharesOwned + shares
            currCashEarnings = currCashEarnings + (stockPrice * shares * (-1-impact)) - commission
        
        #if sell order than for specific date subtract to existing shares of certain stock
        elif order == "SELL":
            currStockSharesOwned = currStockSharesOwned - shares
            currCashEarnings = currCashEarnings + (stockPrice * shares * (1-impact)) - commission
        else:
            raise Exception("Unidentifiable order type")  
          
    return tradesDataFrame

def populateHoldingsDataFrame(self, tradesDataFrame, start_val):
    holdingsDataFrame = tradesDataFrame.copy(deep=True)
    holdingsDataFrame.loc[1:, "Symbol"] = 0
    holdingsDataFrame["Cash"]= 0
    holdingsDataFrame.loc[0,"Cash"]= start_val
    
    #populate the first row for all columns but last with values from trading
    #holdingsDataFrame.iloc[0,0:-1]= tradesDataFrame.iloc[0,0:-1]
    
    #update the cash value with first initial trade cash changes
    holdingsDataFrame.iloc[0,-1]= holdingsDataFrame.iloc[0,-1] + tradesDataFrame.iloc[0,-1]
    
    for i in range(1, len(holdingsDataFrame)):
        #c1,c2,c3,c4 = self.function(holdingsDataFrame, tradesDataFrame, i)
        prevStockHolding = holdingsDataFrame.iloc[i-1,:-1]
        currStockTrades = tradesDataFrame.iloc[i,:-1]
        prevCashHoldEarnings = holdingsDataFrame.iloc[i-1,-1] 
        currTradeCashEarnings = tradesDataFrame.iloc[i,-1] 
        
        holdingsDataFrame.iloc[i,:-1] = prevStockHolding + currStockTrades
        holdingsDataFrame.iloc[i, -1] = prevCashHoldEarnings + currTradeCashEarnings 
        # holdingsDataFrame.iloc[i,:-1]= holdingsDataFrame.iloc[i-1,:-1] + tradesDataFrame.iloc[i,:-1] 
        # holdingsDataFrame.iloc[i,-1]= holdingsDataFrame.iloc[i-1,-1] + tradesDataFrame.iloc[i,-1] 
    
    return holdingsDataFrame

def test_code():  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    """  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    Helper function to test code  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    """  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # this is a helper function you can use to test your code  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # note that during autograding his function will not be called.  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # Define input parameters  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    of = "./orders/orders2.csv"  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    sv = 1000000  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # Process orders  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    portvals = compute_portvals(orders_file=of, start_val=sv)  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    if isinstance(portvals, pd.DataFrame):  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
        portvals = portvals[portvals.columns[0]]  # just get the first column  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    else:  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
        "warning, code did not return a DataFrame"  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # Get portfolio stats  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # Here we just fake the data. you should use your code from previous assignments.  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    start_date = dt.datetime(2008, 1, 1)  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    end_date = dt.datetime(2008, 6, 1)  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    cum_ret, avg_daily_ret, std_daily_ret, sharpe_ratio = [  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
        0.2,  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
        0.01,  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
        0.02,  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
        1.5,  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    ]  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    daily_ret= (portvals[1:]/portvals[:-1])-1
    cum_ret= (portvals[-1]/portvals[0])-1
    avg_daily_ret= daily_ret.mean()
    std_daily_ret= daily_ret.std()
    sharpe_ratio= math.sqrt(252) * (avg_daily_ret/std_daily_ret) 
    
    
    spy = get_data(['SPY'], pd.date_range(start_date, end_date))
    cum_ret_SPY, avg_daily_ret_SPY, std_daily_ret_SPY, sharpe_ratio_SPY = [  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
        0.2,  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
        0.01,  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
        0.02,  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
        1.5,  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    ]
    
    		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # Compare portfolio against $SPX  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    print(f"Date Range: {start_date} to {end_date}")  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    print()  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    print(f"Sharpe Ratio of Fund: {sharpe_ratio}")  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    print(f"Sharpe Ratio of SPY : {sharpe_ratio_SPY}")  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    print()  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    print(f"Cumulative Return of Fund: {cum_ret}")  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    print(f"Cumulative Return of SPY : {cum_ret_SPY}")  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    print()  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    print(f"Standard Deviation of Fund: {std_daily_ret}")  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    print(f"Standard Deviation of SPY : {std_daily_ret_SPY}")  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    print()  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    print(f"Average Daily Return of Fund: {avg_daily_ret}")  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    print(f"Average Daily Return of SPY : {avg_daily_ret_SPY}")  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    print()  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    print(f"Final Portfolio Value: {portvals[-1]}")  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
if __name__ == "__main__":  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    test_code()  		  	   		  	  			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
