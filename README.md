# Brent Oil Price Regime Change Analysis
## 🔍 Short Description

This project detects structural regime shifts in Brent crude oil prices using Bayesian changepoint modeling. It quantifies how geopolitical and economic shocks alter market dynamics and evaluates the financial risk impact before and after detected regime changes.

### 🛠 Built With

- PyMC (Bayesian modeling)  
- Flask (REST API)  
- Streamlit (Interactive dashboard)  
- PyTest + GitHub Actions (CI/CD)  

---

## 💼 Business Problem

Oil prices are heavily influenced by geopolitical shocks, supply disruptions, and macroeconomic crises. Financial institutions, energy traders, and policymakers need to detect structural shifts early to:

- Adjust hedging strategies  
- Reprice risk exposure  
- Rebalance portfolios  
- Understand regime-dependent volatility  

Traditional statistical models assume stable distributions.  
Markets are not stable.

### This Project Addresses

**When did the statistical behavior of Brent oil returns fundamentally change?**

---

## 🧠 Solution Overview

We implement a Bayesian changepoint model that:

- Identifies a structural break in oil returns  
- Estimates regime-specific mean and volatility  
- Quantifies uncertainty in changepoint location  
- Compares financial risk metrics across regimes  

### 🏗 Architecture
```bash
Offline Bayesian Modeling → Flask API → Streamlit Dashboard  
```

Model sampling is performed offline and results are served via API for production-style separation of concerns.


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
## 🔬 Technical Details

### 📊 Data

- Brent Oil Daily Prices  
- Weekly resampling  
- Log return transformation  
- Event dataset integration  

---

### 🧠 Model

**Bayesian continuous changepoint model:**

- τ ~ Uniform(0, N)  
- μ₁, μ₂ ~ Normal(0, 1)  
- σ ~ Exponential(1)  
- Smooth transition via sigmoid weighting  

**Sampling Configuration:**

- NUTS sampler  
- 4 chains  
- 2000 tuning steps  
- 4000 posterior draws  

---

### 📈 Evaluation

- R-hat diagnostics  
- Effective sample size  
- Posterior credible intervals  
- Regime-based risk comparison  

# ⚠ Known Limitations

- Continuous changepoint approximation
- Sampling can be computationally expensive
- Single changepoint assumption

# 🔮 Future Work

- Multiple changepoint extension
- Volatility regime modeling (GARCH)
- SHAP-based explainability for predictive extensions


## 👤 Author

### Kalkidan Abreham  

- **LinkedIn:** https://www.linkedin.com/in/kalkidan-abreham-50040b319/  
- **Email:** kalkidanabreham214@gmail.com  
- **GitHub:** https://github.com/kalkidanzabreham/brent-oil-change-point-analysis  

