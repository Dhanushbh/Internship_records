import sqlite3
import pandas as pd

# 🔗 Open database (your path is already correct)
conn = sqlite3.connect(r"D:/DS_AI_Internship/src/day17/sample.db")
print("Database opened successfully!")

# 📋 Show tables
tables = pd.read_sql_query(
    "SELECT name FROM sqlite_master WHERE type='table';", conn
)
print("\nTables in database:")
print(tables)

# 📊 Show students table (if exists)
try:
    df_students = pd.read_sql_query("SELECT * FROM students;", conn)
    print("\nStudents table:")
    print(df_students)
except Exception as e:
    print("\nStudents table not found:", e)

# 📊 Show departments table (if exists)
try:
    df_dept = pd.read_sql_query("SELECT * FROM departments;", conn)
    print("\nDepartments table:")
    print(df_dept)
except Exception as e:
    print("\nDepartments table not found:", e)

# 🔗 Show JOIN result
join_sql = """
SELECT students.name, departments.dept
FROM students
INNER JOIN departments
ON students.id = departments.id;
"""
try:
    df_join = pd.read_sql_query(join_sql, conn)
    print("\nJOIN result:")
    print(df_join)
except Exception as e:
    print("\nJOIN failed:", e)

conn.close()