import sqlite3
from sqlite3 import Error
from database.db_utils import *



connect = create_connection("db/olympiads_info.db")
cursor = connect.cursor()

try:
    for value in cursor.execute("""SELECT * FROM olympiads"""):
        print()
except Error as e:
    print(e)

# def select_by_attr(attr_name :str, target):
#     try:
#         select_query = """SELECT * FROM olympiads WHERE """ + attr_name + """ = ?"""
#         cursor.execute(select_query, (target, ))
#         #print(cursor.fetchone())
#         return cursor.fetchone()
#     except Error as e:
#         print(e)

def select_by_subject(subject):
    olympiad_ids = []
    try:
        for olympiad in cursor.execute("""SELECT * FROM olympiads"""):
            if subject in olympiad[1]:
                olympiad_ids.append(olympiad[0])
        return set(olympiad_ids)
    except Error as e:
        print(e)

def select_by_class(class_):
    class_ids = []
    try:
        for olympiad in cursor.execute("""SELECT * FROM olympiads"""):
            if class_ == '1' and class_ in olympiad[3]:
                if olympiad[3].index(class_) == 0:
                    class_ids.append(olympiad[0])
            elif class_ in olympiad[3]:
                class_ids.append(olympiad[0])
        return set(class_ids)
    except Error as e:
        print(e)

def get_olympid_by_id(id):
    cursor.execute("""SELECT * FROM events WHERE id = ?""", (id,))
    if(cursor.fetchone() != None):
        return uget_olympid_by_id(id)
    else:
        return ""

