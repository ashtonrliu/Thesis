import pandas as pd
import json

class Json_Loader:
    GROUP_BY = 20 # Number of entries to group by in json

    def __init__(self):
        pass


    def file_to_dict(filename):
        data = pd.read_csv(filename)

        result_dict = {}

        for i in range(len(data) - Json_Loader.GROUP_BY+1):

            start_date = data.iloc[i]['Date']
            # Get the next 20 rows starting from index i
            window = data.iloc[i:i+Json_Loader.GROUP_BY].values.tolist()
            result_dict[start_date] = window        
        
        return result_dict

    def df_to_dict(df):
        """
        Build a dictionary in which each key is a Date (index entry),
        and the value is a 2D list of the rows from that date plus the
        next 19 rows in the DataFrame. Each row is turned into a list
        of strings (one for each column entry).
        
        If there are fewer than 20 rows from a given date to the end
        of the DataFrame, that date is skipped.
        """

        # Preprocess data to be grouped
        df["Date"] = df.index                    # Copy the old date index into a new column
        df["Date"] = df["Date"].dt.strftime("%Y-%m-%d") # Format Date from TimeStamp()

        df.reset_index(drop=True, inplace=True) # Remove index
        cols = df.columns.tolist() # Reorder date to first 
        cols.remove("Date")
        df = df[["Date"] + cols]

        result_dict = {}

        for i in range(len(df) - Json_Loader.GROUP_BY+1):

            start_date = df.iloc[i]['Date']
            # Get the next 20 rows starting from index i
            window = df.iloc[i:i+Json_Loader.GROUP_BY].values.tolist()
            result_dict[start_date] = window        
        print(result_dict)
        return result_dict


