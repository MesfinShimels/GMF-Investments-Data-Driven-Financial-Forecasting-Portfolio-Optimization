import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

def seasonal_decomposition(data, column_name, period):
    """
    Perform seasonal decomposition on the specified column of the DataFrame.
    
    Parameters:
    - data: pandas DataFrame containing the time series data.
    - column_name: Name of the column to decompose.
    - period: Periodicity of the time series data.
    
    Returns:
    - Decomposition object.
    """
    # Ensure the index is a datetime index
    if not isinstance(data.index, pd.DatetimeIndex):
        raise ValueError("Index of the DataFrame must be a datetime index.")
    
    # Ensure the specified column exists
    if column_name not in data.columns:
        raise ValueError(f"Column '{column_name}' does not exist in the DataFrame.")
    
    # Ensure there are no missing values
    if data[column_name].isnull().any():
        raise ValueError(f"Column '{column_name}' contains missing values. Please handle them before decomposition.")
    
    # Perform seasonal decomposition
    decomposition = seasonal_decompose(data[column_name], model='additive', period=period)
    
    # Plot the decomposition
    decomposition.plot()
    plt.show()
    
    return decomposition

# Example usage
# Assuming 'clenspy' is your DataFrame and 'Close' is the column you want to decompose
# Ensure 'clenspy' has a datetime index and 'Close' column
# seasonal_decomposition(clenspy, 'Close', 252)