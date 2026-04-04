from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]

def load_data():
    prices = pd.read_csv(
        BASE_DIR / "data" / "processed" / "crypto_prices_processed.csv",
        parse_dates=["Date"]
    )

    summary = pd.read_csv(
        BASE_DIR / "data" / "processed" / "crypto_summary_metrics.csv"
    )

    simulations = pd.read_csv(
        BASE_DIR / "data" / "processed" / "portfolio_simulations.csv"
    )

    max_sharpe = pd.read_csv(
        BASE_DIR / "data" / "processed" / "max_sharpe_portfolio.csv"
    )

    min_vol = pd.read_csv(
        BASE_DIR / "data" / "processed" / "min_volatility_portfolio.csv"
    )

    return {
        "prices": prices,
        "summary": summary,
        "simulations": simulations,
        "max_sharpe": max_sharpe,
        "min_vol": min_vol,
    }