import numpy as np
import pandas as pd

TRADING_DAYS = 252

def annualized_volatility(returns: pd.Series) -> float:
    return returns.std() * np.sqrt(TRADING_DAYS)

def sharpe_ratio(returns: pd.Series, risk_free_rate: float = 0.0) -> float:
    excess = returns - risk_free_rate/TRADING_DAYS
    return (excess.mean() / excess.std()) * np.sqrt(TRADING_DAYS)

def max_drawdown(prices: pd.Series) -> float:
    cumulative_max = prices.cummax()
    drawdown = (prices - cumulative_max) / cumulative_max
    return drawdown.min()
