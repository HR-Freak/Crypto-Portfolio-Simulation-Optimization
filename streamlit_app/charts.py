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
    title="Monte Carlo Portfolio Map",
    labels={
        "volatility": "Annual Volatility",
        "return": "Annual Return",
        "sharpe_ratio": "Sharpe Ratio"
    },
    color_continuous_scale="Blues",
    )

    fig.update_coloraxes(colorbar=dict(x=0.90))

    for trace in fig.data:
        if trace.name not in ["Max Sharpe", "Min Volatility", "Your Portfolio"]:
            trace.marker.size = 6
            trace.marker.opacity = 0.55

    if not max_sharpe.empty:
        fig.add_trace(go.Scatter(
            x=max_sharpe["volatility"],
            y=max_sharpe["return"],
            mode="markers",
            marker=dict(size=16, symbol="star", color="red"),
            name="Max Sharpe"
        ))

    if not min_vol.empty:
        fig.add_trace(go.Scatter(
            x=min_vol["volatility"],
            y=min_vol["return"],
            mode="markers",
            marker=dict(size=16, symbol="star", color="blue"),
            name="Min Volatility"
        ))

    if user_point:
        fig.add_trace(go.Scatter(
            x=[user_point["volatility"]],
            y=[user_point["return"]],
            mode="markers",
            marker=dict(size=16, symbol="diamond", color="black"),
            name="Your Portfolio"
        ))

    fig.update_layout(
    legend_title_text="Portfolio Type",
    legend=dict(
        orientation="v",
        yanchor="top",
        y=1,
        xanchor="left",
        x=1.02
    ),
    margin=dict(r=160)
    )

    st.plotly_chart(fig, use_container_width=True)

def plot_strategy_comparison(growth_df):
    fig = px.line(
        growth_df,
        x="date",
        y="value",
        color="strategy",
        title="Strategy Comparison: Growth of $1,000"
    )

    # Make the portfolio thicker
    for trace in fig.data:
        if trace.name == "Your Portfolio":
            trace.line.width = 4
        else:
            trace.line.width = 2
            trace.opacity = 0.7

    st.plotly_chart(fig, use_container_width=True)


def plot_metrics_table(metrics_df):
    formatted = metrics_df.copy()
    formatted["annual_return"] = formatted["annual_return"].map(lambda x: f"{x:.2%}")
    formatted["annual_volatility"] = formatted["annual_volatility"].map(lambda x: f"{x:.2%}")
    formatted["sharpe_ratio"] = formatted["sharpe_ratio"].map(lambda x: f"{x:.2f}")
    formatted["max_drawdown"] = formatted["max_drawdown"].map(lambda x: f"{x:.2%}")
    st.dataframe(formatted, use_container_width=True)

def plot_metrics_heatmap(metrics_df, title="Metrics Heatmap"):
    import plotly.express as px

    heatmap_df = metrics_df.copy()

    if "strategy" in heatmap_df.columns:
        index_col = "strategy"
    else:
        index_col = "coin"

    value_cols = [col for col in heatmap_df.columns if col != index_col]

    fig = px.imshow(
        heatmap_df.set_index(index_col)[value_cols],
        text_auto=".2f",
        aspect="auto",
        color_continuous_scale="Blues",
        title=title
    )

    fig.update_layout(
        xaxis_title="Metric",
        yaxis_title=""
    )

    st.plotly_chart(fig, use_container_width=True)