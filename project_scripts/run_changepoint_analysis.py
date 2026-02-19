import os
import pandas as pd
import arviz as az


from src.utils.loader import load_price_data
from src.utils.preprocessing import compute_log_returns
from src.modeling.bayesian_changepoint import build_model, sample_model
from src.config import ModelConfig

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_PATH = os.path.join(BASE_DIR, "data/raw/BrentOilPrices.csv")
OUTPUT_PATH = os.path.join(BASE_DIR, "data/processed/changepoints.csv")

# 1. Load + preprocess
df = load_price_data(DATA_PATH)
df = df.set_index("Date").resample("W").mean().reset_index()

returns = compute_log_returns(df["Price"]).dropna()

# 2. Build model
model = build_model(returns.values)

# 3. Sample
trace = sample_model(model, ModelConfig())

# 4. Extract best tau
best_tau = int(trace.posterior["tau"].mean())

date_cp = df.iloc[best_tau]["Date"]

# 5. Save result
pd.DataFrame({
    "date": [date_cp],
    "type": ["bayesian_detected"]
}).to_csv(OUTPUT_PATH, index=False)

print("Changepoint saved to:", OUTPUT_PATH)

az.to_netcdf(trace, "data/processed/trace.nc")
print("Trace saved to data/processed/trace.nc")
