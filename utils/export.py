import pandas as pd
import json

def export_df(df: pd.DataFrame, filename: str):
    """
    Uses a predefined basepath to export pandas dataframe to a csv file
    """

    BASEPATH = "datasets/historicals/csv/"
    
    df.to_csv(f"{BASEPATH}{filename}.csv")

    return 

def export_dictionary(dictionary: dict, filename: str):
    """
    Uses a predefined basepath to export python dictionaries to a json file
    """

    BASEPATH = "datasets/historicals/json/"

    with open(f"{BASEPATH}{filename}.json", 'w') as f:
        json.dump(dictionary, f, indent=4)
    
    return