#Print all rows for tables in 'users.db'.

import sqlite3
conn = sqlite3.connect('users.db')
c = conn.cursor()

#Table of users.
for row in c.execute('SELECT * FROM users'):
        print(row)

#Table of lists for users, x-ref by name.
for row in c.execute('SELECT * FROM lists'):
        print(row)