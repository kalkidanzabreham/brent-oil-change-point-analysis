import streamlit as st
import requests
import pandas as pd

# Get prices
prices_resp = requests.get("http://127.0.0.1:5000/api/prices")
prices = pd.DataFrame(prices_resp.json())
prices["Date"] = pd.to_datetime(prices["Date"])
prices = prices.sort_values("Date")

# Get changepoints
changepoints_resp = requests.get("http://127.0.0.1:5000/api/changepoints")
changepoints = changepoints_resp.json()

# Loop over the list of change points
for cp in changepoints:
    st.write(f"Change point detected at: {cp['date']} - {cp.get('description', '')}")

# Plot prices with a 7-day rolling average
st.line_chart(prices.set_index("Date")["Price"].rolling(7).mean())
