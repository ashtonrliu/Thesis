import yfinance as yf

class Yahoo_Streaming():
    def __init__(self):
        pass
    
    def download(self, tickers="^GSPC", start=None, end=None, interval="1d"): # https://yfinance-python.org/reference/api/yfinance.download.html#yfinance.download
        """
        Download a specific Stock and send the data to a csv file
        """

        # Date Format: YYYY-MM-DD

        data = yf.download(tickers=tickers, start=start, end=end, interval=interval, auto_adjust=False, progress=False, multi_level_index=False)  
        data["Ticker"] = tickers
        data.reset_index()
        # print(type(data))

        return data

