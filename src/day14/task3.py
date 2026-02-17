import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score


X = np.array([[1], [2], [3], [4], [5], [6]])
y = np.array([1, 4, 9, 16, 25, 36])  


lr = LinearRegression()
lr.fit(X, y)
y_pred_linear = lr.predict(X)
r2_linear = r2_score(y, y_pred_linear)

poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

lr_poly = LinearRegression()
lr_poly.fit(X_poly, y)
y_pred_poly = lr_poly.predict(X_poly)
r2_poly = r2_score(y, y_pred_poly)

print("R2 Score (Linear features):", r2_linear)
print("R2 Score (Polynomial features):", r2_poly)
