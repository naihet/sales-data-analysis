from pathlib import Path
from load_data import load_sales
from clean_data import clean_sales
from analyze import *
from export import export_csv
from visualize import save_bar_chart

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

OUTPUT_DIR = BASE_DIR / "output" # To output path
IMAGE_DIR = BASE_DIR / "images" # To images path

# ==================================* Top Customers *==================================
top_customer = top_customers(df)
print("\n========== Top Customers ==========")
print(top_customer)

export_csv(
    top_customer,
    "top_customers.csv",
    OUTPUT_DIR
) # export csv to output folder

save_bar_chart(
    top_customer,
    "Top 10 Customers",
    "Customer",
    "Sales",
    "top_customers.png",
    IMAGE_DIR
)

# ==================================* Top Products *==================================
top_product = top_products(df)
print("\n===== Top 10 Products =====")
print(top_product)

export_csv(
    top_product,
    "top_products.csv",
    OUTPUT_DIR
) # export csv to output folder

save_bar_chart(
    top_product,
    "Top 10 Products",
    "Product",
    "Sales",
    "top_products.png",
    IMAGE_DIR
)

# ==================================* Profit By Region *==================================
profit_region = profit_by_region(df)
print("\n===== Profit by Region =====")
print(profit_region)

export_csv(
    profit_region,
    "profit_by_region.csv",
    OUTPUT_DIR
) # export csv to output folder

save_bar_chart(
    profit_region,
    "Profit by Region",
    "Region",
    "Profit",
    "profit_by_region.png",
    IMAGE_DIR
)

# ==================================* Monthly Sales *==================================
monthly = monthly_sales(df)
print("\n===== Monthly Sales =====")
print(monthly)

export_csv(
    monthly,
    "monthly_sales.csv",
    OUTPUT_DIR
) # export csv to output folder

save_bar_chart(
    monthly,
    "Monthly Sales",
    "Month",
    "Sales",
    "monthly_sales.png",
    IMAGE_DIR
)