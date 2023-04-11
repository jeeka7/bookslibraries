import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('library.db')
cursor = conn.cursor()

# Create the library table
cursor.execute('''
CREATE TABLE IF NOT EXISTS library (
    library_id INTEGER PRIMARY KEY,
    library_name TEXT,
    due_date TEXT,
    total_fine REAL
)
''')

# Commit the changes and close the connection
conn.commit()
conn.close()
