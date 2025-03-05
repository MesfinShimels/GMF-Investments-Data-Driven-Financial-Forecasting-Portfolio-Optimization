GMF Investments: Data-Driven Financial Forecasting & Portfolio Optimization
Overview
This repository is designed to help GMF Investments—or any financial advisory firm—leverage data-driven insights to optimize investment portfolios. By combining historical financial data (sourced via YFinance) with time series forecasting techniques (e.g., ARIMA) and portfolio optimization strategies (e.g., Markowitz mean-variance), this project aims to:
1.Predict Future Asset Prices: Build and evaluate models that forecast stock prices, focusing on Tesla (TSLA) as a high-volatility growth stock, Vanguard Total Bond Market ETF (BND) for stability, and S&P 500 ETF (SPY) for broad market exposure.
2.Enhance Portfolio Performance: Use forecasts and historical data to optimize asset allocation, balancing risk and return according to user-defined objectives (e.g., maximizing Sharpe Ratio).

Features
1.
Data Acquisition (YFinance):
2.
1.Automated fetching of historical data (Open, High, Low, Close, Volume) for TSLA, BND, and SPY covering the period from January 1, 2015, to January 31, 2025.
2.Storage of raw CSV files in a dedicated directory for reproducibility.
3.
Data Preprocessing & EDA:
4.
1.Cleaning and formatting of time series data (handling missing values, date parsing, etc.).
2.Exploratory Data Analysis to understand price trends, volatility, and correlations.
3.Visualization of rolling means, standard deviations, and daily returns to identify patterns.
5.
Time Series Forecasting:
6.
1.ARIMA / SARIMA Models: Leverage auto_arima from pmdarima to handle univariate forecasting.
2.Performance Metrics: Evaluate models using MAE, RMSE, and MAPE.
3.Future Forecasting: Generate short-term (6–12 months) or custom-range predictions to anticipate market trends.
7.
Portfolio Optimization:
8.
1.Markowitz Mean-Variance Approach: Compute returns, covariance, and volatility for TSLA, BND, and SPY.
2.Random Portfolio Simulation: Generate thousands of random weight allocations to identify the maximum Sharpe Ratio.
3.Risk Metrics: Incorporate measures such as Value at Risk (VaR) or Sharpe Ratio for robust risk management.
4.Visualization: Plot the efficient frontier, highlight optimal weights, and compare to baseline strategies.
9.
Modular Code & Notebooks:
10.
1.Scripts: Production-like Python files (fetch_data.py, forecast.py, optimize.py) for automation.
2.Notebooks: Interactive exploration in Jupyter notebooks (01_data_exploration.ipynb, 02_model_development.ipynb, 03_portfolio_optimization.ipynb) for detailed analysis, experimentation, and visualizations.

