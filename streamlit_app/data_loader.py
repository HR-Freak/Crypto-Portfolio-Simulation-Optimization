import pandas as pd

def standardize_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
    )
    return df

def load_data():
    prices = pd.read_csv("../Data/processed/crypto_prices_processed.csv", parse_dates=["Date"])
    summary = pd.read_csv("../Data/processed/crypto_summary_metrics.csv")
    simulations = pd.read_csv("../Data/processed/portfolio_simulations.csv")
    max_sharpe = pd.read_csv("../Data/processed/max_sharpe_portfolio.csv")
    min_vol = pd.read_csv("../Data/processed/min_volatility_portfolio.csv")

    prices = standardize_columns(prices)
    summary = standardize_columns(summary)
    simulations = standardize_columns(simulations)
    max_sharpe = standardize_columns(max_sharpe)
    min_vol = standardize_columns(min_vol)

    if "date" in prices.columns:
        prices["date"] = pd.to_datetime(prices["date"])

    return {
        "prices": prices,
        "summary": summary,
        "simulations": simulations,
        "max_sharpe": max_sharpe,
        "min_vol": min_vol,
    }