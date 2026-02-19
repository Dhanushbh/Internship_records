import numpy as np

mean = data["value"].mean()
std = data["value"].std()

data["z_score"] = (data["value"] - mean) / std
data.head()
print(mean)
print(std)
