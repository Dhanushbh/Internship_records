import pandas as pd

data = {
    "Location": [" New York", "new york", "NEW YORK ", "New york"]
}

df = pd.DataFrame(data)

print(df["Location"].unique())

df["Location"] = df["Location"].str.strip().str.lower()

print(df["Location"].unique())
print(df)
