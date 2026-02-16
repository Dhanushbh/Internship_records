import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample dataset
df = pd.DataFrame({
    'Price': [20, 25, 30, 35, 40, 80, 90],          # has outliers (80, 90)
    'SquareFootage': [500, 600, 700, 800, 900, 1500, 1800],
    'Bedrooms': [1, 1, 2, 2, 3, 4, 4],
    'Bathrooms': [1, 1, 1, 2, 2, 3, 3]
})

# 1. Correlation Matrix
corr = df.corr()
print(corr)

# Heatmap
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# 2. Find any two variables with correlation > 0.8
high_corr = corr[abs(corr) > 0.8]
print("\nHighly correlated pairs (> 0.8):\n", high_corr)

# 3. Boxplot to find outliers in Price
sns.boxplot(x=df['Price'])
plt.title("Outliers in Price")
plt.xlabel("Price")
plt.show()
