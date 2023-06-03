import sqlite3

conn = sqlite3.connect('invoice.db')

c = conn.cursor()

c.execute("""CREATE TABLE invoices (
    job_name TEXT,
    job_description TEXT,
    charge_description TEXT,
    charge_amount INTEGER
)""")

conn.commit()
conn.close()