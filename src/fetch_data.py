import yfinance as yf
import os

def fetch_data(ticker="AAPL"):
    stock = yf.Ticker(ticker)

    # Make sure data directory exists
    os.makedirs("data", exist_ok=True)

    # Daily (1 year)
    daily = stock.history(period="1y", interval="1d")
    daily.to_csv("data/daily.csv")

    # Hourly (1 month)
    hourly = stock.history(period="1mo", interval="1h")
    hourly.to_csv("data/hourly.csv")

    # Minute (7 days)
    minute = stock.history(period="7d", interval="1m")
    minute.to_csv("data/minute.csv")

    print(f"Data for {ticker} saved in data/ folder.")

if __name__ == "__main__":
    fetch_data("AAPL")
