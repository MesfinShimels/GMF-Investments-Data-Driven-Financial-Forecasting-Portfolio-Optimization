"""
scripts/optimize.py

Script to load asset data (TSLA, BND, SPY), compute returns,
and perform a simplified Markowitz portfolio optimization.
"""

import pandas as pd
import numpy as np
import os

def load_asset_data(tickers, data_dir='../data/raw'):
    """
    Loads CSV files for each ticker from the specified directory.
    Returns a dictionary of DataFrames keyed by ticker.
    """
    data_dict = {}
    for ticker in tickers:
        file_path = os.path.join(data_dir, f"{ticker}.csv")
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found for {ticker} at {file_path}")
        df = pd.read_csv(file_path, parse_dates=['Date'], index_col='Date').sort_index()
        data_dict[ticker] = df
    return data_dict

def compute_returns(data_dict, price_col='Close'):
    """
    Given a dictionary of DataFrames keyed by ticker, compute daily returns
    and return a single DataFrame with each column representing a ticker's returns.
    """
    returns_df = pd.DataFrame()
    for ticker, df in data_dict.items():
        returns_df[ticker] = df[price_col].pct_change()
    return returns_df.dropna()

def random_portfolio_optimization(returns_df, num_portfolios=5000, risk_free_rate=0.02):
    """
    Perform a naive random portfolio simulation to find
    the weights that maximize the Sharpe Ratio.
    """
    tickers = returns_df.columns
    results = []

    for _ in range(num_portfolios):
        # Random weights
        weights = np.random.random(len(tickers))
        weights /= np.sum(weights)
        
        # Calculate expected return & volatility
        port_return = np.sum(returns_df.mean() * weights) * 252  # annualize
        port_vol = np.sqrt(np.dot(weights.T, np.dot(returns_df.cov() * 252, weights)))
        
        # Calculate Sharpe Ratio
        sharpe_ratio = (port_return - risk_free_rate) / port_vol
        
        results.append({
            'weights': weights,
            'return': port_return,
            'volatility': port_vol,
            'sharpe': sharpe_ratio
        })

    # Convert to DataFrame
    results_df = pd.DataFrame(results)
    # Find max Sharpe Ratio
    best_portfolio = results_df.loc[results_df['sharpe'].idxmax()]
    return best_portfolio

def optimize_portfolio(tickers=('TSLA','BND','SPY')):
    """
    High-level function to load data, compute returns,
    and perform naive Markowitz optimization.
    """
    # 1. Load Data
    data_dict = load_asset_data(tickers)
    
    # 2. Compute Returns
    returns_df = compute_returns(data_dict)
    
    # 3. Optimize
    best_portfolio = random_portfolio_optimization(returns_df)
    
    # 4. Print/Save Results
    print("Optimal Weights:")
    for t, w in zip(tickers, best_portfolio['weights']):
        print(f"{t}: {w:.2%}")
    print(f"Expected Annual Return: {best_portfolio['return']:.2%}")
    print(f"Volatility: {best_portfolio['volatility']:.2%}")
    print(f"Sharpe Ratio: {best_portfolio['sharpe']:.2f}")

if __name__ == '__main__':
    optimize_portfolio()
