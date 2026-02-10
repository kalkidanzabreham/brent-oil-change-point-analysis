
# Brent Oil Price Change Point Analysis

## Project Overview
This project analyzes the impact of major geopolitical and economic events on Brent crude oil prices using **Bayesian Change Point Analysis**. The objective is to identify statistically significant structural breaks in oil price dynamics and associate them with real-world events such as financial crises, geopolitical conflicts, pandemics, and OPEC policy changes.

**Business Context:**  
Birhan Energies provides data-driven insights for investors, policymakers, and energy companies. Understanding how political decisions, conflicts, sanctions, and global shocks influence oil prices supports:
- Better risk management  
- Improved investment timing  
- Policy evaluation  
- Strategic operational planning  

---

### 1. Data Understanding and Preparation
- Loaded raw Brent oil price data (`data/raw/BrentOilPrices.csv`)
- Cleaned, parsed dates, and sorted the dataset chronologically
- Computed log returns to stabilize variance and enable stationarity analysis

### 2. Exploratory Data Analysis (EDA)
- Visualized long-term price trends
- Examined volatility clustering via log returns
- Conducted Augmented Dickey-Fuller (ADF) test to confirm stationarity

### 3. Event Data Compilation
- Researched and compiled 10–15 major geopolitical and economic events
- Stored in `data/events/oil_market_events.csv` with:
  - `Date`: approximate event start date
  - `Event`: short description

### 4. Assumptions & Limitations
- Only major, widely documented events are included
- Log returns are assumed to be stationary
- Statistical correlation does not imply causation

---


### Task 2: Bayesian Change Point Modeling
- Implemented a Bayesian change point model using **PyMC**
- Estimated:
  - Change point location (`tau`)
  - Mean returns before and after regime shifts (`μ₁`, `μ₂`)
- Evaluated model convergence using trace plots and R-hat diagnostics
- Visualized posterior distributions to quantify uncertainty

**Key Insight:**  
Detected change points align with major global disruptions such as the **2008 Global Financial Crisis** and the **COVID-19 market shock**, indicating statistically significant regime changes in oil price behavior.

---

### Task 3: Event Impact Analysis & API Dashboard
- Associated detected change points with real-world geopolitical and economic events
- Interpreted impacts on price levels and volatility
- Built a **Flask-based REST API** to expose analysis results for dashboard use

---

## API Endpoints

Once the Flask server is running, the following endpoints are available:

| Endpoint | Description |
|--------|-------------|
| `/api/prices` | Historical Brent oil prices (JSON) |
| `/api/events` | Major geopolitical & economic events |
| `/api/changepoints` | Detected structural change points |

---

## Repository Structure
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
│
├── notebooks/
│ ├── 01_eda.ipynb # EDA and stationarity analysis (Task 1)
│ ├── 02_change_point_model.ipynb # Placeholder for Task 2
│ └── 03_event_impact_analysis.ipynb # Placeholder for Task 2/3
│
├── src/
│ ├── utils/
│ │ └── preprocessing.py # Functions to load and clean data
│ ├── modeling/
│ │ └── bayesian_changepoint.py # Placeholder for Task 2
│ └── api/
│ └── app.py # Placeholder for Task 3 dashboard
│
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
## Running the API Dashboard

From the project root:

```bash
export FLASK_APP=src/api/app.py   # Linux / Mac
# set FLASK_APP=src/api/app.py    # Windows

flask run
```
Access the API at:
```bash
http://127.0.0.1:5000/api/prices

http://127.0.0.1:5000/api/events

http://127.0.0.1:5000/api/changepoints
```
## Assumptions & Limitations

- Change points indicate statistical regime shifts, not definitive causality  
- Event dates are approximate and may not reflect delayed market reactions  
- The model assumes piecewise constant mean behavior  
- External macroeconomic variables were not explicitly included  

## Future Work

- Incorporate macroeconomic indicators (GDP, inflation, FX rates)  
- Extend the model to volatility regime detection  
- Build a full interactive frontend dashboard (React / Plotly)  
- Containerize and deploy the API using Docker  

## Author
### Kalkidan Abreham
