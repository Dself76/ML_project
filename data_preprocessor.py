import pandas as pd
from sklearn.preprocessing import StandardScaler

class DataPreprocessor:
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def handle_missing_values(self):
        # Fill missing numeric values with the median
        self.dataframe.fillna(self.dataframe.median(), inplace=True)
        # Assuming you want to fill missing values in categorical data with the mode (most frequent value)
        for column in self.dataframe.select_dtypes(include=['object']).columns:
            self.dataframe[column].fillna(self.dataframe[column].mode()[0], inplace=True)

    def convert_data_types(self):
        # Convert 'Volume' and 'Avg Vol (3 month)' to float, removing commas and converting M/B to numerical values
        for column in ['Volume', 'Avg Vol (3 month)', 'Market Cap']:
            self.dataframe[column] = self.dataframe[column].replace({',': '', 'M': 'e6', 'B': 'e9'}, regex=True).astype(float)
        # Convert '% Change' from string to float
        self.dataframe['% Change'] = self.dataframe['% Change'].str.rstrip('%').astype(float) / 100

    def drop_unnecessary_columns(self, columns_to_drop):
        # Drop specified columns
        self.dataframe.drop(columns_to_drop, axis=1, inplace=True)

    def scale_features(self, features):
        # Scale specified numerical features
        scaler = StandardScaler()
        self.dataframe[features] = scaler.fit_transform(self.dataframe[features])

    def preprocess(self, columns_to_drop=[], features_to_scale=[]):
        self.handle_missing_values()
        self.convert_data_types()
        if columns_to_drop:
            self.drop_unnecessary_columns(columns_to_drop)
        if features_to_scale:
            self.scale_features(features_to_scale)
        return self.dataframe
