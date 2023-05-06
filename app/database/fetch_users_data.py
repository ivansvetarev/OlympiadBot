import sqlite3
from sqlite3 import Error
from database.db_utils import *


connect = create_connection("db/users_info.db")
cursor = connect.cursor()

try:
    connect.execute("""CREATE TABLE IF NOT EXISTS my_olympiads (
            user_id INTEGER PRIMARY KEY,
            ids TEXT
        )""")
    connect.commit()
except Error as e:
    print(e)

def add_olympiad(user_id, olympiad_id):
    try:
        cursor.execute("""SELECT * FROM my_olympiads WHERE user_id = ?""", (int(user_id),))
        data = cursor.fetchone()
        if data is None:
            olympiad_id = olympiad_id + ' '
            cursor.execute("""INSERT INTO my_olympiads (user_id, ids) VALUES (?, ?)""", (user_id, olympiad_id) )
            connect.commit()
        else:
            if str(olympiad_id) not in data[1]:
                row = data[1] + f'{olympiad_id} '
                print(row)
                cursor.execute("""UPDATE my_olympiads SET ids=? WHERE user_id = ?""", (row, user_id))
                connect.commit()
    except Error as e:
        print(e)

def remove_olympiad(user_id, olympiad_id):
    try:
        ids = get_olympiad_ids(user_id)
        ids.remove(olympiad_id)
        olympiad_ids = " ".join(ids)
        print(olympiad_ids)
        cursor.execute("""UPDATE my_olympiads SET ids=? WHERE user_id = ?""", (olympiad_ids, user_id))
        connect.commit()
    except Error as e:
        print(e)

def get_my_olympiads_message(user_id):
    
    messages = []
    print(user_id)
    try:
        cursor.execute("""SELECT * FROM my_olympiads""")
        cursor.execute("""SELECT * FROM my_olympiads WHERE user_id = ?""", (user_id, ))
        user_info = cursor.fetchone()
        print(f'{user_info[1]}')
        for id in user_info[1].split(" "):
            print(id)
            print(uget_olympid_by_id(int(id)))
            messages.append(uget_olympid_by_id(int(id)))
    except Error as e:
        print(e)
    finally:
        return messages
    
def get_olympiad_ids(user_id) -> list:
    try:
        cursor.execute("""SELECT * FROM my_olympiads WHERE user_id=?""", (user_id,))
        ids = cursor.fetchone()[1].split(" ")
        while " " in ids:
            ids.remove(" ")

        print(ids)

        return ids
    except Error as e:
        print(e)
