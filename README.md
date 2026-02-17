# Brent Oil Price Regime Change Analysis

## 📌 Project Overview
This project analyzes structural regime shifts in Brent crude oil prices using Bayesian changepoint detection. It identifies statistically significant shifts in return dynamics and evaluates their impact on risk metrics such as volatility, Sharpe ratio, and drawdown.

The system is built as a full-stack data science application:
- Offline Bayesian modeling (PyMC)
- Flask REST API
- Streamlit interactive dashboard
- Modular, production-aware architecture

## 🎯 Objectives
- Detect structural breaks in Brent oil returns
- Quantify risk regime differences
- Connect changepoints to real-world geopolitical and economic events
- Provide an interactive analytical dashboard

## 🧠 Methodology

### Data Processing
- Daily Brent oil prices
- Weekly resampling
- Log returns computation
- Event dataset integration

### Bayesian Changepoint Model
We implement a continuous changepoint model:
- Smooth regime transition using sigmoid weighting
- Fully NUTS-based sampling
- 4 chains, 2000 tuning steps, 4000 posterior draws

**Parameters:**
- τ (changepoint location)
- μ₁, μ₂ (regime means)
- σ (volatility)

Posterior summaries are saved to:  
`data/processed/changepoints.csv`

## 🏗 Project Architecture

```bash 
brent-oil-change-point-analysis/
│
├── data/
│ ├── raw/ # Raw Brent oil price CSV
│ │ └── BrentOilPrices.csv
│ ├── processed/ # Preprocessed data, e.g., log returns
│ │ └── log_returns.csv
│ └── events/ # Key events dataset
│ └── oil_market_events.csv
├── project_scripts/
│   └── run_changepoint_analysis.py
├── notebooks/
│ ├── 01_eda.ipynb # EDA and stationarity analysis 
│ ├── 02_change_point_model.ipynb 
│ └── 03_event_impact_analysis.ipynb 
│
├── src/
│   ├── api/
│   ├── modeling/
|       ├── bayesian_change_point.py
│       └── risk_metrics.py
│   ├── utils/
│   ├── config.py
├── tests/
│   ├── test_preprocessing.py
│   ├── test_risk_metrics.py
├── requirements.txt # Project dependencies
└── README.md # Project description and instructions
```

---

## How to Run (Interim Version)

1. Clone the repo:
```bash
git clone https://github.com/kalkidanzabreham/brent-oil-change-point-analysis.git
cd brent-oil-change-point-analysis
```
2.Create and activate virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate   # Linux/Mac
# .\venv\Scripts\activate  # Windows
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```

## 🚀 How to Run
1. **Run Bayesian Analysis**  
```bash
python -m project_scripts.run_changepoint_analysis

```
2. **Start Flask API
```bash
python -m flask --app src.api.app run
```
3. Launch Dashboard
```bash
stereamlit run app.py
```

# 📊 API Endpoints

| Endpoint              | Description                     |
|----------------------|---------------------------------|
| `/api/prices`         | Historical price data           |
| `/api/events`         | Oil market events               |
| `/api/changepoints`   | Bayesian detected regime shift  |
| `/api/risk_metrics`   | Before vs After regime metrics  |

# 📈 Risk Metrics

- **Annualized Volatility**
- **Sharpe Ratio**
- **Maximum Drawdown**

# 🧪 Testing

Run:
```bash
pytest
```
# ⚠ Known Limitations

- Continuous changepoint approximation
- Sampling can be computationally expensive
- Single changepoint assumption

# 🔮 Future Work

- Multiple changepoint extension
- Volatility regime modeling (GARCH)
- SHAP-based explainability for predictive extensions


## Author
### Kalkidan Abreham
