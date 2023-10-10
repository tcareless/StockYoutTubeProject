import yfinance as yf

def fetch_data_on_date(ticker_symbol, date):
    ticker = yf.Ticker(ticker_symbol)
    data = ticker.history(date)
    return data

def calculate_percentage_move(open_price, close_price):
    return (close_price - open_price) / open_price * 100

if __name__ == "__main__":
    tickers = ["AAPL", "TSLA", "AMZN"]
    date = "2023-10-04"

    for ticker_symbol in tickers:
        data = fetch_data_on_date(ticker_symbol, date)
        
        if not data.empty:
            open_price = data["Open"].iloc[0]
            close_price = data["Close"].iloc[0]
            percentage_move = calculate_percentage_move(open_price, close_price)
            sign = '+' if percentage_move >= 0 else '-'
            print(f"{ticker_symbol}: {sign} {abs(percentage_move):.2f}%")
        else:
            print(f"No data available for {ticker_symbol} on {date}.")
