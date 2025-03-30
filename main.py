from data_handler import Data_Handler

def main():
    """
    Initialise dataset calls from here
    """

    data_handler = Data_Handler()
    data_handler.download_ticker_grouped_json("AAPL", "APPLE", start="2021-01-01", end="2024-01-01")
    # data_handler.download_ticker_grouped_json("^GSPC", "SP500")

if __name__ == "__main__":
    main()

    # Secret_Manager() # Loads ENV file to call API keys

    # Initialise Downloader
    

    # Call Historical returns
    # sp500 = yahoo.download(tickers="^GSPC")
    # export_df(sp500, "SP500")

    # aapl = yahoo.download(tickers="AAPL")
    # export_df(aapl, "APPLE")

    # Create json
    # data_loader = Json_Loader()

    # print(aapl)
    # print(pd.read)
    # aapl_json = Json_Loader.file_to_json("datasets/historicals/csv/APPLE.csv")
    # export_json(aapl_json, "APPLE")
    # sp500_json = Json_Loader.file_to_json("datasets/historicals/SP500.csv")

    # print(aapl_json)
    

    # Historical Returns
    # alp = Alpaca_Streaming()
    # stocks = alp.historical_bars(symbols="AAPL,TSLA,NVDA,INTC,F,PLTR,LCID,", limit=10000, start="1900-01-01") # Earliest possible date to query as much data, 
    # print(stocks)
    # stocks.to_csv(f"datasets/historicals/stocks.csv", index=False)

    # crypto = alp.histroical_crypto(symbols="BTC/USD", limit=10000, start="1900-01-01")
    # crypto.to_csv(f"datasets/historicals/crypto.csv", index=False)
    # print(crypto)

    
    # yahoo.to_csv(f"datasets/historicals/crypto.csv", index=False)
   
    # Nasdaq index
    # print(yahoo.download(tickers="^IXIC"))
    
    # S&P 500


    # asset gold, silver, btc
    # print(yahoo.download(tickers="GC=F"))

    # print(yahoo.download(tickers="BTC-USD"))
    # gold.to_csv(f"datasets/historicals/gold.csv", index=False)

    # US long term 5-year 10-year 15-year 20-year bonds 
    # Bond of japanese currecy
    # Exchange rates
    # How to separate 