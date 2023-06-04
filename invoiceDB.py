import sqlite3

conn = sqlite3.connect('invoice.db')

c = conn.cursor()

c.execute("""CREATE TABLE invoices (
    invoice_id INTEGER PRIMARY KEY AUTOINCREMENT,
    job_name TEXT,
    billing_address TEXT,
    phone_number TEXT NULL,
    paid BOOLEAN DEFAULT 0
)""")

c.execute("""CREATE TABLE charges (
    charge_id INTEGER PRIMARY KEY AUTOINCREMENT,
    invoice_id INTEGER,
    charge_description TEXT,
    charge_amount INTEGER,
    FOREIGN KEY (invoice_id) REFERENCES invoices (invoice_id)
)""")

conn.commit()
conn.close()