LOAD DATA LOCAL INFILE '/Users/marisa/Desktop/Data Analytics/Final Project/Crypto-Portfolio-Simulation-Optimization/data/processed/crypto_summary_metrics.csv'
INTO TABLE crypto_summary_metrics
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(coin, `Annual Return`, `Annual Volatility`, `Sharpe Ratio`, `Max Drawdown`);

LOAD DATA LOCAL INFILE '/Users/marisa/Desktop/Data Analytics/Final Project/Crypto-Portfolio-Simulation-Optimization/data/processed/portfolio_simulations.csv'
INTO TABLE portfolio_simulations
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(ADA, BNB, BTC, DOGE, DOT, ETH, LTC, SOL, XRP, `Return`, `Volatility`, `Sharpe Ratio`);

LOAD DATA LOCAL INFILE '/Users/marisa/Desktop/Data Analytics/Final Project/Crypto-Portfolio-Simulation-Optimization/data/processed/crypto_prices_processed.csv'
INTO TABLE crypto_prices_processed
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(Date, coin, Open, High, Low, Close, Volume, `Year`, `Quarter`, `Month`, `Month name`, `Daily Return`, `Cumulative Return`, `Rolling Return 30D`, `Rolling Return 90D`, `Rolling Return 90D v2`, `Rolling Volatility 30D`);