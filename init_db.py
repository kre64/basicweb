#Init two tables, insert 'first user' into each with some data.

import sqlite3
conn = sqlite3.connect('users.db')
c = conn.cursor()

c.execute("DROP TABLE IF EXISTS users")
c.execute("DROP TABLE IF EXISTS lists")

# Table of users
c.execute('''CREATE TABLE IF NOT EXISTS users (
	id INTEGER PRIMARY KEY,
	name TEXT
	)''')

# To prevent duplicate usernames for users.
c.execute("CREATE UNIQUE INDEX idx_username ON users (name)")

# Insert a row of data into users
c.execute("INSERT INTO users (name) VALUES ('first user')")

# Table of lists for users, x-ref with users table by name=uname?
c.execute('''CREATE TABLE IF NOT EXISTS lists (
	id INTEGER PRIMARY KEY,
	uname TEXT,
	item TEXT,
	isdone INTEGER
	)''')

# Insert a row of data into lists
c.execute("INSERT INTO lists (uname, item, isdone) VALUES ('first user', 'item', 0)")

conn.commit()
conn.close()