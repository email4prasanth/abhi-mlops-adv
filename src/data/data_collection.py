import pandas as pd
import numpy as np
import os
from sklearn.model_selection import train_test_split
import yaml

# Load DataFrame and create data
def load_data(data_filepath : str) -> pd.DataFrame:
    try:
        return pd.read_csv(data_filepath)
    except Exception as e:
        raise Exception(f"Error loading parameters from {data_filepath}:{e}")
# Load SPECIFIC parameter from params file and Create test size example 
def load_params(params_file):
    try:
        with open (params_file,"r") as file:
            params = yaml.safe_load(file)
        return params["data_collection"]["test_size"]
    except Exception as e:
        raise Exception(f"Error loading parameters from {params_file}:{e}")
# Generte train and test data in pandas dataframe format 
def split_data(data: pd.DataFrame, test_size: float) -> tuple[pd.DataFrame, pd.DataFrame]:
    try:
        return train_test_split(data, test_size = test_size, random_state = 40)
    except ValueError as e:
        raise ValueError (f"Error spliting data:{e}")
# Convert pandas datafame to .csv file
def save_data(df:pd.DataFrame, filepath:str) -> None:
    try:
        df.to_csv(filepath, index=False)
    except Exception as e:
        raise Exception (f"Error in saving data to {filepath}:{e}")

def main():
    data_filepath = r"https://raw.githubusercontent.com/plotly/datasets/refs/heads/master/diabetes.csv"
    params_file = "params.yaml"
    raw_data_path = "./data/raw"
    try: 
        data = load_data(data_filepath)
        test_size = load_params(params_file)
        train_data, test_data = split_data(data, test_size)
        # Create data path to store train_data, test_data in raw folder under data folder
        os.makedirs(raw_data_path)
        save_data(train_data, os.path.join(raw_data_path, "train.csv"))
        save_data(test_data, os.path.join(raw_data_path, "test.csv"))
    except Exception as e:
        raise Exception ("An error occured:{e}")

if __name__ == "__main__":
    main()

