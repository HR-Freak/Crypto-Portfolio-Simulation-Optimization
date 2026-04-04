import streamlit as st
import pandas as pd
import numpy as np
from data_loader import load_data
from utils import (
    compute_portfolio_metrics,
    compute_cumulative_growth,
    normalize_weights_dict,
    get_equal_weights,
    compute_strategy_growth,
    compute_strategy_metrics,
)

from charts import (
    plot_metric_bars,
    plot_growth_chart,
    plot_weights_pie,
    plot_efficient_frontier,
    plot_strategy_comparison,
    plot_metrics_table,
)

st.set_page_config(
    page_title="Crypto Portfolio Simulator",
    page_icon="📈",
    layout="wide"
)

st.title("Crypto Portfolio Simulation & Optimization App")
st.warning("This tool is for educational purposes only. Not financial advice.")
st.caption("Explore portfolio risk, return, diversification, and simulation using historical cryptocurrency data.")
st.caption(
    "This simulator uses historical returns and does not predict future performance. It is designed for exploratory portfolio analysis only."
)

with st.spinner("Loading crypto data..."):
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
    st.caption("This tab shows fixed historical metrics for each selected coin, so it does not change when portfolio weights are adjusted.")

    filtered_summary = summary[summary["coin"].isin(selected_coins)].copy()
    st.dataframe(filtered_summary, use_container_width=True)

    plot_metric_bars(filtered_summary)

with tab2:
    st.subheader("Portfolio Builder")

    st.markdown("Adjust the portfolio weights below.")
    st.caption("Adjust the weights and see how return, risk, drawdown, and cumulative growth change.")

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
            growth_df = growth_df.rename(columns={"portfolio": "Your Portfolio"})

            equal_weight_array = np.array([1 / len(selected_coins)] * len(selected_coins))
            equal_growth_df = compute_cumulative_growth(prices, selected_coins, equal_weight_array)
            equal_growth_df = equal_growth_df.rename(columns={"portfolio": "Equal Weight"})

            comparison_growth = growth_df.merge(equal_growth_df, on="date", how="inner")

            import plotly.express as px

            fig_growth = px.line(
                comparison_growth,
                x="date",
                y=["Your Portfolio", "Equal Weight"],
                title="Growth of $1: Your Portfolio vs Equal Weight"
            )

            fig_growth.update_layout(
                legend_title_text="Strategy",
                legend=dict(
                    orientation="h",
                    yanchor="bottom",
                    y=1.02,
                    xanchor="right",
                    x=1
                )
            )

            st.plotly_chart(fig_growth, use_container_width=True)

            final_user = comparison_growth["Your Portfolio"].iloc[-1]
            final_equal = comparison_growth["Equal Weight"].iloc[-1]

            if final_user > final_equal:
                st.success(
                    f"Your portfolio outperformed Equal Weight "
                    f"(${final_user:.2f} vs ${final_equal:.2f})."
                )
            elif final_user < final_equal:
                st.info(
                    f"Your portfolio underperformed Equal Weight "
                    f"(${final_user:.2f} vs ${final_equal:.2f})."
                )
            else:
                st.info(
                    f"Your portfolio matched Equal Weight "
                    f"(${final_user:.2f})."
                )

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

    if total_weight != 100:
        st.warning("Please adjust the portfolio weights to total 100% to compare strategies.")
    else:
        selected_weight_array = np.array([weights[c] / 100 for c in selected_coins])

        # user portfolio
        user_growth = compute_strategy_growth(prices, selected_coins, selected_weight_array, "Your Portfolio")
        user_metrics_row = compute_strategy_metrics(prices, selected_coins, selected_weight_array, "Your Portfolio")

        # BTC-only 
        strategy_growth_frames = [user_growth]
        strategy_metrics_rows = [user_metrics_row]

        if "BTC" in selected_coins:
            btc_weights = np.array([1.0 if c == "BTC" else 0.0 for c in selected_coins])
            btc_growth = compute_strategy_growth(prices, selected_coins, btc_weights, "BTC Only")
            btc_metrics = compute_strategy_metrics(prices, selected_coins, btc_weights, "BTC Only")
            strategy_growth_frames.append(btc_growth)
            strategy_metrics_rows.append(btc_metrics)

        # equal weight
        equal_weights = get_equal_weights(selected_coins)
        eq_growth = compute_strategy_growth(prices, selected_coins, equal_weights, "Equal Weight")
        eq_metrics = compute_strategy_metrics(prices, selected_coins, equal_weights, "Equal Weight")
        strategy_growth_frames.append(eq_growth)
        strategy_metrics_rows.append(eq_metrics)

        # max sharpe and min vol from saved portfolios
        max_sharpe_weights = np.array([
            max_sharpe[c.lower()].iloc[0] if c.lower() in max_sharpe.columns else 0.0
            for c in selected_coins
        ])
        if max_sharpe_weights.sum() > 0:
            max_sharpe_weights = max_sharpe_weights / max_sharpe_weights.sum()
            ms_growth = compute_strategy_growth(prices, selected_coins, max_sharpe_weights, "Max Sharpe")
            ms_metrics = compute_strategy_metrics(prices, selected_coins, max_sharpe_weights, "Max Sharpe")
            strategy_growth_frames.append(ms_growth)
            strategy_metrics_rows.append(ms_metrics)

        min_vol_weights = np.array([
            min_vol[c.lower()].iloc[0] if c.lower() in min_vol.columns else 0.0
            for c in selected_coins
        ])
        if min_vol_weights.sum() > 0:
            min_vol_weights = min_vol_weights / min_vol_weights.sum()
            mv_growth = compute_strategy_growth(prices, selected_coins, min_vol_weights, "Min Volatility")
            mv_metrics = compute_strategy_metrics(prices, selected_coins, min_vol_weights, "Min Volatility")
            strategy_growth_frames.append(mv_growth)
            strategy_metrics_rows.append(mv_metrics)

        comparison_growth = pd.concat(strategy_growth_frames, ignore_index=True)
        comparison_metrics = pd.DataFrame(strategy_metrics_rows)
        comparison_metrics = comparison_metrics.sort_values(by="sharpe_ratio", ascending=False)

        plot_strategy_comparison(comparison_growth)

        best_strategy = comparison_metrics.iloc[0]["strategy"]
        st.success(f"🏆 Best risk-adjusted strategy: {best_strategy}")

        st.info(
            "Max Sharpe delivers the highest return but also the highest volatility and drawdown. "
            "Min Volatility reduces risk but sacrifices upside. "
            "Your portfolio sits between these extremes."
        )

        st.markdown("### Strategy Metrics Comparison")
        plot_metrics_table(comparison_metrics)

st.markdown("---")
st.caption("Built by Marisa Oliveira • Crypto Portfolio Simulation App • 2026")