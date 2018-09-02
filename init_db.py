import sqlite3
conn = sqlite3.connect('users.db')
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE users
             (userid INTEGER, username TEXT, item TEXT)''')

# Insert a row of data
c.execute("INSERT INTO users VALUES (0,'first user', 'an item')")

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()