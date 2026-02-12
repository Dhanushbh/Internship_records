import pandas as pd

data = {
    "Price": ["$10.5", "$20.0", "$15.75"],
    "Date": ["2024-01-01", "2024-01-05", "2024-01-10"]
}

df = pd.DataFrame(data)

print(df.dtypes)

df["Price"] = df["Price"].str.replace("$", "", regex=False).astype(float)
df["Date"] = pd.to_datetime(df["Date"])

print(df.dtypes)
print(df)
