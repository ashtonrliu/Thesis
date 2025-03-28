from data_sources.Yahoofinance.yahoo_streaming import Yahoo_Streaming
from utils.export import export_df, export_dictionary
from data_cleaning.json_loader import Json_Loader

import os

class Data_Handler():
    def __init__(self):
        # Initialise Datasources
        self.yahoo = Yahoo_Streaming()

        self.create_dataset_directories()

    def create_dataset_directories(self):
        directories = [
            "datasets/historicals/csv",
            "datasets/historicals/json"
        ]

        for dir_path in directories:
            os.makedirs(dir_path, exist_ok=True)

    
    def download_ticker_grouped_json(self, ticker="AAPL", filename="APPLE"):
        df = self.yahoo.download(tickers=ticker)
        export_df(df, filename)

        dictionary = Json_Loader.file_to_dict(f"datasets/historicals/csv/{filename}.csv")
        export_dictionary(dictionary, filename)

        return dictionary
