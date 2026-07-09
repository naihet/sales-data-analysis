def total_sales(df):
    return df["Sales"].sum()

def total_profit(df):
    return df["Profit"].sum()

def average_sales(df):
    return df["Sales"].mean()

def sales_by_category(df):
    return (
        df.groupby("Category")["Sales"]
          .sum()
          .sort_values(ascending=False)
    )

def sales_by_region(df):
    return (
        df.groupby("Region")["Sales"]
          .sum()
          .sort_values(ascending=False)
    )

def top_customers(df):
    return (
        df.groupby("Customer Name")["Sales"]
          .sum()
          .sort_values(ascending=False)
          .head(10)
    )

def top_products(df, top_n=10):
    return (
        df.groupby("Product Name")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(top_n)
    )