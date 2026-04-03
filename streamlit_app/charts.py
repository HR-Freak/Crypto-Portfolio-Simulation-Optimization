import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

def plot_metric_bars(summary_df):
    fig = px.bar(
        summary_df,
        x="coin",
        y="sharpe_ratio",
        title="Sharpe Ratio by Coin"
    )
    st.plotly_chart(fig, use_container_width=True)

def plot_weights_pie(weights):
    fig = px.pie(
        names=list(weights.keys()),
        values=list(weights.values()),
        title="Portfolio Weights"
    )
    st.plotly_chart(fig, use_container_width=True)

def plot_growth_chart(growth_df, title="Growth"):
    fig = px.line(
        growth_df,
        x="date",
        y="portfolio",
        title=title
    )
    st.plotly_chart(fig, use_container_width=True)

def plot_efficient_frontier(simulations, max_sharpe, min_vol, user_point=None):
    fig = px.scatter(
        simulations,
        x="volatility",
        y="return",
        color="sharpe_ratio",
        title="Efficient Frontier"
    )

    if not max_sharpe.empty:
        fig.add_trace(go.Scatter(
            x=max_sharpe["volatility"],
            y=max_sharpe["return"],
            mode="markers",
            marker=dict(size=14, symbol="star", color="red"),
            name="Max Sharpe"
        ))

    if not min_vol.empty:
        fig.add_trace(go.Scatter(
            x=min_vol["volatility"],
            y=min_vol["return"],
            mode="markers",
            marker=dict(size=14, symbol="star", color="blue"),
            name="Min Volatility"
        ))

    if user_point:
        fig.add_trace(go.Scatter(
            x=[user_point["volatility"]],
            y=[user_point["return"]],
            mode="markers",
            marker=dict(size=14, symbol="diamond", color="black"),
            name="Your Portfolio"
        ))

    st.plotly_chart(fig, use_container_width=True)