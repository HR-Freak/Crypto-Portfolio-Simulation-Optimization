# 📊 Crypto Portfolio Simulation & Optimisation

## 🚀 Project Overview

This project analyses historical cryptocurrency market data to explore return, volatility, drawdowns, diversification, correlation with traditional markets, and portfolio optimisation strategies.

The goal is to understand how crypto assets behave individually and in combination, and to evaluate whether diversification improves risk-adjusted performance.

This is not just an analysis — it is a **full data product**, combining:

- 📈 Exploratory Data Analysis  
- ⚙️ Financial metric engineering  
- 🎲 Monte Carlo portfolio simulation  
- 🗄️ SQL database layer  
- 📊 Tableau dashboards  
- 🌐 Streamlit interactive application  

---

## 💼 Business Context & Motivation

Cryptocurrency markets are extremely volatile, unpredictable, and driven by rapid regime changes.

While they offer high return potential, they also expose investors to:

- sharp drawdowns  
- unstable short-term movements  
- shifting correlations  

Traditional diversification principles don’t always hold in crypto markets.

This project explores whether **data-driven portfolio construction** can improve investment outcomes by balancing:

- return 📈  
- risk ⚠️  
- diversification 🔀  

---

## 🎯 Project Objectives

- Identify top-performing cryptocurrencies  
- Evaluate risk-adjusted performance  
- Measure volatility and drawdowns  
- Analyse time-based trends (short vs long term)  
- Evaluate diversification benefits  
- Compare crypto with S&P 500  
- Optimise portfolios (Max Sharpe / Min Volatility)  
- Compare strategies vs BTC and Equal Weight  

---

## 📦 Dataset

Data collected via **Yahoo Finance API (`yfinance`)**

### 🪙 Assets

- BTC (Bitcoin)  
- ETH (Ethereum)  
- BNB (Binance Coin)  
- SOL (Solana)  
- ADA (Cardano)  
- XRP  
- DOT (Polkadot)  
- DOGE (Dogecoin)  
- LTC (Litecoin)  

### 📊 Benchmark

- S&P 500  

### ⏱ Frequency

- Daily data  

---

## ⚙️ Analytical Pipeline

### 1️⃣ Data Collection
- Python + yfinance API  

### 2️⃣ Data Cleaning
- Missing values handling  
- Time alignment  
- Data consistency  

### 3️⃣ Feature Engineering

- Daily & cumulative returns  
- Annual return & volatility  
- Rolling returns (30D / 90D)  
- Rolling volatility  
- Maximum drawdown  
- Correlation (static & dynamic)  
- Best & worst months/years  

### 4️⃣ Portfolio Simulation 🎲

Monte Carlo simulation generates thousands of portfolios:

- Expected return  
- Volatility  
- Sharpe ratio  

Outputs:
- Max Sharpe portfolio  
- Min Volatility portfolio  
- Efficient frontier  

### 5️⃣ SQL Database 🗄️

- Database creation  
- Table structure  
- CSV ingestion  
- Validation queries  

### 6️⃣ Tableau Dashboard 📊

- Market overview  
- Risk analysis  
- Time-based trends  
- Correlation analysis  
- Portfolio insights  

### 7️⃣ Streamlit Application 🌐

Interactive app where users can:

- Select assets  
- Build portfolios  
- Input exact weights  
- Auto-adjust to 100%  
- Compare strategies  
- Explore Monte Carlo simulation  
- Visualise performance  

---

## 📏 Key Metrics

### Asset-Level

- Annual return  
- Volatility  
- Sharpe ratio  
- Maximum drawdown  
- Rolling metrics  
- Correlation  

### Portfolio-Level

- Expected return  
- Portfolio volatility  
- Sharpe ratio  
- Drawdown  
- Growth over time  
- Optimal weights  

---

## 🔍 Key Findings

### 📈 Performance

- **BNB & SOL → strongest risk-adjusted returns**  
- **DOGE → high returns but extreme volatility**  
- BTC → more stable but lower upside  

### ⚠️ Risk

- All assets show **extreme drawdowns**  
- Risk is not just volatility — downside is significant  

### ⏳ Time Behaviour

- Short-term = unstable and spike-driven  
- Long-term = clearer performance trends  

### 🔗 Correlation

- Low/moderate with S&P 500  
- Increases during crises → diversification weakens  

### 🧠 Portfolio Optimisation

- Max Sharpe = best risk-return balance  
- Min Vol = safer but lower returns  
- Diversification improves stability  

---

## 🧠 Key Takeaways

- High returns = high risk  
- Not all crypto is equal  
- Diversification helps, but fails under stress  
- Portfolio construction matters  
- Everything is a trade-off ⚖️  

---

## 🔄 From Analysis to Application

This project goes beyond static analysis.

It becomes a **decision-support tool** where users can:

- test strategies  
- simulate portfolios  
- explore outcomes interactively  

---

## 🌐 Project Outputs

### 🔗 Streamlit App  
👉 https://your-streamlit-link  

### 🔗 Tableau Dashboard  
👉 https://your-tableau-link  

---

## 🗂 Project Structure

```
Crypto-Portfolio-Simulation-Optimization/
│
├── data/
│   ├── raw/
│   │   └── crypto_prices_raw.csv
│   └── processed/
│       ├── annual_returns_by_coin.csv
│       ├── best_worst_months.csv
│       ├── best_worst_years.csv
│       ├── correlation_with_sp500.csv
│       ├── crypto_prices_processed.csv
│       ├── crypto_prices_processed_time_enriched.csv
│       ├── crypto_sp500_merged.csv
│       ├── crypto_summary_metrics.csv
│       ├── max_sharpe_portfolio.csv
│       ├── min_volatility_portfolio.csv
│       ├── monthly_returns_by_coin.csv
│       └── portfolio_simulations.csv
│
├── notebooks/
│   ├── 01_data_collection.ipynb
│   ├── 02_data_cleaning_and_returns.ipynb
│   ├── 03_risk_metrics.ipynb
│   ├── 04_portfolio_simulation.ipynb
│   └── 05_time_based_analysis.ipynb
│
├── sql/
│   ├── 01_create_database.sql
│   ├── 02_create_tables.sql
│   ├── 03_load_data.sql
│   └── 04_validation_queries.sql
│
├── streamlit_app/
│   ├── app.py
│   ├── charts.py
│   ├── data_loader.py
│   └── utils.py
│
├── tableau/
│   └── Crypto Portfolio Simulation.twbx
│
├── reports/
│   └── figures/
│
├── README.md
└── requirements.txt
```

---

## 🛠 Tools & Technologies

- Python 🐍  
- pandas  
- NumPy  
- yfinance  
- MySQL  
- Tableau  
- Streamlit  
- Plotly  

---

## 📬 Contact

👩‍💻 Marisa Oliveira  

📧 marisaisabel27@hotmail.com  
🔗 https://www.linkedin.com/in/marisa-oliveira-business-data-analyst  

---

## ⚠️ Disclaimer

Cryptocurrency markets are highly volatile and unpredictable.

This project is for **educational purposes only** and does not constitute financial advice.
