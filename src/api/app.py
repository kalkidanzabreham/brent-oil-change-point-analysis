from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd
import os

from src.utils.loader import load_price_data
from src.modeling.risk_metrics import (
    annualized_volatility,
    sharpe_ratio,
    max_drawdown
)

app = Flask(__name__)
CORS(app)

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))

DATA_PATH = os.path.join(BASE_DIR, "data/raw/BrentOilPrices.csv")
EVENTS_PATH = os.path.join(BASE_DIR, "data/events/oil_market_events.csv")
CHANGEPOINT_PATH = os.path.join(BASE_DIR, "data/processed/changepoints.csv")

# -------------------------
# Load data once at startup
# -------------------------

# Raw prices (for chart)
prices = pd.read_csv(DATA_PATH)
prices["Date"] = pd.to_datetime(prices["Date"], errors="coerce")
prices = prices.dropna(subset=["Date"])

# Weekly resampled data (for risk metrics)
df = load_price_data(DATA_PATH)
df = df.set_index("Date").resample("W").mean().reset_index()

# Events
events = pd.read_csv(EVENTS_PATH)
events["date"] = pd.to_datetime(events["date"], errors="coerce")

# Precomputed changepoint
changepoints = pd.read_csv(CHANGEPOINT_PATH)
changepoints["date"] = pd.to_datetime(changepoints["date"], errors="coerce")

# Assume single changepoint for now
change_date = changepoints.iloc[0]["date"]

# Find corresponding index in weekly df
tau_index = df.index[df["Date"] == change_date][0]


# -------------------------
# API Endpoints
# -------------------------

@app.route("/api/prices")
def get_prices():
    return prices.to_json(orient="records", date_format="iso")


@app.route("/api/events")
def get_events():
    return events.to_json(orient="records", date_format="iso")


@app.route("/api/changepoints")
def get_changepoints():
    return changepoints.to_json(orient="records", date_format="iso")


@app.route("/api/risk_metrics")
def get_risk_metrics():

    prices_series = df["Price"]
    returns = prices_series.pct_change().dropna()

    before_returns = returns.iloc[:tau_index]
    after_returns = returns.iloc[tau_index:]

    metrics = {
        "before": {
            "volatility": annualized_volatility(before_returns),
            "sharpe": sharpe_ratio(before_returns),
            "max_drawdown": max_drawdown(prices_series.iloc[:tau_index])
        },
        "after": {
            "volatility": annualized_volatility(after_returns),
            "sharpe": sharpe_ratio(after_returns),
            "max_drawdown": max_drawdown(prices_series.iloc[tau_index:])
        }
    }

    return jsonify(metrics)


if __name__ == "__main__":
    app.run(debug=True)
