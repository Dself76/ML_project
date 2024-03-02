import pandas as pd
from yahoo_scraper import YahooScraper
from data_preprocessor import DataPreprocessor  # Make sure to create this class based on the previous instructions

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

yahoo_scraper = YahooScraper(headers)

# Scrape data and store in pandas DataFrame
df_gainers = yahoo_scraper.scrape_table("gainers")
df_most_active = yahoo_scraper.scrape_table("most_active")

# Initialize the DataPreprocessor with your dataframes
preprocessor_gainers = DataPreprocessor(df_gainers)
preprocessor_most_active = DataPreprocessor(df_most_active)

# Preprocess the data
clean_df_gainers = preprocessor_gainers.preprocess(columns_to_drop=['Row Number'], features_to_scale=['Volume', 'Market Cap'])
clean_df_most_active = preprocessor_most_active.preprocess(columns_to_drop=['Row Number'], features_to_scale=['Volume', 'Market Cap'])

# Save the cleaned dataframes to new CSV files
clean_df_gainers.to_csv('cleaned_gainers.csv', index=False)
clean_df_most_active.to_csv('cleaned_most_active.csv', index=False)
