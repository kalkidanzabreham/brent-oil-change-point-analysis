import pandas as pd
from src.utils.preprocessing import compute_log_returns

def test_log_returns_length():
    prices = pd.Series([100, 101, 102])
    returns = compute_log_returns(prices)
    assert len(returns) == 2
