import pandas as pd
from SQLAlchemy import create_engine
import logging
import os

# ----------------------------
# LOGGING SETUP
# ----------------------------

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/etl.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("ETL Pipeline Started")

# ----------------------------
# EXTRACT
# ----------------------------

df = pd.read_csv("data/SampleSuperstore.csv")

print(f"Original Rows: {len(df)}")
logging.info(f"Original Rows: {len(df)}")

# ----------------------------
# DATA QUALITY CHECKS
# ----------------------------

duplicate_rows = df.duplicated().sum()
null_values = df.isnull().sum().sum()

print(f"Duplicate Rows: {duplicate_rows}")
print(f"Null Values: {null_values}")

logging.info(f"Duplicate Rows Found: {duplicate_rows}")
logging.info(f"Null Values Found: {null_values}")

# ----------------------------
# TRANSFORM
# ----------------------------

df.drop_duplicates(inplace=True)

# Fill missing values if any
df.fillna(0, inplace=True)

# Feature Engineering
df["Revenue_per_Item"] = (
    df["Sales"] / df["Quantity"]
)

df["Profit_Margin"] = (
    (df["Profit"] / df["Sales"]) * 100
).round(2)

df["Discount_Percentage"] = (
    df["Discount"] * 100
)

# Sales Category
df["Sales_Category"] = pd.cut(
    df["Sales"],
    bins=[0, 100, 500, 1000, float("inf")],
    labels=[
        "Low",
        "Medium",
        "High",
        "Very High"
    ]
)

print(f"Cleaned Rows: {len(df)}")
logging.info(f"Cleaned Rows: {len(df)}")

# ----------------------------
# LOAD
# ----------------------------

engine = create_engine(
    "sqlite:///database/sales.db"
)

df.to_sql(
    "sales",
    engine,
    if_exists="replace",
    index=False
)

# ----------------------------
# SUMMARY
# ----------------------------

total_sales = round(df["Sales"].sum(), 2)
total_profit = round(df["Profit"].sum(), 2)

print("\nETL Completed Successfully")
print(f"Total Sales: ${total_sales:,.2f}")
print(f"Total Profit: ${total_profit:,.2f}")

logging.info("Data Loaded Successfully into SQLite")
logging.info(f"Total Sales: {total_sales}")
logging.info(f"Total Profit: {total_profit}")
logging.info("ETL Pipeline Completed Successfully")