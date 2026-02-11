import pandas as pd

products = pd.Series([700, 150, 300], index=["Laptop", "Mouse", "Keyboard"])

print("Full Series:")
print(products)

print("\nPrice of Laptop:")
print(products["Laptop"])

print("\nFirst two products:")
print(products[:2])
