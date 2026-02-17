import pandas as pd
import numpy as np
from src.modeling.risk_metrics import calculate_volatility

def test_volatility_positive():
    returns = pd.Series(np.random.normal(0, 0.01, 100))
    vol = calculate_volatility(returns)
    assert vol > 0
