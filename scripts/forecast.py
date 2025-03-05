"""
scripts/forecast.py

Script to load TSLA data, perform train/test split,
fit an ARIMA model, evaluate performance, and save forecasts.
"""

import pandas as pd
import numpy as np
from pmdarima import auto_arima
from sklearn.metrics import mean_squared_error, mean_absolute_error
import math
import os

def forecast_tsla(
    csv_path='../data/raw/TSLA.csv',
    forecast_periods=30,
    output_path='../results/tsla_forecast.csv'
):
    """
    Loads TSLA data, fits an ARIMA model using auto_arima, and saves the forecast.

    Parameters:
    -----------
    csv_path : str
        Path to the TSLA CSV file.
    forecast_periods : int
        Number of future periods (days) to forecast.
    output_path : str
        File path to save the forecast results as a CSV.
    """

    # 1. Load data
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"CSV file not found at {csv_path}")

    df = pd.read_csv(csv_path, parse_dates=['Date'], index_col='Date').sort_index()
    
    # 2. Focus on 'Close' prices (adjust as needed)
    ts = df['Close'].dropna()

    # 3. Train-test split (example: train until end of 2023)
    train_end = '2023-12-31'
    train_data = ts.loc[:train_end]
    test_data = ts.loc['2024-01-01':]

    if train_data.empty or test_data.empty:
        raise ValueError("Check your date ranges—train or test data is empty.")

    # 4. Fit ARIMA model using auto_arima
    model = auto_arima(
        train_data,
        seasonal=False,
        trace=False,
        error_action='ignore',
        suppress_warnings=True,
        stepwise=True
    )

    # 5. Make predictions on the test set
    n_test = len(test_data)
    forecast_test = model.predict(n_periods=n_test)
    
    # Convert forecast_test to a Pandas Series with matching index
    forecast_index = test_data.index
    forecast_test_series = pd.Series(forecast_test, index=forecast_index)

    # 6. Evaluate performance
    mse = mean_squared_error(test_data, forecast_test_series)
    rmse = math.sqrt(mse)
    mae = mean_absolute_error(test_data, forecast_test_series)
    mape = np.mean(np.abs((test_data - forecast_test_series) / test_data)) * 100

    print(f"Test RMSE: {rmse:.2f}")
    print(f"Test MAE:  {mae:.2f}")
    print(f"Test MAPE: {mape:.2f}%")

    # 7. Forecast future periods
    model_future_forecast = model.predict(n_periods=forecast_periods)
    future_index = pd.date_range(start=test_data.index[-1] + pd.Timedelta(days=1),
                                 periods=forecast_periods, freq='B')  # 'B' for business days
    future_series = pd.Series(model_future_forecast, index=future_index)

    # 8. Save results
    results_df = pd.DataFrame({
        'Historical': ts,
        'Test_Forecast': forecast_test_series,
        'Future_Forecast': future_series
    })
    results_df.to_csv(output_path)
    print(f"Forecast results saved to {output_path}")

if __name__ == '__main__':
    forecast_tsla()
