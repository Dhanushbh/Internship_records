import pandas as pd

usernames = pd.Series([' Alice ', 'bOB', ' Charlie_Data ', 'daisy'])

cleaned = usernames.str.strip().str.lower()

print("Cleaned names:")
print(cleaned)

print("\nContains letter 'a':")
print(cleaned.str.contains('a'))
