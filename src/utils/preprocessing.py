import pandas as pd
import numpy as np

def load_and_clean_data(path):
    df = pd.read_csv(path)
    df["Date"] = pd.to_datetime(df["Date"], format="%d-%b-%y")
    df = df.sort_values("Date")
    return df

def compute_log_returns(df):
    df["log_price"] = np.log(df["Price"])
    df["log_return"] = df["log_price"].diff()
    return df.dropna()
