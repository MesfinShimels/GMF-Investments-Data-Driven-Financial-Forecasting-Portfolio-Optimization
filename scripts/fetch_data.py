
# # def featch_data():
#     import yfinance as yf
#     import pandas as pd

#     # Define the assets and date range
#     tickers = ['TSLA', 'BND', 'SPY']
#     start_date = '2015-01-01'
#     end_date = '2025-01-31'

#     # Fetch the data
#     for ticker in tickers:
#         data = yf.download(ticker, start=start_date, end=end_date)
#         data.to_csv(f'../data/raw/{ticker}.csv')
#         print(f"Data for {ticker} saved.")
import yfinance as yf
import pandas as pd

# Define the assets and date range
tickers = ['TSLA', 'BND', 'SPY']
start_date = '2015-01-01'
end_date = '2025-01-31'

# Fetch the data and save it to CSV files
for ticker in tickers:
    # Download data using yfinance
    data = yf.download(ticker, start=start_date, end=end_date)
    
    # Reset the index to include the Date column
    data.reset_index(inplace=True)
    
    # Save the data to a CSV file
    file_path = f'C:/Users/User/Desktop/GMF-Investments-Data-Driven-Financial-Forecasting-Portfolio-Optimization/data/raw/{ticker}.csv'
    data.to_csv(file_path, index=False)  # Set index=False to avoid saving the index as a separate column
    
    print(f"Data for {ticker} saved to {file_path}.")
