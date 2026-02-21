import sqlite3
import pandas as pd
import os

DB_PATH = "internship_agg.db"

# Fresh DB every run (avoids lock issues)
if os.path.exists(DB_PATH):
    os.remove(DB_PATH)

with sqlite3.connect(DB_PATH, timeout=30) as conn:
    # Create table
    conn.execute("""
    CREATE TABLE interns (
        intern_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        track TEXT,
        stipend INTEGER
    );
    """)

    # Insert sample data
    conn.executemany("""
    INSERT INTO interns (name, track, stipend) VALUES (?, ?, ?)
    """, [
        ("Alice", "Data Science", 6000),
        ("Bob", "AI", 4500),
        ("John", "Data Science", 7000),
        ("Mike", "Web Dev", 4000),
        ("Olivia", "Data Science", 4800),
        ("Rahul", "AI", 8000),
        ("Neha", "Web Dev", 5500)
    ])

    # 1️⃣ FILTER: Data Science interns with stipend > 5000
    filter_query = """
    SELECT name, track, stipend
    FROM interns
    WHERE track = 'Data Science' AND stipend > 5000;
    """
    df_filter = pd.read_sql_query(filter_query, conn)
    print("\n1️⃣ Filter Result (Data Science & stipend > 5000):\n")
    print(df_filter)

    # 2️⃣ AGGREGATE: Average stipend per track
    avg_query = """
    SELECT track, AVG(stipend) AS avg_stipend
    FROM interns
    GROUP BY track;
    """
    df_avg = pd.read_sql_query(avg_query, conn)
    print("\n2️⃣ Average stipend per track:\n")
    print(df_avg)

    # 3️⃣ COUNT: Intern count per track
    count_query = """
    SELECT track, COUNT(*) AS intern_count
    FROM interns
    GROUP BY track;
    """
    df_count = pd.read_sql_query(count_query, conn)
    print("\n3️⃣ Intern count per track:\n")
    print(df_count)