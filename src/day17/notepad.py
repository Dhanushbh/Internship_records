import sqlite3
import pandas as pd
import os

# Connect DB
conn = sqlite3.connect("sample.db")

# Create tables (if not exists)
conn.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT
);
""")

conn.execute("""
CREATE TABLE IF NOT EXISTS departments (
    id INTEGER,
    dept TEXT
);
""")

# Insert sample data (only once)
cur = conn.cursor()

cur.execute("SELECT COUNT(*) FROM students;")
if cur.fetchone()[0] == 0:
    cur.executemany(
        "INSERT INTO students (name) VALUES (?);",
        [("Alice",), ("Bob",), ("John",), ("Mike",), ("Olivia",)]
    )

cur.execute("SELECT COUNT(*) FROM departments;")
if cur.fetchone()[0] == 0:
    cur.executemany(
        "INSERT INTO departments (id, dept) VALUES (?, ?);",
        [
            (1, "Data Science"),
            (2, "Web Dev"),
            (3, "AI"),
            (4, "Cyber Security"),
            (5, "Data Science"),
        ]
    )

conn.commit()

# Queries
df_students = pd.read_sql_query("SELECT * FROM students;", conn)

join_sql = """
SELECT students.name, departments.dept
FROM students
INNER JOIN departments
ON students.id = departments.id;
"""
df_join = pd.read_sql_query(join_sql, conn)

conn.close()

# ✅ Save results to a text file
output_path = "result.txt"
with open(output_path, "w", encoding="utf-8") as f:
    f.write("=== Students Table ===\n")
    f.write(df_students.to_string(index=False))
    f.write("\n\n=== JOIN Result (Students + Departments) ===\n")
    f.write(df_join.to_string(index=False))

print("Results saved to result.txt")

# ✅ Open in Notepad automatically (Windows)
os.startfile(output_path)