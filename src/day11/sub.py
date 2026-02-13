import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y1 = [2, 4, 6, 8]
y2 = [1, 4, 9, 16]

plt.subplot(1, 2, 1)
plt.plot(x, y1)
plt.title("Line Plot")

plt.subplot(1, 2, 2)
plt.bar(x, y2)
plt.title("Bar Plot")

plt.show()
