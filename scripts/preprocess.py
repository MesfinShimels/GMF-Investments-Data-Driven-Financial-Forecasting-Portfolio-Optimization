import pandas as pd

def dataclean(data):
    """
    Clean the DataFrame by filling missing numeric values with the mean of the column.
    
    Parameters:
    - data: pandas DataFrame to be cleaned.
    
    Returns:
    - Cleaned DataFrame.
    """
    # Ensure only numeric columns are filled
    numeric_columns = data.select_dtypes(include=[float, int]).columns
    
    # Create a copy of the original DataFrame to avoid modifying it
    df = data.copy()
    
    # Fill missing values with the mean of the column
    df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].mean())
    
    return df