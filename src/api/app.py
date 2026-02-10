from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)

import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
DATA_PATH = os.path.join(BASE_DIR, "data/raw/BrentOilPrices.csv")

prices = pd.read_csv(DATA_PATH)
prices["Date"] = pd.to_datetime(prices["Date"])  # auto-infer format


events = pd.read_csv(os.path.join(BASE_DIR, "data/events/oil_market_events.csv"))

@app.route("/api/prices")
def get_prices():
    return prices.to_json(orient="records", date_format="iso")

@app.route("/api/events")
def get_events():
    return events.to_json(orient="records")

@app.route("/api/changepoints")
def get_changepoints():
    return jsonify({
        "changepoints": [
            {"date": "2008-09-15", "description": "Global Financial Crisis"},
            {"date": "2020-03-11", "description": "COVID-19 Shock"}
        ]
    })

if __name__ == "__main__":
    app.run(debug=True)
