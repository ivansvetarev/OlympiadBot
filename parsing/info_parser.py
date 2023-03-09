import requests
from bs4 import BeautifulSoup
import datetime

"""
functions:
get_olympiads_urls(url)
get_name(olympiad_soup)
get_subjects(olympiad_soup)
get_dates(olympiad_soup)
get_classes(olympiad_soup)
get_levels(olympiad_soup)
get_ref_to_tasks(olympiad_url)
get_month_number(month: str)
"""

def get_olympiads_urls(url):
    html = requests.get(url)
    soup = BeautifulSoup(html.text, features="html.parser")
    olympiads_urls = soup.find_all("a", class_="none_a black")
    olympiads_urls_size = len(olympiads_urls)
    for i in range(olympiads_urls_size - 1, -1, -1):
        if olympiads_urls[i] is None or (i - 1 != -1 and olympiads_urls[i].get("href") == olympiads_urls[i - 1].get("href")):
            del olympiads_urls[i]
        else:
            olympiads_urls[i] = "https://olimpiada.ru" + olympiads_urls[i].get("href")
    return olympiads_urls

def get_name(olympiad_soup):
    try:
        return olympiad_soup.find("h1").text
    except AttributeError:
        return ""

def get_month_number(month: str) -> int:
    if("янв" in month): return 1
    if("фев" in month): return 2
    if("мар" in month): return 3
    if("апр" in month): return 4
    if("май" in month): return 5
    if("июн" in month): return 6
    if("июл" in month): return 7
    if("авг" in month): return 8
    if("сен" in month): return 9
    if("окт" in month): return 10
    if("ноя" in month): return 11
    if("дек" in month): return 12
    else: 
        raise



def get_dates(olympiad_soup):
    dates = []
    try:
        dates_soup = olympiad_soup.find_all("tr", class_="notgreyclass")
        for date in dates_soup:
            data_soup = date.text.replace("...", "-")
            if data_soup is None:
                return []
            data_soup = data_soup[1:len(data_soup) - 1]
            data_soup = data_soup.split('\n')
            
            datestr = data_soup[1]
            start_month = 0
            end_month = 0
            start_day = 0
            end_day = 0
            if "-" in datestr:
                i = datestr.index("-")
                try:
                    try:    
                        start_month = get_month_number(datestr[i - 3:i])
                    except:
                        start_month = get_month_number(datestr[-3:len(datestr)])
                    end_month = get_month_number(datestr[-3:len(datestr)])
                    start_day = int(datestr[0] )
                    try:
                        start_day = int(datestr[0] + datestr[1])
                    except:
                        start_day = int(datestr[0])
                    try:
                        end_day = int(datestr[i + 1:i + 3])
                    except:
                        end_day = int(datestr[i + 1:i + 2])
                except:
                    start_month = get_month_number(datestr[len(data_soup[1]) - 4:len(datestr)])
                    end_month = start_month
                    if datestr[i] == "-":
                        try: 
                            start_day = int(datestr[i - 2] + datestr[i - 1])
                            end_day = int(datestr[i + 1] + datestr[i + 2])
                        except:
                            start_day = int(datestr[i - 1])
                            end_day = int (datestr[i + 1])     
            elif(datestr[0] == "Д"):
                start_month = 0
                end_month = get_month_number(data_soup[1][len(data_soup[1]) - 4:len(data_soup[1])])
                try:
                    #print(datestr[3] + datestr[4])
                    end_day = int(datestr[3] + datestr[4])
                    start_day = 0
                except:
                    end_day = int(datestr[3])
            else:
                #print(data_soup[1][len(data_soup[1]) - 3:len(data_soup[1])])
                start_month = get_month_number(data_soup[1][len(data_soup[1]) - 3:len(data_soup[1])])
                end_month = start_month
                try:
                    start_day = int(datestr[0] + datestr[1])
                    end_day = start_day
                except:
                    start_day = datestr[0]
                    end_day = start_day

                    
            event = data_soup[0]
            now = datetime.datetime.now()
            start_year = now.year
            end_year = now.year

            if(now.month <= start_month):
                start_year = now.year
            else:
                start_year = now.year + 1
            
            if(now.month <= end_month):
                end_year = now.year
            else:
                end_year = now.year + 1

            if start_month == 0 and start_day == 0:
                start_date = now
            else:
                start_date = datetime.datetime(start_year, start_month, start_day)
            end_date = datetime.datetime(end_year, end_month, end_day)
            event_date = [event, start_date, end_date]
            dates.append(event_date)
            
            #print(event_date)

        return dates #if startDay = 0 and startMonth = 0 => event is already started
    except Exception as e:
        #print(e)
        return dates
    