Detailed Project Workflow
1.
Data Acquisition (scripts/fetch_data.py********************************)
2.
1.Pulls historical data for TSLA, BND, and SPY via YFinance.
2.Saves CSV files to data/raw/.
3.
Data Preprocessing & EDA (01_data_exploration.ipynb********************************)
4.
1.Loads the raw CSV files.
2.Cleans and inspects data (e.g., checking for missing values, data types, outliers).
3.Performs exploratory analyses (time-series plots, rolling statistics, correlation checks).
4.Documents initial insights on market trends, volatility, and anomalies.
5.
Model Development (02_model_development.ipynb******************************** / scripts/forecast.py)
6.
1.Splits data into training and testing sets.
2.Uses auto_arima or other methods (e.g., LSTM if you choose deep learning) to build forecasting models for TSLA (and optionally BND, SPY).
3.Optimizes hyperparameters and evaluates model performance using metrics such as RMSE, MAE, MAPE.
4.Saves the best model’s forecasts for further analysis or integration.
7.
Portfolio Optimization (03_portfolio_optimization.ipynb******************************** / scripts/optimize.py)
8.
1.Integrates the forecasts (TSLA) with historical data (BND, SPY) or forecasted data for all three assets.
2.Calculates daily returns, annualizes them, and computes covariance matrices.
3.Implements a Markowitz mean-variance approach to find the optimal asset weights that maximize risk-adjusted returns (Sharpe Ratio).
4.Visualizes the efficient frontier and highlights the optimal portfolio.
9.
Results & Insights (results/********************************)
10.
1.Stores generated plots, tables, and final CSV files with forecasted prices and optimal weights.
2.Provides a clear reference for comparing different model approaches and portfolio allocations.

File Structure
GMF_Project/
│
├── data/
│   └── raw/                    # Contains raw CSV files for TSLA, BND, SPY
│
├── notebooks/
│   ├── 01_data_exploration.ipynb      # Exploratory Data Analysis (EDA)
│   ├── 02_model_development.ipynb     # Time series forecasting model development
│   └── 03_portfolio_optimization.ipynb# Portfolio optimization analysis
│
├── scripts/
│   ├── fetch_data.py    # Fetches raw data from YFinance
│   ├── preprocess.py    # (Optional) Additional data cleaning, if needed
│   ├── forecast.py      # Builds & evaluates time series forecasting models
│   └── optimize.py      # Performs portfolio optimization (Markowitz)
│
├── results/
│   └── figures/         # Plots, charts, and other visual outputs
│
└── requirements.txt     # Python dependencies for the project

Getting Started
Prerequisites
Python 3.8 or later
pip (or conda if you use Anaconda)
Installation
1.
Clone the Repository:
2.
git clone <repository_url>
cd GMF_Project
3.
4.
Create a Virtual Environment:
5.
python -m venv venv
6.
7.
Activate the Virtual Environment:
8.
oWindows: 
venv\Scripts\activate
o
omacOS/Linux: 
source venv/bin/activate
o
9.
Install Required Packages:
10.
pip install -r requirements.txt
11.

Usage
1. Fetching Data
Run the script to download raw financial data (TSLA, BND, SPY) from YFinance:
python scripts/fetch_data.py
The resulting CSV files will be saved in data/raw/.
2. Data Exploration
Open the EDA Notebook to explore and visualize data trends:
jupyter notebook notebooks/01_data_exploration.ipynb
What You’ll Do Here: 
oLoad the CSV files for TSLA, BND, SPY.
oInspect missing values, data types, and summary statistics.
oPlot closing prices, daily returns, and rolling volatility.
oIdentify any anomalies or trends.
3. Model Development
You can either run the forecasting script or the notebook:

Script:

python scripts/forecast.py

This will train an ARIMA model on TSLA (by default), evaluate it on a test set, and save forecasts.


Notebook:

jupyter notebook notebooks/02_model_development.ipynb

Here, you can:

oExperiment with ARIMA, SARIMA, or LSTM models.
oTune hyperparameters and visually compare predictions vs. actual values.
oSave or export your best forecasts for further analysis.
4. Portfolio Optimization
Finally, move on to the portfolio optimization step:

Script:

python scripts/optimize.py

This script will perform a random portfolio simulation for TSLA, BND, and SPY, printing the best portfolio weights based on the Sharpe Ratio.


Notebook:

jupyter notebook notebooks/03_portfolio_optimization.ipynb

In this notebook, you can:

oMerge forecasted TSLA prices (and optionally BND, SPY) with historical data.
oCalculate returns, covariance matrices, and risk metrics.
oOptimize allocations and visualize the efficient frontier.

Results and Interpretation
Forecast Accuracy:
Compare your model’s predictions with actual market data (if available) to gauge reliability.
Optimal Portfolio Weights:
The final weights recommended by the Markowitz simulation indicate how to distribute capital among TSLA, BND, and SPY to balance risk and return.
Risk Metrics:
Evaluate the portfolio’s Sharpe Ratio, VaR, or other metrics to understand downside risk and volatility.
All charts and result files are saved in the results/ folder for easy reference.

Future Enhancements
Deep Learning Models:
Incorporate LSTM or Transformer-based models for potentially more accurate time series forecasts.
Multi-Factor Analysis:
Include macroeconomic indicators (e.g., interest rates, GDP) to enhance forecasting accuracy.
Advanced Portfolio Techniques:
Explore Black-Litterman or robust optimization frameworks for more sophisticated asset allocation.
Interactive Dashboards:
Build a web-based dashboard (e.g., using Streamlit) for real-time data updates and cenario testing.
Disclaimer
This project is for educational and demonstration purposes only. It is not intended to provide financial advice. Real-world investing involves substantial risks, and any decisions should be made based on professional guidance and thorough due diligence.
Acknowledgements
Data sourced from Yahoo Finance via YFinance.
Thanks to the GMF Investments team for outlining the project requirements.
Inspired by open-source Python libraries such as pmdarima, statsmodels, and scikit-learn.
Contact
For any questions or further information, please contact:
Mesfin s
Email:************Mesfins973@gmail.com
