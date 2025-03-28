from alpaca.data.historical import CryptoHistoricalDataClient
from alpaca.data.requests import CryptoBarsRequest
from alpaca.data.timeframe import TimeFrame
from datetime import datetime, timezone

import requests
import pandas as pd
import os

class Alpaca_Streaming():
    def __init__(self):
        self.client = CryptoHistoricalDataClient()
        self.headers = {
            "accept": "application/json",
            "APCA-API-KEY-ID": f'{os.getenv("APCA-API-KEY-ID")}',
            "APCA-API-SECRET-KEY": f'{os.getenv("APCA-API-SECRET-KEY")}'
        }

    
    def histroical_crypto(self, symbols="BTC/USD", start=None, end=None, limit=10000, timeframe="1Day"): # https://docs.alpaca.markets/reference/cryptobars-1
        # An API to return historical bars for given crypto(s) between date range
        # Symbols are given as a comma separated crypto symbols e.g. BTC/USD,LTC/USD
        # Dates can be given in the form YYYY-MM-DD
        # Timeframes: [1-59]Min, [1-23]Hour, 1Day, 1Week, [1,2,3,4,6,12]Month


        params = {
            "symbols": symbols,  # default symbols
            "timeframe": timeframe,      # default timeframe
            "limit": limit            # default limit
        }
        
        if start:
            params["start"] = start
        if end:
            params["end"] = end

        url = "https://data.alpaca.markets/v1beta3/crypto/us/bars"
        next_page_token = None
        all_dfs = []
        request_index = 0

        while True:
            # Update the page token if necessary.
            if next_page_token:
                params["page_token"] = next_page_token
            else:
                params.pop("page_token", None)  # Remove if not needed

            # Make the API call using the params dictionary.
            response = requests.get(url, headers=self.headers, params=params)
            print("request_index", request_index, response)
            data = response.json()

            # Process each symbol's records.
            for symbol, records in data["bars"].items():
                temp_df = pd.json_normalize(records)
                temp_df["symbol"] = symbol
                all_dfs.append(temp_df)

            # Check for the next_page_token to continue paging.
            next_page_token = data.get("next_page_token")
            if not next_page_token:
                break

            request_index += 1

        # Concatenate all the individual DataFrames.
        df = pd.concat(all_dfs, ignore_index=True)

        # Rename columns for clarity.
        rename_map = {
            'c': 'close',
            'h': 'high',
            'l': 'low',
            'n': 'num_trades',
            'o': 'open',
            't': 'timestamp',
            'v': 'volume',
            'vw': 'vwap'
        }
        df.rename(columns=rename_map, inplace=True)

        return df
    

    def call_auction(self, stock, start=None, end=None, limit=10000): # https://docs.alpaca.markets/reference/stockauctions-1
        # An API to return auction prices for a list of stock symbols between specified dates

        # If start is not provided, defaults to beginning of day
        # If end is notprovided, defaults to end of current day
        

        url = f"https://data.alpaca.markets/v2/stocks/auctions?limit={limit}&feed=sip&sort=asc&symbols={stock}"

        response = requests.get(url, headers=self.headers).json()["auctions"]
        print(response)

        

        return response
    
    def historical_stocks(self, symbols="AAPL,TSLA", start=None, end=None, limit=10000, timeframe="1Day"): # https://docs.alpaca.markets/reference/stockbars
        # An API to return historical bars for given stock(s) between date range
        # Symbols are given as a comma separated string
        # Dates can be given in the form YYYY-MM-DD
        # Timeframes: [1-59]Min, [1-23]Hour, 1Day, 1Week, [1,2,3,4,6,12]Month

        params = {
            "symbols": symbols,  # default symbols
            "timeframe": timeframe,      # default timeframe
            "limit": limit            # default limit
        }
        
        if start:
            params["start"] = start
        if end:
            params["end"] = end

        url = "https://data.alpaca.markets/v2/stocks/bars"
        next_page_token = None
        all_dfs = []
        request_index = 0

        while True:
            # Update the page token if necessary.
            if next_page_token:
                params["page_token"] = next_page_token
            else:
                params.pop("page_token", None)  # Remove if not needed

            # Make the API call using the params dictionary.
            response = requests.get(url, headers=self.headers, params=params)
            print("request_index", request_index, response)
            data = response.json()

            # Process each symbol's records.
            for symbol, records in data["bars"].items():
                temp_df = pd.json_normalize(records)
                temp_df["symbol"] = symbol
                all_dfs.append(temp_df)

            # Check for the next_page_token to continue paging.
            next_page_token = data.get("next_page_token")
            if not next_page_token:
                break

            request_index += 1

        # Concatenate all the individual DataFrames.
        df = pd.concat(all_dfs, ignore_index=True)

        # Rename columns for clarity.
        rename_map = {
            'c': 'close',
            'h': 'high',
            'l': 'low',
            'n': 'num_trades',
            'o': 'open',
            't': 'timestamp',
            'v': 'volume',
            'vw': 'vwap'
        }
        df.rename(columns=rename_map, inplace=True)

        return df
