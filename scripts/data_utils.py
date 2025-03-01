# data_utils.py
import pandas as pd
import os

def load_data(filename, data_dir='../data/raw'):
    path = os.path.join(data_dir, filename)
    return pd.read_csv(path, parse_dates=['Date'], index_col='Date')
