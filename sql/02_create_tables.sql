USE crypto_portfolio_project;

DROP TABLE IF EXISTS crypto_prices_processed;
CREATE TABLE crypto_prices_processed (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Date DATE,
    coin VARCHAR(20),
    Open DECIMAL(18,8),
    High DECIMAL(18,8),
    Low DECIMAL(18,8),
    Close DECIMAL(18,8),
    Volume DECIMAL(24,8),
    `Year` INT,
    `Quarter` INT,
    `Month` INT,
    `Month name` VARCHAR(20),
    `Daily Return` DECIMAL(18,8),
    `Cumulative Return` DECIMAL(18,8),
    `Rolling Return 30D` DECIMAL(18,8),
    `Rolling Return 90D` DECIMAL(18,8),
    `Rolling Return 90D v2` DECIMAL(18,8),
    `Rolling Volatility 30D` DECIMAL(18,8)
);

DROP TABLE IF EXISTS crypto_summary_metrics;
CREATE TABLE crypto_summary_metrics (
    id INT AUTO_INCREMENT PRIMARY KEY,
    coin VARCHAR(20),
    `Annual Return` DECIMAL(18,8),
    `Annual Volatility` DECIMAL(18,8),
    `Sharpe Ratio` DECIMAL(18,8),
    `Max Drawdown` DECIMAL(18,8)
);

DROP TABLE IF EXISTS portfolio_simulations;
CREATE TABLE portfolio_simulations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ADA DECIMAL(18,8),
    BNB DECIMAL(18,8),
    BTC DECIMAL(18,8),
    DOGE DECIMAL(18,8),
    DOT DECIMAL(18,8),
    ETH DECIMAL(18,8),
    LTC DECIMAL(18,8),
    SOL DECIMAL(18,8),
    XRP DECIMAL(18,8),
    `Return` DECIMAL(18,8),
    `Volatility` DECIMAL(18,8),
    `Sharpe Ratio` DECIMAL(18,8)
);

DROP TABLE IF EXISTS max_sharpe_portfolio;
CREATE TABLE max_sharpe_portfolio (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ratio VARCHAR(255),
    ADA DECIMAL(18,8),
    BNB DECIMAL(18,8),
    BTC DECIMAL(18,8),
    DOGE DECIMAL(18,8),
    DOT DECIMAL(18,8),
    ETH DECIMAL(18,8),
    LTC DECIMAL(18,8),
    SOL DECIMAL(18,8),
    XRP DECIMAL(18,8),
    `Return` DECIMAL(18,8),
    `Volatility` DECIMAL(18,8),
    `Sharpe` DECIMAL(18,8)
);

DROP TABLE IF EXISTS min_volatility_portfolio;
CREATE TABLE min_volatility_portfolio (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ratio VARCHAR(255),
    ADA DECIMAL(18,8),
    BNB DECIMAL(18,8),
    BTC DECIMAL(18,8),
    DOGE DECIMAL(18,8),
    DOT DECIMAL(18,8),
    ETH DECIMAL(18,8),
    LTC DECIMAL(18,8),
    SOL DECIMAL(18,8),
    XRP DECIMAL(18,8),
    `Return` DECIMAL(18,8),
    `Volatility` DECIMAL(18,8),
    `Sharpe` DECIMAL(18,8)
);

DROP TABLE IF EXISTS monthly_returns_by_coin;
CREATE TABLE monthly_returns_by_coin (
    id INT AUTO_INCREMENT PRIMARY KEY,
    coin VARCHAR(20),
    `Month` INT,
    `Month name` VARCHAR(20),
    monthly_return DECIMAL(18,8)
);

DROP TABLE IF EXISTS annual_returns_by_coin;
CREATE TABLE annual_returns_by_coin (
    id INT AUTO_INCREMENT PRIMARY KEY,
    coin VARCHAR(20),
    `Year` INT,
    annual_return DECIMAL(18,8)
);

DROP TABLE IF EXISTS best_worst_months;
CREATE TABLE best_worst_months (
    id INT AUTO_INCREMENT PRIMARY KEY,
    coin VARCHAR(20),
    best_month DECIMAL(18,8),
    worst_month DECIMAL(18,8),
    avg_monthly_return DECIMAL(18,8)
);

DROP TABLE IF EXISTS best_worst_years;
CREATE TABLE best_worst_years (
    id INT AUTO_INCREMENT PRIMARY KEY,
    coin VARCHAR(20),
    best_year DECIMAL(18,8),
    worst_year DECIMAL(18,8),
    avg_annual_return DECIMAL(18,8)
);

DROP TABLE IF EXISTS correlation_with_sp500;
CREATE TABLE correlation_with_sp500 (
    id INT AUTO_INCREMENT PRIMARY KEY,
    coin VARCHAR(20),
    `Corr With Sp500` DECIMAL(18,8)
);

DROP TABLE IF EXISTS crypto_sp500_merged;
CREATE TABLE crypto_sp500_merged (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Date DATE,
    coin VARCHAR(20),
    `Daily Return` DECIMAL(18,8),
    `Sp500 Return` DECIMAL(18,8),
    `Rolling Corr Sp500 90D` DECIMAL(18,8)
);