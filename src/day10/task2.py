import pandas as pd

df = pd.read_csv("customer_orders.csv")

print("Before cleaning shape:", df.shape)
print(df.isna().sum())

for col in df.select_dtypes(include="number").columns:
    df[col] = df[col].fillna(df[col].median())

df = df.drop_duplicates()

print("After cleaning shape:", df.shape)
print(df.head())
