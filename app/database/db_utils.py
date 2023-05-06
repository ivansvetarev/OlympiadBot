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

def convert_classes(classes):
    start = ""
    end = ""
    if "13" in classes: return "13"
    elif(classes[0] == "1" and (classes[1] == "2")): start = "1"
    elif(classes[0] == "1" and (classes[1] =="0")): start = "10"
    else: start = classes[0]
        
    l = len(classes)
    if classes[l - 1] == "1" and classes[l - 2] == "1": end = "11"
    elif classes[l - 1] == "0" and classes[l - 2] == "1": end = "1"
    else: end = classes[l - 1]
    return f'{start}-{end}'

def uget_olympiad_events_by_id(id, cursor):
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

def uget_olympid_by_id(id):
    connect = create_connection("db/olympiads_info.db")
    cursor = connect.cursor()
    try:
        cursor.execute("""SELECT * FROM olympiads WHERE olympiad_id=?""", (id,))
        row = cursor.fetchone()
        events = uget_olympiad_events_by_id(id, cursor)
        if "13" not in row[3]:
            class_part = f"Классы: {convert_classes(row[3])} \n"
        else: class_part = ""
        message = f"Название: {row[2]} \nПредметы: {row[1]} \n{class_part}Ссылка на задания прошлых лет: {row[5]} \nСсылка на полную информацию: {row[6]}\n"
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
