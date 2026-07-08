from pathlib import Path
from load_data import load_sales
from clean_data import clean_sales
from analyze import *

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "Sample - Superstore.csv"

df = load_sales(DATA_PATH)
df = clean_sales(df)

print("========== First 5 Rows ==========")
print(df.head())

print("\n========== Data Info ==========")
print(df.info()) # Number of rows,column , Data type , Missing value

print("\n========== Statistics ==========")
print(df.describe()) # mean max min std

print("\n========== Missing Values ==========")
print(df.isnull().sum()) # Missing value

print("\n========== Data Shape ==========")
print(df.shape) # Data size

print("\n========== Column Names ==========")
print(df.columns) # Column name list

print("\n========== Summary ==========")
print(f"Total Sales : {total_sales(df):,.2f}") # Total sales
print(f"Total Profit: {total_profit(df):,.2f}") # Total profit
print(f"Average Sale: {average_sales(df):,.2f}") # Average sales

print("\n========== Sales by Category ==========")
print(sales_by_category(df))

print("\n========== Sales by Region ==========")
print(sales_by_region(df))

print("\n========== Top Customers ==========")
print(top_customers(df))

# ============ Export to .csv ============

OUTPUT_DIR = BASE_DIR / "output"

OUTPUT_DIR.mkdir(exist_ok=True)

top_customers(df).to_csv(
    OUTPUT_DIR / "top_customers.csv"
)