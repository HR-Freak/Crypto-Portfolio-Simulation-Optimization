# Crypto Portfolio Simulation & Optimisation

## Project Overview

This project analyses historical cryptocurrency market data to explore return, volatility, drawdowns, diversification, correlation with traditional markets, and portfolio optimisation strategies.

The main goal is to understand how major crypto assets behave individually and in combination, and to evaluate whether diversification can improve risk-adjusted performance.

The project combines:

- exploratory data analysis
- financial metric engineering
- Monte Carlo portfolio simulation
- SQL-based data storage
- Tableau dashboards for storytelling
- a Streamlit application for interactive portfolio analysis

The final result is a **hybrid analytics product** that blends data science, visualisation, and interactivity.

---

## Business Context & Motivation

Cryptocurrency markets are known for extreme volatility, rapid regime changes, and speculative dynamics.  
While they offer significant return potential, they also expose investors to substantial downside risk and instability.

Traditional portfolio theory suggests diversification as a way to optimise risk-adjusted performance.  
However, in crypto markets, this assumption is not always straightforward:

- correlations between assets can shift rapidly  
- extreme drawdowns can occur across all assets simultaneously  
- short-term performance is often driven by unpredictable spikes  

This project was developed to explore whether **data-driven portfolio construction can improve investment outcomes** in such an environment.

The goal is to move beyond individual asset analysis and provide a **systematic framework for evaluating crypto portfolios**, balancing return, risk, and diversification.

---

## Project Objectives

This analysis aims to answer the following questions:

- Which cryptocurrencies delivered the strongest historical returns?
- Which assets performed best on a risk-adjusted basis?
- How volatile are different crypto assets?
- How severe were historical drawdowns?
- How do short-term and long-term trends differ?
- Which months and years were best and worst for each asset?
- How correlated are cryptocurrencies with the S&P 500?
- Does diversification reduce risk meaningfully?
- What portfolio allocation maximises Sharpe ratio?
- What allocation minimises volatility?
- How does a custom portfolio compare to benchmark strategies?

---

## Dataset

Historical data was collected using the Yahoo Finance API via `yfinance`.

### Assets analysed

- Bitcoin (BTC)
- Ethereum (ETH)
- Binance Coin (BNB)
- Solana (SOL)
- Cardano (ADA)
- XRP (XRP)
- Polkadot (DOT)
- Dogecoin (DOGE)
- Litecoin (LTC)

### Benchmark

- S&P 500 index

### Frequency

- Daily historical prices

---

## Analytical Pipeline

### 1. Data Collection

- Python + yfinance API  
- Automated retrieval of historical crypto and benchmark data  

### 2. Data Cleaning

- handling missing values  
- aligning time series  
- standardising formats  
- ensuring consistent date ranges  

### 3. Feature Engineering

Key financial metrics:

- daily returns  
- cumulative returns  
- annual return  
- annual volatility  
- rolling returns (30D / 90D)  
- rolling volatility  
- maximum drawdown  
- correlation with S&P 500  
- best & worst months  
- best & worst years  

### 4. Portfolio Simulation

Monte Carlo simulation generates thousands of random portfolios.

Each portfolio is evaluated using:

- expected return  
- volatility  
- Sharpe ratio  

Outputs:

- maximum Sharpe portfolio  
- minimum volatility portfolio  
- efficient frontier  

### 5. SQL Database

A MySQL database stores processed datasets.

Includes:

- database creation  
- table definitions  
- CSV ingestion  
- validation queries  

### 6. Tableau Dashboard

Interactive dashboards communicate insights:

- performance overview  
- risk analysis  
- time-based trends  
- correlation analysis  
- portfolio optimisation  

### 7. Streamlit Application

An interactive app allows users to:

- select assets  
- build custom portfolios  
- input exact weights  
- auto-adjust allocations to 100%  
- compare strategies  
- explore Monte Carlo simulations  
- visualise results dynamically  

---

## Key Metrics

### Asset-Level

- annual return  
- annual volatility  
- Sharpe ratio  
- maximum drawdown  
- rolling returns  
- rolling volatility  
- correlation  

### Portfolio-Level

- expected return  
- volatility  
- Sharpe ratio  
- drawdown  
- cumulative growth  
- optimal weights  

---

## Key Findings

### Performance & Risk

- **BNB and SOL show strong risk-adjusted performance**
- **DOGE delivers high returns but extreme volatility**
- BTC is more stable but with lower upside

### Drawdowns

- All assets experience **severe drawdowns**
- Risk is not just volatility — **downside risk is substantial**

### Time-Based Behaviour

- Short-term returns are unstable and spike-driven  
- Longer-term trends reveal clearer performance regimes  

### Correlation & Diversification

- Crypto shows **low-to-moderate correlation with S&P 500**
- BUT correlation increases during stress → diversification weakens  

### Portfolio Optimisation

- Max Sharpe portfolio balances return and risk best  
- Min Volatility reduces risk but sacrifices return  
- Diversified portfolios outperform naive strategies  

---

## Key Takeaways

- High returns in crypto come with extreme risk  
- Risk-adjusted performance varies widely across assets  
- Diversification helps — but is not reliable in crises  
- Portfolio construction significantly impacts outcomes  
- There is no perfect portfolio — only trade-offs  

This highlights the importance of **dynamic, data-driven portfolio decisions**.

---

## From Analysis to Application

To bridge analysis and usability, this project was extended into an interactive tool.

Users can:

- test different allocations  
- explore scenarios  
- compare strategies  
- visualise outcomes instantly  

This transforms the project from a **static analysis** into a **decision-support system**.

---

## Project Outputs

### Streamlit App  
Interactive portfolio simulator  
👉 https://crypto-portfolio-simulation-optimization-isaoli.streamlit.app/  

### Tableau Dashboard  
Visual storytelling dashboards  
👉 https://public.tableau.com/views/CryptoPortfolioSimulation/Summary?:language=pt-BR&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link

---

## Project Structure
Crypto-Portfolio-Simulation-Optimization/

├── data/
│ ├── raw/
│ └── processed/
│
├── notebooks/
│
├── sql/
│
├── streamlit_app/
│
├── tableau/
│
├── reports/
│
├── README.md
└── requirements.txt


---

## Tools & Technologies

- Python  
- pandas  
- NumPy  
- yfinance  
- MySQL  
- Tableau Public  
- Streamlit  
- Plotly  

---

## Future Improvements

- real-time data integration  
- more assets  
- rebalancing strategies  
- advanced optimisation constraints  
- predictive modelling  

---

## Disclaimer

Cryptocurrency markets are highly volatile and unpredictable.

This project is for educational purposes only and does not constitute financial advice.