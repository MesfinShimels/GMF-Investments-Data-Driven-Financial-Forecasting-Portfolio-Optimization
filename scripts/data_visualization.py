import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.seasonal import seasonal_decompose

def closing_price(data,name):
    plt.figure(figsize=(14, 7))
    plt.plot(data['Close'], label=f'{name} Close Price', color='blue')
    plt.title(f'{name} Historical Closing Prices')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()

  
  
  

# def daily_returns(data,name):
#   # Compute daily returns
#  data['Daily_Return'] = data['Close'].pct_change()
#  # Plot daily_returns
#  plt.figure(figsize=(14, 7))
#  plt.plot(data['Daily_Return'], label='Daily Returns', color='green')
#  plt.title(f'{name} Daily Returns')
#  plt.xlabel('Date')
#  plt.ylabel('Daily Return')
#  plt.legend()
#  plt.show()


import pandas as pd
import matplotlib.pyplot as plt

def daily_returns(data, name):
    # Ensure 'Close' column is numeric, convert non-numeric values to NaN
    data['Close'] = pd.to_numeric(data['Close'], errors='coerce')
    
    # Drop rows with NaN values in the 'Close' column
    data = data.dropna(subset=['Close'])
    
    # Compute daily returns
    data['Daily_Return'] = data['Close'].pct_change()
    
    # Drop rows with NaN values in the 'Daily_Return' column (e.g., the first row)
    data = data.dropna(subset=['Daily_Return'])
    
    # Plot daily returns
    plt.figure(figsize=(14, 7))
    plt.plot(data.index, data['Daily_Return'], label='Daily Returns', color='green')
    plt.title(f'{name} Daily Returns')
    plt.xlabel('Date')
    plt.ylabel('Daily Return')
    plt.legend()
    plt.show()


def rolling_statistics(data, name):
    # Ensure 'Close' column is numeric, convert non-numeric values to NaN
    data['Close'] = pd.to_numeric(data['Close'], errors='coerce')
    
    # Drop rows with NaN values in the 'Close' column
    data = data.dropna(subset=['Close'])
    
    # Calculate 30-day rolling statistics
    data['Rolling_Mean'] = data['Close'].rolling(window=30).mean()
    data['Rolling_STD'] = data['Close'].rolling(window=30).std()
    
    # Plot rolling statistics
    plt.figure(figsize=(14, 7))
    plt.plot(data.index, data['Rolling_Mean'], label='30-Day Rolling Mean', color='orange')
    plt.plot(data.index, data['Rolling_STD'], label='30-Day Rolling STD', color='red')
    plt.title(f'{name} Rolling Statistics')
    plt.xlabel('Date')
    plt.legend()
    plt.show()

    