def get_classes(olympiad_soup):
    classes = ""
    try:
        classesstr = olympiad_soup.find("span", class_="classes_types_a").text
        start = 0
        end = 1
        if "–" in classesstr:
            i = classesstr.index('–')
            try:
                start = int(classesstr[0] + classesstr[1])
            except:
                start = int(classesstr[0])
            try:
                end = int(classesstr[i + 1] + classesstr[i + 2]) + 1
            except:
                end = int(classesstr[i + 1]) + 1
        for i in range(start, end):
            classes += str(i)
        return classes
    except Exception as e:
        #print(e)
        return None


def get_subjects(olympiad_soup):
    try:
        subjects = ""
        for span in olympiad_soup.find_all("span", class_="subject_tag"):
            if span.parent.get("class") == ["subject_tags_full"]:
                subject = ""
                for i in span.text:
                    for j in i:
                        if (j not in "\xa0"):
                            subject += j
                        else:
                            subject += " "
                subject = subject[1:len(subject)]
                subjects += subject
        return subjects
    except Exception as e:
        #print(e)
        return None


def get_levels(olympiad_soup):
    try:
        content = olympiad_soup.find_all("div", class_="right")
        levels = ""
        for tag in content:
            tag.find_all("div", id="features", class_="block_with_margin_bottom")
            for div in tag:
                for span in div.find_all("span"):
                    if ("уровень" in span.parent.text):
                        words = span.parent.text.split()
                        for i in range(len(words)):
                            if ("уровень" in words[i]):
                                for j in range(i + 1, len(words)):
                                    for k in words[j]:
                                        if k in "123" and k not in levels:
                                            levels += k
                                        elif k == "П":
                                            return levels

    except Exception as e:
        #print(e)
        return None


def get_ref_to_tasks(olympiad_url):
    return olympiad_url + "/tasks"

# subject_names = [p.find("strong") for p in soup.select("div > p")]
# for i in range(len(subject_names) - 1, -1, -1):
#     if(subject_names[i] == None):
#         del subject_names[i]
#     else:
#         subject_names[i] = subject_names[i].text
# print(subject_names)




# j = 1

# print(len(olympiads_urls))
#                         get_level(olympiad_soup)
#                         )
#     olympiads.append(olympiad)
#     print(get_dates(olympiad_soup))

#     print("\n", get_name(olympiad_soup),
#           "\n Subjects : ", get_subjects(olympiad_soup),
#           "\n Classes : ", get_classes(olympiad_soup),
#           "\n Level : ", get_level(olympiad_soup),
#           "\n Full information : ", olympiad_url, "\n")

# print(olympiad_soup)
# for olympiad_url in olympiads_urls:
#     olympiad_html = requests.get(olympiad_url)
#     olympiad_soup = BeautifulSoup(olympiad_html.text)
    #levels = get_level(olympiad_soup)
    
    # olympiad = Olympiad(
    #                     get_subjects(olympiad_soup),
    #                     get_name(olympiad_soup),
    #                     get_classes(olympiad_soup),
    #                     "date",
    #                     "organizator",
    #                     "registration",
    #                     "tasks",
    #                     get_level(olympiad_soup)
    #                     )
    # olympiads.append(olympiad)
    # print(get_dates(olympiad_soup))

    # print("\n", get_name(olympiad_soup),
    #       "\n Subjects : ", get_subjects(olympiad_soup),
    #       "\n Classes : ", get_classes(olympiad_soup),
    #       "\n Level : ", get_level(olympiad_soup),
    #       "\n Full information : ", olympiad_url, 
    #       "\n Dates : ",  get_dates(olympiad_soup),
    #       "\n Tasks: ", get_ref_to_tasks(olympiad_url),
    #       "\n"
    #       )

# dates = []
# for i in olympiads_urls:
#     olympiad_html = requests.get(i)
#     olympiad_soup = BeautifulSoup(olympiad_html.text, features="html.parser")
#     tasks = get_ref_to_tasks(i)
#     print(tasks)

