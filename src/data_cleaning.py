import pandas as pd

# Load raw data
input_file = "data/raw/sales_data.csv"
output_file = "data/processed/cleaned_sales_data.csv"

try:
    df = pd.read_csv(input_file)
    print("Raw data loaded successfully.")
except FileNotFoundError:
    print("sales_data.csv not found in data/raw/")
    exit()

# Basic cleaning
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

# Convert Date column if exists
if "Date" in df.columns:
    df["Date"] = pd.to_datetime(df["Date"])

# Save cleaned data
df.to_csv(output_file, index=False)
print("Cleaned data saved to:", output_file)
