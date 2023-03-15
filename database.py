import sqlite3
from info_parser import *
from bs4 import BeautifulSoup
import requests

URL = "https://olimpiada.ru/activities"

    
try:
    connect = sqlite3.connect("olympiads_info.db")
    cursor = connect.cursor()

    connect.execute("""CREATE TABLE IF NOT EXISTS olympiads (
            olympiad_id INTEGER PRIMARY KEY,
            subjects TEXT,
            name TEXT,
            classes TEXT,
            levels TEXT,
            ref_to_tasks TEXT,
            olympiad_url TEXT
            )""")
    connect.commit()

    connect.execute("""CREATE TABLE IF NOT EXISTS events (
            id INTEGER,
            event TEXT,
            start_date DATETIME,
            end_date DATETIME,
            FOREIGN KEY(id) REFERENCES olympiads(olympiad_id)
    )""")
    connect.commit()
except sqlite3.Error as error:
    print("Failed to create table ", error)

try:
    olymp_counter = 0
    for olympiad_url in  get_olympiads_urls(URL):
        olympiad_html = requests.get(olympiad_url)
        olympiad_soup = BeautifulSoup(olympiad_html.text)
        # print("\n", get_name(olympiad_soup),
        #       "\n Subjects : ", get_subjects(olympiad_soup),
        #       "\n Classes : ", get_classes(olympiad_soup),
        #       "\n Level : ", get_levels(olympiad_soup),
        #       "\n Full information : ", olympiad_url, 
        #       "\n Dates : ",  get_dates(olympiad_soup),
        #       "\n Tasks: ", get_ref_to_tasks(olympiad_url),
        #       "\n"
        #       )
        subjects =  get_subjects(olympiad_soup)
        name =  get_name(olympiad_soup)
        classes = "13"
        if( get_classes(olympiad_soup) != None) : classes =  get_classes(olympiad_soup)
        levels = "5"
        if( get_levels(olympiad_soup) != None) : classes =  get_levels(olympiad_soup)
        ref_to_tasks =  get_ref_to_tasks(olympiad_url)
        execute_str = """INSERT INTO olympiads (olympiad_id ,subjects, name, classes, levels, ref_to_tasks, olympiad_url) VALUES(?, ?, ?, ?, ?, ?, ?)"""
        cursor.execute(execute_str, 
                                    (
                                    olymp_counter,
                                    subjects, 
                                    name,
                                    classes,
                                    levels,
                                    ref_to_tasks,
                                    olympiad_url
                                    ))
        connect.commit()
        execute_str = """INSERT INTO events (id, event, start_date, end_date) VALUES(?, ?, ?, ?)"""
        for event in  get_dates(olympiad_soup):
            cursor.execute(execute_str, 
                        (
                            olymp_counter, 
                            event[0],
                            event[1],
                            event[2]
                        ))
        connect.commit()
        olymp_counter += 1
    for value in cursor.execute("SELECT * FROM  olympiads"):
        for event in cursor.execute("SELECT * FROM events"):
            print(event)
    cursor.close()
except sqlite3.Error as error:
    print("Failed to insert data ", error)
finally:
    if connect:
        connect.close()
