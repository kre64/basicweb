import sqlite3
conn = sqlite3.connect('users.db')
c = conn.cursor()

#c.execute("DROP TABLE users")

# Create table
c.execute('''CREATE TABLE IF NOT EXISTS users (
	id INTEGER PRIMARY KEY,
	name TEXT
	)''')

# Insert a row of data
c.execute("INSERT INTO users (name) VALUES ('first user')")

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()