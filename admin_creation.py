import sqlite3

conn = sqlite3.connect("database.db")
db = conn.cursor()

try:
    db.execute("ALTER TABLE users ADD COLUMN role TEXT DEFAULT 'user'")
    print("Role column added successfully")
except:
    print("Column already exists")

db.execute("UPDATE users SET role='admin' WHERE username='Tappyokka'")

conn.commit()
conn.close()

print("Done!")