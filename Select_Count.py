import sqlite3
conn = sqlite3.connect('Photogeniks.db')
print "Opened database successfully";
cursor = conn.execute("SELECT count(*) FROM People;")



rows = cursor.fetchall()

for row in rows:
    print(row)

print "Operation done successfully";
conn.close()
