import sqlite3

conn = sqlite3.connect("new.db")
cursor= conn.cursor()

cursor.execute("UPDATE new(отдел)")

con.commit
