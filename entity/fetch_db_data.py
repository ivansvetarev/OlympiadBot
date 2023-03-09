import sqlite3

connect = sqlite3.connect("olympiads_info.db")
cursor = connect.cursor()

for value in cursor.execute("""SELECT * FROM olympiads"""):
    print(value)

def select_by_attr(attr_name :str, target):
    select_query = """SELECT * FROM olympiads where """ + attr_name + """ = ?"""
    cursor.execute(select_query, target)
    print(cursor.fetchall())


select_by_attr("id", 2)