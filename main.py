import sqlite3
import json

conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE activities")

cursor.execute("""
CREATE TABLE IF NOT EXISTS activities
(id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER UNIQUE, text_amount INTEGER, reaction_amount INTEGER, has_role INTEGER)""")

cursor.executemany("""
INSERT INTO activities (user_id, text_amount, reaction_amount, has_role) VALUES (?,?,?,?);

""", [
    (1,0,0,0),
    (2,60,0,1),
    (3,20,0,0),
    (4,80,0,0),
])

conn.commit()
cursor.execute("""
SELECT * FROM activities 
""")

cool = []

rows = cursor.fetchall()
for row in rows:
    print(row)

    if row[2] >= 50 and row[4] == 0:
        print('Пользователь классный')
        cool.append((1, int(row[0])))

print(json.dumps(cool))

cursor.executemany("""UPDATE activities SET has_role = ? WHERE id = ?""", cool)

conn.commit()