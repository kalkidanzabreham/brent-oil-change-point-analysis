# Brent Oil Price Change Point Analysis 

## Project Overview
This project aims to analyze the impact of major geopolitical and economic events on Brent oil prices over the past decades. Using Bayesian change point analysis, the study seeks to identify structural breaks in the time series and associate them with key market events.

**Business Context:**  
Birhan Energies provides data-driven insights for investors, policymakers, and energy companies. Understanding how political decisions, conflicts, sanctions, and OPEC policies affect oil prices can improve risk management and strategic decision-making.

---

## Interim Submission Scope
This interim submission covers **Task 1**:

1. **Data Understanding and Preparation**
   - Loaded raw Brent oil price data (`data/raw/BrentOilPrices.csv`)
   - Cleaned and sorted the data by date
   - Calculated log returns for stationarity analysis

2. **Exploratory Data Analysis (EDA)**
   - Plotted price series to identify trends, volatility, and major shifts
   - Plotted log returns to highlight volatility clustering
   - Performed stationarity test (ADF) on log returns

3. **Event Data Compilation**
   - Compiled 10–15 key geopolitical and economic events impacting oil prices
   - Structured in `data/events/oil_market_events.csv` with:
     - `Date` – approximate start date of the event
     - `Event` – short description

4. **Assumptions & Limitations**
   - Only major, well-documented events are included
   - Analysis assumes log returns are stationary
   - Correlation does not imply causation; change points indicate statistical shifts, not proof of direct cause

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


