import sqlite3

conn = sqlite3.connect('ReviewProject.db')
cur = conn.cursor()
query = 'SELECT Username FROM User'
cur.execute(query)
res = cur.fetchall()
print(res)
conn.close()