import sqlite3

# 1️⃣ Create / connect to database
conn = sqlite3.connect("internship.db")
cur = conn.cursor()

# 2️⃣ Create table
cur.execute("""
CREATE TABLE IF NOT EXISTS interns (
    id INTEGER PRIMARY KEY,
    name TEXT,
    track TEXT,
    stipend INTEGER
)
""")

# 3️⃣ Insert 5 rows (only if table is empty)
cur.execute("SELECT COUNT(*) FROM interns;")
count = cur.fetchone()[0]

if count == 0:
    cur.executemany("""
    INSERT INTO interns (name, track, stipend)
    VALUES (?, ?, ?)
    """, [
        ("Alice", "Data Science", 8000),
        ("Bob", "Web Dev", 7000),
        ("John", "AI", 9000),
        ("Mary", "Data Science", 8500),
        ("Ram", "Web Dev", 6500)
    ])
    conn.commit()

# 4️⃣ SELECT only name and track (your main task)
cur.execute("SELECT name, track FROM interns;")
rows = cur.fetchall()

print("Name and Track of Interns:")
for row in rows:
    print(row)

conn.close()