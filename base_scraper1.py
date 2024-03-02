import csv
import requests
from bs4 import BeautifulSoup
from datetime import datetime

class BaseScraper:
    def __init__(self, headers):
        self.headers = headers
        # Now includes both date and time to ensure uniqueness
        self.current_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")

    def send_request(self, url):
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return BeautifulSoup(response.text, 'html.parser')
        else:
            print(f"Failed to retrieve URL: {url}")
            return None

    def save_to_csv(self, data, filename_prefix, column_names):
        # Filename now includes time to prevent overwriting
        filename = f'{filename_prefix}_{self.current_datetime}.csv'
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(column_names)
            writer.writerows(data)
