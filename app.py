import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(page_title="Stock Data Visualizer", layout="wide")
st.title("Stock Data Fetcher")

# Input ticker symbol
ticker = st.text_input("Enter Stock Ticker (e.g. AAPL, TSLA, MSFT):", "AAPL")

# Interval options based on Yahoo Finance limits
interval_options = {
    "1 Minute (7d)": ("7d", "1m"),
    "1 Hour (1mo)": ("1mo", "1h"),
    "1 Day (1y)": ("1y", "1d"),
}

option = st.selectbox("Choose interval:", list(interval_options.keys()))

if ticker and option:
    period, interval = interval_options[option]
    stock = yf.Ticker(ticker)
    df = stock.history(period=period, interval=interval)

    if df.empty:
        st.error("No data found for this ticker/interval.")
    else:
        # Show preview
        st.subheader(f"{option} Data Preview for {ticker}")
        st.write(f"Showing {len(df)} rows")
        st.dataframe(df)

        # Charts
        st.subheader(f"{option} Close Price Chart")
        st.line_chart(df["Close"])

        st.subheader(f"{option} Volume Chart")
        st.bar_chart(df["Volume"])
