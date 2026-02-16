import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample housing dataset
df = pd.DataFrame({
    'Price': [1200000, 1500000, 1800000, 2000000, 2500000, 3000000, 10000000],
    'City': ['Delhi', 'Mumbai', 'Delhi', 'Bangalore', 'Mumbai', 'Delhi', 'Mumbai']
})

# 1. Histogram with KDE for Price
sns.histplot(data=df, x='Price', kde=True)
plt.title("Distribution of House Prices")
plt.xlabel("Price")
plt.ylabel("Count")
plt.show()

# 2. Skewness and Kurtosis
skewness = df['Price'].skew()
kurtosis = df['Price'].kurt()

print("Skewness of Price:", skewness)
print("Kurtosis of Price:", kurtosis)

# 3. Count Plot for City
sns.countplot(data=df, x='City')
plt.title("Count of Houses by City")
plt.xlabel("City")
plt.ylabel("Count")
plt.show()
