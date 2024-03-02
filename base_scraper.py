import pandas as pd
from base_scraper1 import BaseScraper


class YahooScraper(BaseScraper):
    def __init__(self, headers):
        super().__init__(headers)
        self.urls = {
            "gainers": "https://finance.yahoo.com/gainers/",
            "most_active": "https://finance.yahoo.com/most-active/"
        }
        self.column_names = ['Row Number', 'Symbol', 'Name', 'Price (Intraday)', 'Change', '% Change', 'Volume',
                             'Avg Vol (3 month)', 'Market Cap', 'PE Ratio (TTM)', '52 Week Range']

    def scrape_table(self, url_key):
        soup = self.send_request(self.urls[url_key])
        if soup:
            table = soup.find('table', {'class': 'W(100%)'})
            rows = table.find_all('tr')[1:]
            data = []
            for row_number, row in enumerate(rows, start=1):
                tds = row.find_all('td')
                if len(tds) >= len(self.column_names) - 1:
                    data_row = [td.get_text().strip() for td in tds]
                    data_row.insert(0, str(row_number))
                    data.append(data_row)

            # Convert the list of data into a pandas DataFrame
            df = pd.DataFrame(data, columns=self.column_names)

            # Optional: Data cleaning and transformation goes here
            # For example, converting 'Volume' and 'Avg Vol (3 month)' to numeric and handling N/A values
            # df['Volume'] = pd.to_numeric(df['Volume'], errors='coerce').fillna(0)
            # df['Avg Vol (3 month)'] = pd.to_numeric(df['Avg Vol (3 month)'], errors='coerce').fillna(0)

            # Save the DataFrame to CSV
            self.save_to_csv_pandas(df, f'Y_{url_key}')

    def save_to_csv_pandas(self, dataframe, filename_prefix):
        # Ensure a unique filename for each run
        filename = f'{filename_prefix}_{self.current_datetime}.csv'
        dataframe.to_csv(filename, index=False, encoding='utf-8')
