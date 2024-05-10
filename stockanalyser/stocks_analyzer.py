import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import yfinance as yf
import matplotlib.pyplot as plt
from matplotlib.widgets import Cursor
import plotly.graph_objects as go
import plotly.offline as py_offline
import plotly

from utils import validate, validate_date_range, validate_tickers


#Function to get the data
def get_stock_data(tickers, start, end):
   
    invalid_tickers = validate_tickers(tickers)

    if invalid_tickers:
        raise ValueError(f"Invalid ticker symbols: {', '.join(invalid_tickers)}")
    
    validate(start)
    validate(end)
    validate_date_range(start, end)

    data = {}

    for ticker in tickers:
        try:
            data[ticker] = yf.download(ticker, start=start, end=end)
            if data[ticker].empty:
                raise ValueError(f"No data found for ticker: {ticker}")
            
        except Exception as e:
            print(f"Error fetching data for {ticker}: {e}")
            continue

    return data

def plot_compare_stocks(data):
    print("Starting to plot...")
    fig = go.Figure()
    for ticker, stock_data in data.items():
        fig.add_trace(go.Scatter(x=stock_data.index, 
                                 y=stock_data['Adj Close'],
                                 mode='lines', 
                                 name=f'{ticker} Adjusted Close'))

    fig.update_layout(title='Comparison of Stock Adjusted Close Prices',
                      xaxis_title='Date',
                      yaxis_title='Adjusted Close Price',
                      legend_title='Ticker')
    
    py_offline.plot(fig, filename='./output/Stock_Comparison.html')
    print("Plot should be displayed now...")


#Function to calculate the moving average 
def moving_average_calculate(stock_data, window_size):
  if window_size <= 0:
    raise ValueError("Window size must be greater than 0.")

  moving_average = stock_data['Adj Close'].rolling(window=window_size).mean()
  return moving_average

#Function to analyze the trends
def analyze_trends(stock_data):
  short_window = 50
  long_window = 200
  stock_data['Short_MA'] = moving_average_calculate(stock_data, short_window)
  stock_data['Long_MA'] = moving_average_calculate(stock_data, long_window)
  stock_data['Signal'] = np.where(stock_data['Short_MA'] > stock_data['Long_MA'], 1, 0)
  stock_data['Position'] = stock_data['Signal'].diff()
  stock_data.dropna(inplace=True)
  return stock_data

def plot_ma(ticker,stock_data):
    
    print("Starting to plot...")
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['Close'], mode='lines', name='Close Price'))
    fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['Short_MA'], mode='lines', name='Short Moving Average(50 days)', line=dict(color='red', width=1)))
    fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data["Long_MA"], mode='lines', name ='Long Moving Average(200 days)',line=dict(color='green', width=1)))
    fig.update_layout(title=f'Simple moving averages of {ticker}',
                    xaxis_title='Date',
                    yaxis_title='Price')
    py_offline.plot(fig, filename=f'./output/{ticker}_Short_Long_Moving_Average.html')
    print("Plot should be displayed now...")

