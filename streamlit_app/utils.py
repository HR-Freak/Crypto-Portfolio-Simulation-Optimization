import pandas as pd
import numpy as np

def normalize_weights_dict(weights):
    total = sum(weights.values())
    if total == 0:
        n = len(weights)
        return {k: round(100 / n) for k in weights}
    normalized = {k: (v / total) * 100 for k, v in weights.items()}
    rounded = {k: round(v) for k, v in normalized.items()}

    diff = 100 - sum(rounded.values())
    if diff != 0:
        first_key = next(iter(rounded))
        rounded[first_key] += diff

    return rounded

def compute_returns_matrix(prices, selected_coins):
    df = prices[prices["coin"].isin(selected_coins)].copy()
    pivot = df.pivot(index="Date", columns="coin", values="daily_return").dropna()
    return pivot[selected_coins]

def compute_portfolio_metrics(prices, selected_coins, weights):
    returns = compute_returns_matrix(prices, selected_coins)
    portfolio_returns = returns.dot(weights)

    annual_return = portfolio_returns.mean() * 252
    annual_volatility = portfolio_returns.std() * np.sqrt(252)
    sharpe_ratio = annual_return / annual_volatility if annual_volatility != 0 else 0

    cumulative = (1 + portfolio_returns).cumprod()
    running_max = cumulative.cummax()
    drawdown = cumulative / running_max - 1
    max_drawdown = drawdown.min()

    return {
        "annual_return": annual_return,
        "annual_volatility": annual_volatility,
        "sharpe_ratio": sharpe_ratio,
        "max_drawdown": max_drawdown,
    }

def compute_cumulative_growth(prices, selected_coins, weights):
    returns = compute_returns_matrix(prices, selected_coins)
    portfolio_returns = returns.dot(weights)
    growth = 1000 * (1 + portfolio_returns).cumprod()
    return pd.DataFrame({"date": growth.index, "portfolio": growth.values})

def get_equal_weights(selected_coins):
    n = len(selected_coins)
    return np.array([1 / n] * n)

def compute_strategy_growth(prices, selected_coins, weights, strategy_name):
    returns = compute_returns_matrix(prices, selected_coins)
    portfolio_returns = returns.dot(weights)
    growth = (1 + portfolio_returns).cumprod()

    return pd.DataFrame({
        "date": growth.index,
        "value": growth.values,
        "strategy": strategy_name
    })


def compute_strategy_metrics(prices, selected_coins, weights, strategy_name):
    metrics = compute_portfolio_metrics(prices, selected_coins, weights)
    return {
        "strategy": strategy_name,
        "annual_return": metrics["annual_return"],
        "annual_volatility": metrics["annual_volatility"],
        "sharpe_ratio": metrics["sharpe_ratio"],
        "max_drawdown": metrics["max_drawdown"],
    }