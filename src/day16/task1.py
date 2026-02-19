import numpy as np
import matplotlib.pyplot as plt

# Small sample data
normal = np.random.normal(50, 10, 100)
right_skew = np.random.exponential(1, 100)
left_skew = -np.random.exponential(1, 100) + 50

for data, title in [(normal, "Normal"), (right_skew, "Right-Skewed"), (left_skew, "Left-Skewed")]:
    plt.hist(data, bins=20)
    plt.title(title)
    plt.show()
    
    print(title, "Mean:", data.mean(), "Median:", np.median(data))
