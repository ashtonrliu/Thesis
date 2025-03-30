from data_sources.Yahoofinance.yahoo_streaming import Yahoo_Streaming
from utils.export import export_df, export_dictionary
from data_cleaning.json_loader import Json_Loader

import os

class Data_Handler():
    def __init__(self):
        """
        Initialises requirements for downloading and storing data, the data sources and the data storage
        """
        # Initialise Datasources
        self.yahoo = Yahoo_Streaming()

        self.create_dataset_directories()

    def create_dataset_directories(self):
        """
        Checks if directories already exists, then creates if they don't
        """

        directories = [
            "datasets/historicals/csv",
            "datasets/historicals/json"
        ]

        for dir_path in directories:
            os.makedirs(dir_path, exist_ok=True)

    
    def download_ticker_grouped_json(self, ticker="AAPL", filename="APPLE", start="2021-01-01", end=None):
        """
        Function takes a ticker and downloads the data from yahoofinance from a start and end date.

        It then stores the data in datasets/historicals/csv and datasets/historicals/json. The json file data contains
        a list of dates. Each of those dates contains data for itself and the next 19 days. 

        The data for each entry is in the following format without the labels:
        

        "2021-01-04": [
            [
                Date: "2021-01-04",
                Adj Close: 126.41,
                Close: 129.41,
                High: 133.61,
                Low: 126.76,
                Open: 133.52,
                Volume: 143301900,
                Ticker: "AAPL"
            ] , 
            ... Price data for the next 19 days
        ] 

        """

        df = self.yahoo.download(tickers=ticker, start=start, end=end)
        dictionary = Json_Loader.df_to_dict(df)
        export_dictionary(dictionary, filename)

        # CSV handling
        # export_df(df, filename)
        # dictionary = Json_Loader.file_to_dict(f"datasets/historicals/csv/{filename}.csv")

        return dictionary
