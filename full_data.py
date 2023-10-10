from selenium import webdriver
from selenium.webdriver.common.by import By
import yfinance as yf

class WikipediaWebScrape:

    def __init__(self):
        self.URL = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
        self.driver = webdriver.Chrome()

    def fetch_table_rows(self):
        self.driver.get(self.URL)
        table = self.driver.find_element(By.CLASS_NAME, "wikitable")
        return table.find_elements(By.TAG_NAME, "tr")

    def fetch_tickers(self):
        rows = self.fetch_table_rows()
        tickers = []
        for row in rows[1:]:  # skip header row
            columns = row.find_elements(By.TAG_NAME, "td")
            ticker_symbol = columns[0].text
            tickers.append(ticker_symbol)
        return tickers

    def close(self):
        self.driver.quit()


def fetch_data_on_date(ticker_symbol, date):
    ticker = yf.Ticker(ticker_symbol)
    data = ticker.history(date)
    return data

def calculate_percentage_move(open_price, close_price):
    return (close_price - open_price) / open_price * 100

if __name__ == "__main__":
    scraper = WikipediaWebScrape()
    tickers = scraper.fetch_tickers()
    scraper.close()

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
