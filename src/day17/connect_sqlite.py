import sqlite3
import pandas as pd

# Python connection (same as slide)
conn = sqlite3.connect("sample.db")

# ✅ Create students table (needed for JOIN)
conn.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT
);
""")

# ✅ Create departments table (same as slide)
conn.execute("""
CREATE TABLE IF NOT EXISTS departments (
    id INTEGER,
    dept TEXT
);
""")

# ✅ Insert sample data (only if tables are empty)
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

# 🔗 Join tables (same SQL as slide)
join_sql = """
SELECT students.name, departments.dept
FROM students
INNER JOIN departments
ON students.id = departments.id;
"""

# 📤 Read from SQLite using pandas (same as slide)
df = pd.read_sql_query("SELECT * FROM students", conn)
print("Students Table:\n", df)

# 📤 Run JOIN and print
df_join = pd.read_sql_query(join_sql, conn)
print("\nJOIN Result:\n", df_join)

conn.close()