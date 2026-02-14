import matplotlib.pyplot as plt

categories = ['Electronics', 'Clothing', 'Home']
values = [300, 450, 200]


months = [1, 2, 3, 4, 5]
sales_trend = [200, 250, 300, 400, 450]


plt.subplot(1, 2, 1)
plt.bar(categories, values)
plt.title("Category-wise Sales")
plt.xlabel("Category")
plt.ylabel("Sales")


plt.subplot(1, 2, 2)
plt.plot(months, sales_trend, marker='o')
plt.title("Sales Trend Over Time")
plt.xlabel("Month")
plt.ylabel("Sales")


plt.tight_layout()

plt.show()
