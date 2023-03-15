import sqlite3
from sqlite3 import Error

def create_connection(db_file):

    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

connect = create_connection("olympiads_info.db")
cursor = connect.cursor()

try:
    for value in cursor.execute("""SELECT * FROM olympiads"""):
        print(value)
except Error as e:
    print(e)

def select_by_attr(attr_name :str, target):
    try:
        select_query = """SELECT * FROM olympiads WHERE """ + attr_name + """ = ?"""
        cursor.execute(select_query, (target, ))
        #print(cursor.fetchone())
        return cursor.fetchone()
    except Error as e:
        print(e)
