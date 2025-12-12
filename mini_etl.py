import pandas as pd

# Extract
df = pd.read_csv("raw_data.csv")

# Transform
df = df.drop_duplicates()
df = df.fillna("Unknown")

# Load
df.to_csv("processed_data.csv", index=False)

print("ETL completed.")
