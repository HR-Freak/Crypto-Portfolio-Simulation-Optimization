# Crypto Portfolio Simulation & Optimisation

## Project Overview

This project analyses historical cryptocurrency market data to explore risk, volatility, diversification, and portfolio optimisation strategies.

The objective is to help investors better understand how different crypto assets behave and how portfolio diversification can impact risk-adjusted performance.

This project focuses on data-driven analysis of historical performance to identify optimal portfolio allocations.

The final result is an interactive dashboard that visualises market trends, risk metrics, and portfolio simulations.

_____________________________________________________________________________________________________________

## Project Objectives

This analysis aims to answer the following key questions:

- Which major cryptocurrencies delivered the best risk-adjusted returns historically?

- How volatile are different crypto assets?

- Are major cryptocurrencies highly correlated?

- Does diversification meaningfully reduce portfolio risk?

- What portfolio allocation would have maximised the Sharpe ratio historically?

- What portfolio allocation would have minimised portfolio volatility?

- How does a diversified crypto portfolio compare to holding only Bitcoin?

_____________________________________________________________________________________________________________

## Dataset

Historical price data is collected using the Yahoo Finance API through the Python yfinance library.

Assets analysed:

- Bitcoin (BTC)

- Ethereum (ETH)

- Binance Coin (BNB)

- Solana (SOL)

- Cardano (ADA)

- Ledger (XRP)

- Dorothy ((DOT)

- Dogecoin (DOGE)

- Litecoin (LTC)

Data frequency:
Daily historical prices.

_____________________________________________________________________________________________________________

## Analytical Pipeline

The project follows an end-to-end data analytics workflow.

### 1. Data Collection

Historical cryptocurrency data is retrieved using Python.

Tools used:

- Python

- yfinance

- pandas

### 2. Data Cleaning

Steps include:

- checking missing values

- aligning time series across assets

- ensuring consistent date ranges

- removing duplicates

Output dataset:

data/processed/crypto_prices_clean.csv

### 3. Feature Engineering

Financial metrics are calculated including:

- daily returns

- cumulative returns

- annualised return

- annualised volatility

- rolling volatility

- maximum drawdown

- correlation matrix

### 4. Portfolio Simulation

A Monte Carlo simulation generates thousands of random portfolio allocations.

Each portfolio is evaluated using:

- expected return

- volatility

- Sharpe ratio

This allows identification of:

- maximum Sharpe ratio portfolio

- minimum volatility portfolio

- efficient portfolio distribution

### 5. SQL Analytical Layer

Processed datasets are stored in a SQL database to support analytical queries and dashboard integration.

SQL is used to:

- structure the data

- calculate KPIs

- support dashboard visualizations

### 6. Dashboard

An interactive dashboard in Tableau visualises:

- market overview

- risk & volatility metrics

- asset correlations

- diversification insights

- portfolio simulation results

_____________________________________________________________________________________________________________

## Key Metrics

### Asset-Level Metrics

- cumulative return

- annualised return

- annualised volatility

- Sharpe ratio

- maximum drawdown

### Portfolio-Level Metrics

- expected portfolio return

- portfolio volatility

- Sharpe ratio

- optimal portfolio weights

_____________________________________________________________________________________________________________

## Project Structure

crypto-portfolio-analytics

data/
    raw/
    processed/

notebooks/
    01_data_collection.ipynb
    02_data_cleaning.ipynb
    03_risk_metrics.ipynb
    04_portfolio_simulation.ipynb

sql/
    schema.sql
    kpi_queries.sql

dashboard/
    dashboard_file.pbix

reports/
    figures/

README.md
requirements.txt

_____________________________________________________________________________________________________________

## Tools & Technologies

Python
Pandas
NumPy
SQL
Tableau
yfinance API

_____________________________________________________________________________________________________________

## Key Insights (To be completed after analysis)

This section will summarize the most important insights discovered during the analysis.

Examples may include:

- which assets show the best risk-adjusted performance

- which assets contribute most to diversification

- how portfolio allocation impacts volatility

_____________________________________________________________________________________________________________

## Future Improvements

Possible extensions of this project include:

- building a Streamlit application for interactive portfolio exploration

- mplementing experimental ML models for return forecasting

- expanding the analysis to additional crypto assets

- integrating real-time market data APIs

# Disclaimer

Cryptocurrency markets are highly volatile and unpredictable.

This project is intended for educational and analytical purposes only and should not be considered financial advice.
