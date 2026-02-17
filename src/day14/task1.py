import pandas as pd
from sklearn.preprocessing import LabelEncoder

data = {
    "Transmission": ["Automatic", "Manual", "Automatic", "Manual"],
    "Color": ["Red", "Blue", "Green", "Red"]
}

df = pd.DataFrame(data)
print("Original Data:\n", df)


le = LabelEncoder()
df["Transmission"] = le.fit_transform(df["Transmission"])


df = pd.get_dummies(df, columns=["Color"], drop_first=True)

print("\nEncoded Data:\n", df)
