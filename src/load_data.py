import pandas as pd

def load_sales(path):
    return pd.read_csv(path, encoding="latin1")