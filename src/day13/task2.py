import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Small sample dataset
df = pd.DataFrame({
    'SquareFootage': [500, 700, 900, 1100, 1300, 1600, 2000],
    'Price': [15, 22, 35, 50, 65, 90, 130],   # example values
    'City': ['Delhi', 'Mumbai', 'Delhi', 'Bangalore', 'Mumbai', 'Delhi', 'Mumbai']
})

# Scatter Plot: SquareFootage vs Price
plt.scatter(df['SquareFootage'], df['Price'])
plt.xlabel("Square Footage")
plt.ylabel("Price")
plt.title("Square Footage vs Price")
plt.show()

# Box Plot: City vs Price
sns.boxplot(data=df, x='City', y='Price')
plt.xlabel("City")
plt.ylabel("Price")
plt.title("Price by City")
plt.show()
