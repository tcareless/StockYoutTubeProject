from selenium import webdriver
from selenium.webdriver.common.by import By
# hello world
class WikipediaWebScrape:

    def __init__(self):
        self.URL = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
        self.driver = webdriver.Chrome()

    def fetch_table_rows(self):
        self.driver.get(self.URL)
        table = self.driver.find_element(By.CLASS_NAME, "wikitable")
        return table.find_elements(By.TAG_NAME, "tr")

    def print_header(self):
        rows = self.fetch_table_rows()
        header = rows[0].find_elements(By.TAG_NAME, "th")
        print([x.text for x in header])

    def print_ticker_and_company(self):
        rows = self.fetch_table_rows()
        for row in rows[1:]:  # skip header row
            columns = row.find_elements(By.TAG_NAME, "td")
            ticker_symbol = columns[0].text
            company_name = columns[1].text
            print(f"{ticker_symbol}\t{company_name}")

    def print_only_tickers(self):
        rows = self.fetch_table_rows()
        for row in rows[1:]:  # skip header row
            columns = row.find_elements(By.TAG_NAME, "td")
            ticker_symbol = columns[0].text
            print(ticker_symbol)

    def close(self):
        self.driver.quit()

if __name__ == "__main__":
    scraper = WikipediaWebScrape()

    # Uncomment the desired method
    #scraper.print_header()
    #scraper.print_ticker_and_company()
    scraper.print_only_tickers()

    scraper.close()
