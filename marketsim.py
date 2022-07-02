""""""
import math

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
    # Step 1: Read in orders file using pandas
    orders = pd.read_csv(orders_file)
    orders = orders.sort_values(by=['Date']).reset_index(drop=True)

    # Step 2: Fetch the start/ end date and symbols
    startDate = orders.iloc[0,0]
    endDate = orders.iloc[-1,0]
    symbols = sorted(list((set(orders.Symbol.tolist()))))

    # Step 3: Generate prices df, trades df, holdings df
    pricesDF = get_data(symbols, pd.date_range(startDate, endDate))
    pricesDF["Cash"] = 1

    # Step 4: Populate the trades data frame
    tradesDF = populateTradesDataFrame(orders, pricesDF, commission, impact, symbols)

    # Step 5: Populate the holdings data
    holdingsDF = populateHoldingsDataFrame(tradesDF, start_val, symbols)
    portVals = computePortVals(pricesDF, holdingsDF)
    portVals = portVals.set_index('Date')

    return portVals


def computePortVals(pricesDF, holdingsDF):
    symbols = holdingsDF.columns[1:-1]
    holdingsDF["PortVal"] = 0
    stockPriceForDayT = {}
    for i in range(len(holdingsDF)):
        # for each row in orders fetch the column data
        val = 0
        date = holdingsDF.loc[i, "Date"]
        cash = holdingsDF.loc[i, "Cash"]
        stockPriceForDayT = {}
        for sym in symbols:
            val = val + (pricesDF.loc[date, sym] * holdingsDF.loc[i, sym])
        val += cash
        holdingsDF.loc[i, "PortVal"] = val

    return holdingsDF[["Date", "PortVal"]]


def populateTradesDataFrame(orders, pricesDF, commission, impact, symbols):
    col_names = ["Date", "Cash"]
    col_names.extend(symbols)
    tradesDataFrame = pd.DataFrame(np.zeros((len(orders), len(col_names))), columns=col_names)

    # orders.copy(deep=True)

    # tradesDataFrame.loc[:, "Symbol"] = 0
    tradesDataFrame["Cash"] = 0

    for i in range(len(orders)):
        # for each row in orders fetch the column data
        date = orders.loc[i, "Date"]
        symbol = orders.loc[i, "Symbol"]
        order = orders.loc[i, "Order"]
        shares = orders.loc[i, "Shares"]

        # if buy order than for specific date add to existing shares of certain stock

        stockPrice = pricesDF.loc[date, symbol]

        if order == "BUY":
            currCashEarnings = ((stockPrice * shares * (-1 - impact)) - commission)

        # if sell order than for specific date subtract to existing shares of certain stock
        elif order == "SELL":
            currCashEarnings = (stockPrice * shares * (1 - impact)) - commission
            shares = shares * -1
        else:
            raise Exception("Unidentifiable order type")
        tradesDataFrame.loc[i, symbol] = shares
        tradesDataFrame.loc[i, "Date"] = date
        tradesDataFrame.loc[i, "Cash"] = currCashEarnings
        # tradesDataFrame.loc[len(tradesDataFrame)] = [date, symbol, shares, currCashEarnings]
    return tradesDataFrame


def createNewRowToInsert(tradesOnDate_DF, symbols, date):
    totalCashEarningsOnTradeDate = tradesOnDate_DF["Cash"].sum()
    shareCountForEachStock = []
    newRowToAppend = []
    for sym in symbols:
        shareCount = tradesOnDate_DF[sym].sum()
        shareCountForEachStock.append(shareCount)
    newRowToAppend.extend([date, totalCashEarningsOnTradeDate])
    newRowToAppend.extend(shareCountForEachStock)

    return newRowToAppend


def populateHoldingsDataFrame(tradesDataFrame, start_val, symbols):
    col_names = ["Date", "Cash"]
    col_names.extend(symbols)
    holdingsDataFrame = pd.DataFrame(columns=col_names)
    holdingsDataFrame.loc[len(holdingsDataFrame)] = 0

    holdingsDataFrame.loc[0, "Cash"] = start_val

    # populate the first row of holdings according to the trades holding
    date_set = set([])
    date = tradesDataFrame.loc[0, "Date"]
    date_set.add(date)
    holdingsDataFrame.iloc[0, 0] = date
    tradesOnDate_DF = tradesDataFrame.loc[tradesDataFrame["Date"] == date]
    newRow = createNewRowToInsert(tradesOnDate_DF, symbols, date)
    # create a df from new row
    newRowDf = pd.DataFrame(newRow).T
    newRowDf.columns = col_names

    holdingsDataFrame.iloc[0, 1:] = holdingsDataFrame.iloc[0, 1:] + newRowDf.iloc[0, 1:]

    # populate
    currIndex = len(holdingsDataFrame)
    for i in range(1, len(tradesDataFrame)):
        # parse out the date
        date = tradesDataFrame.loc[i, "Date"]
        if date in date_set:
            continue
        date_set.add(date)
        tradesOnDate_DF = tradesDataFrame.loc[tradesDataFrame["Date"] == date]
        newRow = createNewRowToInsert(tradesOnDate_DF, symbols, date)
        newRowDf = pd.DataFrame(newRow).T
        newRowDf.columns = col_names

        holdingsDataFrame.loc[currIndex] = holdingsDataFrame.iloc[currIndex - 1, 1:] + newRowDf.iloc[0, 1:]
        holdingsDataFrame.loc[currIndex, "Date"] = date
        currIndex += 1

    cashCol = holdingsDataFrame.pop("Cash")
    holdingsDataFrame.insert(len(holdingsDataFrame.columns), "Cash", cashCol)
    return holdingsDataFrame


def test_code():
    """
    Helper function to test code
    """
    # this is a helper function you can use to test your code
    # note that during autograding his function will not be called.
    # Define input parameters

    of = "./orders/orders-02.csv"
    sv = 1000000

    # Process orders
    portvals = compute_portvals(orders_file=of, start_val=sv)
    if isinstance(portvals, pd.DataFrame):
        portvals = portvals[portvals.columns[0]]  # just get the first column
    else:
        raise Exception("warning, code did not return a DataFrame")

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
    daily_ret = (portvals/ portvals.shift(1))-1
    cum_ret = (portvals[-1] / portvals[0]) - 1
    avg_daily_ret = daily_ret.mean()
    std_daily_ret = daily_ret.std()
    sharpe_ratio = math.sqrt(252) * (avg_daily_ret / std_daily_ret)

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
