import pandas as pd
import json

class Json_Loader:

    def __init__(self):
        pass

    def file_to_dict(filename):
        data = pd.read_csv(filename)

        GROUP_BY = 20 # Group last 20 entries

        result_dict = {}

        for i in range(len(data) - GROUP_BY+1):

            start_date = data.iloc[i]['Date']
            # Get the next 20 rows starting from index i
            window = data.iloc[i:i+20].to_dict(orient='records')
            result_dict[start_date] = window        
        
        return result_dict

