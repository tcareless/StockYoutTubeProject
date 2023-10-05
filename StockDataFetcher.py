import yfinance as yf

def fetch_data_on_date(ticker_symbol, date):
    ticker = yf.Ticker(ticker_symbol)
    data = ticker.history(date)
    return data

if __name__ == "__main__":
    tickers = ["AAPL", "TSLA", "AMZN"]
    date = "2023-10-02"

    for ticker_symbol in tickers:
        data = fetch_data_on_date(ticker_symbol, date)
        print(f"\nData for {ticker_symbol} on {date}:")
        print(data)

