import pandas as pd
import numpy as np
from statsmodels.tsa.stattools import adfuller
from typing import Tuple

def compute_log_returns(prices: pd.Series) -> pd.Series:
    return np.log(prices).diff().dropna()

def run_adf_test(series: pd.Series) -> Tuple[float, float]:
    result = adfuller(series.dropna())
    return result[0], result[1]
