import sqlite3

connect = sqlite3.connect("students.db")

cursor = connect.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS students (
id INTEGER PRIMARY KEY,
name TEXT,
age INTEGER,
average_grade INTEGER )""")

cursor.execute("""INSERT INTO students (name, age, average_grade) VALUES ('Danek', 24, 3)""")
cursor.execute("""DELETE FROM students WHERE name='Dan' """)
connect.commit()

cursor.execute("""SELECT * FROM students""")
rows = cursor.fetchall()
cursor.execute("""SELECT * FROM students""")
rowe = cursor.fetchmany(3)

print(rows)
print(rowe)
connect.close()
