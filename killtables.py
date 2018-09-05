import sqlite3
conn = sqlite3.connect('users.db')
c = conn.cursor()

c.execute("DROP TABLE IF EXISTS users")
c.execute("DROP TABLE IF EXISTS lists")

conn.commit()
conn.close()