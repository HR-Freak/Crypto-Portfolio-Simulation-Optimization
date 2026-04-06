USE crypto_portfolio_project;

SELECT COUNT(*) AS rows_prices FROM crypto_prices_processed;
SELECT COUNT(*) AS rows_summary FROM crypto_summary_metrics;
SELECT COUNT(*) AS rows_simulations FROM portfolio_simulations;
SELECT COUNT(*) AS rows_max_sharpe FROM max_sharpe_portfolio;
SELECT COUNT(*) AS rows_min_vol FROM min_volatility_portfolio;
SELECT COUNT(*) AS rows_monthly FROM monthly_returns_by_coin;
SELECT COUNT(*) AS rows_annual FROM annual_returns_by_coin;
SELECT COUNT(*) AS rows_best_worst_months FROM best_worst_months;
SELECT COUNT(*) AS rows_best_worst_years FROM best_worst_years;
SELECT COUNT(*) AS rows_corr_static FROM correlation_with_sp500;
SELECT COUNT(*) AS rows_corr_merged FROM crypto_sp500_merged;

SELECT coin, `Annual Return`, `Sharpe Ratio`
FROM crypto_summary_metrics
ORDER BY `Sharpe Ratio` DESC;

SELECT coin, `Annual Volatility`, `Max Drawdown`
FROM crypto_summary_metrics
ORDER BY `Annual Volatility` DESC;

SELECT coin, best_month, worst_month, avg_monthly_return
FROM best_worst_months
ORDER BY avg_monthly_return DESC;

SELECT coin, best_year, worst_year, avg_annual_return
FROM best_worst_years
ORDER BY avg_annual_return DESC;

SELECT coin, `Corr With Sp500`
FROM correlation_with_sp500
ORDER BY `Corr With Sp500` DESC;