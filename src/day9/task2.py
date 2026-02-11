import pandas as pd

grades = pd.Series([85, None, 92, 45, None, 78, 55])

print("Original Series:")
print(grades)

print("\nMissing values (True = missing):")
print(grades.isnull())

filled_grades = grades.fillna(0)

print("\nSeries after filling missing values with 0:")
print(filled_grades)

print("\nScores greater than 60:")
print(filled_grades[filled_grades > 60])
