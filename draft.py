import sqlite3
from sqlite3 import Error

def create_connection(db_file):

    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Connected")
    except Error as e:
        print(e)

    return conn


try:
    connect = create_connection("db/olympiads_info.db")
    connect.execute("""CREATE TABLE IF NOT EXISTS my_olympiads (
            user_id INTEGER PRIMARY KEY,
            ids TEXT
        )""")
    connect.commit()
except Error as e:
    print(e)
finally:
    connect.close()

# try:
#     connect = create_connection("db/olympiads_info.db")
#     cursor = connect.cursor()
#     for value in cursor.execute("""SELECT * FROM olympiads"""):
#         print()
# except Error as e:
#     print(e)
# finally:
#     connect.close()
# def select_by_attr(attr_name :str, target):
#     try:
#         select_query = """SELECT * FROM olympiads WHERE """ + attr_name + """ = ?"""
#         cursor.execute(select_query, (target, ))
#         #print(cursor.fetchone())
#         return cursor.fetchone()
#     except Error as e:
#         print(e)

def select_by_subject(subject):
    connect = create_connection("db/olympiads_info.db")
    cursor = connect.cursor()
    olympiad_ids = []
    try:
        for olympiad in cursor.execute("""SELECT * FROM olympiads"""):
            if subject in olympiad[1]:
                olympiad_ids.append(olympiad[0])
        return set(olympiad_ids)
    except Error as e:
        print(e)
    finally: 
        connect.close()
def select_by_class(class_):
    connect = create_connection("db/olympiads_info.db")
    cursor = connect.cursor()
    class_ids = []
    try:
        for olympiad in cursor.execute("""SELECT * FROM olympiads"""):
            if class_ in olympiad[3]:
                class_ids.append(olympiad[0])
        return set(class_ids)
    except Error as e:
        print(e)
    finally:
        connect.close()

def get_olympid_by_id(id):
    connect = create_connection("db/olympiads_info.db")
    cursor = connect.cursor()
    try:
        cursor.execute("""SELECT * FROM olympiads WHERE olympiad_id=?""", (id,))
        row = cursor.fetchone()
        events = get_olympiad_events_by_id(id, cursor)
        message = f"Название: {row[2]} \nПредмет: {row[1]} \nКлассы: {row[3]} \nСсылка на задания прошлых лет: {row[5]} \nСсылка на полную информацию: {row[6]}\n"
        if events != {}:
            message += "События: \n"
            for event in events:
                if events[event][0] != events[event][0]:
                    message += f"{event}: {events[event][0][8:10]}.{events[event][0][5:7]}.{events[event][0][0:4]} - {events[event][1][8:10]}.{events[event][1][5:7]}.{events[event][1][0:4]}\n"
                else:
                    message += f"{event}: {events[event][0][8:10]}.{events[event][0][5:7]}.{events[event][0][0:4]}\n"
        return message
    except Error as e:
        print(e)
    finally:
        connect.close()
def get_olympiad_events_by_id(id, cursor):

    try:
        events = {}
        
        for event in cursor.execute("""SELECT * FROM events WHERE id=?""", (id,)):
            try:
                print(event[2], event[3])
                events[event[1]] = [event[2], event[3]]
            except Exception as e:
                print(e)
        return events
    except Error as e:
        print(e)

def add_olympiad(user_id, olympiad_id):
    connect = create_connection("db/olympiads_info.db")
    cursor = connect.cursor()
    try:
        cursor.execute("""SELECT * FROM my_olympiads WHERE user_id=?""", (int(user_id),))
        if cursor.fetchone() is None:
            cursor.execute("""INSERT INTO my_olympiads (user_id, ids) VALUES (?, ?)""", (user_id, olympiad_id) )
            connect.commit()
        else:
            row = cursor.fetchone()[1] + f'{olympiad_id} '
            cursor.execute("""UPDATE my_olympiads SET ids=? WHERE user_id = ?""", row, user_id)
            connect.commit()
    except Error as e:
        print(e)
    finally:
        connect.close()

