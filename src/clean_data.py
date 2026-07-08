import pandas as pd

def clean_sales(df):
    df = df.drop_duplicates() # Delete duplicate data
    df.columns = df.columns.str.strip() # Delete front and back blanks
    return df
