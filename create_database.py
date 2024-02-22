import sqlite3

# Database initialization
conn = sqlite3.connect('passwords.db')
c = conn.cursor()

# Create table if not exists
c.execute('''CREATE TABLE IF NOT EXISTS passwords
             (id INTEGER PRIMARY KEY, service TEXT, username TEXT, password TEXT)''')

# Commit the transaction
conn.commit()

# Close the connection
conn.close()
