GMF Investments: Data-Driven Financial Forecasting & Portfolio Optimization
Overview
This project was developed for GMF Investments to build a data-driven framework for forecasting market trends and optimizing investment portfolios. Leveraging historical financial data from Yahoo Finance (via the YFinance Python library), the project employs time series forecasting models and portfolio optimization techniques to help manage risks and enhance returns. The main assets in focus are Tesla (TSLA), Vanguard Total Bond Market ETF (BND), and S&P 500 ETF (SPY).
Features
Data Acquisition: Fetch historical data for TSLA, BND, and SPY from YFinance covering January 1, 2015 to January 31, 2025.
Data Preprocessing & EDA: Clean and explore data to understand trends, volatility, and seasonality.
Time Series Forecasting: Develop forecasting models (ARIMA, SARIMA, or LSTM) to predict future market trends.
Portfolio Optimization: Integrate forecasts with historical data to optimize asset allocation based on risk-adjusted returns.
File Structure
GMF_Project/
│
├── data/
│   └── raw/             # Contains CSV files for TSLA, BND, SPY data
│
├── notebooks/
│   ├── 01_data_exploration.ipynb   # EDA and data preprocessing
│   ├── 02_model_development.ipynb    # Time series forecasting model development
│   └── 03_portfolio_optimization.ipynb  # Portfolio optimization analysis
│
├── scripts/
│   ├── fetch_data.py    # Script to fetch data from YFinance
│   ├── preprocess.py    # Data cleaning and preprocessing script
│   ├── forecast.py      # Script for building forecasting models
│   └── optimize.py      # Script for portfolio optimization
│
├── results/
│   └── figures/         # Plots, charts, and other visualizations
│
└── requirements.txt     # Project dependencies
Getting Started
Prerequisites
Python 3.8 or later
pip
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
Run the following script to download the raw financial data:
python scripts/fetch_data.py
2. Data Preprocessing and EDA
Launch the first Jupyter Notebook to explore and preprocess the data:
jupyter notebook notebooks/01_data_exploration.ipynb
In this notebook, you will:
Load data from CSV files.
Inspect and clean the data (handle missing values, adjust data types).
Visualize trends (closing prices, daily returns, rolling statistics).
Perform seasonal decomposition.
Placeholder for EDA Visualizations:
[Insert Image Here: EDA Visualizations]
3. Forecasting Model Development
Open the forecasting notebook to build and evaluate time series models:
jupyter notebook notebooks/02_model_development.ipynb
Steps include:
Splitting data into training and test sets.
Implementing forecasting models (ARIMA, SARIMA, or LSTM).
Optimizing model parameters and evaluating performance using MAE, RMSE, and MAPE.
4. Portfolio Optimization
Access the portfolio optimization notebook:
jupyter notebook notebooks/03_portfolio_optimization.ipynb
In this notebook, you will:
Integrate forecasted data with historical asset performance.
Calculate annual returns, covariance, and risk metrics (VaR, Sharpe Ratio).
Use optimization techniques to find the optimal asset allocation.
Placeholder for Portfolio Optimization Visualizations:
[Insert Image Here: Portfolio Optimization Results]
Project Timeline
Discussion: Wednesday, 26 Feb 2025 (use #all-week11 for pre-ask questions)
Interim Solution Deadline: Friday, 28 Feb 2025 at 20:00 UTC
Final Submission Deadline: Tuesday, 04 Feb 2025 at 20:00 UTC
License
[Include your license information here if applicable.]
Acknowledgements
Data sourced from Yahoo Finance via YFinance
Special thanks to the GMF Investments team for the project opportunity.
Contact
For any questions or further information, please contact:
[Your Name]
Email: Mesfins973@gmail.com
