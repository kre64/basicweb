import sqlite3
conn = sqlite3.connect('users.db')
c = conn.cursor()

for row in c.execute('SELECT * FROM users'):
        print(row)

for row in c.execute('SELECT * FROM lists'):
        print(row)