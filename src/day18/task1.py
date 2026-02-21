import sqlite3
import pandas as pd

DB_PATH = "internship.db"

# Use context manager to auto-close connection
with sqlite3.connect(DB_PATH, timeout=30) as conn:
    # Create tables
    conn.execute("""
    CREATE TABLE IF NOT EXISTS interns (
        intern_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        mentor_id INTEGER
    );
    """)

    conn.execute("""
    CREATE TABLE IF NOT EXISTS mentors (
        mentor_id INTEGER PRIMARY KEY,
        mentor_name TEXT,
        track TEXT
    );
    """)

 
    conn.execute("DELETE FROM interns;")
    conn.execute("DELETE FROM mentors;")


    conn.executemany("INSERT INTO interns (name, mentor_id) VALUES (?, ?)", [
        ("Alice", 101),
        ("Bob", 102),
        ("John", 101),
        ("Mike", 103)
    ])

    conn.executemany("INSERT INTO mentors VALUES (?, ?, ?)", [
        (101, "Rahul", "Data Science"),
        (102, "Priya", "AI"),
        (103, "Amit", "Web Dev")
    ])

    # INNER JOIN query → Pandas
    query = """
    SELECT interns.intern_id,
           interns.name AS intern_name,
           mentors.mentor_name,
           mentors.track
    FROM interns
    INNER JOIN mentors
    ON interns.mentor_id = mentors.mentor_id;
    """

    df = pd.read_sql_query(query, conn)
    print("\nJOIN Result:\n")
    print(df)