import pandas as pd
import json

def export_df(df: pd.DataFrame, filename: str):
    BASEPATH = "datasets/historicals/csv/"
    
    df.to_csv(f"{BASEPATH}{filename}.csv")

    return 

def export_dictionary(dictionary: dict, filename: str):
    BASEPATH = "datasets/historicals/json/"

    with open(f"{BASEPATH}{filename}.json", 'w') as f:
        json.dump(dictionary, f, indent=4)
    
    return