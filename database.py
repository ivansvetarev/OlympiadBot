import sqlite3
from parsing import olympiads
connect = sqlite3.connect("database.db")

cursor = connect.cursor()

connect.execute("""CREATE TABLE IF NOT EXISTS olympiads (
        subjects TEXT,
        name TEXT,
        classes TEXT,
        level TEXT
        )""")
connect.commit()



for olympiad in olympiads:
    if olympiad.subject_names is not None:
        subject_names = "".join(subject_name + " " for subject_name in olympiad.subject_names)
    name = olympiad.name
    classes = olympiad.classes
    if olympiad.level is not None:
        level = "".join(level + " " for level in olympiad.level)

    print(type(level))

    cursor.execute(f"INSERT INTO olympiads VALUES (?, ?, ?, ?)", (subject_names, name, classes, level))

for value in cursor.execute("SELECT * FROM  olympiads"):
    print(value)

