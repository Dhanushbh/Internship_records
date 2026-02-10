import numpy as np


scores = np.random.randint(50, 101, size=(5, 3))


mean_scores = scores.mean(axis=0)


centered_scores = scores - mean_scores

# Output
print("Original Scores:")
print(scores)

print("\nCentered Scores (After Subtracting Subject Mean):")
print(centered_scores)
