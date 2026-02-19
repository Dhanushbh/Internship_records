import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")

plt.hist(data["value"], bins=30)
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Distribution of Values")
plt.show()