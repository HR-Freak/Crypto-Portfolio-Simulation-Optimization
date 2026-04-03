import streamlit as st
import pandas as pd
import numpy as np
from data_loader import load_data
from utils import (
    compute_portfolio_metrics,
    compute_cumulative_growth,
    normalize_weights_dict,
    get_equal_weights,
)
from charts import (
    plot_metric_bars,
    plot_growth_chart,
    plot_weights_pie,
    plot_efficient_frontier,
)

st.set_page_config(
    page_title="Crypto Portfolio Simulator",
    page_icon="📈",
    layout="wide"
)

st.title("Crypto Portfolio Simulation & Optimization App")
st.caption("Explore portfolio risk, return, diversification, and simulation using historical cryptocurrency data.")

data = load_data()

prices = data["prices"]
summary = data["summary"]
simulations = data["simulations"]
max_sharpe = data["max_sharpe"]
min_vol = data["min_vol"]

prices = data["prices"]
summary = data["summary"]
simulations = data["simulations"]
max_sharpe = data["max_sharpe"]
min_vol = data["min_vol"]

all_coins = sorted(prices["coin"].unique().tolist())

with st.sidebar:
    st.header("Portfolio Settings")

    selected_coins = st.multiselect(
        "Select coins",
        options=all_coins,
        default=["BTC", "ETH", "SOL", "BNB"]
    )

    n_sims_to_show = st.slider(
        "Simulation sample size",
        min_value=1000,
        max_value=20000,
        value=5000,
        step=1000
    )

if not selected_coins:
    st.warning("Please select at least one coin.")
    st.stop()

tab1, tab2, tab3, tab4 = st.tabs([
    "Market Overview",
    "Portfolio Builder",
    "Monte Carlo",
    "Scenario Explorer"
])

with tab1:
    st.subheader("Market Overview")

    filtered_summary = summary[summary["coin"].isin(selected_coins)].copy()
    st.dataframe(filtered_summary, use_container_width=True)

    plot_metric_bars(filtered_summary)

with tab2:
    st.subheader("Portfolio Builder")

    st.markdown("Adjust the portfolio weights below.")

    weights = {}
    cols = st.columns(min(4, len(selected_coins)))

    for i, coin in enumerate(selected_coins):
        with cols[i % len(cols)]:
            weights[coin] = st.slider(
                f"{coin} weight (%)",
                min_value=0,
                max_value=100,
                value=int(100 / len(selected_coins)),
                step=1
            )

    total_weight = sum(weights.values())
    st.write(f"**Total weight:** {total_weight}%")

    if st.button("Normalize weights to 100%"):
        weights = normalize_weights_dict(weights)
        st.rerun()

    if total_weight != 100:
        st.warning("Weights do not sum to 100%. Metrics below are hidden until corrected.")
    else:
        weight_array = np.array([weights[c] / 100 for c in selected_coins])

        portfolio_metrics = compute_portfolio_metrics(prices, selected_coins, weight_array)
        k1, k2, k3, k4 = st.columns(4)
        k1.metric("Annual Return", f"{portfolio_metrics['annual_return']:.2%}")
        k2.metric("Annual Volatility", f"{portfolio_metrics['annual_volatility']:.2%}")
        k3.metric("Sharpe Ratio", f"{portfolio_metrics['sharpe_ratio']:.2f}")
        k4.metric("Max Drawdown", f"{portfolio_metrics['max_drawdown']:.2%}")

        left, right = st.columns([1, 2])
        with left:
            plot_weights_pie(weights)
        with right:
            growth_df = compute_cumulative_growth(prices, selected_coins, weight_array)
            plot_growth_chart(growth_df, title="Growth of $1 Portfolio")

with tab3:
    st.subheader("Monte Carlo Simulation")

    filtered_sims = simulations.copy()
    if len(filtered_sims) > n_sims_to_show:
        filtered_sims = filtered_sims.sample(n_sims_to_show, random_state=42)

    user_point = None
    if total_weight == 100:
        user_metrics = compute_portfolio_metrics(
            prices,
            selected_coins,
            np.array([weights[c] / 100 for c in selected_coins])
        )
        user_point = {
            "volatility": user_metrics["annual_volatility"],
            "return": user_metrics["annual_return"],
            "sharpe": user_metrics["sharpe_ratio"]
        }

    plot_efficient_frontier(filtered_sims, max_sharpe, min_vol, user_point)

with tab4:
    st.subheader("Scenario Explorer")
    st.info("Compare a custom portfolio to benchmark allocations such as BTC-only, equal-weight, max-Sharpe, and minimum-volatility portfolios.")