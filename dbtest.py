import sqlite3
conn = sqlite3.connect('users.db')
c = conn.cursor()


for row in c.execute('SELECT name FROM users'):
        print(row)