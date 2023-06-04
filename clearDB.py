import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('invoice.db')
cursor = conn.cursor()

# Get a list of all tables in the database
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

# Drop each table
for table in tables:
    drop_table_query = "DROP TABLE IF EXISTS " + table[0]
    cursor.execute(drop_table_query)

# Commit the changes
conn.commit()

# Close the connection
conn.close()
