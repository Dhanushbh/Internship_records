import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, MinMaxScaler


age = [[22], [25], [30], [35], [40]]
salary = [[20000], [30000], [45000], [60000], [80000]]


plt.hist([x[0] for x in age])
plt.title("Age - Before Scaling")
plt.show()


std = StandardScaler()
age_std = std.fit_transform(age)

plt.hist(age_std)
plt.title("Age - After Standardization")
plt.show()


mm = MinMaxScaler()
age_norm = mm.fit_transform(age)

plt.hist(age_norm)
plt.title("Age - After Normalization")
plt.show()
